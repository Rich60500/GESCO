"""
GESCO v5.0 - Modèles de données Axonaut
Classes pour manipuler les données de l'API Axonaut
"""

from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any
from datetime import datetime


@dataclass
class BusinessManager:
    """Responsable commercial d'une entreprise"""
    id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'BusinessManager':
        """Crée une instance depuis un dictionnaire"""
        if not data:
            return cls()
        return cls(
            id=data.get('id'),
            name=data.get('name'),
            email=data.get('email')
        )

    def to_dict(self) -> dict:
        """Convertit en dictionnaire"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }


@dataclass
class Category:
    """Catégorie d'entreprise"""
    id: Optional[int] = None
    name: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'Category':
        """Crée une instance depuis un dictionnaire"""
        if not data:
            return cls()
        return cls(
            id=data.get('id'),
            name=data.get('name')
        )

    def to_dict(self) -> dict:
        """Convertit en dictionnaire"""
        return {
            'id': self.id,
            'name': self.name
        }


@dataclass
class Address:
    """Adresse de chantier liée à une entreprise"""
    id: Optional[int] = None
    company_id: Optional[int] = None
    name: Optional[str] = None  # Nom de l'adresse (ex: "Chantier Paris Nord")
    contact_name: Optional[str] = None
    street: Optional[str] = None
    zip_code: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = "France"
    phone: Optional[str] = None
    email: Optional[str] = None
    comments: Optional[str] = None
    custom_fields: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict) -> 'Address':
        """Crée une instance depuis un dictionnaire"""
        if not data:
            return cls()
        return cls(
            id=data.get('id'),
            company_id=data.get('company_id'),
            name=data.get('name'),
            contact_name=data.get('contact_name'),
            street=data.get('street'),
            zip_code=data.get('zip_code'),
            city=data.get('city'),
            country=data.get('country', 'France'),
            phone=data.get('phone'),
            email=data.get('email'),
            comments=data.get('comments'),
            custom_fields=data.get('custom_fields', {})
        )

    def to_dict(self, for_api: bool = False) -> dict:
        """
        Convertit en dictionnaire

        Args:
            for_api: Si True, utilise le format attendu par l'API (POST/PATCH)
        """
        result = {
            'name': self.name,
            'contact_name': self.contact_name,
            'street': self.street,
            'zip_code': self.zip_code,
            'city': self.city,
            'country': self.country,
            'phone': self.phone,
            'email': self.email,
            'comments': self.comments
        }

        if self.custom_fields:
            result['custom_fields'] = self.custom_fields

        if not for_api:
            result['id'] = self.id
            result['company_id'] = self.company_id

        return result

    @property
    def full_address(self) -> str:
        """Retourne l'adresse complète formatée"""
        parts = []
        if self.name:
            parts.append(f"📍 {self.name}")
        if self.street:
            parts.append(self.street)
        if self.zip_code or self.city:
            city_line = []
            if self.zip_code:
                city_line.append(self.zip_code)
            if self.city:
                city_line.append(self.city)
            parts.append(' '.join(city_line))
        if self.country:
            parts.append(self.country)
        return '\n'.join(parts) if parts else 'Pas d\'adresse'

    @property
    def short_label(self) -> str:
        """Retourne un libellé court pour affichage"""
        if self.name:
            return f"{self.name} ({self.city or 'N/A'})"
        elif self.city:
            return self.city
        return "Adresse sans nom"


@dataclass
class Employee:
    """Contact/Employé d'une entreprise"""
    id: Optional[int] = None
    gender: Optional[int] = None  # 1=M, 2=F
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    cellphone_number: Optional[str] = None
    job: Optional[str] = None
    is_billing_contact: bool = False
    company_id: Optional[int] = None
    custom_fields: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: dict) -> 'Employee':
        """Crée une instance depuis un dictionnaire"""
        return cls(
            id=data.get('id'),
            gender=data.get('gender'),
            firstname=data.get('firstname'),
            lastname=data.get('lastname'),
            email=data.get('email'),
            phone_number=data.get('phone_number'),
            cellphone_number=data.get('cellphone_number'),
            job=data.get('job'),
            is_billing_contact=data.get('is_billing_contact', False),
            company_id=data.get('company_id'),
            custom_fields=data.get('custom_fields', {})
        )

    def to_dict(self, for_api: bool = False) -> dict:
        """
        Convertit en dictionnaire

        Args:
            for_api: Si True, utilise le format attendu par l'API (POST/PATCH)
        """
        result = {
            'firstname': self.firstname,
            'lastname': self.lastname,
            'email': self.email,
            'job': self.job,
            'is_billing_contact': self.is_billing_contact
        }

        if for_api:
            # Format API pour POST/PATCH
            if self.phone_number:
                result['phoneNumber'] = self.phone_number
            if self.cellphone_number:
                result['cellphoneNumber'] = self.cellphone_number
        else:
            # Format interne
            result['id'] = self.id
            result['gender'] = self.gender
            result['phone_number'] = self.phone_number
            result['cellphone_number'] = self.cellphone_number
            result['company_id'] = self.company_id

        if self.custom_fields:
            result['custom_fields'] = self.custom_fields

        return result

    @property
    def full_name(self) -> str:
        """Retourne le nom complet"""
        parts = []
        if self.firstname:
            parts.append(self.firstname)
        if self.lastname:
            parts.append(self.lastname)
        return ' '.join(parts) if parts else 'Sans nom'


@dataclass
class Company:
    """Entreprise/Client/Prospect Axonaut"""
    id: Optional[int] = None
    name: Optional[str] = None
    creation_date: Optional[str] = None
    address_contact_name: Optional[str] = None
    address_street: Optional[str] = None
    address_zip_code: Optional[str] = None
    address_city: Optional[str] = None
    address_country: Optional[str] = "France"
    comments: Optional[str] = None
    is_prospect: bool = False
    is_customer: bool = False
    isB2C: bool = False
    currency: str = "EUR"
    language: str = "fr"
    thirdparty_code: Optional[str] = None
    supplier_thirdparty_code: Optional[str] = None
    intracommunity_number: Optional[str] = None
    iban: Optional[str] = None
    bic: Optional[str] = None
    siret: Optional[str] = None
    internal_id: Optional[str] = None
    business_manager: Optional[BusinessManager] = None
    custom_fields: Dict[str, Any] = field(default_factory=dict)
    categories: Optional[Category] = None
    employees: List[Employee] = field(default_factory=list)
    documents: List[int] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict) -> 'Company':
        """Crée une instance depuis un dictionnaire"""
        # Business manager
        business_manager = None
        if data.get('business_manager'):
            business_manager = BusinessManager.from_dict(data['business_manager'])

        # Categories
        categories = None
        if data.get('categories'):
            categories = Category.from_dict(data['categories'])

        # Employees
        employees = []
        if data.get('employees'):
            employees = [Employee.from_dict(emp) for emp in data['employees']]

        return cls(
            id=data.get('id'),
            name=data.get('name'),
            creation_date=data.get('creation_date'),
            address_contact_name=data.get('address_contact_name'),
            address_street=data.get('address_street'),
            address_zip_code=data.get('address_zip_code'),
            address_city=data.get('address_city'),
            address_country=data.get('address_country', 'France'),
            comments=data.get('comments'),
            is_prospect=data.get('is_prospect', False),
            is_customer=data.get('is_customer', False),
            isB2C=data.get('isB2C', False),
            currency=data.get('currency', 'EUR'),
            language=data.get('language', 'fr'),
            thirdparty_code=data.get('thirdparty_code'),
            supplier_thirdparty_code=data.get('supplier_thirdparty_code'),
            intracommunity_number=data.get('intracommunity_number'),
            iban=data.get('iban'),
            bic=data.get('bic'),
            siret=data.get('siret'),
            internal_id=data.get('internal_id'),
            business_manager=business_manager,
            custom_fields=data.get('custom_fields', {}),
            categories=categories,
            employees=employees,
            documents=data.get('documents', [])
        )

    def to_dict(self, for_api: bool = False) -> dict:
        """
        Convertit en dictionnaire

        Args:
            for_api: Si True, utilise le format attendu par l'API (POST/PATCH)
        """
        result = {
            'name': self.name,
            'address_contact_name': self.address_contact_name,
            'address_street': self.address_street,
            'address_zip_code': self.address_zip_code,
            'address_city': self.address_city,
            'address_country': self.address_country,
            'is_prospect': self.is_prospect,
            'is_customer': self.is_customer,
            'isB2C': self.isB2C,
            'currency': self.currency,
            'language': self.language,
            'comments': self.comments
        }

        # Champs optionnels
        optional_fields = [
            'thirdparty_code', 'intracommunity_number', 'iban',
            'bic', 'siret', 'internal_id'
        ]
        for field_name in optional_fields:
            value = getattr(self, field_name)
            if value:
                result[field_name] = value

        # Custom fields
        if self.custom_fields:
            result['custom_fields'] = self.custom_fields

        # Business manager
        if self.business_manager and self.business_manager.email:
            result['business_manager'] = self.business_manager.email

        # Categories
        if self.categories and self.categories.name:
            result['categories'] = [self.categories.name]

        # Employees (uniquement pour POST)
        if for_api and self.employees:
            result['employees'] = [emp.to_dict(for_api=True) for emp in self.employees]

        if not for_api:
            # Inclure les champs en lecture seule
            result['id'] = self.id
            result['creation_date'] = self.creation_date
            if self.business_manager:
                result['business_manager'] = self.business_manager.to_dict()
            if self.categories:
                result['categories'] = self.categories.to_dict()
            result['documents'] = self.documents

        return result

    @property
    def full_address(self) -> str:
        """Retourne l'adresse complète formatée"""
        parts = []
        if self.address_street:
            parts.append(self.address_street)
        if self.address_zip_code or self.address_city:
            city_line = []
            if self.address_zip_code:
                city_line.append(self.address_zip_code)
            if self.address_city:
                city_line.append(self.address_city)
            parts.append(' '.join(city_line))
        if self.address_country:
            parts.append(self.address_country)
        return '\n'.join(parts) if parts else 'Pas d\'adresse'

    @property
    def type_label(self) -> str:
        """Retourne le type de tiers"""
        if self.is_customer and self.is_prospect:
            return "Client / Prospect"
        elif self.is_customer:
            return "Client"
        elif self.is_prospect:
            return "Prospect"
        else:
            return "Tiers"

    @property
    def b2c_label(self) -> str:
        """Retourne le type B2B/B2C"""
        return "B2C" if self.isB2C else "B2B"
