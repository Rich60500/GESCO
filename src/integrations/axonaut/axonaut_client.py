"""
GESCO v5.0 - Client API Axonaut
Client HTTP pour interagir avec l'API Axonaut
"""

import requests
from typing import List, Optional, Dict, Any

from .axonaut_config import AxonautConfig
from .axonaut_models import Company, Employee


class AxonautAPIError(Exception):
    """Exception levée lors d'une erreur API Axonaut"""
    pass


class AxonautClient:
    """Client pour l'API Axonaut"""

    def __init__(self, config: Optional[AxonautConfig] = None):
        """
        Initialise le client Axonaut

        Args:
            config: Configuration Axonaut (utilise la config par défaut si None)
        """
        self.config = config or AxonautConfig()
        self.session = requests.Session()
        self.session.headers.update(self.config.headers)

    def _request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """
        Effectue une requête HTTP vers l'API

        Args:
            method: Méthode HTTP (GET, POST, PATCH, DELETE)
            endpoint: Endpoint de l'API
            **kwargs: Arguments additionnels pour requests

        Returns:
            Response object

        Raises:
            AxonautAPIError: En cas d'erreur API
        """
        url = self.config.get_endpoint(endpoint)
        kwargs.setdefault('timeout', self.config.timeout)

        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            error_msg = f"Erreur API Axonaut ({e.response.status_code}): {e.response.text}"
            raise AxonautAPIError(error_msg) from e
        except requests.exceptions.RequestException as e:
            raise AxonautAPIError(f"Erreur de connexion à l'API Axonaut: {str(e)}") from e

    # ==================== COMPANIES ====================

    def get_companies(self) -> List[Company]:
        """
        Récupère la liste de toutes les entreprises

        Returns:
            Liste des entreprises
        """
        response = self._request('GET', '/companies')
        data = response.json()

        if isinstance(data, list):
            return [Company.from_dict(item) for item in data]
        return []

    def get_company(self, company_id: int) -> Optional[Company]:
        """
        Récupère une entreprise par son ID

        Args:
            company_id: ID de l'entreprise

        Returns:
            Entreprise ou None si non trouvée
        """
        try:
            response = self._request('GET', f'/companies/{company_id}')
            data = response.json()
            return Company.from_dict(data)
        except AxonautAPIError:
            return None

    def create_company(self, company: Company) -> Company:
        """
        Crée une nouvelle entreprise

        Args:
            company: Objet Company à créer

        Returns:
            Entreprise créée avec son ID
        """
        data = company.to_dict(for_api=True)
        response = self._request('POST', '/companies', json=data)
        result = response.json()
        return Company.from_dict(result)

    def update_company(self, company_id: int, company: Company) -> Company:
        """
        Met à jour une entreprise existante

        Args:
            company_id: ID de l'entreprise
            company: Objet Company avec les nouvelles données

        Returns:
            Entreprise mise à jour
        """
        data = company.to_dict(for_api=True)
        response = self._request('PATCH', f'/companies/{company_id}', json=data)
        result = response.json()
        return Company.from_dict(result)

    def delete_company(self, company_id: int) -> bool:
        """
        Supprime une entreprise

        Args:
            company_id: ID de l'entreprise

        Returns:
            True si succès
        """
        try:
            self._request('DELETE', f'/companies/{company_id}')
            return True
        except AxonautAPIError:
            return False

    # ==================== EMPLOYEES ====================

    def get_company_employees(self, company_id: int) -> List[Employee]:
        """
        Récupère les employés d'une entreprise

        Args:
            company_id: ID de l'entreprise

        Returns:
            Liste des employés
        """
        company = self.get_company(company_id)
        return company.employees if company else []

    def create_employee(self, company_id: int, employee: Employee) -> Employee:
        """
        Crée un nouvel employé pour une entreprise

        Args:
            company_id: ID de l'entreprise
            employee: Objet Employee à créer

        Returns:
            Employé créé avec son ID
        """
        data = employee.to_dict(for_api=True)
        response = self._request('POST', f'/companies/{company_id}/employees', json=data)
        result = response.json()
        return Employee.from_dict(result)

    def update_employee(self, company_id: int, employee_id: int, employee: Employee) -> Employee:
        """
        Met à jour un employé existant

        Args:
            company_id: ID de l'entreprise
            employee_id: ID de l'employé
            employee: Objet Employee avec les nouvelles données

        Returns:
            Employé mis à jour
        """
        data = employee.to_dict(for_api=True)
        response = self._request('PATCH', f'/companies/{company_id}/employees/{employee_id}', json=data)
        result = response.json()
        return Employee.from_dict(result)

    def delete_employee(self, company_id: int, employee_id: int) -> bool:
        """
        Supprime un employé

        Args:
            company_id: ID de l'entreprise
            employee_id: ID de l'employé

        Returns:
            True si succès
        """
        try:
            self._request('DELETE', f'/companies/{company_id}/employees/{employee_id}')
            return True
        except AxonautAPIError:
            return False

    # ==================== RECHERCHE ====================

    def search_companies(self,
                        query: Optional[str] = None,
                        is_customer: Optional[bool] = None,
                        is_prospect: Optional[bool] = None) -> List[Company]:
        """
        Recherche des entreprises avec filtres

        Args:
            query: Terme de recherche (nom, ville, etc.)
            is_customer: Filtrer par clients
            is_prospect: Filtrer par prospects

        Returns:
            Liste des entreprises correspondantes
        """
        companies = self.get_companies()

        # Filtrer par type
        if is_customer is not None:
            companies = [c for c in companies if c.is_customer == is_customer]
        if is_prospect is not None:
            companies = [c for c in companies if c.is_prospect == is_prospect]

        # Filtrer par recherche textuelle
        if query:
            query_lower = query.lower()
            companies = [
                c for c in companies
                if (c.name and query_lower in c.name.lower()) or
                   (c.address_city and query_lower in c.address_city.lower()) or
                   (c.siret and query_lower in c.siret.lower())
            ]

        return companies

    def sync_company(self, company_id: int) -> Optional[Company]:
        """
        Synchronise une entreprise depuis l'API

        Args:
            company_id: ID de l'entreprise

        Returns:
            Entreprise synchronisée ou None
        """
        return self.get_company(company_id)
