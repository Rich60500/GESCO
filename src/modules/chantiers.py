"""
GESCO v5.0 - Module Chantiers
Gestion complète des chantiers avec interface moderne
"""

from datetime import datetime
from typing import Optional

from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QTableWidget,
                               QTableWidgetItem, QHeaderView, QLineEdit, QPushButton,
                               QMessageBox, QLabel, QGridLayout, QAbstractItemView)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from design_system import (DesignSystem, ModernLabel, ModernInput, ModernComboBox,
                           ModernTextEdit, ModernButton, ModernCard, ResponsiveDialog)
from database import Database


class ChantierDialog(ResponsiveDialog):
    """Dialogue pour créer un nouveau chantier"""

    def __init__(self, parent=None):
        super().__init__("Nouveau Chantier", 700, parent)

        # Section Informations générales
        section_info = self.add_section("Informations générales")

        self.input_nom = ModernInput("Nom du chantier")
        self.add_form_field(section_info, "Nom du chantier *", self.input_nom)

        self.input_numero = ModernInput("Numéro de commande")
        self.add_form_field(section_info, "Numéro de commande", self.input_numero)

        self.input_client = ModernInput("Nom du client")
        self.add_form_field(section_info, "Client *", self.input_client)

        # Section Localisation
        section_localisation = self.add_section("Localisation")

        self.input_adresse = ModernInput("Adresse complète")
        self.add_form_field(section_localisation, "Adresse", self.input_adresse)

        # Ligne avec code postal et ville
        location_layout = QHBoxLayout()
        location_layout.setSpacing(DesignSystem.SPACING_MD)

        cp_layout = QVBoxLayout()
        cp_layout.setSpacing(DesignSystem.SPACING_SM)
        cp_label = ModernLabel("Code postal")
        self.input_code_postal = ModernInput("75001")
        cp_layout.addWidget(cp_label)
        cp_layout.addWidget(self.input_code_postal)

        ville_layout = QVBoxLayout()
        ville_layout.setSpacing(DesignSystem.SPACING_SM)
        ville_label = ModernLabel("Ville")
        self.input_ville = ModernInput("Paris")
        ville_layout.addWidget(ville_label)
        ville_layout.addWidget(self.input_ville)

        location_layout.addLayout(cp_layout, 1)
        location_layout.addLayout(ville_layout, 2)

        section_localisation.addLayout(location_layout)

        # Section Contact
        section_contact = self.add_section("Contact")

        self.input_telephone = ModernInput("06 12 34 56 78")
        self.add_form_field(section_contact, "Téléphone", self.input_telephone)

        self.input_email = ModernInput("client@example.com")
        self.add_form_field(section_contact, "Email", self.input_email)

        # Section Dates et Budget
        section_dates = self.add_section("Dates et Budget")

        # Date d'ouverture (défaut: aujourd'hui)
        self.input_date_ouverture = ModernInput(datetime.now().strftime("%Y-%m-%d"))
        self.add_form_field(section_dates, "Date d'ouverture *", self.input_date_ouverture)

        # État initial
        self.combo_etat = ModernComboBox()
        self.combo_etat.addItems(["Accepté", "En cours", "Terminé", "Facturé", "Clôturé"])
        self.add_form_field(section_dates, "État initial", self.combo_etat)

        # Budget prévisionnel
        self.input_budget = ModernInput("0.00")
        self.add_form_field(section_dates, "Budget prévisionnel (€)", self.input_budget)

        # Section Notes
        section_notes = self.add_section("Notes")

        self.input_notes = ModernTextEdit()
        self.input_notes.setMinimumHeight(100)
        self.input_notes.setPlaceholderText("Notes et remarques sur le chantier...")
        section_notes.addWidget(self.input_notes)

        # Boutons
        btn_annuler = ModernButton("Annuler", "secondary")
        btn_annuler.clicked.connect(self.reject)

        btn_creer = ModernButton("Créer le chantier", "primary")
        btn_creer.clicked.connect(self.valider)

        self.add_button_bar([btn_annuler, btn_creer])

    def valider(self):
        """Valide les données du formulaire"""
        # Vérifier les champs obligatoires
        if not self.input_nom.text().strip():
            QMessageBox.warning(self, "Champ manquant", "Le nom du chantier est obligatoire.")
            self.input_nom.setFocus()
            return

        if not self.input_client.text().strip():
            QMessageBox.warning(self, "Champ manquant", "Le nom du client est obligatoire.")
            self.input_client.setFocus()
            return

        if not self.input_date_ouverture.text().strip():
            QMessageBox.warning(self, "Champ manquant", "La date d'ouverture est obligatoire.")
            self.input_date_ouverture.setFocus()
            return

        # Valider le budget
        try:
            budget = float(self.input_budget.text().replace(',', '.'))
            if budget < 0:
                raise ValueError()
        except ValueError:
            QMessageBox.warning(self, "Format invalide", "Le budget doit être un nombre positif.")
            self.input_budget.setFocus()
            return

        self.accept()

    def get_data(self):
        """Retourne les données du formulaire"""
        return {
            'nom': self.input_nom.text().strip(),
            'numero_commande': self.input_numero.text().strip(),
            'client': self.input_client.text().strip(),
            'adresse': self.input_adresse.text().strip(),
            'code_postal': self.input_code_postal.text().strip(),
            'ville': self.input_ville.text().strip(),
            'telephone': self.input_telephone.text().strip(),
            'email': self.input_email.text().strip(),
            'date_ouverture': self.input_date_ouverture.text().strip(),
            'etat': self.combo_etat.currentText(),
            'budget_previsionnel': float(self.input_budget.text().replace(',', '.')),
            'notes': self.input_notes.toPlainText().strip()
        }


class ModifierChantierDialog(ResponsiveDialog):
    """Dialogue pour modifier un chantier existant"""

    def __init__(self, chantier_data: dict, parent=None):
        super().__init__("Modifier le Chantier", 700, parent)

        self.chantier_data = chantier_data

        # Section Informations générales
        section_info = self.add_section("Informations générales")

        self.input_nom = ModernInput()
        self.input_nom.setText(chantier_data.get('nom', ''))
        self.add_form_field(section_info, "Nom du chantier *", self.input_nom)

        self.input_numero = ModernInput()
        self.input_numero.setText(chantier_data.get('numero_commande', ''))
        self.add_form_field(section_info, "Numéro de commande", self.input_numero)

        self.input_client = ModernInput()
        self.input_client.setText(chantier_data.get('client', ''))
        self.add_form_field(section_info, "Client *", self.input_client)

        # Section Localisation
        section_localisation = self.add_section("Localisation")

        self.input_adresse = ModernInput()
        self.input_adresse.setText(chantier_data.get('adresse', ''))
        self.add_form_field(section_localisation, "Adresse", self.input_adresse)

        # Ligne avec code postal et ville
        location_layout = QHBoxLayout()
        location_layout.setSpacing(DesignSystem.SPACING_MD)

        cp_layout = QVBoxLayout()
        cp_layout.setSpacing(DesignSystem.SPACING_SM)
        cp_label = ModernLabel("Code postal")
        self.input_code_postal = ModernInput()
        self.input_code_postal.setText(chantier_data.get('code_postal', ''))
        cp_layout.addWidget(cp_label)
        cp_layout.addWidget(self.input_code_postal)

        ville_layout = QVBoxLayout()
        ville_layout.setSpacing(DesignSystem.SPACING_SM)
        ville_label = ModernLabel("Ville")
        self.input_ville = ModernInput()
        self.input_ville.setText(chantier_data.get('ville', ''))
        ville_layout.addWidget(ville_label)
        ville_layout.addWidget(self.input_ville)

        location_layout.addLayout(cp_layout, 1)
        location_layout.addLayout(ville_layout, 2)

        section_localisation.addLayout(location_layout)

        # Section Contact
        section_contact = self.add_section("Contact")

        self.input_telephone = ModernInput()
        self.input_telephone.setText(chantier_data.get('telephone', ''))
        self.add_form_field(section_contact, "Téléphone", self.input_telephone)

        self.input_email = ModernInput()
        self.input_email.setText(chantier_data.get('email', ''))
        self.add_form_field(section_contact, "Email", self.input_email)

        # Section Dates et Budget
        section_dates = self.add_section("Dates et Budget")

        self.input_date_ouverture = ModernInput()
        self.input_date_ouverture.setText(chantier_data.get('date_ouverture', ''))
        self.add_form_field(section_dates, "Date d'ouverture *", self.input_date_ouverture)

        self.combo_etat = ModernComboBox()
        self.combo_etat.addItems(["Accepté", "En cours", "Terminé", "Facturé", "Clôturé"])
        self.combo_etat.setCurrentText(chantier_data.get('etat', 'Accepté'))
        self.add_form_field(section_dates, "État", self.combo_etat)

        self.input_budget_prev = ModernInput()
        self.input_budget_prev.setText(str(chantier_data.get('budget_previsionnel', 0)))
        self.add_form_field(section_dates, "Budget prévisionnel (€)", self.input_budget_prev)

        self.input_budget_reel = ModernInput()
        self.input_budget_reel.setText(str(chantier_data.get('budget_reel', 0)))
        self.add_form_field(section_dates, "Budget réel (€)", self.input_budget_reel)

        # Section Notes
        section_notes = self.add_section("Notes")

        self.input_notes = ModernTextEdit()
        self.input_notes.setMinimumHeight(100)
        self.input_notes.setPlainText(chantier_data.get('notes', ''))
        section_notes.addWidget(self.input_notes)

        # Boutons
        btn_annuler = ModernButton("Annuler", "secondary")
        btn_annuler.clicked.connect(self.reject)

        btn_enregistrer = ModernButton("Enregistrer", "primary")
        btn_enregistrer.clicked.connect(self.valider)

        self.add_button_bar([btn_annuler, btn_enregistrer])

    def valider(self):
        """Valide les données du formulaire"""
        if not self.input_nom.text().strip():
            QMessageBox.warning(self, "Champ manquant", "Le nom du chantier est obligatoire.")
            self.input_nom.setFocus()
            return

        if not self.input_client.text().strip():
            QMessageBox.warning(self, "Champ manquant", "Le nom du client est obligatoire.")
            self.input_client.setFocus()
            return

        try:
            float(self.input_budget_prev.text().replace(',', '.'))
            float(self.input_budget_reel.text().replace(',', '.'))
        except ValueError:
            QMessageBox.warning(self, "Format invalide", "Les budgets doivent être des nombres valides.")
            return

        self.accept()

    def get_data(self):
        """Retourne les données modifiées"""
        return {
            'nom': self.input_nom.text().strip(),
            'numero_commande': self.input_numero.text().strip(),
            'client': self.input_client.text().strip(),
            'adresse': self.input_adresse.text().strip(),
            'code_postal': self.input_code_postal.text().strip(),
            'ville': self.input_ville.text().strip(),
            'telephone': self.input_telephone.text().strip(),
            'email': self.input_email.text().strip(),
            'date_ouverture': self.input_date_ouverture.text().strip(),
            'etat': self.combo_etat.currentText(),
            'budget_previsionnel': float(self.input_budget_prev.text().replace(',', '.')),
            'budget_reel': float(self.input_budget_reel.text().replace(',', '.')),
            'notes': self.input_notes.toPlainText().strip()
        }


class DetailPanel(QWidget):
    """Panneau de détails d'un chantier"""

    etat_changed = Signal(int, str)  # chantier_id, nouvel_etat

    def __init__(self, parent=None):
        super().__init__(parent)

        self.chantier_id = None

        # Layout principal
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(
            DesignSystem.SPACING_XL,
            DesignSystem.SPACING_XL,
            DesignSystem.SPACING_XL,
            DesignSystem.SPACING_XL
        )
        main_layout.setSpacing(DesignSystem.SPACING_LG)

        # Titre
        self.title_label = ModernLabel("Sélectionnez un chantier", "large")
        main_layout.addWidget(self.title_label)

        # Carte 1: Informations principales
        card_info = ModernCard()
        self.info_layout = card_info.card_layout

        self.label_client = ModernLabel("", "body")
        self.label_numero = ModernLabel("", "secondary")
        self.label_date = ModernLabel("", "secondary")

        self.info_layout.addWidget(ModernLabel("Client", "secondary"))
        self.info_layout.addWidget(self.label_client)
        self.info_layout.addSpacing(DesignSystem.SPACING_SM)
        self.info_layout.addWidget(ModernLabel("N° Commande", "secondary"))
        self.info_layout.addWidget(self.label_numero)
        self.info_layout.addSpacing(DesignSystem.SPACING_SM)
        self.info_layout.addWidget(ModernLabel("Date d'ouverture", "secondary"))
        self.info_layout.addWidget(self.label_date)

        main_layout.addWidget(card_info)

        # Carte 2: Localisation
        card_location = ModernCard()
        self.location_layout = card_location.card_layout

        self.label_adresse = ModernLabel("", "body")
        self.label_ville = ModernLabel("", "body")
        self.label_contact = ModernLabel("", "secondary")

        self.location_layout.addWidget(ModernLabel("Localisation", "title"))
        self.location_layout.addWidget(self.label_adresse)
        self.location_layout.addWidget(self.label_ville)
        self.location_layout.addSpacing(DesignSystem.SPACING_SM)
        self.location_layout.addWidget(ModernLabel("Contact", "secondary"))
        self.location_layout.addWidget(self.label_contact)

        main_layout.addWidget(card_location)

        # Carte 3: État et Budget
        card_budget = ModernCard()
        budget_layout = card_budget.card_layout

        budget_layout.addWidget(ModernLabel("État et Budget", "title"))

        # ComboBox pour changer l'état
        budget_layout.addWidget(ModernLabel("État du chantier", "secondary"))
        self.combo_etat = ModernComboBox()
        self.combo_etat.addItems(["Accepté", "En cours", "Terminé", "Facturé", "Clôturé"])
        self.combo_etat.currentTextChanged.connect(self.on_etat_changed)
        budget_layout.addWidget(self.combo_etat)

        budget_layout.addSpacing(DesignSystem.SPACING_SM)

        # Budgets
        self.label_budget_prev = ModernLabel("", "body")
        self.label_budget_reel = ModernLabel("", "body")
        self.label_ecart = ModernLabel("", "body")

        budget_layout.addWidget(ModernLabel("Budget prévisionnel", "secondary"))
        budget_layout.addWidget(self.label_budget_prev)
        budget_layout.addSpacing(DesignSystem.SPACING_SM)
        budget_layout.addWidget(ModernLabel("Budget réel", "secondary"))
        budget_layout.addWidget(self.label_budget_reel)
        budget_layout.addSpacing(DesignSystem.SPACING_SM)
        budget_layout.addWidget(ModernLabel("Écart", "secondary"))
        budget_layout.addWidget(self.label_ecart)

        main_layout.addWidget(card_budget)

        # Carte 4: Notes
        card_notes = ModernCard()
        notes_layout = card_notes.card_layout

        notes_layout.addWidget(ModernLabel("Notes", "title"))
        self.label_notes = ModernLabel("", "secondary")
        self.label_notes.setWordWrap(True)
        notes_layout.addWidget(self.label_notes)

        main_layout.addWidget(card_notes)

        # Espaceur pour pousser tout en haut
        main_layout.addStretch()

        # Message par défaut (caché quand un chantier est affiché)
        self.empty_state = QLabel("👈 Sélectionnez un chantier\npour voir ses détails")
        self.empty_state.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.empty_state.setStyleSheet(f"""
            font-size: 16px;
            color: {DesignSystem.TEXT_SECONDARY};
        """)
        main_layout.addWidget(self.empty_state)

        # Cacher les cartes par défaut
        card_info.hide()
        card_location.hide()
        card_budget.hide()
        card_notes.hide()

        self.cards = [card_info, card_location, card_budget, card_notes]

    def display_chantier(self, chantier_data: dict):
        """Affiche les détails d'un chantier"""
        self.chantier_id = chantier_data['id']

        # Afficher les cartes
        self.empty_state.hide()
        for card in self.cards:
            card.show()

        # Mettre à jour les labels
        self.title_label.setText(chantier_data.get('nom', 'Sans nom'))
        self.label_client.setText(chantier_data.get('client', '-'))
        self.label_numero.setText(f"N° {chantier_data.get('numero_commande', '-')}")
        self.label_date.setText(chantier_data.get('date_ouverture', '-'))

        adresse = chantier_data.get('adresse', '')
        cp = chantier_data.get('code_postal', '')
        ville = chantier_data.get('ville', '')

        self.label_adresse.setText(adresse if adresse else '-')
        self.label_ville.setText(f"{cp} {ville}" if cp or ville else '-')

        tel = chantier_data.get('telephone', '')
        email = chantier_data.get('email', '')
        contact = []
        if tel:
            contact.append(f"📞 {tel}")
        if email:
            contact.append(f"✉️ {email}")
        self.label_contact.setText('\n'.join(contact) if contact else '-')

        # État (bloquer le signal temporairement)
        self.combo_etat.blockSignals(True)
        self.combo_etat.setCurrentText(chantier_data.get('etat', 'Accepté'))
        self.combo_etat.blockSignals(False)

        # Budgets
        budget_prev = chantier_data.get('budget_previsionnel', 0)
        budget_reel = chantier_data.get('budget_reel', 0)
        ecart = budget_reel - budget_prev

        self.label_budget_prev.setText(f"{budget_prev:,.2f} €")
        self.label_budget_reel.setText(f"{budget_reel:,.2f} €")

        # Colorer l'écart
        ecart_text = f"{ecart:+,.2f} €"
        if ecart > 0:
            color = DesignSystem.ERROR_RED
        elif ecart < 0:
            color = DesignSystem.SUCCESS_GREEN
        else:
            color = DesignSystem.TEXT_SECONDARY

        self.label_ecart.setText(ecart_text)
        self.label_ecart.setStyleSheet(f"color: {color}; font-weight: 600;")

        # Notes
        notes = chantier_data.get('notes', '')
        self.label_notes.setText(notes if notes else 'Aucune note')

    def clear(self):
        """Efface l'affichage"""
        self.chantier_id = None
        self.title_label.setText("Sélectionnez un chantier")

        for card in self.cards:
            card.hide()

        self.empty_state.show()

    def on_etat_changed(self, nouvel_etat: str):
        """Gère le changement d'état"""
        if self.chantier_id:
            self.etat_changed.emit(self.chantier_id, nouvel_etat)


class ModuleChantiers(QWidget):
    """Module de gestion des chantiers"""

    def __init__(self, db: Database, parent=None):
        super().__init__(parent)

        self.db = db
        self.chantiers = []
        self.chantier_selectionne = None

        # Layout principal horizontal (liste + détails)
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # === PANNEAU GAUCHE : Liste des chantiers ===
        left_panel = QWidget()
        left_panel.setMinimumWidth(600)
        left_panel.setStyleSheet(f"background-color: {DesignSystem.SURFACE};")

        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(
            DesignSystem.SPACING_XL,
            DesignSystem.SPACING_XL,
            DesignSystem.SPACING_XL,
            DesignSystem.SPACING_XL
        )
        left_layout.setSpacing(DesignSystem.SPACING_LG)

        # En-tête avec titre et bouton
        header_layout = QHBoxLayout()

        title_label = ModernLabel("Chantiers", "large")
        header_layout.addWidget(title_label)

        header_layout.addStretch()

        btn_nouveau = ModernButton("+ Nouveau", "primary")
        btn_nouveau.clicked.connect(self.creer_chantier)
        header_layout.addWidget(btn_nouveau)

        left_layout.addLayout(header_layout)

        # Barre de recherche
        search_layout = QHBoxLayout()
        search_layout.setSpacing(DesignSystem.SPACING_SM)

        self.search_input = ModernInput("Rechercher un chantier...")
        self.search_input.textChanged.connect(self.rechercher)
        search_layout.addWidget(self.search_input)

        btn_refresh = ModernButton("🔄", "secondary")
        btn_refresh.setFixedWidth(DesignSystem.BUTTON_HEIGHT)
        btn_refresh.clicked.connect(self.charger_chantiers)
        search_layout.addWidget(btn_refresh)

        left_layout.addLayout(search_layout)

        # Tableau des chantiers
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Nom", "N° Commande", "Client", "Date d'ouverture"])

        # Configuration du tableau
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)

        # Ajuster les colonnes
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)

        # Style du tableau
        self.table.setStyleSheet(f"""
            QTableWidget {{
                background-color: {DesignSystem.SURFACE};
                border: 1px solid {DesignSystem.BORDER_COLOR};
                border-radius: {DesignSystem.RADIUS_MD}px;
                gridline-color: {DesignSystem.BORDER_COLOR};
            }}
            QTableWidget::item {{
                padding: {DesignSystem.SPACING_SM}px;
            }}
            QTableWidget::item:selected {{
                background-color: {DesignSystem.ACCENT_BLUE};
                color: white;
            }}
            QHeaderView::section {{
                background-color: {DesignSystem.SURFACE_ELEVATED};
                color: {DesignSystem.TEXT_SECONDARY};
                padding: {DesignSystem.SPACING_MD}px;
                border: none;
                border-bottom: 1px solid {DesignSystem.BORDER_COLOR};
                font-weight: 600;
            }}
        """)

        # Connexions
        self.table.itemSelectionChanged.connect(self.on_selection_changed)

        left_layout.addWidget(self.table)

        # Boutons d'action
        actions_layout = QHBoxLayout()
        actions_layout.setSpacing(DesignSystem.SPACING_SM)

        btn_modifier = ModernButton("Modifier", "secondary")
        btn_modifier.clicked.connect(self.modifier_chantier)
        actions_layout.addWidget(btn_modifier)

        btn_supprimer = ModernButton("Supprimer", "danger")
        btn_supprimer.clicked.connect(self.supprimer_chantier)
        actions_layout.addWidget(btn_supprimer)

        actions_layout.addStretch()

        left_layout.addLayout(actions_layout)

        main_layout.addWidget(left_panel, 3)

        # === PANNEAU DROIT : Détails du chantier ===
        self.detail_panel = DetailPanel()
        self.detail_panel.setMinimumWidth(400)
        self.detail_panel.setStyleSheet(f"background-color: {DesignSystem.BACKGROUND};")
        self.detail_panel.etat_changed.connect(self.changer_etat)

        main_layout.addWidget(self.detail_panel, 2)

        # Charger les chantiers
        self.charger_chantiers()

    def charger_chantiers(self):
        """Charge tous les chantiers depuis la base de données"""
        self.chantiers = self.db.get_chantiers_tries()
        self.afficher_chantiers(self.chantiers)

    def afficher_chantiers(self, chantiers: list):
        """Affiche la liste des chantiers dans le tableau"""
        self.table.setRowCount(0)

        for chantier in chantiers:
            row = self.table.rowCount()
            self.table.insertRow(row)

            # Nom
            item_nom = QTableWidgetItem(chantier.get('nom', ''))
            item_nom.setData(Qt.ItemDataRole.UserRole, chantier['id'])

            # Couleur selon l'état
            etat = chantier.get('etat', '')
            color = DesignSystem.get_etat_color(etat)

            # Griser les chantiers clôturés
            if etat == 'Clôturé':
                item_nom.setForeground(QColor(DesignSystem.TEXT_SECONDARY))

            # Indicateur coloré
            item_nom.setText(f"● {chantier.get('nom', '')}")
            item_nom.setForeground(QColor(color))

            # N° Commande
            item_numero = QTableWidgetItem(chantier.get('numero_commande', '-'))
            if etat == 'Clôturé':
                item_numero.setForeground(QColor(DesignSystem.TEXT_SECONDARY))

            # Client
            item_client = QTableWidgetItem(chantier.get('client', ''))
            if etat == 'Clôturé':
                item_client.setForeground(QColor(DesignSystem.TEXT_SECONDARY))

            # Date
            item_date = QTableWidgetItem(chantier.get('date_ouverture', ''))
            if etat == 'Clôturé':
                item_date.setForeground(QColor(DesignSystem.TEXT_SECONDARY))

            self.table.setItem(row, 0, item_nom)
            self.table.setItem(row, 1, item_numero)
            self.table.setItem(row, 2, item_client)
            self.table.setItem(row, 3, item_date)

    def rechercher(self):
        """Recherche des chantiers"""
        terme = self.search_input.text().strip()

        if terme:
            chantiers_trouves = self.db.rechercher_chantiers(terme)
            self.afficher_chantiers(chantiers_trouves)
        else:
            self.charger_chantiers()

    def on_selection_changed(self):
        """Gère le changement de sélection dans la liste"""
        selected_items = self.table.selectedItems()

        if selected_items:
            # Récupérer l'ID du chantier (stocké dans la première colonne)
            chantier_id = self.table.item(selected_items[0].row(), 0).data(Qt.ItemDataRole.UserRole)

            # Récupérer les données complètes
            chantier_data = self.db.get_chantier(chantier_id)

            if chantier_data:
                self.chantier_selectionne = chantier_data
                self.detail_panel.display_chantier(chantier_data)
        else:
            self.chantier_selectionne = None
            self.detail_panel.clear()

    def creer_chantier(self):
        """Ouvre le dialogue de création d'un chantier"""
        dialog = ChantierDialog(self)

        if dialog.exec():
            data = dialog.get_data()

            try:
                self.db.ajouter_chantier(data)
                QMessageBox.information(self, "Succès", "Le chantier a été créé avec succès.")
                self.charger_chantiers()
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur lors de la création : {str(e)}")

    def modifier_chantier(self):
        """Ouvre le dialogue de modification d'un chantier"""
        if not self.chantier_selectionne:
            QMessageBox.warning(self, "Aucune sélection", "Veuillez sélectionner un chantier à modifier.")
            return

        dialog = ModifierChantierDialog(self.chantier_selectionne, self)

        if dialog.exec():
            data = dialog.get_data()

            try:
                self.db.modifier_chantier(self.chantier_selectionne['id'], data)
                QMessageBox.information(self, "Succès", "Le chantier a été modifié avec succès.")
                self.charger_chantiers()

                # Mettre à jour le panneau de détails
                chantier_data = self.db.get_chantier(self.chantier_selectionne['id'])
                if chantier_data:
                    self.chantier_selectionne = chantier_data
                    self.detail_panel.display_chantier(chantier_data)
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur lors de la modification : {str(e)}")

    def supprimer_chantier(self):
        """Supprime le chantier sélectionné"""
        if not self.chantier_selectionne:
            QMessageBox.warning(self, "Aucune sélection", "Veuillez sélectionner un chantier à supprimer.")
            return

        reply = QMessageBox.question(
            self,
            "Confirmer la suppression",
            f"Êtes-vous sûr de vouloir supprimer le chantier '{self.chantier_selectionne['nom']}' ?\n\n"
            "Cette action est irréversible.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                self.db.supprimer_chantier(self.chantier_selectionne['id'])
                QMessageBox.information(self, "Succès", "Le chantier a été supprimé.")
                self.chantier_selectionne = None
                self.detail_panel.clear()
                self.charger_chantiers()
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur lors de la suppression : {str(e)}")

    def changer_etat(self, chantier_id: int, nouvel_etat: str):
        """Change l'état d'un chantier"""
        try:
            self.db.changer_etat_chantier(chantier_id, nouvel_etat)
            self.charger_chantiers()

            # Mettre à jour le panneau de détails
            chantier_data = self.db.get_chantier(chantier_id)
            if chantier_data:
                self.chantier_selectionne = chantier_data
                self.detail_panel.display_chantier(chantier_data)

            # Message de confirmation
            QMessageBox.information(
                self,
                "État modifié",
                f"L'état du chantier a été changé en '{nouvel_etat}'."
            )
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Erreur lors du changement d'état : {str(e)}")
