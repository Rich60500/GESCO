"""
GESCO v5.0 - Module Chantier Complet
Interface moderne avec gestion complète des chantiers

Fonctionnalités :
- CRUD complet (Créer, Modifier, Supprimer)
- Gestion des états : Accepté, En cours, Terminé, Facturé, Clôturé
- Liste avec : nom, numéro commande, client, date ouverture
- Volet de détails avec modification d'état
- Chantiers clôturés en fin de liste
"""

import sys
import os
import pickle
from datetime import datetime
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTableWidget, QTableWidgetItem, QLabel, QPushButton,
    QHeaderView, QFrame, QComboBox, QMessageBox, QLineEdit
)

from gesco_modern_ui import (
    DesignSystem,
    ResponsiveDialog,
    ModernLabel,
    ModernInput,
    ModernComboBox,
    ModernButton,
    ModernCard
)


# ============================================================================
# GESTION DES DONNÉES CHANTIERS
# ============================================================================

class GestionChantier:
    """Classe pour gérer les données des chantiers"""

    # États possibles d'un chantier
    ETATS = ["Accepté", "En cours", "Terminé", "Facturé", "Clôturé"]

    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        self.data_file = os.path.join(data_dir, "chantiers.pkl")
        self.chantiers = []

        # Créer le dossier data s'il n'existe pas
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        # Charger les données
        self.load()

    def load(self):
        """Charger les chantiers depuis le fichier"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'rb') as f:
                    self.chantiers = pickle.load(f)
                print(f"✅ {len(self.chantiers)} chantiers chargés")
            except Exception as e:
                print(f"⚠️ Erreur chargement : {e}")
                self.chantiers = []
        else:
            self.chantiers = []
            print("ℹ️ Aucune donnée existante, démarrage avec liste vide")

    def save(self):
        """Sauvegarder les chantiers dans le fichier"""
        try:
            with open(self.data_file, 'wb') as f:
                pickle.dump(self.chantiers, f)
            print(f"✅ {len(self.chantiers)} chantiers sauvegardés")
            return True
        except Exception as e:
            print(f"❌ Erreur sauvegarde : {e}")
            return False

    def ajouter_chantier(self, chantier_data):
        """Ajouter un nouveau chantier"""
        chantier_data['id'] = len(self.chantiers) + 1
        chantier_data['date_creation'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # État par défaut si non spécifié
        if 'etat' not in chantier_data:
            chantier_data['etat'] = "Accepté"

        self.chantiers.append(chantier_data)
        self.save()
        return chantier_data['id']

    def modifier_chantier(self, chantier_id, chantier_data):
        """Modifier un chantier existant"""
        for i, chantier in enumerate(self.chantiers):
            if chantier['id'] == chantier_id:
                # Conserver l'ID et la date de création
                chantier_data['id'] = chantier_id
                chantier_data['date_creation'] = chantier['date_creation']
                chantier_data['date_modification'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                self.chantiers[i] = chantier_data
                self.save()
                return True
        return False

    def supprimer_chantier(self, chantier_id):
        """Supprimer un chantier"""
        for i, chantier in enumerate(self.chantiers):
            if chantier['id'] == chantier_id:
                del self.chantiers[i]
                self.save()
                return True
        return False

    def get_chantier(self, chantier_id):
        """Obtenir un chantier par son ID"""
        for chantier in self.chantiers:
            if chantier['id'] == chantier_id:
                return chantier
        return None

    def changer_etat(self, chantier_id, nouvel_etat):
        """Changer l'état d'un chantier"""
        if nouvel_etat not in self.ETATS:
            return False

        for chantier in self.chantiers:
            if chantier['id'] == chantier_id:
                chantier['etat'] = nouvel_etat
                chantier['date_changement_etat'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save()
                return True
        return False

    def get_chantiers_tries(self):
        """Obtenir la liste des chantiers triés (clôturés en fin)"""
        # Séparer les chantiers clôturés et non-clôturés
        non_clotures = [c for c in self.chantiers if c['etat'] != 'Clôturé']
        clotures = [c for c in self.chantiers if c['etat'] == 'Clôturé']

        # Trier par date d'ouverture décroissante
        non_clotures.sort(key=lambda x: x.get('date_ouverture', ''), reverse=True)
        clotures.sort(key=lambda x: x.get('date_ouverture', ''), reverse=True)

        return non_clotures + clotures


# ============================================================================
# DIALOGUES MODERNES
# ============================================================================

class ChantierDialog(ResponsiveDialog):
    """Dialog pour créer un nouveau chantier"""

    def __init__(self, gestion, parent=None):
        super().__init__("Nouveau Chantier", parent)
        self.gestion = gestion
        self.resize(700, 650)

        # Section 1 : Informations générales
        section1 = self.add_form_section("Informations générales")

        # Nom du chantier
        self.nom_input = ModernInput(placeholder="Ex: Rénovation appartement Paris 15")
        self.add_form_field(section1, "Nom du chantier", self.nom_input, required=True)

        # Numéro de commande
        self.num_commande_input = ModernInput(placeholder="Ex: CMD-2024-001")
        self.add_form_field(section1, "N° Commande Client", self.num_commande_input, required=True)

        # Client
        self.client_input = ModernInput(placeholder="Nom du client")
        self.add_form_field(section1, "Client", self.client_input, required=True)

        # Date d'ouverture
        self.date_input = ModernInput(placeholder="JJ/MM/AAAA")
        self.date_input.setText(datetime.now().strftime("%d/%m/%Y"))
        self.add_form_field(section1, "Date d'ouverture", self.date_input, required=True)

        # Section 2 : Localisation
        section2 = self.add_form_section("Localisation")

        # Adresse
        self.adresse_input = ModernInput(placeholder="Numéro et nom de rue")
        self.add_form_field(section2, "Adresse", self.adresse_input, required=True)

        # Ville et code postal
        ville_cp_widget = QWidget()
        ville_cp_layout = QHBoxLayout()
        ville_cp_layout.setContentsMargins(0, 0, 0, 0)
        ville_cp_layout.setSpacing(DesignSystem.SPACING_SM)

        self.cp_input = ModernInput(placeholder="75000")
        self.cp_input.setMaximumWidth(120)
        ville_cp_layout.addWidget(self.cp_input)

        self.ville_input = ModernInput(placeholder="Ville")
        ville_cp_layout.addWidget(self.ville_input)

        ville_cp_widget.setLayout(ville_cp_layout)
        self.add_form_field(section2, "Code postal / Ville", ville_cp_widget, required=True)

        # Section 3 : Budget et durée
        section3 = self.add_form_section("Budget et durée")

        # Durée prévue
        self.duree_input = ModernInput(placeholder="30")
        self.add_form_field(
            section3,
            "Durée prévue (jours)",
            self.duree_input,
            help_text="Nombre de jours ouvrés estimés"
        )

        # Chiffrage Global
        self.chiffrage_input = ModernInput(placeholder="0.00")
        self.add_form_field(section3, "Chiffrage global (€)", self.chiffrage_input)

        # Coût Estimé Achats
        self.cout_achats_input = ModernInput(placeholder="0.00")
        self.add_form_field(section3, "Coût estimé achats (€)", self.cout_achats_input)

        # Coût Estimé Main d'Œuvre
        self.cout_mo_input = ModernInput(placeholder="0.00")
        self.add_form_field(section3, "Coût estimé main d'œuvre (€)", self.cout_mo_input)

        # État initial
        self.etat_combo = ModernComboBox()
        self.etat_combo.addItems(GestionChantier.ETATS)
        self.add_form_field(section3, "État initial", self.etat_combo)

        # Stretch
        self.content_layout.addStretch()

        # Boutons
        self.add_button_bar([
            ("Annuler", "secondary", self.reject),
            ("Créer le chantier", "success", self.accept)
        ])

    def get_data(self):
        """Récupérer les données du formulaire"""
        return {
            'nom': self.nom_input.text(),
            'numero_commande': self.num_commande_input.text(),
            'client': self.client_input.text(),
            'date_ouverture': self.date_input.text(),
            'adresse': self.adresse_input.text(),
            'code_postal': self.cp_input.text(),
            'ville': self.ville_input.text(),
            'duree_prevue': self.duree_input.text() or "0",
            'chiffrage_global': self.chiffrage_input.text() or "0",
            'cout_achats': self.cout_achats_input.text() or "0",
            'cout_mo': self.cout_mo_input.text() or "0",
            'etat': self.etat_combo.currentText()
        }


class ModifierChantierDialog(ChantierDialog):
    """Dialog pour modifier un chantier existant"""

    def __init__(self, gestion, chantier, parent=None):
        super().__init__(gestion, parent)
        self.setWindowTitle("Modifier Chantier")

        # Remplir les champs avec les données existantes
        self.nom_input.setText(chantier.get('nom', ''))
        self.num_commande_input.setText(chantier.get('numero_commande', ''))
        self.client_input.setText(chantier.get('client', ''))
        self.date_input.setText(chantier.get('date_ouverture', ''))
        self.adresse_input.setText(chantier.get('adresse', ''))
        self.cp_input.setText(chantier.get('code_postal', ''))
        self.ville_input.setText(chantier.get('ville', ''))
        self.duree_input.setText(str(chantier.get('duree_prevue', '')))
        self.chiffrage_input.setText(str(chantier.get('chiffrage_global', '')))
        self.cout_achats_input.setText(str(chantier.get('cout_achats', '')))
        self.cout_mo_input.setText(str(chantier.get('cout_mo', '')))

        # Sélectionner l'état actuel
        etat_index = self.etat_combo.findText(chantier.get('etat', 'Accepté'))
        if etat_index >= 0:
            self.etat_combo.setCurrentIndex(etat_index)

        # Changer le texte du bouton
        # (On doit retrouver le bouton dans la barre)
        # Pour simplifier, on recrée la barre de boutons
        # Note : Dans une vraie application, on stockerait les boutons


# ============================================================================
# FENÊTRE PRINCIPALE MODULE CHANTIER
# ============================================================================

class ModuleChantierWindow(QMainWindow):
    """Fenêtre principale du module Chantier"""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("GESCO v5.0 - Module Chantier")
        self.setGeometry(100, 100, 1400, 800)

        # Gestion des données
        self.gestion = GestionChantier()

        # Créer l'interface
        self.init_ui()

        # Charger les données
        self.refresh_list()

    def init_ui(self):
        """Initialiser l'interface utilisateur"""

        # Widget central
        central = QWidget()
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Barre de titre avec boutons
        header = self.create_header()
        main_layout.addWidget(header)

        # Splitter pour diviser en 2 volets
        splitter = QSplitter(Qt.Orientation.Horizontal)

        # Volet gauche : Liste des chantiers
        left_panel = self.create_list_panel()
        splitter.addWidget(left_panel)

        # Volet droit : Détails du chantier
        right_panel = self.create_details_panel()
        splitter.addWidget(right_panel)

        # Proportions 40/60
        splitter.setSizes([560, 840])

        main_layout.addWidget(splitter)

        central.setLayout(main_layout)
        self.setCentralWidget(central)

        # Style
        self.setStyleSheet(f"""
            QMainWindow {{
                background-color: {DesignSystem.BACKGROUND};
            }}
        """)

    def create_header(self):
        """Créer la barre de titre avec boutons"""
        header = QFrame()
        header.setStyleSheet(f"""
            QFrame {{
                background-color: {DesignSystem.SURFACE};
                border-bottom: 1px solid {DesignSystem.BORDER_LIGHT};
                padding: {DesignSystem.SPACING_LG}px {DesignSystem.SPACING_XL}px;
            }}
        """)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # Titre
        title = QLabel("Module Chantier")
        title.setFont(QFont(DesignSystem.FONT_FAMILY, DesignSystem.FONT_SIZE_LARGE_TITLE, QFont.Weight.Bold))
        title.setStyleSheet(f"color: {DesignSystem.TEXT_PRIMARY};")
        layout.addWidget(title)

        # Compteur
        self.count_label = QLabel("0 chantiers")
        self.count_label.setFont(QFont(DesignSystem.FONT_FAMILY, DesignSystem.FONT_SIZE_BODY))
        self.count_label.setStyleSheet(f"color: {DesignSystem.TEXT_SECONDARY};")
        layout.addWidget(self.count_label)

        layout.addStretch()

        # Boutons d'action
        btn_nouveau = ModernButton("+ Nouveau Chantier", "success")
        btn_nouveau.clicked.connect(self.nouveau_chantier)
        layout.addWidget(btn_nouveau)

        header.setLayout(layout)
        return header

    def create_list_panel(self):
        """Créer le panneau de liste des chantiers"""
        panel = QWidget()
        panel.setStyleSheet(f"background-color: {DesignSystem.BACKGROUND};")

        layout = QVBoxLayout()
        layout.setContentsMargins(
            DesignSystem.SPACING_LG,
            DesignSystem.SPACING_LG,
            DesignSystem.SPACING_SM,
            DesignSystem.SPACING_LG
        )

        # Barre de recherche
        search_layout = QHBoxLayout()
        self.search_input = ModernInput(placeholder="Rechercher un chantier...")
        self.search_input.textChanged.connect(self.filter_list)
        search_layout.addWidget(self.search_input)
        layout.addLayout(search_layout)

        # Tableau des chantiers
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels([
            "Nom du chantier",
            "N° Commande",
            "Client",
            "Date ouverture"
        ])

        # Style du tableau
        self.table.setStyleSheet(f"""
            QTableWidget {{
                background-color: {DesignSystem.SURFACE};
                border: 1px solid {DesignSystem.BORDER_LIGHT};
                border-radius: {DesignSystem.RADIUS_MD}px;
                gridline-color: {DesignSystem.BORDER_LIGHT};
                selection-background-color: {DesignSystem.ACCENT_BLUE};
                selection-color: white;
            }}
            QTableWidget::item {{
                padding: {DesignSystem.SPACING_MD}px;
                border-bottom: 1px solid {DesignSystem.BORDER_LIGHT};
            }}
            QTableWidget::item:selected {{
                background-color: {DesignSystem.ACCENT_BLUE};
                color: white;
            }}
            QHeaderView::section {{
                background-color: {DesignSystem.SURFACE_SECONDARY};
                padding: {DesignSystem.SPACING_MD}px;
                border: none;
                border-bottom: 2px solid {DesignSystem.BORDER_MEDIUM};
                font-weight: bold;
                color: {DesignSystem.TEXT_PRIMARY};
            }}
        """)

        # Configuration du tableau
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.horizontalHeader().setStretchLastSection(False)
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        self.table.verticalHeader().setVisible(False)

        # Connexion de la sélection
        self.table.itemSelectionChanged.connect(self.on_selection_changed)

        layout.addWidget(self.table)

        panel.setLayout(layout)
        return panel

    def create_details_panel(self):
        """Créer le panneau de détails du chantier"""
        panel = QWidget()
        panel.setStyleSheet(f"background-color: {DesignSystem.BACKGROUND};")

        self.details_layout = QVBoxLayout()
        self.details_layout.setContentsMargins(
            DesignSystem.SPACING_SM,
            DesignSystem.SPACING_LG,
            DesignSystem.SPACING_LG,
            DesignSystem.SPACING_LG
        )

        # Message par défaut
        empty_label = QLabel("Sélectionnez un chantier pour voir les détails")
        empty_label.setFont(QFont(DesignSystem.FONT_FAMILY, DesignSystem.FONT_SIZE_TITLE))
        empty_label.setStyleSheet(f"color: {DesignSystem.TEXT_SECONDARY}; padding: 40px;")
        empty_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.details_layout.addWidget(empty_label)
        self.details_layout.addStretch()

        panel.setLayout(self.details_layout)
        return panel

    def refresh_list(self):
        """Rafraîchir la liste des chantiers"""
        # Vider la table
        self.table.setRowCount(0)

        # Récupérer les chantiers triés
        chantiers = self.gestion.get_chantiers_tries()

        # Mettre à jour le compteur
        self.count_label.setText(f"{len(chantiers)} chantier{'s' if len(chantiers) > 1 else ''}")

        # Remplir la table
        for chantier in chantiers:
            row = self.table.rowCount()
            self.table.insertRow(row)

            # Nom
            item_nom = QTableWidgetItem(chantier.get('nom', ''))
            item_nom.setData(Qt.ItemDataRole.UserRole, chantier['id'])

            # Si clôturé, griser la ligne
            if chantier.get('etat') == 'Clôturé':
                item_nom.setForeground(Qt.GlobalColor.gray)

            self.table.setItem(row, 0, item_nom)

            # Numéro commande
            item_num = QTableWidgetItem(chantier.get('numero_commande', ''))
            if chantier.get('etat') == 'Clôturé':
                item_num.setForeground(Qt.GlobalColor.gray)
            self.table.setItem(row, 1, item_num)

            # Client
            item_client = QTableWidgetItem(chantier.get('client', ''))
            if chantier.get('etat') == 'Clôturé':
                item_client.setForeground(Qt.GlobalColor.gray)
            self.table.setItem(row, 2, item_client)

            # Date
            item_date = QTableWidgetItem(chantier.get('date_ouverture', ''))
            if chantier.get('etat') == 'Clôturé':
                item_date.setForeground(Qt.GlobalColor.gray)
            self.table.setItem(row, 3, item_date)

    def filter_list(self, text):
        """Filtrer la liste selon le texte de recherche"""
        for row in range(self.table.rowCount()):
            match = False
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                if item and text.lower() in item.text().lower():
                    match = True
                    break
            self.table.setRowHidden(row, not match)

    def on_selection_changed(self):
        """Gérer la sélection d'un chantier"""
        selected = self.table.selectedItems()
        if not selected:
            return

        # Récupérer l'ID du chantier
        chantier_id = selected[0].data(Qt.ItemDataRole.UserRole)
        chantier = self.gestion.get_chantier(chantier_id)

        if chantier:
            self.show_details(chantier)

    def show_details(self, chantier):
        """Afficher les détails d'un chantier"""
        # Vider le layout
        while self.details_layout.count():
            child = self.details_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        # Carte informations principales
        card1 = ModernCard()
        card1_layout = QVBoxLayout()
        card1_layout.setContentsMargins(DesignSystem.SPACING_XL, DesignSystem.SPACING_XL, DesignSystem.SPACING_XL, DesignSystem.SPACING_XL)
        card1_layout.setSpacing(DesignSystem.SPACING_MD)

        title1 = ModernLabel("Informations principales", bold=True)
        title1.setFont(QFont(DesignSystem.FONT_FAMILY, DesignSystem.FONT_SIZE_TITLE, QFont.Weight.Bold))
        card1_layout.addWidget(title1)

        # Nom
        self.add_detail_row(card1_layout, "Nom du chantier", chantier.get('nom', '-'))

        # Numéro commande
        self.add_detail_row(card1_layout, "N° Commande", chantier.get('numero_commande', '-'))

        # Client
        self.add_detail_row(card1_layout, "Client", chantier.get('client', '-'))

        # Date
        self.add_detail_row(card1_layout, "Date d'ouverture", chantier.get('date_ouverture', '-'))

        # État avec ComboBox
        etat_layout = QHBoxLayout()
        etat_label = ModernLabel("État", bold=True)
        etat_label.setMinimumWidth(150)
        etat_layout.addWidget(etat_label)

        etat_combo = ModernComboBox()
        etat_combo.addItems(GestionChantier.ETATS)
        etat_combo.setCurrentText(chantier.get('etat', 'Accepté'))
        etat_combo.currentTextChanged.connect(
            lambda text: self.changer_etat_chantier(chantier['id'], text)
        )
        etat_layout.addWidget(etat_combo)
        etat_layout.addStretch()

        card1_layout.addLayout(etat_layout)

        card1.setLayout(card1_layout)
        self.details_layout.addWidget(card1)

        # Carte localisation
        card2 = ModernCard()
        card2_layout = QVBoxLayout()
        card2_layout.setContentsMargins(DesignSystem.SPACING_XL, DesignSystem.SPACING_XL, DesignSystem.SPACING_XL, DesignSystem.SPACING_XL)
        card2_layout.setSpacing(DesignSystem.SPACING_MD)

        title2 = ModernLabel("Localisation", bold=True)
        title2.setFont(QFont(DesignSystem.FONT_FAMILY, DesignSystem.FONT_SIZE_TITLE, QFont.Weight.Bold))
        card2_layout.addWidget(title2)

        self.add_detail_row(card2_layout, "Adresse", chantier.get('adresse', '-'))
        self.add_detail_row(card2_layout, "Code postal", chantier.get('code_postal', '-'))
        self.add_detail_row(card2_layout, "Ville", chantier.get('ville', '-'))

        card2.setLayout(card2_layout)
        self.details_layout.addWidget(card2)

        # Carte budget
        card3 = ModernCard()
        card3_layout = QVBoxLayout()
        card3_layout.setContentsMargins(DesignSystem.SPACING_XL, DesignSystem.SPACING_XL, DesignSystem.SPACING_XL, DesignSystem.SPACING_XL)
        card3_layout.setSpacing(DesignSystem.SPACING_MD)

        title3 = ModernLabel("Budget et durée", bold=True)
        title3.setFont(QFont(DesignSystem.FONT_FAMILY, DesignSystem.FONT_SIZE_TITLE, QFont.Weight.Bold))
        card3_layout.addWidget(title3)

        self.add_detail_row(card3_layout, "Durée prévue", f"{chantier.get('duree_prevue', '0')} jours")
        self.add_detail_row(card3_layout, "Chiffrage global", f"{chantier.get('chiffrage_global', '0')} €")
        self.add_detail_row(card3_layout, "Coût achats", f"{chantier.get('cout_achats', '0')} €")
        self.add_detail_row(card3_layout, "Coût main d'œuvre", f"{chantier.get('cout_mo', '0')} €")

        card3.setLayout(card3_layout)
        self.details_layout.addWidget(card3)

        # Boutons d'action
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(DesignSystem.SPACING_MD)

        btn_modifier = ModernButton("✏️ Modifier", "primary")
        btn_modifier.clicked.connect(lambda: self.modifier_chantier(chantier['id']))
        buttons_layout.addWidget(btn_modifier)

        btn_supprimer = ModernButton("🗑️ Supprimer", "danger")
        btn_supprimer.clicked.connect(lambda: self.supprimer_chantier(chantier['id']))
        buttons_layout.addWidget(btn_supprimer)

        buttons_layout.addStretch()

        self.details_layout.addLayout(buttons_layout)

        self.details_layout.addStretch()

    def add_detail_row(self, layout, label, value):
        """Ajouter une ligne de détail"""
        row = QHBoxLayout()

        lbl = ModernLabel(label, bold=True)
        lbl.setMinimumWidth(150)
        row.addWidget(lbl)

        val = ModernLabel(str(value))
        row.addWidget(val)

        row.addStretch()

        layout.addLayout(row)

    def nouveau_chantier(self):
        """Créer un nouveau chantier"""
        dialog = ChantierDialog(self.gestion, self)
        if dialog.exec():
            data = dialog.get_data()

            # Valider les données
            if not data['nom'] or not data['numero_commande'] or not data['client']:
                QMessageBox.warning(self, "Erreur", "Veuillez remplir tous les champs obligatoires")
                return

            # Ajouter le chantier
            chantier_id = self.gestion.ajouter_chantier(data)

            # Rafraîchir la liste
            self.refresh_list()

            QMessageBox.information(self, "Succès", f"Chantier '{data['nom']}' créé avec succès!")

    def modifier_chantier(self, chantier_id):
        """Modifier un chantier"""
        chantier = self.gestion.get_chantier(chantier_id)
        if not chantier:
            return

        dialog = ModifierChantierDialog(self.gestion, chantier, self)
        if dialog.exec():
            data = dialog.get_data()

            # Valider les données
            if not data['nom'] or not data['numero_commande'] or not data['client']:
                QMessageBox.warning(self, "Erreur", "Veuillez remplir tous les champs obligatoires")
                return

            # Modifier le chantier
            if self.gestion.modifier_chantier(chantier_id, data):
                # Rafraîchir la liste
                self.refresh_list()

                # Réafficher les détails
                chantier_updated = self.gestion.get_chantier(chantier_id)
                self.show_details(chantier_updated)

                QMessageBox.information(self, "Succès", "Chantier modifié avec succès!")

    def supprimer_chantier(self, chantier_id):
        """Supprimer un chantier"""
        chantier = self.gestion.get_chantier(chantier_id)
        if not chantier:
            return

        # Confirmation
        reply = QMessageBox.question(
            self,
            "Confirmation",
            f"Êtes-vous sûr de vouloir supprimer le chantier '{chantier['nom']}' ?\n\nCette action est irréversible.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            if self.gestion.supprimer_chantier(chantier_id):
                # Rafraîchir la liste
                self.refresh_list()

                # Vider le panneau de détails
                while self.details_layout.count():
                    child = self.details_layout.takeAt(0)
                    if child.widget():
                        child.widget().deleteLater()

                empty_label = QLabel("Sélectionnez un chantier pour voir les détails")
                empty_label.setFont(QFont(DesignSystem.FONT_FAMILY, DesignSystem.FONT_SIZE_TITLE))
                empty_label.setStyleSheet(f"color: {DesignSystem.TEXT_SECONDARY}; padding: 40px;")
                empty_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.details_layout.addWidget(empty_label)
                self.details_layout.addStretch()

                QMessageBox.information(self, "Succès", "Chantier supprimé avec succès!")

    def changer_etat_chantier(self, chantier_id, nouvel_etat):
        """Changer l'état d'un chantier"""
        if self.gestion.changer_etat(chantier_id, nouvel_etat):
            # Rafraîchir la liste (pour mettre à jour le tri)
            self.refresh_list()

            # Afficher un message
            print(f"✅ État changé: {nouvel_etat}")


# ============================================================================
# POINT D'ENTRÉE
# ============================================================================

def main():
    app = QApplication(sys.argv)

    window = ModuleChantierWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
