"""
GESCO v5.0 - Module Tiers / Clients / Contacts
Gestion des tiers avec intégration Axonaut
"""

from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QTableWidget,
                               QTableWidgetItem, QPushButton, QHeaderView, QMessageBox,
                               QLabel, QGridLayout, QCheckBox, QSpinBox, QFrame)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont

from design_system import (DesignSystem, ModernLabel, ModernInput, ModernComboBox,
                          ModernTextEdit, ModernButton, ModernCard, ResponsiveDialog)
from integrations.axonaut import AxonautClient, AxonautConfig, AxonautDatabase, Company, Employee, Address


class TiersModule(QWidget):
    """Module principal pour la gestion des tiers/clients/contacts"""

    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialisation des clients Axonaut
        self.axonaut_config = AxonautConfig()
        self.axonaut_client = AxonautClient(self.axonaut_config)
        self.axonaut_db = AxonautDatabase()

        # Filtre actuel
        self.current_filter = "tous"  # tous, clients, prospects

        self.init_ui()
        self.charger_tiers()

    def init_ui(self):
        """Initialise l'interface utilisateur"""
        layout = QVBoxLayout(self)
        layout.setSpacing(DesignSystem.SPACING_LG)
        layout.setContentsMargins(
            DesignSystem.SPACING_LG,
            DesignSystem.SPACING_LG,
            DesignSystem.SPACING_LG,
            DesignSystem.SPACING_LG
        )

        # En-tête
        header = ModernLabel("Tiers / Clients / Contacts", "large")
        header.setStyleSheet(f"color: {DesignSystem.TEXT_PRIMARY}; font-weight: 600;")
        layout.addWidget(header)

        # Carte principale
        card = ModernCard()
        card_layout = card.card_layout

        # Barre d'outils
        toolbar = QHBoxLayout()
        toolbar.setSpacing(DesignSystem.SPACING_MD)

        # Recherche
        self.search_input = ModernInput("Rechercher un tiers...")
        self.search_input.setMaximumWidth(300)
        self.search_input.textChanged.connect(self.filtrer_tiers)
        toolbar.addWidget(self.search_input)

        # Filtres
        self.btn_tous = ModernButton("Tous", "secondary")
        self.btn_tous.clicked.connect(lambda: self.changer_filtre("tous"))
        toolbar.addWidget(self.btn_tous)

        self.btn_clients = ModernButton("Clients", "secondary")
        self.btn_clients.clicked.connect(lambda: self.changer_filtre("clients"))
        toolbar.addWidget(self.btn_clients)

        self.btn_prospects = ModernButton("Prospects", "secondary")
        self.btn_prospects.clicked.connect(lambda: self.changer_filtre("prospects"))
        toolbar.addWidget(self.btn_prospects)

        toolbar.addStretch()

        # Actions
        btn_sync = ModernButton("🔄 Synchroniser", "secondary")
        btn_sync.clicked.connect(self.synchroniser_avec_axonaut)
        toolbar.addWidget(btn_sync)

        btn_nouveau = ModernButton("+ Nouveau Tiers", "primary")
        btn_nouveau.clicked.connect(self.nouveau_tiers)
        toolbar.addWidget(btn_nouveau)

        card_layout.addLayout(toolbar)

        # Table des tiers
        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels([
            "Nom", "Type", "B2B/B2C", "Ville", "SIRET", "Contacts", "Actions"
        ])

        # Style de la table
        self.table.setStyleSheet(f"""
            QTableWidget {{
                background-color: {DesignSystem.SURFACE};
                border: none;
                border-radius: {DesignSystem.RADIUS_MD}px;
                gridline-color: {DesignSystem.BORDER_COLOR};
            }}
            QTableWidget::item {{
                padding: {DesignSystem.SPACING_SM}px;
                border: none;
            }}
            QTableWidget::item:selected {{
                background-color: {DesignSystem.ACCENT_BLUE};
                color: white;
            }}
            QHeaderView::section {{
                background-color: {DesignSystem.SURFACE_ELEVATED};
                padding: {DesignSystem.SPACING_MD}px;
                border: none;
                border-bottom: 1px solid {DesignSystem.BORDER_COLOR};
                font-weight: 600;
                font-family: {DesignSystem.FONT_FAMILY};
                font-size: {DesignSystem.FONT_SIZE_BODY}px;
                color: {DesignSystem.TEXT_SECONDARY};
            }}
        """)

        # Configuration des colonnes
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)  # Nom
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)  # Type
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)  # B2B/B2C
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)  # Ville
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)  # SIRET
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)  # Contacts
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.Fixed)  # Actions - largeur fixe
        header.resizeSection(6, 480)  # Largeur pour 4 boutons

        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setDefaultSectionSize(48)  # Hauteur des lignes

        card_layout.addWidget(self.table)

        layout.addWidget(card)

        # Mettre à jour l'apparence du filtre actif
        self.mettre_a_jour_filtres()

    def mettre_a_jour_filtres(self):
        """Met à jour l'apparence des boutons de filtre"""
        # Réinitialiser tous les boutons
        for btn in [self.btn_tous, self.btn_clients, self.btn_prospects]:
            btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {DesignSystem.SURFACE_ELEVATED};
                    color: {DesignSystem.TEXT_PRIMARY};
                    border: none;
                    border-radius: {DesignSystem.RADIUS_SM}px;
                    padding: {DesignSystem.SPACING_SM}px {DesignSystem.SPACING_MD}px;
                    font-family: {DesignSystem.FONT_FAMILY};
                    font-size: {DesignSystem.FONT_SIZE_BODY}px;
                    font-weight: 500;
                }}
                QPushButton:hover {{
                    background-color: #F0F0F2;
                }}
            """)

        # Mettre en surbrillance le filtre actif
        active_btn = None
        if self.current_filter == "tous":
            active_btn = self.btn_tous
        elif self.current_filter == "clients":
            active_btn = self.btn_clients
        elif self.current_filter == "prospects":
            active_btn = self.btn_prospects

        if active_btn:
            active_btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {DesignSystem.ACCENT_BLUE};
                    color: white;
                    border: none;
                    border-radius: {DesignSystem.RADIUS_SM}px;
                    padding: {DesignSystem.SPACING_SM}px {DesignSystem.SPACING_MD}px;
                    font-family: {DesignSystem.FONT_FAMILY};
                    font-size: {DesignSystem.FONT_SIZE_BODY}px;
                    font-weight: 600;
                }}
                QPushButton:hover {{
                    background-color: {DesignSystem.ACCENT_BLUE};
                }}
            """)

    def changer_filtre(self, filtre: str):
        """Change le filtre actif"""
        self.current_filter = filtre
        self.mettre_a_jour_filtres()
        self.charger_tiers()

    def charger_tiers(self):
        """Charge les tiers selon le filtre actif"""
        # Déterminer les filtres
        is_customer = None
        is_prospect = None

        if self.current_filter == "clients":
            is_customer = True
        elif self.current_filter == "prospects":
            is_prospect = True

        # Charger depuis la base locale
        search_term = self.search_input.text() if self.search_input.text() else None
        companies = self.axonaut_db.get_companies(
            is_customer=is_customer,
            is_prospect=is_prospect,
            search=search_term
        )

        # Afficher dans la table
        self.table.setRowCount(len(companies))

        for row, company in enumerate(companies):
            # Nom
            self.table.setItem(row, 0, QTableWidgetItem(company.name or "Sans nom"))

            # Type
            self.table.setItem(row, 1, QTableWidgetItem(company.type_label))

            # B2B/B2C
            self.table.setItem(row, 2, QTableWidgetItem(company.b2c_label))

            # Ville
            self.table.setItem(row, 3, QTableWidgetItem(company.address_city or "-"))

            # SIRET
            self.table.setItem(row, 4, QTableWidgetItem(company.siret or "-"))

            # Nombre de contacts
            nb_contacts = len(company.employees)
            self.table.setItem(row, 5, QTableWidgetItem(str(nb_contacts)))

            # Boutons d'actions
            actions_widget = QWidget()
            actions_layout = QHBoxLayout(actions_widget)
            actions_layout.setContentsMargins(8, 4, 8, 4)
            actions_layout.setSpacing(6)

            # Bouton Modifier
            btn_edit = ModernButton("Modifier", "secondary")
            btn_edit.setFixedHeight(32)
            btn_edit.clicked.connect(lambda checked, c=company: self.modifier_tiers(c))
            actions_layout.addWidget(btn_edit)

            # Bouton Contacts
            btn_contacts = ModernButton("Contacts", "success")
            btn_contacts.setFixedHeight(32)
            btn_contacts.clicked.connect(lambda checked, c=company: self.gerer_contacts(c))
            actions_layout.addWidget(btn_contacts)

            # Bouton Adresses
            btn_addresses = ModernButton("Adresses", "warning")
            btn_addresses.setFixedHeight(32)
            btn_addresses.clicked.connect(lambda checked, c=company: self.gerer_adresses(c))
            actions_layout.addWidget(btn_addresses)

            # Bouton Supprimer
            btn_delete = ModernButton("Supprimer", "danger")
            btn_delete.setFixedHeight(32)
            btn_delete.clicked.connect(lambda checked, c=company: self.supprimer_tiers(c))
            actions_layout.addWidget(btn_delete)

            self.table.setCellWidget(row, 6, actions_widget)

    def filtrer_tiers(self):
        """Filtre les tiers selon la recherche"""
        self.charger_tiers()

    def nouveau_tiers(self):
        """Ouvre le dialogue pour créer un nouveau tiers"""
        dialog = TiersDialog(self.axonaut_db, self.axonaut_client, parent=self)

        if dialog.exec():
            company = dialog.get_company()

            try:
                # Créer dans Axonaut
                created_company = self.axonaut_client.create_company(company)

                # Sauvegarder localement
                self.axonaut_db.save_company(created_company)

                QMessageBox.information(
                    self,
                    "Succès",
                    f"Le tiers '{created_company.name}' a été créé avec succès."
                )

                self.charger_tiers()

            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Erreur",
                    f"Impossible de créer le tiers:\n{str(e)}"
                )

    def modifier_tiers(self, company: Company):
        """Ouvre le dialogue pour modifier un tiers"""
        dialog = TiersDialog(self.axonaut_db, self.axonaut_client, company=company, parent=self)

        if dialog.exec():
            updated_company = dialog.get_company()

            try:
                if company.id:
                    # Mettre à jour dans Axonaut
                    result = self.axonaut_client.update_company(company.id, updated_company)
                    # Sauvegarder localement
                    self.axonaut_db.save_company(result)
                else:
                    # Créer dans Axonaut si pas encore d'ID
                    result = self.axonaut_client.create_company(updated_company)
                    self.axonaut_db.save_company(result)

                QMessageBox.information(
                    self,
                    "Succès",
                    f"Le tiers '{result.name}' a été modifié avec succès."
                )

                self.charger_tiers()

            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Erreur",
                    f"Impossible de modifier le tiers:\n{str(e)}"
                )

    def gerer_contacts(self, company: Company):
        """Ouvre le dialogue pour gérer les contacts d'un tiers"""
        dialog = ContactsDialog(self.axonaut_db, self.axonaut_client, company, parent=self)

        if dialog.exec():
            # Recharger les tiers pour mettre à jour le nombre de contacts
            self.charger_tiers()

    def gerer_adresses(self, company: Company):
        """Ouvre le dialogue pour gérer les adresses de chantier d'un tiers"""
        dialog = AddressesDialog(self.axonaut_db, self.axonaut_client, company, parent=self)

        if dialog.exec():
            # Recharger les tiers
            self.charger_tiers()

    def supprimer_tiers(self, company: Company):
        """Supprime un tiers"""
        reply = QMessageBox.question(
            self,
            "Confirmation",
            f"Êtes-vous sûr de vouloir supprimer le tiers '{company.name}' ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                if company.id:
                    # Supprimer dans Axonaut
                    self.axonaut_client.delete_company(company.id)
                    # Supprimer localement par ID Axonaut
                    self.axonaut_db.delete_company_by_axonaut_id(company.id)
                else:
                    # Pas d'ID Axonaut, suppression locale uniquement
                    # (ne devrait pas arriver normalement)
                    pass

                QMessageBox.information(
                    self,
                    "Succès",
                    f"Le tiers '{company.name}' a été supprimé."
                )

                self.charger_tiers()

            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Erreur",
                    f"Impossible de supprimer le tiers:\n{str(e)}"
                )

    def synchroniser_avec_axonaut(self):
        """Synchronise les données avec Axonaut"""
        try:
            # Récupérer toutes les entreprises depuis Axonaut
            companies = self.axonaut_client.get_companies()

            # Sauvegarder localement
            for company in companies:
                self.axonaut_db.save_company(company)

            QMessageBox.information(
                self,
                "Synchronisation réussie",
                f"{len(companies)} tiers ont été synchronisés depuis Axonaut."
            )

            self.charger_tiers()

        except Exception as e:
            QMessageBox.critical(
                self,
                "Erreur de synchronisation",
                f"Impossible de synchroniser avec Axonaut:\n{str(e)}"
            )


class TiersDialog(ResponsiveDialog):
    """Dialogue pour créer ou modifier un tiers"""

    def __init__(self, db: AxonautDatabase, client: AxonautClient,
                 company: Company = None, parent=None):
        title = "Modifier le Tiers" if company else "Nouveau Tiers"
        super().__init__(title, 800, parent)

        self.db = db
        self.client = client
        self.company = company or Company()

        self.init_form()
        if company:
            self.load_company_data()

    def init_form(self):
        """Initialise le formulaire"""
        layout = QVBoxLayout()
        layout.setSpacing(DesignSystem.SPACING_LG)

        # Section Informations générales
        section_general = ModernLabel("Informations générales", "title")
        section_general.setStyleSheet(f"color: {DesignSystem.TEXT_PRIMARY}; font-weight: 600; margin-top: {DesignSystem.SPACING_MD}px;")
        layout.addWidget(section_general)

        # Grid pour les champs alignés
        grid_general = QGridLayout()
        grid_general.setSpacing(DesignSystem.SPACING_MD)
        grid_general.setColumnStretch(1, 1)

        # Nom (obligatoire)
        grid_general.addWidget(ModernLabel("Nom *"), 0, 0)
        self.input_name = ModernInput()
        grid_general.addWidget(self.input_name, 0, 1)

        # Type de tiers
        grid_general.addWidget(ModernLabel("Type"), 1, 0)
        type_layout = QHBoxLayout()
        self.check_client = QCheckBox("Client")
        self.check_prospect = QCheckBox("Prospect")
        self.check_b2c = QCheckBox("B2C")
        self.check_client.setStyleSheet(self._get_checkbox_style())
        self.check_prospect.setStyleSheet(self._get_checkbox_style())
        self.check_b2c.setStyleSheet(self._get_checkbox_style())
        type_layout.addWidget(self.check_client)
        type_layout.addWidget(self.check_prospect)
        type_layout.addWidget(self.check_b2c)
        type_layout.addStretch()
        grid_general.addLayout(type_layout, 1, 1)

        layout.addLayout(grid_general)

        # Section Adresse
        section_adresse = ModernLabel("Adresse", "title")
        section_adresse.setStyleSheet(f"color: {DesignSystem.TEXT_PRIMARY}; font-weight: 600; margin-top: {DesignSystem.SPACING_LG}px;")
        layout.addWidget(section_adresse)

        grid_adresse = QGridLayout()
        grid_adresse.setSpacing(DesignSystem.SPACING_MD)
        grid_adresse.setColumnStretch(1, 2)

        # Contact
        grid_adresse.addWidget(ModernLabel("Contact"), 0, 0)
        self.input_contact_name = ModernInput()
        grid_adresse.addWidget(self.input_contact_name, 0, 1)

        # Rue
        grid_adresse.addWidget(ModernLabel("Rue"), 1, 0)
        self.input_street = ModernInput()
        grid_adresse.addWidget(self.input_street, 1, 1)

        # Code postal et Ville (sur la même ligne)
        grid_adresse.addWidget(ModernLabel("Code postal / Ville"), 2, 0)
        city_layout = QHBoxLayout()
        city_layout.setSpacing(DesignSystem.SPACING_MD)
        self.input_zip = ModernInput()
        self.input_zip.setMaximumWidth(120)
        self.input_city = ModernInput()
        city_layout.addWidget(self.input_zip)
        city_layout.addWidget(self.input_city)
        grid_adresse.addLayout(city_layout, 2, 1)

        # Pays
        grid_adresse.addWidget(ModernLabel("Pays"), 3, 0)
        self.input_country = ModernInput()
        self.input_country.setText("France")
        grid_adresse.addWidget(self.input_country, 3, 1)

        layout.addLayout(grid_adresse)

        # Section Informations financières
        section_finance = ModernLabel("Informations financières", "title")
        section_finance.setStyleSheet(f"color: {DesignSystem.TEXT_PRIMARY}; font-weight: 600; margin-top: {DesignSystem.SPACING_LG}px;")
        layout.addWidget(section_finance)

        grid_finance = QGridLayout()
        grid_finance.setSpacing(DesignSystem.SPACING_MD)
        grid_finance.setColumnStretch(1, 1)

        # SIRET
        grid_finance.addWidget(ModernLabel("SIRET"), 0, 0)
        self.input_siret = ModernInput()
        grid_finance.addWidget(self.input_siret, 0, 1)

        # N° TVA Intracommunautaire
        grid_finance.addWidget(ModernLabel("N° TVA Intra."), 1, 0)
        self.input_tva = ModernInput()
        grid_finance.addWidget(self.input_tva, 1, 1)

        # Code tiers
        grid_finance.addWidget(ModernLabel("Code tiers"), 2, 0)
        self.input_code_tiers = ModernInput()
        grid_finance.addWidget(self.input_code_tiers, 2, 1)

        # IBAN
        grid_finance.addWidget(ModernLabel("IBAN"), 3, 0)
        self.input_iban = ModernInput()
        grid_finance.addWidget(self.input_iban, 3, 1)

        # BIC
        grid_finance.addWidget(ModernLabel("BIC"), 4, 0)
        self.input_bic = ModernInput()
        grid_finance.addWidget(self.input_bic, 4, 1)

        layout.addLayout(grid_finance)

        # Commentaires
        section_comments = ModernLabel("Commentaires", "title")
        section_comments.setStyleSheet(f"color: {DesignSystem.TEXT_PRIMARY}; font-weight: 600; margin-top: {DesignSystem.SPACING_LG}px;")
        layout.addWidget(section_comments)

        self.input_comments = ModernTextEdit()
        self.input_comments.setMaximumHeight(100)
        layout.addWidget(self.input_comments)

        self.content_layout.addLayout(layout)

    def _get_checkbox_style(self) -> str:
        """Retourne le style pour les checkboxes"""
        return f"""
            QCheckBox {{
                font-family: {DesignSystem.FONT_FAMILY};
                font-size: {DesignSystem.FONT_SIZE_BODY}px;
                color: {DesignSystem.TEXT_PRIMARY};
                spacing: {DesignSystem.SPACING_SM}px;
            }}
            QCheckBox::indicator {{
                width: 18px;
                height: 18px;
                border-radius: 4px;
                background-color: {DesignSystem.SURFACE_ELEVATED};
            }}
            QCheckBox::indicator:hover {{
                background-color: #F0F0F2;
            }}
            QCheckBox::indicator:checked {{
                background-color: {DesignSystem.ACCENT_BLUE};
                border: 2px solid {DesignSystem.ACCENT_BLUE};
            }}
        """

    def load_company_data(self):
        """Charge les données de l'entreprise dans le formulaire"""
        self.input_name.setText(self.company.name or "")
        self.check_client.setChecked(self.company.is_customer)
        self.check_prospect.setChecked(self.company.is_prospect)
        self.check_b2c.setChecked(self.company.isB2C)

        self.input_contact_name.setText(self.company.address_contact_name or "")
        self.input_street.setText(self.company.address_street or "")
        self.input_zip.setText(self.company.address_zip_code or "")
        self.input_city.setText(self.company.address_city or "")
        self.input_country.setText(self.company.address_country or "France")

        self.input_siret.setText(self.company.siret or "")
        self.input_tva.setText(self.company.intracommunity_number or "")
        self.input_code_tiers.setText(self.company.thirdparty_code or "")
        self.input_iban.setText(self.company.iban or "")
        self.input_bic.setText(self.company.bic or "")

        self.input_comments.setText(self.company.comments or "")

    def get_company(self) -> Company:
        """Récupère les données du formulaire"""
        self.company.name = self.input_name.text()
        self.company.is_customer = self.check_client.isChecked()
        self.company.is_prospect = self.check_prospect.isChecked()
        self.company.isB2C = self.check_b2c.isChecked()

        self.company.address_contact_name = self.input_contact_name.text()
        self.company.address_street = self.input_street.text()
        self.company.address_zip_code = self.input_zip.text()
        self.company.address_city = self.input_city.text()
        self.company.address_country = self.input_country.text()

        self.company.siret = self.input_siret.text()
        self.company.intracommunity_number = self.input_tva.text()
        self.company.thirdparty_code = self.input_code_tiers.text()
        self.company.iban = self.input_iban.text()
        self.company.bic = self.input_bic.text()

        self.company.comments = self.input_comments.toPlainText()

        return self.company

    def validate(self) -> bool:
        """Valide le formulaire"""
        if not self.input_name.text().strip():
            QMessageBox.warning(self, "Validation", "Le nom est obligatoire.")
            return False

        return True


class ContactsDialog(ResponsiveDialog):
    """Dialogue pour gérer les contacts d'un tiers"""

    def __init__(self, db: AxonautDatabase, client: AxonautClient,
                 company: Company, parent=None):
        super().__init__(f"Contacts - {company.name}", 900, parent)

        self.db = db
        self.client = client
        self.company = company

        self.init_ui()
        self.charger_contacts()

    def init_ui(self):
        """Initialise l'interface"""
        layout = QVBoxLayout()
        layout.setSpacing(DesignSystem.SPACING_MD)

        # Barre d'outils
        toolbar = QHBoxLayout()
        toolbar.addStretch()

        btn_nouveau = ModernButton("+ Nouveau Contact", "primary")
        btn_nouveau.clicked.connect(self.nouveau_contact)
        toolbar.addWidget(btn_nouveau)

        layout.addLayout(toolbar)

        # Table des contacts
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "Nom", "Email", "Téléphone", "Mobile", "Fonction", "Actions"
        ])

        # Style
        self.table.setStyleSheet(f"""
            QTableWidget {{
                background-color: {DesignSystem.SURFACE};
                border: none;
                border-radius: {DesignSystem.RADIUS_MD}px;
                gridline-color: {DesignSystem.BORDER_COLOR};
            }}
            QTableWidget::item {{
                padding: {DesignSystem.SPACING_SM}px;
                border: none;
            }}
            QHeaderView::section {{
                background-color: {DesignSystem.SURFACE_ELEVATED};
                padding: {DesignSystem.SPACING_MD}px;
                border: none;
                border-bottom: 1px solid {DesignSystem.BORDER_COLOR};
                font-weight: 600;
            }}
        """)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.Fixed)
        header.resizeSection(5, 240)  # Largeur pour 2 boutons

        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setDefaultSectionSize(40)  # Hauteur des lignes

        layout.addWidget(self.table)

        self.content_layout.addLayout(layout)

        # Ajouter un bouton Fermer
        btn_close = ModernButton("Fermer", "secondary")
        btn_close.clicked.connect(self.accept)
        self.content_layout.addWidget(btn_close)

    def charger_contacts(self):
        """Charge les contacts du tiers"""
        # Récupérer les employés depuis la base locale ou l'objet company
        employees = self.company.employees

        self.table.setRowCount(len(employees))

        for row, employee in enumerate(employees):
            # Nom
            self.table.setItem(row, 0, QTableWidgetItem(employee.full_name))

            # Email
            self.table.setItem(row, 1, QTableWidgetItem(employee.email or "-"))

            # Téléphone
            self.table.setItem(row, 2, QTableWidgetItem(employee.phone_number or "-"))

            # Mobile
            self.table.setItem(row, 3, QTableWidgetItem(employee.cellphone_number or "-"))

            # Fonction
            job_text = employee.job or "-"
            if employee.is_billing_contact:
                job_text += " 📧"
            self.table.setItem(row, 4, QTableWidgetItem(job_text))

            # Actions
            actions_widget = QWidget()
            actions_layout = QHBoxLayout(actions_widget)
            actions_layout.setContentsMargins(6, 4, 6, 4)
            actions_layout.setSpacing(6)

            btn_edit = ModernButton("Modifier", "secondary")
            btn_edit.setFixedHeight(28)
            btn_edit.clicked.connect(lambda checked, e=employee: self.modifier_contact(e))
            actions_layout.addWidget(btn_edit)

            btn_delete = ModernButton("Supprimer", "danger")
            btn_delete.setFixedHeight(28)
            btn_delete.clicked.connect(lambda checked, e=employee: self.supprimer_contact(e))
            actions_layout.addWidget(btn_delete)

            self.table.setCellWidget(row, 5, actions_widget)

    def nouveau_contact(self):
        """Ouvre le dialogue pour créer un nouveau contact"""
        dialog = EmployeeDialog(employee=None, parent=self)

        if dialog.exec():
            employee = dialog.get_employee()

            try:
                if self.company.id:
                    # Créer dans Axonaut
                    created = self.client.create_employee(self.company.id, employee)
                    # Ajouter à la liste locale
                    self.company.employees.append(created)
                    # Sauvegarder dans la BDD locale
                    self.db.save_employee(created)
                else:
                    # Juste ajouter localement si pas encore dans Axonaut
                    self.company.employees.append(employee)

                QMessageBox.information(
                    self,
                    "Succès",
                    f"Le contact '{employee.full_name}' a été ajouté."
                )

                self.charger_contacts()

            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Erreur",
                    f"Impossible d'ajouter le contact:\n{str(e)}"
                )

    def modifier_contact(self, employee: Employee):
        """Modifie un contact"""
        dialog = EmployeeDialog(employee=employee, parent=self)

        if dialog.exec():
            updated = dialog.get_employee()

            try:
                if self.company.id and employee.id:
                    # Mettre à jour dans Axonaut
                    result = self.client.update_employee(employee.id, updated, company_id=self.company.id)
                    # Mettre à jour localement
                    self.db.save_employee(result)

                    # Mettre à jour dans la liste
                    for i, emp in enumerate(self.company.employees):
                        if emp.id == employee.id:
                            self.company.employees[i] = result
                            break

                QMessageBox.information(
                    self,
                    "Succès",
                    f"Le contact '{updated.full_name}' a été modifié."
                )

                self.charger_contacts()

            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Erreur",
                    f"Impossible de modifier le contact:\n{str(e)}"
                )

    def supprimer_contact(self, employee: Employee):
        """Supprime un contact"""
        reply = QMessageBox.question(
            self,
            "Confirmation",
            f"Êtes-vous sûr de vouloir supprimer le contact '{employee.full_name}' ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                if self.company.id and employee.id:
                    # Supprimer dans Axonaut
                    self.client.delete_employee(employee.id, company_id=self.company.id)

                # Supprimer de la liste
                self.company.employees = [e for e in self.company.employees if e.id != employee.id]

                QMessageBox.information(
                    self,
                    "Succès",
                    f"Le contact '{employee.full_name}' a été supprimé."
                )

                self.charger_contacts()

            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Erreur",
                    f"Impossible de supprimer le contact:\n{str(e)}"
                )


class EmployeeDialog(ResponsiveDialog):
    """Dialogue pour créer ou modifier un contact"""

    def __init__(self, employee: Employee = None, parent=None):
        title = "Modifier le Contact" if employee else "Nouveau Contact"
        super().__init__(title, 600, parent)

        self.employee = employee or Employee()
        self.init_form()

        if employee:
            self.load_employee_data()

    def init_form(self):
        """Initialise le formulaire"""
        layout = QVBoxLayout()
        layout.setSpacing(DesignSystem.SPACING_MD)

        grid = QGridLayout()
        grid.setSpacing(DesignSystem.SPACING_MD)
        grid.setColumnStretch(1, 1)

        # Prénom
        grid.addWidget(ModernLabel("Prénom *"), 0, 0)
        self.input_firstname = ModernInput()
        grid.addWidget(self.input_firstname, 0, 1)

        # Nom
        grid.addWidget(ModernLabel("Nom *"), 1, 0)
        self.input_lastname = ModernInput()
        grid.addWidget(self.input_lastname, 1, 1)

        # Email
        grid.addWidget(ModernLabel("Email"), 2, 0)
        self.input_email = ModernInput()
        grid.addWidget(self.input_email, 2, 1)

        # Téléphone
        grid.addWidget(ModernLabel("Téléphone"), 3, 0)
        self.input_phone = ModernInput()
        grid.addWidget(self.input_phone, 3, 1)

        # Mobile
        grid.addWidget(ModernLabel("Mobile"), 4, 0)
        self.input_mobile = ModernInput()
        grid.addWidget(self.input_mobile, 4, 1)

        # Fonction
        grid.addWidget(ModernLabel("Fonction"), 5, 0)
        self.input_job = ModernInput()
        grid.addWidget(self.input_job, 5, 1)

        # Contact de facturation
        grid.addWidget(ModernLabel("Contact facturation"), 6, 0)
        self.check_billing = QCheckBox("Ce contact reçoit les factures")
        self.check_billing.setStyleSheet(f"""
            QCheckBox {{
                font-family: {DesignSystem.FONT_FAMILY};
                font-size: {DesignSystem.FONT_SIZE_BODY}px;
                color: {DesignSystem.TEXT_PRIMARY};
            }}
            QCheckBox::indicator {{
                width: 18px;
                height: 18px;
                border-radius: 4px;
                background-color: {DesignSystem.SURFACE_ELEVATED};
            }}
            QCheckBox::indicator:checked {{
                background-color: {DesignSystem.ACCENT_BLUE};
            }}
        """)
        grid.addWidget(self.check_billing, 6, 1)

        layout.addLayout(grid)
        self.content_layout.addLayout(layout)

    def load_employee_data(self):
        """Charge les données du contact"""
        self.input_firstname.setText(self.employee.firstname or "")
        self.input_lastname.setText(self.employee.lastname or "")
        self.input_email.setText(self.employee.email or "")
        self.input_phone.setText(self.employee.phone_number or "")
        self.input_mobile.setText(self.employee.cellphone_number or "")
        self.input_job.setText(self.employee.job or "")
        self.check_billing.setChecked(self.employee.is_billing_contact)

    def get_employee(self) -> Employee:
        """Récupère les données du formulaire"""
        self.employee.firstname = self.input_firstname.text()
        self.employee.lastname = self.input_lastname.text()
        self.employee.email = self.input_email.text()
        self.employee.phone_number = self.input_phone.text()
        self.employee.cellphone_number = self.input_mobile.text()
        self.employee.job = self.input_job.text()
        self.employee.is_billing_contact = self.check_billing.isChecked()

        return self.employee

    def validate(self) -> bool:
        """Valide le formulaire"""
        if not self.input_firstname.text().strip() or not self.input_lastname.text().strip():
            QMessageBox.warning(self, "Validation", "Le prénom et le nom sont obligatoires.")
            return False

        return True


class AddressesDialog(ResponsiveDialog):
    """Dialogue pour gérer les adresses de chantier d'un tiers"""

    def __init__(self, db: AxonautDatabase, client: AxonautClient,
                 company: Company, parent=None):
        super().__init__(f"Adresses de chantier - {company.name}", 900, parent)

        self.db = db
        self.client = client
        self.company = company

        self.init_ui()
        self.charger_adresses()

    def init_ui(self):
        """Initialise l'interface"""
        layout = QVBoxLayout()
        layout.setSpacing(DesignSystem.SPACING_MD)

        # Barre d'outils
        toolbar = QHBoxLayout()
        toolbar.addStretch()

        btn_nouveau = ModernButton("+ Nouvelle Adresse", "primary")
        btn_nouveau.clicked.connect(self.nouvelle_adresse)
        toolbar.addWidget(btn_nouveau)

        layout.addLayout(toolbar)

        # Table des adresses
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "Nom", "Adresse", "Code Postal", "Ville", "Contact", "Actions"
        ])

        # Style
        self.table.setStyleSheet(f"""
            QTableWidget {{
                background-color: {DesignSystem.SURFACE};
                border: none;
                border-radius: {DesignSystem.RADIUS_MD}px;
                gridline-color: {DesignSystem.BORDER_COLOR};
            }}
            QTableWidget::item {{
                padding: {DesignSystem.SPACING_SM}px;
                border: none;
            }}
            QHeaderView::section {{
                background-color: {DesignSystem.SURFACE_ELEVATED};
                padding: {DesignSystem.SPACING_MD}px;
                border: none;
                border-bottom: 1px solid {DesignSystem.BORDER_COLOR};
                font-weight: 600;
            }}
        """)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.Fixed)
        header.resizeSection(5, 240)  # Largeur pour 2 boutons

        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setDefaultSectionSize(40)  # Hauteur des lignes

        layout.addWidget(self.table)

        self.content_layout.addLayout(layout)

        # Ajouter un bouton Fermer
        btn_close = ModernButton("Fermer", "secondary")
        btn_close.clicked.connect(self.accept)
        self.content_layout.addWidget(btn_close)

    def charger_adresses(self):
        """Charge les adresses du tiers"""
        try:
            if self.company.id:
                # Récupérer depuis l'API Axonaut
                addresses = self.client.get_company_addresses(self.company.id)
                # Sauvegarder localement
                for address in addresses:
                    self.db.save_address(address)
            else:
                # Récupérer depuis la base locale
                addresses = []

            self.table.setRowCount(len(addresses))

            for row, address in enumerate(addresses):
                # Nom
                self.table.setItem(row, 0, QTableWidgetItem(address.name or "-"))

                # Adresse
                self.table.setItem(row, 1, QTableWidgetItem(address.street or "-"))

                # Code Postal
                self.table.setItem(row, 2, QTableWidgetItem(address.zip_code or "-"))

                # Ville
                self.table.setItem(row, 3, QTableWidgetItem(address.city or "-"))

                # Contact
                self.table.setItem(row, 4, QTableWidgetItem(address.contact_name or "-"))

                # Actions
                actions_widget = QWidget()
                actions_layout = QHBoxLayout(actions_widget)
                actions_layout.setContentsMargins(6, 4, 6, 4)
                actions_layout.setSpacing(6)

                btn_edit = ModernButton("Modifier", "secondary")
                btn_edit.setFixedHeight(28)
                btn_edit.clicked.connect(lambda checked, a=address: self.modifier_adresse(a))
                actions_layout.addWidget(btn_edit)

                btn_delete = ModernButton("Supprimer", "danger")
                btn_delete.setFixedHeight(28)
                btn_delete.clicked.connect(lambda checked, a=address: self.supprimer_adresse(a))
                actions_layout.addWidget(btn_delete)

                self.table.setCellWidget(row, 5, actions_widget)

        except Exception as e:
            QMessageBox.warning(
                self,
                "Erreur",
                f"Impossible de charger les adresses:\n{str(e)}"
            )

    def nouvelle_adresse(self):
        """Ouvre le dialogue pour créer une nouvelle adresse"""
        dialog = AddressDialog(address=None, parent=self)

        if dialog.exec():
            address = dialog.get_address()
            address.company_id = self.company.id

            try:
                if self.company.id:
                    # Créer dans Axonaut
                    created = self.client.create_address(self.company.id, address)
                    # Sauvegarder dans la BDD locale
                    self.db.save_address(created)

                QMessageBox.information(
                    self,
                    "Succès",
                    f"L'adresse '{created.name}' a été ajoutée."
                )

                self.charger_adresses()

            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Erreur",
                    f"Impossible d'ajouter l'adresse:\n{str(e)}"
                )

    def modifier_adresse(self, address: Address):
        """Modifie une adresse"""
        dialog = AddressDialog(address=address, parent=self)

        if dialog.exec():
            updated = dialog.get_address()

            try:
                if address.id:
                    # Mettre à jour dans Axonaut
                    result = self.client.update_address(address.id, updated)
                    # Mettre à jour localement
                    self.db.save_address(result)

                QMessageBox.information(
                    self,
                    "Succès",
                    f"L'adresse '{updated.name}' a été modifiée."
                )

                self.charger_adresses()

            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Erreur",
                    f"Impossible de modifier l'adresse:\n{str(e)}"
                )

    def supprimer_adresse(self, address: Address):
        """Supprime une adresse"""
        reply = QMessageBox.question(
            self,
            "Confirmation",
            f"Êtes-vous sûr de vouloir supprimer l'adresse '{address.name}' ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                if address.id:
                    # Supprimer dans Axonaut
                    self.client.delete_address(address.id)

                QMessageBox.information(
                    self,
                    "Succès",
                    f"L'adresse '{address.name}' a été supprimée."
                )

                self.charger_adresses()

            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Erreur",
                    f"Impossible de supprimer l'adresse:\n{str(e)}"
                )


class AddressDialog(ResponsiveDialog):
    """Dialogue pour créer ou modifier une adresse de chantier"""

    def __init__(self, address: Address = None, parent=None):
        title = "Modifier l'Adresse" if address else "Nouvelle Adresse"
        super().__init__(title, 600, parent)

        self.address = address or Address()
        self.init_form()

        if address:
            self.load_address_data()

    def init_form(self):
        """Initialise le formulaire"""
        layout = QVBoxLayout()
        layout.setSpacing(DesignSystem.SPACING_MD)

        grid = QGridLayout()
        grid.setSpacing(DesignSystem.SPACING_MD)
        grid.setColumnStretch(1, 1)

        # Nom de l'adresse
        grid.addWidget(ModernLabel("Nom de l'adresse *"), 0, 0)
        self.input_name = ModernInput("Ex: Chantier Paris Nord")
        grid.addWidget(self.input_name, 0, 1)

        # Contact
        grid.addWidget(ModernLabel("Contact"), 1, 0)
        self.input_contact = ModernInput()
        grid.addWidget(self.input_contact, 1, 1)

        # Rue
        grid.addWidget(ModernLabel("Rue"), 2, 0)
        self.input_street = ModernInput()
        grid.addWidget(self.input_street, 2, 1)

        # Code postal et Ville (sur la même ligne)
        grid.addWidget(ModernLabel("Code postal / Ville"), 3, 0)
        city_layout = QHBoxLayout()
        city_layout.setSpacing(DesignSystem.SPACING_MD)
        self.input_zip = ModernInput()
        self.input_zip.setMaximumWidth(120)
        self.input_city = ModernInput()
        city_layout.addWidget(self.input_zip)
        city_layout.addWidget(self.input_city)
        grid.addLayout(city_layout, 3, 1)

        # Pays
        grid.addWidget(ModernLabel("Pays"), 4, 0)
        self.input_country = ModernInput()
        self.input_country.setText("France")
        grid.addWidget(self.input_country, 4, 1)

        # Téléphone
        grid.addWidget(ModernLabel("Téléphone"), 5, 0)
        self.input_phone = ModernInput()
        grid.addWidget(self.input_phone, 5, 1)

        # Email
        grid.addWidget(ModernLabel("Email"), 6, 0)
        self.input_email = ModernInput()
        grid.addWidget(self.input_email, 6, 1)

        # Commentaires
        grid.addWidget(ModernLabel("Commentaires"), 7, 0)
        self.input_comments = ModernTextEdit()
        self.input_comments.setMaximumHeight(80)
        grid.addWidget(self.input_comments, 7, 1)

        layout.addLayout(grid)
        self.content_layout.addLayout(layout)

    def load_address_data(self):
        """Charge les données de l'adresse"""
        self.input_name.setText(self.address.name or "")
        self.input_contact.setText(self.address.contact_name or "")
        self.input_street.setText(self.address.street or "")
        self.input_zip.setText(self.address.zip_code or "")
        self.input_city.setText(self.address.city or "")
        self.input_country.setText(self.address.country or "France")
        self.input_phone.setText(self.address.phone or "")
        self.input_email.setText(self.address.email or "")
        self.input_comments.setText(self.address.comments or "")

    def get_address(self) -> Address:
        """Récupère les données du formulaire"""
        self.address.name = self.input_name.text()
        self.address.contact_name = self.input_contact.text()
        self.address.street = self.input_street.text()
        self.address.zip_code = self.input_zip.text()
        self.address.city = self.input_city.text()
        self.address.country = self.input_country.text()
        self.address.phone = self.input_phone.text()
        self.address.email = self.input_email.text()
        self.address.comments = self.input_comments.toPlainText()

        return self.address

    def validate(self) -> bool:
        """Valide le formulaire"""
        if not self.input_name.text().strip():
            QMessageBox.warning(self, "Validation", "Le nom de l'adresse est obligatoire.")
            return False

        return True
