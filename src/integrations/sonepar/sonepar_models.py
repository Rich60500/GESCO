"""
GESCO v5.0 - Modèles de données Sonepar
Structures de données pour l'API Sonepar
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import List, Optional


class ProductStatus(Enum):
    """Statut d'un produit"""
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DISCONTINUED = "DISCONTINUED"


class OrderType(Enum):
    """Type de commande"""
    STANDARD = "STANDARD"
    EXPRESS = "EXPRESS"
    DEPOT = "DEPOT"


class StockType(Enum):
    """Type de stock"""
    AVAILABLE = "AVAILABLE"
    RESERVED = "RESERVED"
    ON_ORDER = "ON_ORDER"


class OrderStatus(Enum):
    """Statut d'une commande"""
    DRAFT = "DRAFT"
    SUBMITTED = "SUBMITTED"
    CONFIRMED = "CONFIRMED"
    IN_PREPARATION = "IN_PREPARATION"
    READY = "READY"
    DELIVERED = "DELIVERED"
    CANCELLED = "CANCELLED"


@dataclass
class Brand:
    """Marque de produits"""
    id: str
    name: str
    logo_url: Optional[str] = None


@dataclass
class Stock:
    """Information de stock"""
    quantity: int
    stock_type: StockType
    location: str = ""
    last_updated: Optional[datetime] = None


@dataclass
class Price:
    """Information de prix"""
    net_price: float
    gross_price: float
    currency: str = "EUR"
    unit: str = "PCE"
    discount_rate: float = 0.0
    valid_from: Optional[datetime] = None
    valid_to: Optional[datetime] = None


@dataclass
class Product:
    """Produit du catalogue Sonepar"""
    id: str
    ean: str
    reference: str
    description: str
    brand: Brand
    family: str = ""
    subfamily: str = ""
    status: ProductStatus = ProductStatus.ACTIVE
    weight: Optional[float] = None
    unit: str = "PCE"
    packaging: int = 1
    image_url: Optional[str] = None
    technical_sheet_url: Optional[str] = None


@dataclass
class ProductWithPricing:
    """Produit avec informations de prix et stock"""
    product: Product
    price: Optional[Price] = None
    stock: Optional[Stock] = None


@dataclass
class OrderLine:
    """Ligne de commande"""
    product_id: str
    product_reference: str
    product_description: str
    quantity: int
    unit_price: float
    total_price: float
    line_number: int = 0
    discount_rate: float = 0.0


@dataclass
class Order:
    """Commande Sonepar"""
    order_number: str
    order_type: OrderType
    status: OrderStatus
    lines: List[OrderLine]
    total_amount: float
    order_date: datetime
    customer_reference: Optional[str] = None
    delivery_address: Optional[str] = None
    notes: Optional[str] = None
    expected_delivery_date: Optional[datetime] = None


@dataclass
class DeliveryNote:
    """Bon de livraison"""
    delivery_note_number: str
    order_number: str
    delivery_date: datetime
    lines: List[OrderLine]
    total_delivered: int
    carrier: Optional[str] = None
    tracking_number: Optional[str] = None


@dataclass
class ChantierOrder:
    """Liaison entre une commande Sonepar et un chantier GESCO"""
    chantier_id: int
    chantier_name: str
    order_number: str
    order_date: datetime
    total_amount: float
    status: OrderStatus
    notes: Optional[str] = None
