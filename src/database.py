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
