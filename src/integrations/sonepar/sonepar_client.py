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

    def __init__(self, config: Optional[SoneParConfig] = None):
        """
        Initialise le client API

        Args:
            config: Configuration Sonepar (utilise la config par défaut si None)
        """
        self.config = config or SoneParConfig()

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
        limit: int = 50
    ) -> List[Product]:
        """
        Recherche des produits dans le catalogue

        Args:
            query: Terme de recherche
            brand_id: Filtrer par marque
            limit: Nombre maximum de résultats

        Returns:
            Liste de produits
        """
        params = {
            'q': query,
            'limit': limit
        }

        if brand_id:
            params['brand_id'] = brand_id

        data = self._make_request(
            'GET',
            '/catalog/products/search',
            use_catalog_limiter=True,
            params=params
        )

        products = []
        for item in data.get('products', []):
            # Parse brand
            brand_data = item.get('brand', {})
            brand = Brand(
                id=brand_data.get('id', ''),
                name=brand_data.get('name', ''),
                logo_url=brand_data.get('logo_url')
            )

            # Parse product
            product = Product(
                id=item['id'],
                ean=item.get('ean', ''),
                reference=item['reference'],
                description=item['description'],
                brand=brand,
                family=item.get('family', ''),
                subfamily=item.get('subfamily', ''),
                status=ProductStatus(item.get('status', 'ACTIVE')),
                weight=item.get('weight'),
                unit=item.get('unit', 'PCE'),
                packaging=item.get('packaging', 1),
                image_url=item.get('image_url'),
                technical_sheet_url=item.get('technical_sheet_url')
            )

            products.append(product)

        return products

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
