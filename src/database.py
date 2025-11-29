"""
GESCO v5.0 - Gestionnaire de base de données SQLite
Gestion centralisée de toutes les données de l'application
"""

import sqlite3
import json
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any


class Database:
    """Gestionnaire de base de données SQLite pour GESCO"""

    def __init__(self, db_path: str = "data/gesco.db"):
        """
        Initialise la connexion à la base de données

        Args:
            db_path: Chemin vers le fichier de base de données
        """
        self.db_path = db_path

        # Créer le répertoire data s'il n'existe pas
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)

        # Initialiser la base de données
        self._init_database()

    def _get_connection(self) -> sqlite3.Connection:
        """Crée une nouvelle connexion à la base de données"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Permet d'accéder aux colonnes par nom
        return conn

    def _init_database(self):
        """Initialise les tables de la base de données"""
        conn = self._get_connection()
        cursor = conn.cursor()

        # Table des chantiers
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS chantiers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                numero_commande TEXT,
                client TEXT NOT NULL,
                adresse TEXT,
                code_postal TEXT,
                ville TEXT,
                telephone TEXT,
                email TEXT,
                date_ouverture TEXT NOT NULL,
                date_cloture TEXT,
                etat TEXT NOT NULL DEFAULT 'Accepté',
                budget_previsionnel REAL DEFAULT 0,
                budget_reel REAL DEFAULT 0,
                notes TEXT,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                UNIQUE(numero_commande)
            )
        """)

        # Index pour les recherches fréquentes
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_chantiers_etat
            ON chantiers(etat)
        """)

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_chantiers_client
            ON chantiers(client)
        """)

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_chantiers_numero
            ON chantiers(numero_commande)
        """)

        # Table des fournisseurs (achats directs)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS fournisseurs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL,
                type TEXT NOT NULL,
                siret TEXT,
                adresse TEXT,
                code_postal TEXT,
                ville TEXT,
                telephone TEXT,
                email TEXT,
                site_web TEXT,
                contact_nom TEXT,
                notes TEXT,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                UNIQUE(nom)
            )
        """)

        # Table des catégories d'achats
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories_achats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT NOT NULL UNIQUE,
                description TEXT,
                created_at TEXT NOT NULL
            )
        """)

        # Insérer les catégories par défaut
        cursor.execute("""
            INSERT OR IGNORE INTO categories_achats (nom, description, created_at)
            VALUES
                ('Matériel électrique', 'Câbles, disjoncteurs, tableaux, etc.', ?),
                ('Outillage', 'Outils manuels et électriques', ?),
                ('Matériel de sécurité', 'EPI, signalisation, etc.', ?),
                ('Consommables', 'Petites fournitures, visserie, etc.', ?),
                ('Location', 'Location de matériel', ?),
                ('Sous-traitance', 'Prestations externes', ?),
                ('Autres', 'Achats divers', ?)
        """, tuple([datetime.now().isoformat()] * 7))

        # Table des achats directs
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS achats_directs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                chantier_id INTEGER NOT NULL,
                fournisseur_id INTEGER,
                fournisseur_nom TEXT,
                categorie_id INTEGER,
                date_achat TEXT NOT NULL,
                numero_facture TEXT,
                description TEXT NOT NULL,
                montant_ht REAL NOT NULL,
                montant_ttc REAL NOT NULL,
                tva REAL DEFAULT 20.0,
                moyen_paiement TEXT,
                reference_paiement TEXT,
                fichier_facture TEXT,
                notes TEXT,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                FOREIGN KEY (chantier_id) REFERENCES chantiers(id) ON DELETE CASCADE,
                FOREIGN KEY (fournisseur_id) REFERENCES fournisseurs(id) ON DELETE SET NULL,
                FOREIGN KEY (categorie_id) REFERENCES categories_achats(id) ON DELETE SET NULL
            )
        """)

        # Index pour les achats directs
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_achats_chantier
            ON achats_directs(chantier_id)
        """)

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_achats_fournisseur
            ON achats_directs(fournisseur_id)
        """)

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_achats_date
            ON achats_directs(date_achat)
        """)

        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_achats_categorie
            ON achats_directs(categorie_id)
        """)

        conn.commit()
        conn.close()

    # === GESTION DES CHANTIERS ===

    def ajouter_chantier(self, chantier_data: Dict[str, Any]) -> int:
        """
        Ajoute un nouveau chantier

        Args:
            chantier_data: Dictionnaire avec les données du chantier

        Returns:
            ID du chantier créé
        """
        conn = self._get_connection()
        cursor = conn.cursor()

        now = datetime.now().isoformat()

        cursor.execute("""
            INSERT INTO chantiers (
                nom, numero_commande, client, adresse, code_postal, ville,
                telephone, email, date_ouverture, etat, budget_previsionnel,
                notes, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            chantier_data.get('nom'),
            chantier_data.get('numero_commande'),
            chantier_data.get('client'),
            chantier_data.get('adresse', ''),
            chantier_data.get('code_postal', ''),
            chantier_data.get('ville', ''),
            chantier_data.get('telephone', ''),
            chantier_data.get('email', ''),
            chantier_data.get('date_ouverture'),
            chantier_data.get('etat', 'Accepté'),
            chantier_data.get('budget_previsionnel', 0),
            chantier_data.get('notes', ''),
            now,
            now
        ))

        chantier_id = cursor.lastrowid
        conn.commit()
        conn.close()

        return chantier_id

    def modifier_chantier(self, chantier_id: int, chantier_data: Dict[str, Any]) -> bool:
        """
        Modifie un chantier existant

        Args:
            chantier_id: ID du chantier à modifier
            chantier_data: Dictionnaire avec les nouvelles données

        Returns:
            True si la modification a réussi, False sinon
        """
        conn = self._get_connection()
        cursor = conn.cursor()

        now = datetime.now().isoformat()

        cursor.execute("""
            UPDATE chantiers SET
                nom = ?,
                numero_commande = ?,
                client = ?,
                adresse = ?,
                code_postal = ?,
                ville = ?,
                telephone = ?,
                email = ?,
                date_ouverture = ?,
                etat = ?,
                budget_previsionnel = ?,
                budget_reel = ?,
                notes = ?,
                updated_at = ?
            WHERE id = ?
        """, (
            chantier_data.get('nom'),
            chantier_data.get('numero_commande'),
            chantier_data.get('client'),
            chantier_data.get('adresse', ''),
            chantier_data.get('code_postal', ''),
            chantier_data.get('ville', ''),
            chantier_data.get('telephone', ''),
            chantier_data.get('email', ''),
            chantier_data.get('date_ouverture'),
            chantier_data.get('etat'),
            chantier_data.get('budget_previsionnel', 0),
            chantier_data.get('budget_reel', 0),
            chantier_data.get('notes', ''),
            now,
            chantier_id
        ))

        success = cursor.rowcount > 0
        conn.commit()
        conn.close()

        return success

    def supprimer_chantier(self, chantier_id: int) -> bool:
        """
        Supprime un chantier

        Args:
            chantier_id: ID du chantier à supprimer

        Returns:
            True si la suppression a réussi, False sinon
        """
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM chantiers WHERE id = ?", (chantier_id,))

        success = cursor.rowcount > 0
        conn.commit()
        conn.close()

        return success

    def get_chantier(self, chantier_id: int) -> Optional[Dict[str, Any]]:
        """
        Récupère un chantier par son ID

        Args:
            chantier_id: ID du chantier

        Returns:
            Dictionnaire avec les données du chantier ou None
        """
        conn = self._get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM chantiers WHERE id = ?", (chantier_id,))
        row = cursor.fetchone()

        conn.close()

        if row:
            return dict(row)
        return None

    def get_chantiers(self, etat: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Récupère tous les chantiers, optionnellement filtrés par état

        Args:
            etat: État des chantiers à récupérer (None = tous)

        Returns:
            Liste de dictionnaires avec les données des chantiers
        """
        conn = self._get_connection()
        cursor = conn.cursor()

        if etat:
            cursor.execute(
                "SELECT * FROM chantiers WHERE etat = ? ORDER BY date_ouverture DESC",
                (etat,)
            )
        else:
            cursor.execute("SELECT * FROM chantiers ORDER BY date_ouverture DESC")

        rows = cursor.fetchall()
        conn.close()

        return [dict(row) for row in rows]

    def get_chantiers_tries(self) -> List[Dict[str, Any]]:
        """
        Récupère tous les chantiers triés (chantiers clôturés en fin de liste)

        Returns:
            Liste triée de dictionnaires avec les données des chantiers
        """
        tous_chantiers = self.get_chantiers()

        # Séparer clôturés et non-clôturés
        non_clotures = [c for c in tous_chantiers if c['etat'] != 'Clôturé']
        clotures = [c for c in tous_chantiers if c['etat'] == 'Clôturé']

        # Trier chaque groupe par date d'ouverture (plus récent en premier)
        non_clotures.sort(key=lambda x: x['date_ouverture'], reverse=True)
        clotures.sort(key=lambda x: x['date_ouverture'], reverse=True)

        # Concaténer : non-clôturés en premier, clôturés à la fin
        return non_clotures + clotures

    def changer_etat_chantier(self, chantier_id: int, nouvel_etat: str) -> bool:
        """
        Change l'état d'un chantier

        Args:
            chantier_id: ID du chantier
            nouvel_etat: Nouvel état du chantier

        Returns:
            True si le changement a réussi, False sinon
        """
        conn = self._get_connection()
        cursor = conn.cursor()

        now = datetime.now().isoformat()

        # Si on clôture le chantier, enregistrer la date de clôture
        if nouvel_etat == 'Clôturé':
            cursor.execute("""
                UPDATE chantiers SET
                    etat = ?,
                    date_cloture = ?,
                    updated_at = ?
                WHERE id = ?
            """, (nouvel_etat, now, now, chantier_id))
        else:
            cursor.execute("""
                UPDATE chantiers SET
                    etat = ?,
                    updated_at = ?
                WHERE id = ?
            """, (nouvel_etat, now, chantier_id))

        success = cursor.rowcount > 0
        conn.commit()
        conn.close()

        return success

    def rechercher_chantiers(self, terme: str) -> List[Dict[str, Any]]:
        """
        Recherche des chantiers par nom, numéro de commande ou client

        Args:
            terme: Terme de recherche

        Returns:
            Liste de dictionnaires avec les chantiers trouvés
        """
        conn = self._get_connection()
        cursor = conn.cursor()

        terme_like = f"%{terme}%"

        cursor.execute("""
            SELECT * FROM chantiers
            WHERE nom LIKE ? OR numero_commande LIKE ? OR client LIKE ?
            ORDER BY date_ouverture DESC
        """, (terme_like, terme_like, terme_like))

        rows = cursor.fetchall()
        conn.close()

        return [dict(row) for row in rows]

    def get_statistiques_chantiers(self) -> Dict[str, Any]:
        """
        Récupère des statistiques sur les chantiers

        Returns:
            Dictionnaire avec les statistiques
        """
        conn = self._get_connection()
        cursor = conn.cursor()

        # Nombre total de chantiers
        cursor.execute("SELECT COUNT(*) as total FROM chantiers")
        total = cursor.fetchone()['total']

        # Nombre par état
        cursor.execute("""
            SELECT etat, COUNT(*) as count
            FROM chantiers
            GROUP BY etat
        """)
        par_etat = {row['etat']: row['count'] for row in cursor.fetchall()}

        # Budget total prévisionnel
        cursor.execute("SELECT SUM(budget_previsionnel) as total FROM chantiers")
        budget_prev = cursor.fetchone()['total'] or 0

        # Budget total réel
        cursor.execute("SELECT SUM(budget_reel) as total FROM chantiers")
        budget_reel = cursor.fetchone()['total'] or 0

        conn.close()

        return {
            'total': total,
            'par_etat': par_etat,
            'budget_previsionnel_total': budget_prev,
            'budget_reel_total': budget_reel
        }

    # === GESTION DES FOURNISSEURS ===

    def ajouter_fournisseur(self, fournisseur_data: Dict[str, Any]) -> int:
        """Ajoute un nouveau fournisseur"""
        conn = self._get_connection()
        cursor = conn.cursor()
        now = datetime.now().isoformat()

        cursor.execute("""
            INSERT INTO fournisseurs (
                nom, type, siret, adresse, code_postal, ville,
                telephone, email, site_web, contact_nom, notes,
                created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            fournisseur_data.get('nom'),
            fournisseur_data.get('type', 'Autre'),
            fournisseur_data.get('siret'),
            fournisseur_data.get('adresse'),
            fournisseur_data.get('code_postal'),
            fournisseur_data.get('ville'),
            fournisseur_data.get('telephone'),
            fournisseur_data.get('email'),
            fournisseur_data.get('site_web'),
            fournisseur_data.get('contact_nom'),
            fournisseur_data.get('notes'),
            now, now
        ))

        fournisseur_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return fournisseur_id

    def get_fournisseurs(self, type_fournisseur: Optional[str] = None) -> List[Dict[str, Any]]:
        """Récupère tous les fournisseurs"""
        conn = self._get_connection()
        cursor = conn.cursor()

        if type_fournisseur:
            cursor.execute(
                "SELECT * FROM fournisseurs WHERE type = ? ORDER BY nom",
                (type_fournisseur,)
            )
        else:
            cursor.execute("SELECT * FROM fournisseurs ORDER BY nom")

        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def get_categories_achats(self) -> List[Dict[str, Any]]:
        """Récupère toutes les catégories d'achats"""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM categories_achats ORDER BY nom")
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    # === GESTION DES ACHATS DIRECTS ===

    def ajouter_achat_direct(self, achat_data: Dict[str, Any]) -> int:
        """Ajoute un achat direct"""
        conn = self._get_connection()
        cursor = conn.cursor()
        now = datetime.now().isoformat()

        cursor.execute("""
            INSERT INTO achats_directs (
                chantier_id, fournisseur_id, fournisseur_nom, categorie_id,
                date_achat, numero_facture, description,
                montant_ht, montant_ttc, tva,
                moyen_paiement, reference_paiement, fichier_facture,
                notes, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            achat_data.get('chantier_id'),
            achat_data.get('fournisseur_id'),
            achat_data.get('fournisseur_nom'),
            achat_data.get('categorie_id'),
            achat_data.get('date_achat'),
            achat_data.get('numero_facture'),
            achat_data.get('description'),
            achat_data.get('montant_ht', 0),
            achat_data.get('montant_ttc', 0),
            achat_data.get('tva', 20.0),
            achat_data.get('moyen_paiement'),
            achat_data.get('reference_paiement'),
            achat_data.get('fichier_facture'),
            achat_data.get('notes'),
            now, now
        ))

        achat_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return achat_id

    def get_achats_directs(
        self,
        chantier_id: Optional[int] = None,
        categorie_id: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """Récupère les achats directs"""
        conn = self._get_connection()
        cursor = conn.cursor()

        query = """
            SELECT
                ad.*,
                c.nom as chantier_nom,
                ca.nom as categorie_nom
            FROM achats_directs ad
            LEFT JOIN chantiers c ON ad.chantier_id = c.id
            LEFT JOIN categories_achats ca ON ad.categorie_id = ca.id
            WHERE 1=1
        """
        params = []

        if chantier_id:
            query += " AND ad.chantier_id = ?"
            params.append(chantier_id)

        if categorie_id:
            query += " AND ad.categorie_id = ?"
            params.append(categorie_id)

        query += " ORDER BY ad.date_achat DESC"

        cursor.execute(query, params)
        rows = cursor.fetchall()
        conn.close()
        return [dict(row) for row in rows]

    def get_total_achats_chantier(self, chantier_id: int) -> Dict[str, float]:
        """Calcule le total des achats d'un chantier (directs + API)"""
        conn = self._get_connection()
        cursor = conn.cursor()

        # Achats directs
        cursor.execute("""
            SELECT COALESCE(SUM(montant_ttc), 0) as total
            FROM achats_directs
            WHERE chantier_id = ?
        """, (chantier_id,))
        total_directs = cursor.fetchone()['total']

        # Commandes Sonepar
        cursor.execute("""
            SELECT COALESCE(SUM(total_amount), 0) as total
            FROM chantier_orders
            WHERE chantier_id = ?
        """, (chantier_id,))
        total_sonepar = cursor.fetchone()['total']

        conn.close()

        return {
            'achats_directs': total_directs,
            'commandes_sonepar': total_sonepar,
            'total': total_directs + total_sonepar
        }
