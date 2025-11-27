"""
GESCO v5.0 - Configuration Axonaut
Configuration de l'API Axonaut pour la gestion des tiers/clients/contacts
"""

from dataclasses import dataclass


@dataclass
class AxonautConfig:
    """Configuration pour l'API Axonaut"""

    # Clé API Axonaut
    api_key: str = "1048373916eaf56f880c5959078cfa5230b524104837"

    # URL de base de l'API
    base_url: str = "https://axonaut.com/api/v2"

    # Timeouts et limites
    timeout: int = 30  # secondes
    max_retries: int = 3

    @property
    def headers(self) -> dict:
        """Retourne les headers HTTP pour les requêtes"""
        return {
            "userApiKey": self.api_key,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def get_endpoint(self, path: str) -> str:
        """
        Construit l'URL complète pour un endpoint

        Args:
            path: Chemin de l'endpoint (ex: "/companies")

        Returns:
            URL complète
        """
        # Nettoyer le path
        path = path.lstrip('/')
        return f"{self.base_url}/{path}"
