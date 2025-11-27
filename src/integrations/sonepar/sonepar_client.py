"""
GESCO v5.0 - Client API Sonepar
Client HTTP pour interagir avec l'API Sonepar
"""

import time
import requests
from datetime import datetime
from typing import List, Optional, Dict, Any
from collections import deque

from .sonepar_config import SoneParConfig
from .sonepar_models import (
    Brand, Product, ProductWithPricing, Stock, Price,
    Order, OrderLine, DeliveryNote, ProductStatus,
    OrderType, StockType, OrderStatus
)
from .sonepar_database import SoneParDatabase


class RateLimiter:
    """Gestionnaire de rate limiting"""

    def __init__(self, max_calls: int, period: int):
        """
        Initialise le rate limiter

        Args:
            max_calls: Nombre maximum d'appels
            period: Période en secondes
        """
        self.max_calls = max_calls
        self.period = period
        self.calls = deque()

    def wait_if_needed(self):
        """Attend si nécessaire pour respecter le rate limit"""
        now = time.time()

        # Supprimer les appels trop anciens
        while self.calls and self.calls[0] < now - self.period:
            self.calls.popleft()

        # Si on a atteint la limite, attendre
        if len(self.calls) >= self.max_calls:
            sleep_time = self.period - (now - self.calls[0])
            if sleep_time > 0:
                time.sleep(sleep_time)
            # Nettoyer à nouveau après le sleep
            now = time.time()
            while self.calls and self.calls[0] < now - self.period:
                self.calls.popleft()

        # Enregistrer cet appel
        self.calls.append(now)


class SoneParClient:
    """Client pour l'API Sonepar"""

    def __init__(self, config: Optional[SoneParConfig] = None, db_path: str = "data/gesco.db"):
        """
        Initialise le client API

        Args:
            config: Configuration Sonepar (utilise la config par défaut si None)
            db_path: Chemin vers la base de données locale
        """
        self.config = config or SoneParConfig()
        self.db = SoneParDatabase(db_path)

        # Rate limiters
        self.rate_limiter = RateLimiter(
            self.config.rate_limit_calls,
            self.config.rate_limit_period
        )
        self.catalog_rate_limiter = RateLimiter(
            self.config.catalog_rate_limit_calls,
            self.config.catalog_rate_limit_period
        )

        # Session HTTP
        self.session = requests.Session()
        self.session.headers.update(self.config.headers)

    def _make_request(
        self,
        method: str,
        endpoint: str,
        use_catalog_limiter: bool = False,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Effectue une requête HTTP avec rate limiting

        Args:
            method: Méthode HTTP (GET, POST, etc.)
            endpoint: Endpoint de l'API
            use_catalog_limiter: Utiliser le rate limiter catalogue
            **kwargs: Arguments additionnels pour requests

        Returns:
            Réponse JSON

        Raises:
            requests.exceptions.RequestException: En cas d'erreur HTTP
        """
        # Appliquer le rate limiting
        if use_catalog_limiter:
            self.catalog_rate_limiter.wait_if_needed()
        else:
            self.rate_limiter.wait_if_needed()

        # URL complète
        url = self.config.get_endpoint(endpoint)

        # Timeout par défaut
        kwargs.setdefault('timeout', self.config.timeout)

        # Effectuer la requête avec retry
        for attempt in range(self.config.max_retries):
            try:
                response = self.session.request(method, url, **kwargs)
                response.raise_for_status()
                return response.json()

            except requests.exceptions.RequestException as e:
                if attempt == self.config.max_retries - 1:
                    raise
                time.sleep(2 ** attempt)  # Backoff exponentiel

    # === BRANDS ===

    def get_brands(self) -> List[Brand]:
        """
        Récupère la liste des marques

        Returns:
            Liste des marques
        """
        data = self._make_request('GET', '/brands')

        brands = []
        for item in data.get('brands', []):
            brands.append(Brand(
                id=item['id'],
                name=item['name'],
                logo_url=item.get('logo_url')
            ))

        return brands

    # === CATALOG ===

    def search_products(
        self,
        query: str,
        brand_id: Optional[str] = None,
        limit: int = 50,
        use_local_db: bool = True
    ) -> List[Product]:
        """
        Recherche des produits dans le catalogue Sonepar

        Cette méthode privilégie la recherche dans la base locale pour
        de meilleures performances. Si aucun résultat n'est trouvé localement,
        elle peut interroger l'API.

        Args:
            query: Terme de recherche (référence, description, etc.)
            brand_id: Filtrer par marque (optionnel)
            limit: Nombre maximum de résultats
            use_local_db: Rechercher d'abord dans la base locale (défaut: True)

        Returns:
            Liste de produits correspondants
        """
        # 1. Essayer la recherche locale d'abord si activée
        if use_local_db:
            local_results = self.db.search_products(query, brand_id, limit)
            if local_results:
                # Convertir les résultats dict en objets Product
                products = []
                for row in local_results:
                    brand = Brand(
                        id=row.get('brand_id', ''),
                        name=row.get('brand', ''),
                        logo_url=None
                    )

                    product = Product(
                        id=row.get('id', ''),
                        ean=row.get('ean', ''),
                        reference=row.get('reference', ''),
                        description=row.get('description', ''),
                        brand=brand,
                        status=ProductStatus(row.get('status', 'UNKNOWN'))
                    )
                    products.append(product)

                return products

        # 2. Si pas de résultats locaux, interroger l'API
        # NOTE: L'API Sonepar ne supporte PAS la recherche textuelle directe.
        # Cette méthode utilise GET /products/v1/catalogs qui télécharge un
        # catalogue complet et filtre localement.
        params = {
            'responseType': 'json',
            'page': 1  # Première page uniquement pour la recherche
        }

        if brand_id:
            params['brandId'] = brand_id

        # Si query ressemble à un ID produit, utiliser soneparProductId
        if query.replace(',', '').isdigit():
            params['soneparProductId'] = query
        # Sinon, télécharger le catalogue et filtrer localement
        # (peu optimal mais c'est la seule option)

        data = self._make_request(
            'GET',
            '/products/v1/catalogs',
            use_catalog_limiter=True,
            params=params
        )

        products = []
        query_lower = query.lower()

        for item in data.get('products', []):
            # Filtrer par query si recherche textuelle
            description = item.get('description', '')
            supplier_ref = item.get('supplierProductId', '')
            sonepar_id = item.get('soneparProductId', item.get('id', ''))

            # Si pas une recherche par ID, filtrer par texte
            if not query.replace(',', '').isdigit():
                if (query_lower not in description.lower() and
                    query_lower not in str(supplier_ref).lower() and
                    query_lower not in str(sonepar_id).lower()):
                    continue

            # Parse brand
            brand_data = item.get('brand', {})
            brand = Brand(
                id=brand_data.get('id', '') if brand_data else '',
                name=brand_data.get('name', '') if brand_data else '',
                logo_url=brand_data.get('logo_url') if brand_data else None
            )

            # Parse status (API v1 utilise des codes numériques)
            status_code = item.get('status', 20)
            if isinstance(status_code, int):
                status = ProductStatus.ACTIVE if status_code == 20 else ProductStatus.DISCONTINUED
            else:
                status = ProductStatus(status_code)

            # Parse product (gérer les deux formats API)
            product = Product(
                id=sonepar_id,
                ean=item.get('gtin', item.get('ean', '')),
                reference=supplier_ref or item.get('reference', ''),
                description=description,
                brand=brand,
                family=item.get('family', ''),
                subfamily=item.get('subfamily', ''),
                status=status,
                weight=item.get('weight'),
                unit=item.get('unit', 'PCE'),
                packaging=item.get('packaging', 1),
                image_url=item.get('image_url'),
                technical_sheet_url=item.get('technical_sheet_url')
            )

            products.append(product)

            # Limiter les résultats
            if len(products) >= limit:
                break

        return products

    def sync_catalog(
        self,
        brand_id: Optional[str] = None,
        max_pages: int = 10,
        progress_callback: Optional[callable] = None
    ) -> Dict[str, Any]:
        """
        Synchronise le catalogue Sonepar dans la base de données locale

        Cette méthode télécharge les produits du catalogue Sonepar par pages
        et les stocke en base locale pour permettre des recherches rapides.

        Args:
            brand_id: Filtrer par marque (optionnel, sinon tous les produits)
            max_pages: Nombre maximum de pages à télécharger (défaut: 10)
            progress_callback: Fonction appelée avec (page, total_pages, products_count)

        Returns:
            Statistiques de synchronisation:
            {
                'total_products': int,
                'pages_downloaded': int,
                'duration': float,
                'last_sync': datetime
            }
        """
        start_time = time.time()
        total_products = 0
        page = 1

        print(f"Début de la synchronisation du catalogue Sonepar...")
        if brand_id:
            print(f"  Marque: {brand_id}")
        print(f"  Pages max: {max_pages}")

        while page <= max_pages:
            try:
                params = {
                    'responseType': 'json',
                    'page': page
                }

                if brand_id:
                    params['brandId'] = brand_id

                print(f"  Téléchargement page {page}/{max_pages}...")

                data = self._make_request(
                    'GET',
                    '/products/v1/catalogs',
                    use_catalog_limiter=True,
                    params=params
                )

                products_data = data.get('products', [])
                if not products_data:
                    print(f"  Aucun produit trouvé sur la page {page}, arrêt.")
                    break

                # Convertir les produits en format dict pour la DB
                products_to_save = []
                for item in products_data:
                    brand_data = item.get('brand', {})
                    status_code = item.get('status', 20)

                    if isinstance(status_code, int):
                        status = 'ACTIVE' if status_code == 20 else 'DISCONTINUED'
                    else:
                        status = status_code

                    product_dict = {
                        'id': item.get('soneparProductId', item.get('id', '')),
                        'ean': item.get('gtin', item.get('ean', '')),
                        'reference': item.get('supplierProductId', item.get('reference', '')),
                        'description': item.get('description', ''),
                        'brand': brand_data.get('name', '') if brand_data else '',
                        'brand_id': brand_data.get('id', '') if brand_data else '',
                        'unit_price': 0.0,  # Prix nécessite un endpoint séparé
                        'stock_available': 0,  # Stock nécessite un endpoint séparé
                        'status': status,
                        'image_url': item.get('image_url', ''),
                        'technical_specs': ''  # Specs nécessitent un endpoint séparé
                    }
                    products_to_save.append(product_dict)

                # Sauvegarder en base
                count = self.db.save_products(products_to_save)
                total_products += count

                print(f"  ✓ Page {page}: {count} produits sauvegardés")

                # Callback de progression
                if progress_callback:
                    progress_callback(page, max_pages, total_products)

                # Vérifier s'il y a d'autres pages
                pagination = data.get('pagination', {})
                total_pages = pagination.get('totalPages', page)

                if page >= total_pages:
                    print(f"  Dernière page atteinte ({total_pages} pages au total)")
                    break

                page += 1

            except Exception as e:
                print(f"  ✗ Erreur page {page}: {e}")
                break

        # Enregistrer la date de synchronisation
        sync_date = datetime.now()
        self.db.set_last_sync_date(sync_date)

        duration = time.time() - start_time

        result = {
            'total_products': total_products,
            'pages_downloaded': page,
            'duration': duration,
            'last_sync': sync_date
        }

        print(f"\n✓ Synchronisation terminée:")
        print(f"  Produits: {total_products}")
        print(f"  Pages: {page}")
        print(f"  Durée: {duration:.1f}s")

        return result

    def get_catalog_info(self) -> Dict[str, Any]:
        """
        Retourne des informations sur le catalogue local

        Returns:
            Informations du catalogue:
            {
                'product_count': int,
                'last_sync': datetime or None
            }
        """
        return {
            'product_count': self.db.get_product_count(),
            'last_sync': self.db.get_last_sync_date()
        }

    def get_product_by_reference(self, reference: str) -> Optional[Product]:
        """
        Récupère un produit par sa référence

        Args:
            reference: Référence du produit

        Returns:
            Produit ou None si non trouvé
        """
        try:
            data = self._make_request(
                'GET',
                f'/catalog/products/{reference}',
                use_catalog_limiter=True
            )

            # Parse brand
            brand_data = data.get('brand', {})
            brand = Brand(
                id=brand_data.get('id', ''),
                name=brand_data.get('name', ''),
                logo_url=brand_data.get('logo_url')
            )

            # Parse product
            product = Product(
                id=data['id'],
                ean=data.get('ean', ''),
                reference=data['reference'],
                description=data['description'],
                brand=brand,
                family=data.get('family', ''),
                subfamily=data.get('subfamily', ''),
                status=ProductStatus(data.get('status', 'ACTIVE')),
                weight=data.get('weight'),
                unit=data.get('unit', 'PCE'),
                packaging=data.get('packaging', 1),
                image_url=data.get('image_url'),
                technical_sheet_url=data.get('technical_sheet_url')
            )

            return product

        except requests.exceptions.RequestException:
            return None

    # === PRICES AND STOCK ===

    def get_prices_and_stocks(
        self,
        product_references: List[str]
    ) -> List[ProductWithPricing]:
        """
        Récupère les prix et stocks pour une liste de produits

        Args:
            product_references: Liste de références produits

        Returns:
            Liste de produits avec prix et stock
        """
        data = self._make_request(
            'POST',
            '/pricing/bulk',
            json={'references': product_references}
        )

        results = []
        for item in data.get('products', []):
            # Parse product (simplifié)
            brand = Brand(
                id=item['brand']['id'],
                name=item['brand']['name']
            )

            product = Product(
                id=item['id'],
                ean=item.get('ean', ''),
                reference=item['reference'],
                description=item['description'],
                brand=brand
            )

            # Parse price
            price_data = item.get('price')
            price = None
            if price_data:
                price = Price(
                    net_price=price_data['net_price'],
                    gross_price=price_data['gross_price'],
                    currency=price_data.get('currency', 'EUR'),
                    unit=price_data.get('unit', 'PCE'),
                    discount_rate=price_data.get('discount_rate', 0.0)
                )

            # Parse stock
            stock_data = item.get('stock')
            stock = None
            if stock_data:
                stock = Stock(
                    quantity=stock_data['quantity'],
                    stock_type=StockType(stock_data.get('type', 'AVAILABLE')),
                    location=stock_data.get('location', '')
                )

            results.append(ProductWithPricing(
                product=product,
                price=price,
                stock=stock
            ))

        return results

    # === ORDERS ===

    def create_order(
        self,
        order_lines: List[Dict[str, Any]],
        order_type: OrderType = OrderType.STANDARD,
        customer_reference: Optional[str] = None,
        delivery_address: Optional[str] = None,
        notes: Optional[str] = None
    ) -> Order:
        """
        Crée une nouvelle commande

        Args:
            order_lines: Liste de lignes de commande
                Format: [{'reference': 'REF123', 'quantity': 10}, ...]
            order_type: Type de commande
            customer_reference: Référence client
            delivery_address: Adresse de livraison
            notes: Notes sur la commande

        Returns:
            Commande créée
        """
        payload = {
            'order_type': order_type.value,
            'lines': order_lines
        }

        if customer_reference:
            payload['customer_reference'] = customer_reference
        if delivery_address:
            payload['delivery_address'] = delivery_address
        if notes:
            payload['notes'] = notes

        data = self._make_request('POST', '/orders', json=payload)

        # Parse order lines
        lines = []
        for line_data in data.get('lines', []):
            lines.append(OrderLine(
                product_id=line_data['product_id'],
                product_reference=line_data['product_reference'],
                product_description=line_data['product_description'],
                quantity=line_data['quantity'],
                unit_price=line_data['unit_price'],
                total_price=line_data['total_price'],
                line_number=line_data.get('line_number', 0),
                discount_rate=line_data.get('discount_rate', 0.0)
            ))

        # Parse order
        order = Order(
            order_number=data['order_number'],
            order_type=OrderType(data['order_type']),
            status=OrderStatus(data['status']),
            lines=lines,
            total_amount=data['total_amount'],
            order_date=datetime.fromisoformat(data['order_date']),
            customer_reference=data.get('customer_reference'),
            delivery_address=data.get('delivery_address'),
            notes=data.get('notes')
        )

        return order

    def get_order(self, order_number: str) -> Optional[Order]:
        """
        Récupère une commande par son numéro

        Args:
            order_number: Numéro de commande

        Returns:
            Commande ou None si non trouvée
        """
        try:
            data = self._make_request('GET', f'/orders/{order_number}')

            # Parse order lines
            lines = []
            for line_data in data.get('lines', []):
                lines.append(OrderLine(
                    product_id=line_data['product_id'],
                    product_reference=line_data['product_reference'],
                    product_description=line_data['product_description'],
                    quantity=line_data['quantity'],
                    unit_price=line_data['unit_price'],
                    total_price=line_data['total_price'],
                    line_number=line_data.get('line_number', 0),
                    discount_rate=line_data.get('discount_rate', 0.0)
                ))

            # Parse order
            order = Order(
                order_number=data['order_number'],
                order_type=OrderType(data['order_type']),
                status=OrderStatus(data['status']),
                lines=lines,
                total_amount=data['total_amount'],
                order_date=datetime.fromisoformat(data['order_date']),
                customer_reference=data.get('customer_reference'),
                delivery_address=data.get('delivery_address'),
                notes=data.get('notes')
            )

            return order

        except requests.exceptions.RequestException:
            return None

    # === DELIVERY NOTES ===

    def get_delivery_notes(
        self,
        order_number: Optional[str] = None,
        from_date: Optional[datetime] = None,
        to_date: Optional[datetime] = None
    ) -> List[DeliveryNote]:
        """
        Récupère les bons de livraison

        Args:
            order_number: Filtrer par numéro de commande
            from_date: Date de début
            to_date: Date de fin

        Returns:
            Liste de bons de livraison
        """
        params = {}

        if order_number:
            params['order_number'] = order_number
        if from_date:
            params['from_date'] = from_date.isoformat()
        if to_date:
            params['to_date'] = to_date.isoformat()

        data = self._make_request('GET', '/delivery-notes', params=params)

        delivery_notes = []
        for item in data.get('delivery_notes', []):
            # Parse lines
            lines = []
            for line_data in item.get('lines', []):
                lines.append(OrderLine(
                    product_id=line_data['product_id'],
                    product_reference=line_data['product_reference'],
                    product_description=line_data['product_description'],
                    quantity=line_data['quantity'],
                    unit_price=line_data.get('unit_price', 0.0),
                    total_price=line_data.get('total_price', 0.0),
                    line_number=line_data.get('line_number', 0)
                ))

            delivery_note = DeliveryNote(
                delivery_note_number=item['delivery_note_number'],
                order_number=item['order_number'],
                delivery_date=datetime.fromisoformat(item['delivery_date']),
                lines=lines,
                total_delivered=item['total_delivered'],
                carrier=item.get('carrier'),
                tracking_number=item.get('tracking_number')
            )

            delivery_notes.append(delivery_note)

        return delivery_notes

    def close(self):
        """Ferme la session HTTP"""
        self.session.close()
