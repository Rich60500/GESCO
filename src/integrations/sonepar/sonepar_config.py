"""
GESCO v5.0 - Configuration Sonepar
Configuration de l'API Sonepar
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class SoneParConfig:
    """Configuration pour l'API Sonepar"""

    # Identifiants API (DENIS EURL)
    api_key: str = "95791076"
    customer_code: str = "4146EB1"
    org_id: str = "5QD"

    # URLs des environnements
    base_url_test: str = "https://apitst.sonepar.fr/api"
    base_url_prod: str = "https://api.sonepar.fr/api"

    # Environnement actif (test par défaut)
    use_production: bool = False

    # Timeouts et limites
    timeout: int = 30  # secondes
    max_retries: int = 3

    # Rate limiting
    rate_limit_calls: int = 10
    rate_limit_period: int = 60  # secondes

    # Rate limiting catalogue (plus restrictif)
    catalog_rate_limit_calls: int = 5
    catalog_rate_limit_period: int = 1  # secondes

    @property
    def base_url(self) -> str:
        """Retourne l'URL de base selon l'environnement"""
        return self.base_url_prod if self.use_production else self.base_url_test

    @property
    def headers(self) -> dict:
        """Retourne les headers HTTP pour les requêtes"""
        return {
            "X-API-Key": self.api_key,
            "X-Customer-Code": self.customer_code,
            "X-Org-Id": self.org_id,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def get_endpoint(self, path: str) -> str:
        """
        Construit l'URL complète pour un endpoint

        Args:
            path: Chemin de l'endpoint (ex: "/catalog/products")

        Returns:
            URL complète
        """
        # Nettoyer le path
        path = path.lstrip('/')
        return f"{self.base_url}/{path}"
