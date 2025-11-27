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
    api_key: str = "95791076"  # Ocp-Apim-Subscription-Key
    customer_code: str = "4146EB1"
    org_id: str = "5QD"

    # Authentification utilisateur (à configurer)
    # Ces identifiants doivent être encodés en Base64
    user_id: str = ""  # TODO: Remplir avec l'identifiant utilisateur Sonepar
    user_password: str = ""  # TODO: Remplir avec le mot de passe Sonepar

    # URLs des environnements
    base_url_test: str = "https://apitst.sonepar.fr/api"
    base_url_prod: str = "https://api.sonepar.fr/api"

    # Environnement actif (test par défaut)
    use_production: bool = False

    # Timeouts et limites
    timeout: int = 30  # secondes
    max_retries: int = 3

    # Rate limiting (selon doc API Sonepar)
    rate_limit_calls: int = 10
    rate_limit_period: int = 60  # secondes

    # Rate limiting catalogue (plus restrictif : 5/seconde)
    catalog_rate_limit_calls: int = 5
    catalog_rate_limit_period: int = 1  # secondes

    @property
    def base_url(self) -> str:
        """Retourne l'URL de base selon l'environnement"""
        return self.base_url_prod if self.use_production else self.base_url_test

    @property
    def headers(self) -> dict:
        """Retourne les headers HTTP pour les requêtes (selon doc API v1.4)"""
        import base64

        headers = {
            "Ocp-Apim-Subscription-Key": self.api_key,
            "customerCode": self.customer_code,
            "orgId": self.org_id,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        # Ajouter l'authentification user/pass si configurée
        if self.user_id and self.user_password:
            # Encoder en Base64 si ce n'est pas déjà fait
            try:
                base64.b64decode(self.user_id)
                headers["X-snp-user"] = self.user_id
            except:
                headers["X-snp-user"] = base64.b64encode(self.user_id.encode()).decode()

            try:
                base64.b64decode(self.user_password)
                headers["X-snp-pass"] = self.user_password
            except:
                headers["X-snp-pass"] = base64.b64encode(self.user_password.encode()).decode()

        return headers

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
