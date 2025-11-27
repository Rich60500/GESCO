"""
GESCO v5.0 - Client API Axonaut
Client HTTP pour interagir avec l'API Axonaut
"""

import requests
from typing import List, Optional, Dict, Any

from .axonaut_config import AxonautConfig
from .axonaut_models import Company, Employee, Address


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

    def get_employees(self) -> List[Employee]:
        """
        Récupère la liste de tous les employés

        Returns:
            Liste des employés
        """
        response = self._request('GET', '/employees')
        data = response.json()

        if isinstance(data, list):
            return [Employee.from_dict(item) for item in data]
        return []

    def get_company_employees(self, company_id: int) -> List[Employee]:
        """
        Récupère les employés d'une entreprise

        Args:
            company_id: ID de l'entreprise

        Returns:
            Liste des employés
        """
        response = self._request('GET', f'/companies/{company_id}/employees')
        data = response.json()

        if isinstance(data, list):
            return [Employee.from_dict(item) for item in data]
        return []

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
        # Ajouter company_id dans le body
        data['company_id'] = company_id

        response = self._request('POST', '/employees', json=data)
        result = response.json()
        return Employee.from_dict(result)

    def update_employee(self, employee_id: int, employee: Employee, company_id: Optional[int] = None) -> Employee:
        """
        Met à jour un employé existant

        Args:
            employee_id: ID de l'employé
            employee: Objet Employee avec les nouvelles données
            company_id: ID de l'entreprise (optionnel, pour compatibilité)

        Returns:
            Employé mis à jour
        """
        data = employee.to_dict(for_api=True)
        response = self._request('PATCH', f'/employees/{employee_id}', json=data)
        result = response.json()
        return Employee.from_dict(result)

    def delete_employee(self, employee_id: int, company_id: Optional[int] = None) -> bool:
        """
        Supprime un employé

        Args:
            employee_id: ID de l'employé
            company_id: ID de l'entreprise (optionnel, pour compatibilité)

        Returns:
            True si succès
        """
        try:
            self._request('DELETE', f'/employees/{employee_id}')
            return True
        except AxonautAPIError:
            return False

    # ==================== ADDRESSES ====================

    def get_company_addresses(self, company_id: int) -> List[Address]:
        """
        Récupère les adresses de chantier d'une entreprise

        Args:
            company_id: ID de l'entreprise

        Returns:
            Liste des adresses
        """
        response = self._request('GET', f'/companies/{company_id}/addresses')
        data = response.json()

        if isinstance(data, list):
            return [Address.from_dict(item) for item in data]
        return []

    def create_address(self, company_id: int, address: Address) -> Address:
        """
        Crée une nouvelle adresse de chantier pour une entreprise

        Args:
            company_id: ID de l'entreprise
            address: Objet Address à créer

        Returns:
            Adresse créée avec son ID
        """
        data = address.to_dict(for_api=True)

        response = self._request('POST', f'/companies/{company_id}/addresses', json=data)
        result = response.json()
        return Address.from_dict(result)

    def update_address(self, address_id: int, address: Address) -> Address:
        """
        Met à jour une adresse existante

        Args:
            address_id: ID de l'adresse
            address: Objet Address avec les nouvelles données

        Returns:
            Adresse mise à jour
        """
        data = address.to_dict(for_api=True)
        response = self._request('PATCH', f'/addresses/{address_id}', json=data)
        result = response.json()
        return Address.from_dict(result)

    def delete_address(self, address_id: int) -> bool:
        """
        Supprime une adresse

        Args:
            address_id: ID de l'adresse

        Returns:
            True si succès
        """
        try:
            self._request('DELETE', f'/addresses/{address_id}')
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
