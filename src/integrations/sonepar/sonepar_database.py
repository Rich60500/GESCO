"""
GESCO v5.0 - Base de données Sonepar
Gestion de la liaison entre commandes Sonepar et chantiers GESCO
"""

import sqlite3
from datetime import datetime
from typing import List, Dict, Any, Optional
from pathlib import Path

from .sonepar_models import OrderStatus, ChantierOrder


class SoneParDatabase:
    """Gestionnaire de base de données pour l'intégration Sonepar"""

    def __init__(self, db_path: str = "data/gesco.db"):
        """
        Initialise la connexion à la base de données

        Args:
            db_path: Chemin vers le fichier de base de données
        """
        self.db_path = db_path

        # Créer le répertoire data s'il n'existe pas
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)

        # Initialiser les tables Sonepar
        self._init_sonepar_tables()

    def _get_connection(self) -> sqlite3.Connection:
        """Crée une nouvelle connexion à la base de données"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_sonepar_tables(self):
        """Initialise les tables Sonepar dans la base de données"""
        conn = self._get_connection()
        cursor = conn.cursor()

        # Table des commandes Sonepar liées aux chantiers
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chantier_orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chantier_id INTEGER NOT NULL,
                order_number TEXT NOT NULL,
                order_date TEXT NOT NULL,
                total_amount REAL NOT NULL,
                status TEXT NOT NULL,
                notes TEXT,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                FOREIGN KEY (chantier_id) REFERENCES chantiers(id) ON DELETE CASCADE,
                UNIQUE(order_number)
            )
        """)

        # Table des bons de livraison liés aux chantiers
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chantier_delivery_notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chantier_id INTEGER NOT NULL,
                order_number TEXT NOT NULL,
                delivery_note_number TEXT NOT NULL,
                delivery_date TEXT NOT NULL,
                total_delivered INTEGER NOT NULL,
                carrier TEXT,
                tracking_number TEXT,
                created_at TEXT NOT NULL,
                FOREIGN KEY (chantier_id) REFERENCES chantiers(id) ON DELETE CASCADE,
                FOREIGN KEY (order_number) REFERENCES chantier_orders(order_number) ON DELETE CASCADE,
                UNIQUE(delivery_note_number)
            )
        """)

        # Table des produits commandés par chantier
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chantier_products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chantier_id INTEGER NOT NULL,
                order_number TEXT NOT NULL,
                product_id TEXT NOT NULL,
                product_reference TEXT NOT NULL,
                product_description TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                unit_price REAL NOT NULL,
                total_price REAL NOT NULL,
                line_number INTEGER,
                FOREIGN KEY (chantier_id) REFERENCES chantiers(id) ON DELETE CASCADE,
                FOREIGN KEY (order_number) REFERENCES chantier_orders(order_number) ON DELETE CASCADE
            )
        """)

        # Index pour les recherches fréquentes
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_chantier_orders_chantier
            ON chantier_orders(chantier_id)
        """)

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_chantier_orders_status
            ON chantier_orders(status)
        """)

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_chantier_delivery_chantier
            ON chantier_delivery_notes(chantier_id)
        """)

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_chantier_products_chantier
            ON chantier_products(chantier_id)
        """)

        conn.commit()
        conn.close()

    # === GESTION DES COMMANDES ===

    def link_order_to_chantier(
        self,
        chantier_id: int,
        order_number: str,
        order_date: datetime,
        total_amount: float,
        status: OrderStatus,
        order_lines: List[Dict[str, Any]],
        notes: Optional[str] = None
    ) -> int:
        """
        Lie une commande Sonepar à un chantier GESCO

        Args:
            chantier_id: ID du chantier
            order_number: Numéro de commande Sonepar
            order_date: Date de la commande
            total_amount: Montant total
            status: Statut de la commande
            order_lines: Lignes de commande
            notes: Notes optionnelles

        Returns:
            ID de l'enregistrement créé
        """
        conn = self._get_connection()
        cursor = conn.cursor()

        now = datetime.now().isoformat()

        # Insérer la commande
        cursor.execute("""
            INSERT INTO chantier_orders (
                chantier_id, order_number, order_date, total_amount,
                status, notes, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            chantier_id,
            order_number,
            order_date.isoformat(),
            total_amount,
            status.value,
            notes,
            now,
            now
        ))

        order_id = cursor.lastrowid

        # Insérer les lignes de commande
        for line in order_lines:
            cursor.execute("""
                INSERT INTO chantier_products (
                    chantier_id, order_number, product_id, product_reference,
                    product_description, quantity, unit_price, total_price, line_number
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                chantier_id,
                order_number,
                line.get('product_id', ''),
                line.get('product_reference', ''),
                line.get('product_description', ''),
                line.get('quantity', 0),
                line.get('unit_price', 0.0),
                line.get('total_price', 0.0),
                line.get('line_number', 0)
            ))

        conn.commit()
        conn.close()

        return order_id

    def get_chantier_orders(self, chantier_id: int) -> List[ChantierOrder]:
        """
        Récupère toutes les commandes d'un chantier

        Args:
            chantier_id: ID du chantier

        Returns:
            Liste des commandes du chantier
        """
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT co.*, c.nom as chantier_name
            FROM chantier_orders co
            JOIN chantiers c ON co.chantier_id = c.id
            WHERE co.chantier_id = ?
            ORDER BY co.order_date DESC
        """, (chantier_id,))

        rows = cursor.fetchall()
        conn.close()

        orders = []
        for row in rows:
            orders.append(ChantierOrder(
                chantier_id=row['chantier_id'],
                chantier_name=row['chantier_name'],
                order_number=row['order_number'],
                order_date=datetime.fromisoformat(row['order_date']),
                total_amount=row['total_amount'],
                status=OrderStatus(row['status']),
                notes=row['notes']
            ))

        return orders

    def get_order_details(self, order_number: str) -> Optional[Dict[str, Any]]:
        """
        Récupère les détails complets d'une commande

        Args:
            order_number: Numéro de commande

        Returns:
            Dictionnaire avec les détails ou None
        """
        conn = self._get_connection()
        cursor = conn.cursor()

        # Récupérer la commande
        cursor.execute("""
            SELECT co.*, c.nom as chantier_name
            FROM chantier_orders co
            JOIN chantiers c ON co.chantier_id = c.id
            WHERE co.order_number = ?
        """, (order_number,))

        order_row = cursor.fetchone()
        if not order_row:
            conn.close()
            return None

        # Récupérer les lignes de commande
        cursor.execute("""
            SELECT * FROM chantier_products
            WHERE order_number = ?
            ORDER BY line_number
        """, (order_number,))

        product_rows = cursor.fetchall()

        conn.close()

        return {
            'order': dict(order_row),
            'products': [dict(row) for row in product_rows]
        }

    def update_order_status(
        self,
        order_number: str,
        new_status: OrderStatus
    ) -> bool:
        """
        Met à jour le statut d'une commande

        Args:
            order_number: Numéro de commande
            new_status: Nouveau statut

        Returns:
            True si mis à jour, False sinon
        """
        conn = self._get_connection()
        cursor = conn.cursor()

        now = datetime.now().isoformat()

        cursor.execute("""
            UPDATE chantier_orders
            SET status = ?, updated_at = ?
            WHERE order_number = ?
        """, (new_status.value, now, order_number))

        success = cursor.rowcount > 0
        conn.commit()
        conn.close()

        return success

    # === GESTION DES BONS DE LIVRAISON ===

    def add_delivery_note(
        self,
        chantier_id: int,
        order_number: str,
        delivery_note_number: str,
        delivery_date: datetime,
        total_delivered: int,
        carrier: Optional[str] = None,
        tracking_number: Optional[str] = None
    ) -> int:
        """
        Enregistre un bon de livraison

        Args:
            chantier_id: ID du chantier
            order_number: Numéro de commande
            delivery_note_number: Numéro du bon de livraison
            delivery_date: Date de livraison
            total_delivered: Quantité totale livrée
            carrier: Transporteur
            tracking_number: Numéro de suivi

        Returns:
            ID de l'enregistrement créé
        """
        conn = self._get_connection()
        cursor = conn.cursor()

        now = datetime.now().isoformat()

        cursor.execute("""
            INSERT INTO chantier_delivery_notes (
                chantier_id, order_number, delivery_note_number,
                delivery_date, total_delivered, carrier, tracking_number, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            chantier_id,
            order_number,
            delivery_note_number,
            delivery_date.isoformat(),
            total_delivered,
            carrier,
            tracking_number,
            now
        ))

        delivery_id = cursor.lastrowid
        conn.commit()
        conn.close()

        return delivery_id

    def get_chantier_deliveries(self, chantier_id: int) -> List[Dict[str, Any]]:
        """
        Récupère tous les bons de livraison d'un chantier

        Args:
            chantier_id: ID du chantier

        Returns:
            Liste des bons de livraison
        """
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM chantier_delivery_notes
            WHERE chantier_id = ?
            ORDER BY delivery_date DESC
        """, (chantier_id,))

        rows = cursor.fetchall()
        conn.close()

        return [dict(row) for row in rows]

    # === STATISTIQUES ===

    def get_chantier_statistics(self, chantier_id: int) -> Dict[str, Any]:
        """
        Calcule les statistiques d'achat d'un chantier

        Args:
            chantier_id: ID du chantier

        Returns:
            Dictionnaire avec les statistiques
        """
        conn = self._get_connection()
        cursor = conn.cursor()

        # Nombre de commandes
        cursor.execute("""
            SELECT COUNT(*) as count FROM chantier_orders
            WHERE chantier_id = ?
        """, (chantier_id,))
        nb_commandes = cursor.fetchone()['count']

        # Montant total
        cursor.execute("""
            SELECT SUM(total_amount) as total FROM chantier_orders
            WHERE chantier_id = ?
        """, (chantier_id,))
        montant_total = cursor.fetchone()['total'] or 0.0

        # Nombre de produits distincts
        cursor.execute("""
            SELECT COUNT(DISTINCT product_reference) as count FROM chantier_products
            WHERE chantier_id = ?
        """, (chantier_id,))
        nb_produits_distincts = cursor.fetchone()['count']

        # Quantité totale
        cursor.execute("""
            SELECT SUM(quantity) as total FROM chantier_products
            WHERE chantier_id = ?
        """, (chantier_id,))
        quantite_totale = cursor.fetchone()['total'] or 0

        # Nombre de livraisons
        cursor.execute("""
            SELECT COUNT(*) as count FROM chantier_delivery_notes
            WHERE chantier_id = ?
        """, (chantier_id,))
        nb_livraisons = cursor.fetchone()['count']

        conn.close()

        return {
            'nb_commandes': nb_commandes,
            'montant_total': montant_total,
            'nb_produits_distincts': nb_produits_distincts,
            'quantite_totale': quantite_totale,
            'nb_livraisons': nb_livraisons
        }

    def search_products_by_chantier(
        self,
        chantier_id: int,
        search_term: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Recherche les produits commandés pour un chantier

        Args:
            chantier_id: ID du chantier
            search_term: Terme de recherche optionnel

        Returns:
            Liste des produits
        """
        conn = self._get_connection()
        cursor = conn.cursor()

        if search_term:
            cursor.execute("""
                SELECT
                    product_reference,
                    product_description,
                    SUM(quantity) as total_quantity,
                    AVG(unit_price) as avg_unit_price,
                    SUM(total_price) as total_price
                FROM chantier_products
                WHERE chantier_id = ?
                AND (product_reference LIKE ? OR product_description LIKE ?)
                GROUP BY product_reference, product_description
                ORDER BY total_price DESC
            """, (chantier_id, f'%{search_term}%', f'%{search_term}%'))
        else:
            cursor.execute("""
                SELECT
                    product_reference,
                    product_description,
                    SUM(quantity) as total_quantity,
                    AVG(unit_price) as avg_unit_price,
                    SUM(total_price) as total_price
                FROM chantier_products
                WHERE chantier_id = ?
                GROUP BY product_reference, product_description
                ORDER BY total_price DESC
            """, (chantier_id,))

        rows = cursor.fetchall()
        conn.close()

        return [dict(row) for row in rows]
