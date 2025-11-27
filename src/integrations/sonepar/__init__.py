"""
GESCO v5.0 - Intégration Sonepar
Client API pour Sonepar (fournisseur électrique)
"""

from .sonepar_models import (
    Brand, Product, ProductWithPricing, Stock, Price,
    Order, OrderLine, DeliveryNote, ProductStatus,
    OrderType, StockType, OrderStatus
)
from .sonepar_config import SoneParConfig
from .sonepar_client import SoneParClient
from .sonepar_database import SoneParDatabase

__all__ = [
    'Brand', 'Product', 'ProductWithPricing', 'Stock', 'Price',
    'Order', 'OrderLine', 'DeliveryNote', 'ProductStatus',
    'OrderType', 'StockType', 'OrderStatus',
    'SoneParConfig', 'SoneParClient', 'SoneParDatabase'
]
