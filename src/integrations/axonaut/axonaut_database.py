"""
GESCO v5.0 - Base de données Axonaut
Gestion de la base de données locale pour les tiers/clients/contacts
"""

import sqlite3
import json
from pathlib import Path
from typing import List, Optional, Dict, Any
from datetime import datetime

from .axonaut_models import Company, Employee, Address


class AxonautDatabase:
    """Gestionnaire de base de données pour Axonaut"""

    def __init__(self, db_path: Optional[str] = None):
        """
        Initialise la base de données

        Args:
            db_path: Chemin vers le fichier de base de données
        """
        if db_path is None:
            data_dir = Path.home() / ".gesco" / "data"
            data_dir.mkdir(parents=True, exist_ok=True)
            db_path = str(data_dir / "axonaut.db")

        self.db_path = db_path
        self.init_database()

    def get_connection(self) -> sqlite3.Connection:
        """Retourne une connexion à la base de données"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_database(self):
        """Initialise les tables de la base de données"""
        conn = self.get_connection()
        cursor = conn.cursor()

        # Table des entreprises (cache local)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS companies (
                id INTEGER PRIMARY KEY,
                axonaut_id INTEGER UNIQUE,
                name TEXT NOT NULL,
                creation_date TEXT,
                address_contact_name TEXT,
                address_street TEXT,
                address_zip_code TEXT,
                address_city TEXT,
                address_country TEXT,
                comments TEXT,
                is_prospect INTEGER DEFAULT 0,
                is_customer INTEGER DEFAULT 0,
                isB2C INTEGER DEFAULT 0,
                currency TEXT DEFAULT 'EUR',
                language TEXT DEFAULT 'fr',
                thirdparty_code TEXT,
                supplier_thirdparty_code TEXT,
                intracommunity_number TEXT,
                iban TEXT,
                bic TEXT,
                siret TEXT,
                internal_id TEXT,
                business_manager_data TEXT,
                custom_fields TEXT,
                categories_data TEXT,
                last_sync TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Table des employés/contacts
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY,
                axonaut_id INTEGER UNIQUE,
                company_id INTEGER,
                axonaut_company_id INTEGER,
                gender INTEGER,
                firstname TEXT,
                lastname TEXT,
                email TEXT,
                phone_number TEXT,
                cellphone_number TEXT,
                job TEXT,
                is_billing_contact INTEGER DEFAULT 0,
                custom_fields TEXT,
                last_sync TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE CASCADE
            )
        """)

        # Table des adresses de chantier
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS addresses (
                id INTEGER PRIMARY KEY,
                axonaut_id INTEGER UNIQUE,
                company_id INTEGER,
                axonaut_company_id INTEGER,
                name TEXT,
                contact_name TEXT,
                street TEXT,
                zip_code TEXT,
                city TEXT,
                country TEXT DEFAULT 'France',
                phone TEXT,
                email TEXT,
                comments TEXT,
                custom_fields TEXT,
                last_sync TEXT,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (company_id) REFERENCES companies(id) ON DELETE CASCADE
            )
        """)

        # Index pour les recherches
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_companies_name ON companies(name)
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_companies_type ON companies(is_customer, is_prospect)
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_employees_company ON employees(company_id)
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_addresses_company ON addresses(company_id)
        """)

        conn.commit()
        conn.close()

    # ==================== COMPANIES ====================

    def save_company(self, company: Company) -> int:
        """
        Sauvegarde ou met à jour une entreprise

        Args:
            company: Objet Company

        Returns:
            ID local de l'entreprise
        """
        conn = self.get_connection()
        cursor = conn.cursor()

        # Préparer les données JSON
        business_manager_data = json.dumps(company.business_manager.to_dict()) if company.business_manager else None
        categories_data = json.dumps(company.categories.to_dict()) if company.categories else None
        custom_fields = json.dumps(company.custom_fields) if company.custom_fields else None

        # Vérifier si l'entreprise existe déjà
        if company.id:
            cursor.execute("SELECT id FROM companies WHERE axonaut_id = ?", (company.id,))
            existing = cursor.fetchone()

            if existing:
                # Mise à jour
                cursor.execute("""
                    UPDATE companies SET
                        name = ?, creation_date = ?, address_contact_name = ?,
                        address_street = ?, address_zip_code = ?, address_city = ?,
                        address_country = ?, comments = ?, is_prospect = ?,
                        is_customer = ?, isB2C = ?, currency = ?, language = ?,
                        thirdparty_code = ?, supplier_thirdparty_code = ?,
                        intracommunity_number = ?, iban = ?, bic = ?, siret = ?,
                        internal_id = ?, business_manager_data = ?, custom_fields = ?,
                        categories_data = ?, last_sync = ?, updated_at = CURRENT_TIMESTAMP
                    WHERE axonaut_id = ?
                """, (
                    company.name, company.creation_date, company.address_contact_name,
                    company.address_street, company.address_zip_code, company.address_city,
                    company.address_country, company.comments, int(company.is_prospect or False),
                    int(company.is_customer or False), int(company.isB2C or False), company.currency,
                    company.language, company.thirdparty_code, company.supplier_thirdparty_code,
                    company.intracommunity_number, company.iban, company.bic, company.siret,
                    company.internal_id, business_manager_data, custom_fields,
                    categories_data, datetime.now().isoformat(), company.id
                ))
                local_id = existing['id']
            else:
                # Insertion
                cursor.execute("""
                    INSERT INTO companies (
                        axonaut_id, name, creation_date, address_contact_name,
                        address_street, address_zip_code, address_city, address_country,
                        comments, is_prospect, is_customer, isB2C, currency, language,
                        thirdparty_code, supplier_thirdparty_code, intracommunity_number,
                        iban, bic, siret, internal_id, business_manager_data,
                        custom_fields, categories_data, last_sync
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    company.id, company.name, company.creation_date, company.address_contact_name,
                    company.address_street, company.address_zip_code, company.address_city,
                    company.address_country, company.comments, int(company.is_prospect or False),
                    int(company.is_customer or False), int(company.isB2C or False), company.currency,
                    company.language, company.thirdparty_code, company.supplier_thirdparty_code,
                    company.intracommunity_number, company.iban, company.bic, company.siret,
                    company.internal_id, business_manager_data, custom_fields,
                    categories_data, datetime.now().isoformat()
                ))
                local_id = cursor.lastrowid
        else:
            # Nouvelle entreprise sans ID Axonaut (sera créée plus tard)
            cursor.execute("""
                INSERT INTO companies (
                    name, address_contact_name, address_street, address_zip_code,
                    address_city, address_country, comments, is_prospect, is_customer,
                    isB2C, currency, language, thirdparty_code, intracommunity_number,
                    iban, bic, siret, internal_id, custom_fields
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                company.name, company.address_contact_name, company.address_street,
                company.address_zip_code, company.address_city, company.address_country,
                company.comments, int(company.is_prospect or False), int(company.is_customer or False),
                int(company.isB2C or False), company.currency, company.language,
                company.thirdparty_code, company.intracommunity_number, company.iban,
                company.bic, company.siret, company.internal_id, custom_fields
            ))
            local_id = cursor.lastrowid

        conn.commit()
        conn.close()

        # Sauvegarder les employés
        if company.employees:
            for employee in company.employees:
                # Utiliser l'ID local pour la relation company_id
                self.save_employee(employee, company_local_id=local_id)

        return local_id

    def get_companies(self,
                     is_customer: Optional[bool] = None,
                     is_prospect: Optional[bool] = None,
                     search: Optional[str] = None) -> List[Company]:
        """
        Récupère les entreprises avec filtres

        Args:
            is_customer: Filtrer par clients
            is_prospect: Filtrer par prospects
            search: Terme de recherche

        Returns:
            Liste des entreprises
        """
        conn = self.get_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM companies WHERE 1=1"
        params = []

        if is_customer is not None:
            query += " AND is_customer = ?"
            params.append(int(is_customer))

        if is_prospect is not None:
            query += " AND is_prospect = ?"
            params.append(int(is_prospect))

        if search:
            query += " AND (name LIKE ? OR address_city LIKE ? OR siret LIKE ?)"
            search_pattern = f"%{search}%"
            params.extend([search_pattern, search_pattern, search_pattern])

        query += " ORDER BY name"

        cursor.execute(query, params)
        rows = cursor.fetchall()

        companies = []
        for row in rows:
            company = self._row_to_company(row)
            # Charger les employés
            company.employees = self.get_company_employees(row['id'])
            companies.append(company)

        conn.close()
        return companies

    def get_company(self, company_id: int) -> Optional[Company]:
        """
        Récupère une entreprise par son ID local

        Args:
            company_id: ID local de l'entreprise

        Returns:
            Entreprise ou None
        """
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM companies WHERE id = ?", (company_id,))
        row = cursor.fetchone()

        if not row:
            conn.close()
            return None

        company = self._row_to_company(row)
        company.employees = self.get_company_employees(company_id)

        conn.close()
        return company

    def _row_to_company(self, row: sqlite3.Row) -> Company:
        """Convertit une ligne SQL en objet Company"""
        from .axonaut_models import BusinessManager, Category

        # Désérialiser les données JSON
        business_manager = None
        if row['business_manager_data']:
            business_manager = BusinessManager.from_dict(json.loads(row['business_manager_data']))

        categories = None
        if row['categories_data']:
            categories = Category.from_dict(json.loads(row['categories_data']))

        custom_fields = {}
        if row['custom_fields']:
            custom_fields = json.loads(row['custom_fields'])

        return Company(
            id=row['axonaut_id'],
            name=row['name'],
            creation_date=row['creation_date'],
            address_contact_name=row['address_contact_name'],
            address_street=row['address_street'],
            address_zip_code=row['address_zip_code'],
            address_city=row['address_city'],
            address_country=row['address_country'],
            comments=row['comments'],
            is_prospect=bool(row['is_prospect']),
            is_customer=bool(row['is_customer']),
            isB2C=bool(row['isB2C']),
            currency=row['currency'],
            language=row['language'],
            thirdparty_code=row['thirdparty_code'],
            supplier_thirdparty_code=row['supplier_thirdparty_code'],
            intracommunity_number=row['intracommunity_number'],
            iban=row['iban'],
            bic=row['bic'],
            siret=row['siret'],
            internal_id=row['internal_id'],
            business_manager=business_manager,
            custom_fields=custom_fields,
            categories=categories
        )

    # ==================== EMPLOYEES ====================

    def save_employee(self, employee: Employee, company_local_id: Optional[int] = None) -> int:
        """
        Sauvegarde ou met à jour un employé

        Args:
            employee: Objet Employee
            company_local_id: ID local de l'entreprise (si différent de employee.company_id)

        Returns:
            ID local de l'employé
        """
        conn = self.get_connection()
        cursor = conn.cursor()

        custom_fields = json.dumps(employee.custom_fields) if employee.custom_fields else None

        # Utiliser company_local_id si fourni, sinon employee.company_id
        local_company_id = company_local_id if company_local_id is not None else employee.company_id

        if employee.id:
            cursor.execute("SELECT id FROM employees WHERE axonaut_id = ?", (employee.id,))
            existing = cursor.fetchone()

            if existing:
                # Mise à jour - ne pas changer company_id
                cursor.execute("""
                    UPDATE employees SET
                        gender = ?, firstname = ?, lastname = ?, email = ?,
                        phone_number = ?, cellphone_number = ?, job = ?,
                        is_billing_contact = ?, custom_fields = ?,
                        last_sync = ?, updated_at = CURRENT_TIMESTAMP
                    WHERE axonaut_id = ?
                """, (
                    employee.gender, employee.firstname, employee.lastname, employee.email,
                    employee.phone_number, employee.cellphone_number, employee.job,
                    int(employee.is_billing_contact or False), custom_fields,
                    datetime.now().isoformat(), employee.id
                ))
                local_id = existing['id']
            else:
                # Insertion avec ID Axonaut
                cursor.execute("""
                    INSERT INTO employees (
                        axonaut_id, company_id, axonaut_company_id, gender, firstname, lastname, email,
                        phone_number, cellphone_number, job, is_billing_contact,
                        custom_fields, last_sync
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    employee.id, local_company_id, employee.company_id, employee.gender, employee.firstname,
                    employee.lastname, employee.email, employee.phone_number,
                    employee.cellphone_number, employee.job, int(employee.is_billing_contact or False),
                    custom_fields, datetime.now().isoformat()
                ))
                local_id = cursor.lastrowid
        else:
            # Nouvelle employee sans ID Axonaut
            cursor.execute("""
                INSERT INTO employees (
                    company_id, gender, firstname, lastname, email, phone_number,
                    cellphone_number, job, is_billing_contact, custom_fields
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                local_company_id, employee.gender, employee.firstname, employee.lastname,
                employee.email, employee.phone_number, employee.cellphone_number,
                employee.job, int(employee.is_billing_contact or False), custom_fields
            ))
            local_id = cursor.lastrowid

        conn.commit()
        conn.close()
        return local_id

    def get_company_employees(self, company_id: int) -> List[Employee]:
        """
        Récupère les employés d'une entreprise

        Args:
            company_id: ID local de l'entreprise

        Returns:
            Liste des employés
        """
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM employees WHERE company_id = ?", (company_id,))
        rows = cursor.fetchall()

        employees = [self._row_to_employee(row) for row in rows]

        conn.close()
        return employees

    def _row_to_employee(self, row: sqlite3.Row) -> Employee:
        """Convertit une ligne SQL en objet Employee"""
        custom_fields = {}
        if row['custom_fields']:
            custom_fields = json.loads(row['custom_fields'])

        return Employee(
            id=row['axonaut_id'],
            gender=row['gender'],
            firstname=row['firstname'],
            lastname=row['lastname'],
            email=row['email'],
            phone_number=row['phone_number'],
            cellphone_number=row['cellphone_number'],
            job=row['job'],
            is_billing_contact=bool(row['is_billing_contact']),
            company_id=row['company_id'],
            custom_fields=custom_fields
        )

    def delete_company(self, company_id: int):
        """Supprime une entreprise et ses employés (cascade)"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM companies WHERE id = ?", (company_id,))
        conn.commit()
        conn.close()

    # ==================== ADDRESSES ====================

    def save_address(self, address: Address, company_local_id: Optional[int] = None) -> int:
        """
        Sauvegarde ou met à jour une adresse

        Args:
            address: Objet Address
            company_local_id: ID local de l'entreprise (optionnel)

        Returns:
            ID local de l'adresse
        """
        conn = self.get_connection()
        cursor = conn.cursor()

        custom_fields = json.dumps(address.custom_fields) if address.custom_fields else None

        if address.id:
            cursor.execute("SELECT id FROM addresses WHERE axonaut_id = ?", (address.id,))
            existing = cursor.fetchone()

            if existing:
                # Mise à jour
                cursor.execute("""
                    UPDATE addresses SET
                        name = ?, contact_name = ?, street = ?, zip_code = ?,
                        city = ?, country = ?, phone = ?, email = ?,
                        comments = ?, custom_fields = ?,
                        last_sync = ?, updated_at = CURRENT_TIMESTAMP
                    WHERE axonaut_id = ?
                """, (
                    address.name, address.contact_name, address.street, address.zip_code,
                    address.city, address.country, address.phone, address.email,
                    address.comments, custom_fields,
                    datetime.now().isoformat(), address.id
                ))
                local_id = existing['id']
            else:
                # Insertion avec ID Axonaut
                cursor.execute("""
                    INSERT INTO addresses (
                        axonaut_id, company_id, axonaut_company_id, name, contact_name,
                        street, zip_code, city, country, phone, email,
                        comments, custom_fields, last_sync
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    address.id, company_local_id, address.company_id, address.name,
                    address.contact_name, address.street, address.zip_code, address.city,
                    address.country, address.phone, address.email,
                    address.comments, custom_fields, datetime.now().isoformat()
                ))
                local_id = cursor.lastrowid
        else:
            # Nouvelle adresse sans ID Axonaut
            cursor.execute("""
                INSERT INTO addresses (
                    company_id, name, contact_name, street, zip_code,
                    city, country, phone, email, comments, custom_fields
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                company_local_id, address.name, address.contact_name, address.street,
                address.zip_code, address.city, address.country, address.phone,
                address.email, address.comments, custom_fields
            ))
            local_id = cursor.lastrowid

        conn.commit()
        conn.close()
        return local_id

    def get_company_addresses(self, company_id: int) -> List[Address]:
        """
        Récupère les adresses d'une entreprise

        Args:
            company_id: ID local de l'entreprise

        Returns:
            Liste des adresses
        """
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM addresses WHERE company_id = ? ORDER BY name", (company_id,))
        rows = cursor.fetchall()

        addresses = [self._row_to_address(row) for row in rows]

        conn.close()
        return addresses

    def get_address(self, address_id: int) -> Optional[Address]:
        """
        Récupère une adresse par son ID local

        Args:
            address_id: ID local de l'adresse

        Returns:
            Adresse ou None
        """
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM addresses WHERE id = ?", (address_id,))
        row = cursor.fetchone()

        conn.close()

        if not row:
            return None

        return self._row_to_address(row)

    def get_all_addresses(self) -> List[Address]:
        """
        Récupère toutes les adresses

        Returns:
            Liste de toutes les adresses
        """
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM addresses ORDER BY city, name")
        rows = cursor.fetchall()

        addresses = [self._row_to_address(row) for row in rows]

        conn.close()
        return addresses

    def _row_to_address(self, row: sqlite3.Row) -> Address:
        """Convertit une ligne SQL en objet Address"""
        custom_fields = {}
        if row['custom_fields']:
            custom_fields = json.loads(row['custom_fields'])

        return Address(
            id=row['axonaut_id'],
            company_id=row['axonaut_company_id'] or row['company_id'],
            name=row['name'],
            contact_name=row['contact_name'],
            street=row['street'],
            zip_code=row['zip_code'],
            city=row['city'],
            country=row['country'],
            phone=row['phone'],
            email=row['email'],
            comments=row['comments'],
            custom_fields=custom_fields
        )

    def delete_address(self, address_id: int):
        """Supprime une adresse"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM addresses WHERE id = ?", (address_id,))
        conn.commit()
        conn.close()
