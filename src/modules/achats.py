"""
GESCO v5.0 - Module Achats
Gestion des achats : directs (manuels) et via fournisseurs API (Sonepar, etc.)
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime
from typing import List, Optional

from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QTableWidget,
                               QTableWidgetItem, QHeaderView, QPushButton,
                               QMessageBox, QTabWidget, QComboBox, QDateEdit,
                               QDoubleSpinBox, QAbstractItemView, QFileDialog)
from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QColor

from design_system import (DesignSystem, ModernLabel, ModernInput, ModernComboBox,
                           ModernTextEdit, ModernButton, ModernCard, ResponsiveDialog)
from database import Database
from integrations.sonepar import SoneParClient, SoneParConfig, SoneParDatabase


class AjouterAchatDialog(ResponsiveDialog):
    """Dialogue pour ajouter un achat direct"""

    def __init__(self, db: Database, parent=None):
        super().__init__("Nouvel Achat Direct", 700, parent)
        self.db = db

        # Section Chantier
        section_chantier = self.add_section("Chantier")

        self.combo_chantier = ModernComboBox()
        chantiers = [c for c in self.db.get_chantiers() if c['etat'] != 'Clôturé']
        for chantier in chantiers:
            self.combo_chantier.addItem(f"{chantier['nom']} - {chantier['client']}", chantier['id'])
        self.add_form_field(section_chantier, "Chantier *", self.combo_chantier)

        # Section Fournisseur
        section_fournisseur = self.add_section("Fournisseur")

        self.combo_fournisseur = ModernComboBox()
        self.combo_fournisseur.addItem("(Nouveau fournisseur...)", None)
        fournisseurs = self.db.get_fournisseurs()
        for f in fournisseurs:
            self.combo_fournisseur.addItem(f['nom'], f['id'])
        self.combo_fournisseur.currentIndexChanged.connect(self.on_fournisseur_changed)
        self.add_form_field(section_fournisseur, "Fournisseur", self.combo_fournisseur)

        self.input_nouveau_fournisseur = ModernInput("Nom du nouveau fournisseur")
        self.input_nouveau_fournisseur.hide()
        section_fournisseur.addWidget(self.input_nouveau_fournisseur)

        # Section Achat
        section_achat = self.add_section("Détails de l'achat")

        self.combo_categorie = ModernComboBox()
        categories = self.db.get_categories_achats()
        for cat in categories:
            self.combo_categorie.addItem(cat['nom'], cat['id'])
        self.add_form_field(section_achat, "Catégorie *", self.combo_categorie)

        self.date_achat = QDateEdit()
        self.date_achat.setDate(QDate.currentDate())
        self.date_achat.setCalendarPopup(True)
        self.date_achat.setStyleSheet(f"""
            QDateEdit {{
                background-color: {DesignSystem.SURFACE};
                border: 1px solid {DesignSystem.BORDER_COLOR};
                border-radius: {DesignSystem.RADIUS_SM}px;
                padding: 0 {DesignSystem.SPACING_MD}px;
                min-height: {DesignSystem.INPUT_HEIGHT}px;
            }}
        """)
        self.add_form_field(section_achat, "Date *", self.date_achat)

        self.input_numero_facture = ModernInput("Numéro de facture")
        self.add_form_field(section_achat, "N° Facture", self.input_numero_facture)

        self.input_description = ModernTextEdit()
        self.input_description.setMaximumHeight(80)
        self.input_description.setPlaceholderText("Description de l'achat")
        self.add_form_field(section_achat, "Description *", self.input_description)

        # Section Montants
        section_montants = self.add_section("Montants")

        montants_layout = QHBoxLayout()
        montants_layout.setSpacing(DesignSystem.SPACING_MD)

        ht_layout = QVBoxLayout()
        ht_layout.setSpacing(DesignSystem.SPACING_SM)
        ht_layout.addWidget(ModernLabel("Montant HT (€) *"))
        self.input_montant_ht = QDoubleSpinBox()
        self.input_montant_ht.setRange(0, 999999.99)
        self.input_montant_ht.setDecimals(2)
        self.input_montant_ht.setSuffix(" €")
        self.input_montant_ht.valueChanged.connect(self.calculer_ttc)
        self.input_montant_ht.setStyleSheet(f"""
            QDoubleSpinBox {{
                background-color: {DesignSystem.SURFACE};
                border: 1px solid {DesignSystem.BORDER_COLOR};
                border-radius: {DesignSystem.RADIUS_SM}px;
                padding: 0 {DesignSystem.SPACING_MD}px;
                min-height: {DesignSystem.INPUT_HEIGHT}px;
            }}
        """)
        ht_layout.addWidget(self.input_montant_ht)
        montants_layout.addLayout(ht_layout, 1)

        tva_layout = QVBoxLayout()
        tva_layout.setSpacing(DesignSystem.SPACING_SM)
        tva_layout.addWidget(ModernLabel("TVA (%)"))
        self.input_tva = QDoubleSpinBox()
        self.input_tva.setRange(0, 100)
        self.input_tva.setDecimals(1)
        self.input_tva.setValue(20.0)
        self.input_tva.setSuffix(" %")
        self.input_tva.valueChanged.connect(self.calculer_ttc)
        self.input_tva.setStyleSheet(self.input_montant_ht.styleSheet())
        tva_layout.addWidget(self.input_tva)
        montants_layout.addLayout(tva_layout, 1)

        ttc_layout = QVBoxLayout()
        ttc_layout.setSpacing(DesignSystem.SPACING_SM)
        ttc_layout.addWidget(ModernLabel("Montant TTC (€)"))
        self.input_montant_ttc = QDoubleSpinBox()
        self.input_montant_ttc.setRange(0, 999999.99)
        self.input_montant_ttc.setDecimals(2)
        self.input_montant_ttc.setSuffix(" €")
        self.input_montant_ttc.setReadOnly(True)
        self.input_montant_ttc.setStyleSheet(f"""
            QDoubleSpinBox {{
                background-color: {DesignSystem.SURFACE_ELEVATED};
                border: 1px solid {DesignSystem.BORDER_COLOR};
                border-radius: {DesignSystem.RADIUS_SM}px;
                padding: 0 {DesignSystem.SPACING_MD}px;
                min-height: {DesignSystem.INPUT_HEIGHT}px;
                color: {DesignSystem.TEXT_SECONDARY};
            }}
        """)
        ttc_layout.addWidget(self.input_montant_ttc)
        montants_layout.addLayout(ttc_layout, 1)

        section_montants.addLayout(montants_layout)

        # Section Paiement
        section_paiement = self.add_section("Paiement")

        self.combo_paiement = ModernComboBox()
        self.combo_paiement.addItems(["Carte bancaire", "Chèque", "Virement", "Espèces", "Autre"])
        self.add_form_field(section_paiement, "Moyen de paiement", self.combo_paiement)

        self.input_reference = ModernInput("Numéro de chèque, référence virement, etc.")
        self.add_form_field(section_paiement, "Référence", self.input_reference)

        # Section Notes
        section_notes = self.add_section("Notes")

        self.input_notes = ModernTextEdit()
        self.input_notes.setMaximumHeight(60)
        self.input_notes.setPlaceholderText("Notes complémentaires (optionnel)")
        section_notes.addWidget(self.input_notes)

        # Boutons
        btn_annuler = ModernButton("Annuler", "secondary")
        btn_annuler.clicked.connect(self.reject)

        btn_ajouter = ModernButton("Ajouter l'achat", "success")
        btn_ajouter.clicked.connect(self.valider)

        self.add_button_bar([btn_annuler, btn_ajouter])

    def on_fournisseur_changed(self):
        """Affiche/cache le champ nouveau fournisseur"""
        if self.combo_fournisseur.currentData() is None:
            self.input_nouveau_fournisseur.show()
        else:
            self.input_nouveau_fournisseur.hide()

    def calculer_ttc(self):
        """Calcule automatiquement le montant TTC"""
        ht = self.input_montant_ht.value()
        tva = self.input_tva.value()
        ttc = ht * (1 + tva / 100)
        self.input_montant_ttc.setValue(ttc)

    def valider(self):
        """Valide les données"""
        if self.combo_chantier.count() == 0:
            QMessageBox.warning(self, "Aucun chantier", "Créez d'abord un chantier.")
            return

        if not self.input_description.toPlainText().strip():
            QMessageBox.warning(self, "Champ manquant", "La description est obligatoire.")
            return

        if self.input_montant_ht.value() == 0:
            QMessageBox.warning(self, "Montant invalide", "Le montant HT doit être supérieur à 0.")
            return

        self.accept()

    def get_data(self):
        """Retourne les données de l'achat"""
        fournisseur_id = self.combo_fournisseur.currentData()
        fournisseur_nom = None

        if fournisseur_id is None:
            # Nouveau fournisseur
            fournisseur_nom = self.input_nouveau_fournisseur.text().strip()
            if fournisseur_nom:
                # Créer le fournisseur
                fournisseur_id = self.db.ajouter_fournisseur({
                    'nom': fournisseur_nom,
                    'type': 'Autre'
                })
        else:
            # Récupérer le nom du fournisseur existant
            fournisseur_nom = self.combo_fournisseur.currentText()

        return {
            'chantier_id': self.combo_chantier.currentData(),
            'fournisseur_id': fournisseur_id,
            'fournisseur_nom': fournisseur_nom,
            'categorie_id': self.combo_categorie.currentData(),
            'date_achat': self.date_achat.date().toString("yyyy-MM-dd"),
            'numero_facture': self.input_numero_facture.text().strip(),
            'description': self.input_description.toPlainText().strip(),
            'montant_ht': self.input_montant_ht.value(),
            'montant_ttc': self.input_montant_ttc.value(),
            'tva': self.input_tva.value(),
            'moyen_paiement': self.combo_paiement.currentText(),
            'reference_paiement': self.input_reference.text().strip(),
            'notes': self.input_notes.toPlainText().strip()
        }


class AchatsDirectsWidget(QWidget):
    """Widget pour les achats directs (saisie manuelle)"""

    def __init__(self, db: Database, parent=None):
        super().__init__(parent)
        self.db = db

        # Layout principal
        layout = QVBoxLayout(self)
        layout.setContentsMargins(
            DesignSystem.SPACING_XL,
            DesignSystem.SPACING_XL,
            DesignSystem.SPACING_XL,
            DesignSystem.SPACING_XL
        )
        layout.setSpacing(DesignSystem.SPACING_LG)

        # En-tête
        header_layout = QHBoxLayout()

        title_label = ModernLabel("Achats Directs", "large")
        header_layout.addWidget(title_label)

        header_layout.addStretch()

        btn_nouvel_achat = ModernButton("+ Nouvel achat", "primary")
        btn_nouvel_achat.clicked.connect(self.ajouter_achat)
        header_layout.addWidget(btn_nouvel_achat)

        layout.addLayout(header_layout)

        # Info
        info_label = ModernLabel(
            "💡 Saisissez ici vos achats manuels : tickets, factures locales, etc.",
            "secondary"
        )
        layout.addWidget(info_label)

        # Filtres
        filters_layout = QHBoxLayout()
        filters_layout.setSpacing(DesignSystem.SPACING_SM)

        filters_layout.addWidget(ModernLabel("Filtrer :"))

        self.filter_chantier = ModernComboBox()
        self.filter_chantier.addItem("Tous les chantiers", None)
        chantiers = self.db.get_chantiers()
        for c in chantiers:
            self.filter_chantier.addItem(c['nom'], c['id'])
        self.filter_chantier.currentIndexChanged.connect(self.charger_achats)
        filters_layout.addWidget(self.filter_chantier, 1)

        self.filter_categorie = ModernComboBox()
        self.filter_categorie.addItem("Toutes catégories", None)
        categories = self.db.get_categories_achats()
        for cat in categories:
            self.filter_categorie.addItem(cat['nom'], cat['id'])
        self.filter_categorie.currentIndexChanged.connect(self.charger_achats)
        filters_layout.addWidget(self.filter_categorie, 1)

        filters_layout.addStretch()

        layout.addLayout(filters_layout)

        # Tableau des achats
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "Date", "Chantier", "Catégorie", "Fournisseur",
            "Description", "Montant HT", "Montant TTC", "N° Facture"
        ])

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(7, QHeaderView.ResizeMode.ResizeToContents)

        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
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

        layout.addWidget(self.table)

        # Totaux
        totaux_layout = QHBoxLayout()
        totaux_layout.addStretch()

        self.label_total = ModernLabel("Total : 0.00 € TTC", "title")
        totaux_layout.addWidget(self.label_total)

        layout.addLayout(totaux_layout)

        # Charger les achats
        self.charger_achats()

    def ajouter_achat(self):
        """Ouvre le dialogue d'ajout d'achat"""
        dialog = AjouterAchatDialog(self.db, self)

        if dialog.exec():
            data = dialog.get_data()

            try:
                self.db.ajouter_achat_direct(data)
                QMessageBox.information(self, "Succès", "L'achat a été enregistré.")
                self.charger_achats()
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur lors de l'enregistrement : {str(e)}")

    def charger_achats(self):
        """Charge les achats depuis la base"""
        chantier_id = self.filter_chantier.currentData()
        categorie_id = self.filter_categorie.currentData()

        achats = self.db.get_achats_directs(chantier_id=chantier_id, categorie_id=categorie_id)

        self.table.setRowCount(0)
        total = 0.0

        for achat in achats:
            row = self.table.rowCount()
            self.table.insertRow(row)

            self.table.setItem(row, 0, QTableWidgetItem(achat['date_achat']))
            self.table.setItem(row, 1, QTableWidgetItem(achat['chantier_nom'] or '-'))
            self.table.setItem(row, 2, QTableWidgetItem(achat['categorie_nom'] or '-'))
            self.table.setItem(row, 3, QTableWidgetItem(achat['fournisseur_nom'] or '-'))
            self.table.setItem(row, 4, QTableWidgetItem(achat['description'][:50] + '...'))
            self.table.setItem(row, 5, QTableWidgetItem(f"{achat['montant_ht']:.2f} €"))
            self.table.setItem(row, 6, QTableWidgetItem(f"{achat['montant_ttc']:.2f} €"))
            self.table.setItem(row, 7, QTableWidgetItem(achat['numero_facture'] or '-'))

            total += achat['montant_ttc']

        self.label_total.setText(f"Total : {total:.2f} € TTC")


class ModuleAchats(QWidget):
    """Module de gestion des achats : directs + fournisseurs API"""

    def __init__(self, db: Database, parent=None):
        super().__init__(parent)
        self.db = db

        # Layout principal
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Onglets principaux
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet(f"""
            QTabWidget::pane {{
                border: none;
                background-color: {DesignSystem.BACKGROUND};
            }}
            QTabBar::tab {{
                background-color: {DesignSystem.SURFACE_ELEVATED};
                border: 1px solid {DesignSystem.BORDER_COLOR};
                border-bottom: none;
                border-top-left-radius: {DesignSystem.RADIUS_SM}px;
                border-top-right-radius: {DesignSystem.RADIUS_SM}px;
                padding: {DesignSystem.SPACING_MD}px {DesignSystem.SPACING_XL}px;
                margin-right: 2px;
                margin-left: {DesignSystem.SPACING_LG}px;
                font-size: {DesignSystem.FONT_SIZE_BODY}px;
                font-weight: 500;
            }}
            QTabBar::tab:first {{
                margin-left: {DesignSystem.SPACING_XL}px;
            }}
            QTabBar::tab:selected {{
                background-color: {DesignSystem.BACKGROUND};
                color: {DesignSystem.ACCENT_BLUE};
                font-weight: 600;
            }}
            QTabBar::tab:hover:!selected {{
                background-color: {DesignSystem.SURFACE};
            }}
        """)

        # Onglet 1 : Achats directs (saisie manuelle)
        self.achats_directs_widget = AchatsDirectsWidget(self.db)
        self.tabs.addTab(self.achats_directs_widget, "📝 Achats Directs")

        # Onglet 2 : Fournisseurs API (Sonepar, etc.)
        try:
            from modules.achats_old import RechercheProduitsWidget, CreerCommandeDialog

            # Créer l'onglet Sonepar
            sonepar_widget = QWidget()
            sonepar_layout = QVBoxLayout(sonepar_widget)
            sonepar_layout.setContentsMargins(0, 0, 0, 0)

            # Sous-onglets pour Sonepar
            sonepar_tabs = QTabWidget()
            sonepar_tabs.setStyleSheet(self.tabs.styleSheet())

            # Initialiser clients Sonepar
            sonepar_config = SoneParConfig()
            sonepar_client = SoneParClient(sonepar_config)

            # Catalogue
            recherche_widget = RechercheProduitsWidget(sonepar_client)
            sonepar_tabs.addTab(recherche_widget, "🔍 Catalogue")

            # Commandes (à implémenter proprement)
            commandes_widget = QWidget()
            commandes_layout = QVBoxLayout(commandes_widget)
            commandes_layout.addWidget(ModernLabel("Commandes Sonepar", "large"))
            commandes_layout.addWidget(ModernLabel("En cours de développement...", "secondary"))
            commandes_layout.addStretch()
            sonepar_tabs.addTab(commandes_widget, "📦 Commandes")

            sonepar_layout.addWidget(sonepar_tabs)

            self.tabs.addTab(sonepar_widget, "🔌 Fournisseurs API")

        except ImportError:
            # Si l'ancien module n'est pas disponible
            placeholder = QWidget()
            placeholder_layout = QVBoxLayout(placeholder)
            placeholder_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            placeholder_layout.addWidget(ModernLabel("🚧 Module Fournisseurs API", "large"))
            placeholder_layout.addWidget(ModernLabel("En cours de développement", "secondary"))
            self.tabs.addTab(placeholder, "🔌 Fournisseurs API")

        main_layout.addWidget(self.tabs)
