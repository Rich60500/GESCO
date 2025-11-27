"""
GESCO v5.0 - Module Achats
Gestion des achats avec intégration Sonepar API
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime
from typing import List, Optional

from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QTableWidget,
                               QTableWidgetItem, QHeaderView, QLineEdit, QPushButton,
                               QMessageBox, QLabel, QTabWidget, QSpinBox, QDoubleSpinBox,
                               QAbstractItemView, QTextEdit, QComboBox, QGroupBox, QGridLayout)
from PySide6.QtCore import Qt, Signal, QThread
from PySide6.QtGui import QColor

from design_system import (DesignSystem, ModernLabel, ModernInput, ModernComboBox,
                           ModernTextEdit, ModernButton, ModernCard, ResponsiveDialog)
from database import Database
from integrations.sonepar import (
    SoneParClient, SoneParConfig, SoneParDatabase,
    Product, ProductWithPricing, OrderType, OrderStatus
)


class RechercheProduitsWidget(QWidget):
    """Widget de recherche de produits dans le catalogue Sonepar"""

    produit_selectionne = Signal(Product)

    def __init__(self, client: SoneParClient, parent=None):
        super().__init__(parent)

        self.client = client
        self.produits_results = []

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
        title_label = ModernLabel("Recherche Catalogue Sonepar", "large")
        layout.addWidget(title_label)

        # Barre de recherche
        search_layout = QHBoxLayout()
        search_layout.setSpacing(DesignSystem.SPACING_SM)

        self.search_input = ModernInput("Référence, EAN ou description...")
        self.search_input.returnPressed.connect(self.rechercher_produits)
        search_layout.addWidget(self.search_input)

        btn_rechercher = ModernButton("Rechercher", "primary")
        btn_rechercher.clicked.connect(self.rechercher_produits)
        search_layout.addWidget(btn_rechercher)

        layout.addLayout(search_layout)

        # Info
        info_label = ModernLabel(
            "💡 Recherchez par référence, code EAN ou mots-clés dans la description",
            "secondary"
        )
        layout.addWidget(info_label)

        # Tableau des résultats
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels([
            "Référence", "Description", "Marque", "EAN", "Conditionnement", "Unité"
        ])

        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)

        # Ajuster les colonnes
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)

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

        self.table.doubleClicked.connect(self.on_produit_double_click)

        layout.addWidget(self.table)

        # Boutons
        actions_layout = QHBoxLayout()
        actions_layout.setSpacing(DesignSystem.SPACING_SM)

        btn_voir_prix = ModernButton("Voir Prix & Stock", "primary")
        btn_voir_prix.clicked.connect(self.voir_prix_stock)
        actions_layout.addWidget(btn_voir_prix)

        actions_layout.addStretch()

        self.label_results = ModernLabel("", "secondary")
        actions_layout.addWidget(self.label_results)

        layout.addLayout(actions_layout)

    def rechercher_produits(self):
        """Recherche des produits dans le catalogue"""
        query = self.search_input.text().strip()

        if not query:
            QMessageBox.warning(self, "Champ vide", "Veuillez saisir un terme de recherche.")
            return

        try:
            # Afficher un message de chargement
            self.label_results.setText("🔄 Recherche en cours...")
            self.table.setRowCount(0)

            # Rechercher (avec rate limiting automatique)
            self.produits_results = self.client.search_products(query, limit=100)

            # Afficher les résultats
            self.afficher_produits(self.produits_results)

            self.label_results.setText(f"✓ {len(self.produits_results)} produit(s) trouvé(s)")

        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Erreur lors de la recherche : {str(e)}")
            self.label_results.setText("✗ Erreur de recherche")

    def afficher_produits(self, produits: List[Product]):
        """Affiche les produits dans le tableau"""
        self.table.setRowCount(0)

        for produit in produits:
            row = self.table.rowCount()
            self.table.insertRow(row)

            # Référence
            item_ref = QTableWidgetItem(produit.reference)
            item_ref.setData(Qt.ItemDataRole.UserRole, produit)

            # Description
            item_desc = QTableWidgetItem(produit.description)

            # Marque
            item_brand = QTableWidgetItem(produit.brand.name)

            # EAN
            item_ean = QTableWidgetItem(produit.ean)

            # Conditionnement
            item_pack = QTableWidgetItem(str(produit.packaging))

            # Unité
            item_unit = QTableWidgetItem(produit.unit)

            self.table.setItem(row, 0, item_ref)
            self.table.setItem(row, 1, item_desc)
            self.table.setItem(row, 2, item_brand)
            self.table.setItem(row, 3, item_ean)
            self.table.setItem(row, 4, item_pack)
            self.table.setItem(row, 5, item_unit)

    def voir_prix_stock(self):
        """Affiche les prix et stock du produit sélectionné"""
        selected_items = self.table.selectedItems()

        if not selected_items:
            QMessageBox.warning(self, "Aucune sélection", "Veuillez sélectionner un produit.")
            return

        produit = self.table.item(selected_items[0].row(), 0).data(Qt.ItemDataRole.UserRole)

        try:
            # Récupérer prix et stock
            results = self.client.get_prices_and_stocks([produit.reference])

            if results:
                result = results[0]
                self.afficher_details_produit(result)
            else:
                QMessageBox.information(
                    self,
                    "Aucune donnée",
                    "Aucune information de prix ou stock disponible pour ce produit."
                )

        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Erreur lors de la récupération : {str(e)}")

    def afficher_details_produit(self, produit_pricing: ProductWithPricing):
        """Affiche les détails d'un produit avec prix et stock"""
        produit = produit_pricing.product
        price = produit_pricing.price
        stock = produit_pricing.stock

        details = f"""
<h3>{produit.description}</h3>
<p><b>Référence:</b> {produit.reference}<br>
<b>Marque:</b> {produit.brand.name}<br>
<b>EAN:</b> {produit.ean}</p>
"""

        if price:
            details += f"""
<h4>Prix</h4>
<p><b>Prix net:</b> {price.net_price:.2f} {price.currency}<br>
<b>Prix brut:</b> {price.gross_price:.2f} {price.currency}<br>
<b>Remise:</b> {price.discount_rate:.1f}%<br>
<b>Unité:</b> {price.unit}</p>
"""

        if stock:
            details += f"""
<h4>Stock</h4>
<p><b>Quantité disponible:</b> {stock.quantity}<br>
<b>Type:</b> {stock.stock_type.value}<br>
<b>Emplacement:</b> {stock.location or 'Non spécifié'}</p>
"""

        msg = QMessageBox(self)
        msg.setWindowTitle("Détails du produit")
        msg.setTextFormat(Qt.TextFormat.RichText)
        msg.setText(details)
        msg.setIcon(QMessageBox.Icon.Information)
        msg.exec()

    def on_produit_double_click(self):
        """Émet le signal de sélection de produit"""
        selected_items = self.table.selectedItems()

        if selected_items:
            produit = self.table.item(selected_items[0].row(), 0).data(Qt.ItemDataRole.UserRole)
            self.produit_selectionne.emit(produit)


class CreerCommandeDialog(ResponsiveDialog):
    """Dialogue pour créer une commande Sonepar"""

    def __init__(self, client: SoneParClient, db: Database, parent=None):
        super().__init__("Nouvelle Commande Sonepar", 800, parent)

        self.client = client
        self.db = db
        self.lignes_commande = []

        # Section Chantier
        section_chantier = self.add_section("Chantier")

        self.combo_chantier = ModernComboBox()
        self.charger_chantiers()
        self.add_form_field(section_chantier, "Chantier *", self.combo_chantier)

        # Section Type de commande
        section_type = self.add_section("Type de commande")

        self.combo_type = ModernComboBox()
        self.combo_type.addItems(["STANDARD", "EXPRESS", "DEPOT"])
        self.add_form_field(section_type, "Type *", self.combo_type)

        # Section Adresse de livraison
        section_adresse = self.add_section("Livraison")

        self.input_adresse = ModernTextEdit()
        self.input_adresse.setMaximumHeight(80)
        self.input_adresse.setPlaceholderText("Adresse de livraison (optionnelle, sinon adresse du chantier)")
        section_adresse.addWidget(self.input_adresse)

        # Section Lignes de commande
        section_lignes = self.add_section("Lignes de commande")

        # Ajout de ligne
        add_line_layout = QHBoxLayout()
        add_line_layout.setSpacing(DesignSystem.SPACING_SM)

        self.input_reference = ModernInput("Référence produit")
        add_line_layout.addWidget(self.input_reference, 2)

        self.input_quantite = QSpinBox()
        self.input_quantite.setMinimum(1)
        self.input_quantite.setMaximum(9999)
        self.input_quantite.setValue(1)
        self.input_quantite.setStyleSheet(f"""
            QSpinBox {{
                background-color: {DesignSystem.SURFACE};
                border: 1px solid {DesignSystem.BORDER_COLOR};
                border-radius: {DesignSystem.RADIUS_SM}px;
                padding: 0 {DesignSystem.SPACING_MD}px;
                min-height: {DesignSystem.INPUT_HEIGHT}px;
            }}
        """)
        add_line_layout.addWidget(self.input_quantite, 1)

        btn_ajouter_ligne = ModernButton("+ Ajouter", "primary")
        btn_ajouter_ligne.clicked.connect(self.ajouter_ligne)
        add_line_layout.addWidget(btn_ajouter_ligne)

        section_lignes.addLayout(add_line_layout)

        # Liste des lignes
        self.table_lignes = QTableWidget()
        self.table_lignes.setColumnCount(3)
        self.table_lignes.setHorizontalHeaderLabels(["Référence", "Quantité", ""])
        self.table_lignes.horizontalHeader().setStretchLastSection(False)
        self.table_lignes.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.table_lignes.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        self.table_lignes.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        self.table_lignes.setMaximumHeight(200)
        self.table_lignes.verticalHeader().setVisible(False)
        section_lignes.addWidget(self.table_lignes)

        # Section Notes
        section_notes = self.add_section("Notes")

        self.input_notes = ModernTextEdit()
        self.input_notes.setMaximumHeight(80)
        self.input_notes.setPlaceholderText("Notes sur la commande (optionnel)")
        section_notes.addWidget(self.input_notes)

        # Boutons
        btn_annuler = ModernButton("Annuler", "secondary")
        btn_annuler.clicked.connect(self.reject)

        btn_creer = ModernButton("Créer la commande", "success")
        btn_creer.clicked.connect(self.valider)

        self.add_button_bar([btn_annuler, btn_creer])

    def charger_chantiers(self):
        """Charge la liste des chantiers actifs"""
        # Récupérer les chantiers non clôturés
        chantiers = [c for c in self.db.get_chantiers() if c['etat'] != 'Clôturé']

        for chantier in chantiers:
            self.combo_chantier.addItem(
                f"{chantier['nom']} - {chantier['client']}",
                chantier['id']
            )

    def ajouter_ligne(self):
        """Ajoute une ligne de commande"""
        reference = self.input_reference.text().strip()
        quantite = self.input_quantite.value()

        if not reference:
            QMessageBox.warning(self, "Champ manquant", "Veuillez saisir une référence produit.")
            return

        # Ajouter à la liste
        self.lignes_commande.append({
            'reference': reference,
            'quantity': quantite
        })

        # Ajouter au tableau
        row = self.table_lignes.rowCount()
        self.table_lignes.insertRow(row)

        self.table_lignes.setItem(row, 0, QTableWidgetItem(reference))
        self.table_lignes.setItem(row, 1, QTableWidgetItem(str(quantite)))

        btn_supprimer = ModernButton("✕", "danger")
        btn_supprimer.setFixedWidth(40)
        btn_supprimer.clicked.connect(lambda: self.supprimer_ligne(row))
        self.table_lignes.setCellWidget(row, 2, btn_supprimer)

        # Réinitialiser les champs
        self.input_reference.clear()
        self.input_quantite.setValue(1)
        self.input_reference.setFocus()

    def supprimer_ligne(self, row: int):
        """Supprime une ligne de commande"""
        self.table_lignes.removeRow(row)
        if row < len(self.lignes_commande):
            self.lignes_commande.pop(row)

    def valider(self):
        """Valide et crée la commande"""
        if self.combo_chantier.count() == 0:
            QMessageBox.warning(self, "Aucun chantier", "Aucun chantier disponible. Créez un chantier d'abord.")
            return

        if not self.lignes_commande:
            QMessageBox.warning(self, "Commande vide", "Ajoutez au moins une ligne de commande.")
            return

        self.accept()

    def get_data(self):
        """Retourne les données de la commande"""
        return {
            'chantier_id': self.combo_chantier.currentData(),
            'order_type': OrderType[self.combo_type.currentText()],
            'delivery_address': self.input_adresse.toPlainText().strip() or None,
            'lines': self.lignes_commande,
            'notes': self.input_notes.toPlainText().strip() or None
        }


class ModuleAchats(QWidget):
    """Module de gestion des achats avec intégration Sonepar"""

    def __init__(self, db: Database, parent=None):
        super().__init__(parent)

        self.db = db

        # Initialiser le client Sonepar
        self.sonepar_config = SoneParConfig()
        self.sonepar_client = SoneParClient(self.sonepar_config)
        self.sonepar_db = SoneParDatabase()

        # Layout principal
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(
            DesignSystem.SPACING_XL,
            DesignSystem.SPACING_XL,
            DesignSystem.SPACING_XL,
            DesignSystem.SPACING_XL
        )
        main_layout.setSpacing(DesignSystem.SPACING_LG)

        # En-tête
        header_layout = QHBoxLayout()

        title_label = ModernLabel("Achats & Sonepar", "large")
        header_layout.addWidget(title_label)

        header_layout.addStretch()

        # Indicateur environnement
        env_text = "🔴 PROD" if self.sonepar_config.use_production else "🟢 TEST"
        env_label = ModernLabel(env_text, "secondary")
        header_layout.addWidget(env_label)

        btn_nouvelle_commande = ModernButton("+ Nouvelle commande", "primary")
        btn_nouvelle_commande.clicked.connect(self.creer_commande)
        header_layout.addWidget(btn_nouvelle_commande)

        main_layout.addLayout(header_layout)

        # Onglets
        self.tabs = QTabWidget()
        self.tabs.setStyleSheet(f"""
            QTabWidget::pane {{
                border: 1px solid {DesignSystem.BORDER_COLOR};
                border-radius: {DesignSystem.RADIUS_MD}px;
                background-color: {DesignSystem.SURFACE};
            }}
            QTabBar::tab {{
                background-color: {DesignSystem.SURFACE_ELEVATED};
                border: 1px solid {DesignSystem.BORDER_COLOR};
                border-bottom: none;
                border-top-left-radius: {DesignSystem.RADIUS_SM}px;
                border-top-right-radius: {DesignSystem.RADIUS_SM}px;
                padding: {DesignSystem.SPACING_MD}px {DesignSystem.SPACING_LG}px;
                margin-right: 2px;
            }}
            QTabBar::tab:selected {{
                background-color: {DesignSystem.SURFACE};
                border-bottom: none;
            }}
            QTabBar::tab:hover {{
                background-color: {DesignSystem.SURFACE};
            }}
        """)

        # Onglet 1: Recherche catalogue
        self.recherche_widget = RechercheProduitsWidget(self.sonepar_client)
        self.tabs.addTab(self.recherche_widget, "🔍 Catalogue")

        # Onglet 2: Commandes
        self.commandes_widget = self.creer_onglet_commandes()
        self.tabs.addTab(self.commandes_widget, "📦 Commandes")

        # Onglet 3: Livraisons
        self.livraisons_widget = self.creer_onglet_livraisons()
        self.tabs.addTab(self.livraisons_widget, "🚚 Livraisons")

        main_layout.addWidget(self.tabs)

    def creer_onglet_commandes(self) -> QWidget:
        """Crée l'onglet des commandes"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(
            DesignSystem.SPACING_LG,
            DesignSystem.SPACING_LG,
            DesignSystem.SPACING_LG,
            DesignSystem.SPACING_LG
        )

        # Filtre par chantier
        filter_layout = QHBoxLayout()
        filter_layout.addWidget(ModernLabel("Filtrer par chantier:"))

        self.filter_chantier = ModernComboBox()
        self.filter_chantier.addItem("Tous les chantiers", None)

        chantiers = self.db.get_chantiers()
        for chantier in chantiers:
            self.filter_chantier.addItem(chantier['nom'], chantier['id'])

        self.filter_chantier.currentIndexChanged.connect(self.filtrer_commandes)
        filter_layout.addWidget(self.filter_chantier, 1)

        filter_layout.addStretch()

        layout.addLayout(filter_layout)

        # Tableau des commandes
        self.table_commandes = QTableWidget()
        self.table_commandes.setColumnCount(6)
        self.table_commandes.setHorizontalHeaderLabels([
            "N° Commande", "Date", "Chantier", "Montant", "Statut", "Notes"
        ])

        header = self.table_commandes.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.Stretch)

        self.table_commandes.verticalHeader().setVisible(False)
        self.table_commandes.setAlternatingRowColors(True)
        self.table_commandes.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        layout.addWidget(self.table_commandes)

        self.charger_commandes()

        return widget

    def creer_onglet_livraisons(self) -> QWidget:
        """Crée l'onglet des livraisons"""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(
            DesignSystem.SPACING_LG,
            DesignSystem.SPACING_LG,
            DesignSystem.SPACING_LG,
            DesignSystem.SPACING_LG
        )

        info_label = ModernLabel("📦 Bons de livraison à venir...", "title")
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(info_label)

        layout.addStretch()

        return widget

    def creer_commande(self):
        """Ouvre le dialogue de création de commande"""
        dialog = CreerCommandeDialog(self.sonepar_client, self.db, self)

        if dialog.exec():
            data = dialog.get_data()

            try:
                # Créer la commande via l'API Sonepar
                order = self.sonepar_client.create_order(
                    order_lines=data['lines'],
                    order_type=data['order_type'],
                    customer_reference=f"GESCO-{data['chantier_id']}",
                    delivery_address=data.get('delivery_address'),
                    notes=data.get('notes')
                )

                # Enregistrer dans la base locale
                order_lines_data = [
                    {
                        'product_id': line.product_id,
                        'product_reference': line.product_reference,
                        'product_description': line.product_description,
                        'quantity': line.quantity,
                        'unit_price': line.unit_price,
                        'total_price': line.total_price,
                        'line_number': line.line_number
                    }
                    for line in order.lines
                ]

                self.sonepar_db.link_order_to_chantier(
                    chantier_id=data['chantier_id'],
                    order_number=order.order_number,
                    order_date=order.order_date,
                    total_amount=order.total_amount,
                    status=order.status,
                    order_lines=order_lines_data,
                    notes=order.notes
                )

                QMessageBox.information(
                    self,
                    "Commande créée",
                    f"La commande {order.order_number} a été créée avec succès !\n"
                    f"Montant total : {order.total_amount:.2f} €"
                )

                self.charger_commandes()

            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Erreur",
                    f"Erreur lors de la création de la commande : {str(e)}"
                )

    def charger_commandes(self, chantier_id: Optional[int] = None):
        """Charge toutes les commandes ou celles d'un chantier spécifique"""
        self.table_commandes.setRowCount(0)

        # Récupérer toutes les commandes de tous les chantiers
        if chantier_id:
            orders = self.sonepar_db.get_chantier_orders(chantier_id)
        else:
            # Récupérer pour tous les chantiers
            chantiers = self.db.get_chantiers()
            orders = []
            for chantier in chantiers:
                orders.extend(self.sonepar_db.get_chantier_orders(chantier['id']))

        # Afficher dans le tableau
        for order in orders:
            row = self.table_commandes.rowCount()
            self.table_commandes.insertRow(row)

            self.table_commandes.setItem(row, 0, QTableWidgetItem(order.order_number))
            self.table_commandes.setItem(
                row, 1,
                QTableWidgetItem(order.order_date.strftime("%Y-%m-%d"))
            )
            self.table_commandes.setItem(row, 2, QTableWidgetItem(order.chantier_name))
            self.table_commandes.setItem(
                row, 3,
                QTableWidgetItem(f"{order.total_amount:.2f} €")
            )

            # Statut avec couleur
            status_item = QTableWidgetItem(order.status.value)
            if order.status == OrderStatus.DELIVERED:
                status_item.setForeground(QColor(DesignSystem.SUCCESS_GREEN))
            elif order.status == OrderStatus.CANCELLED:
                status_item.setForeground(QColor(DesignSystem.ERROR_RED))
            elif order.status in [OrderStatus.IN_PREPARATION, OrderStatus.READY]:
                status_item.setForeground(QColor(DesignSystem.WARNING_ORANGE))

            self.table_commandes.setItem(row, 4, status_item)
            self.table_commandes.setItem(row, 5, QTableWidgetItem(order.notes or ""))

    def filtrer_commandes(self):
        """Filtre les commandes par chantier"""
        chantier_id = self.filter_chantier.currentData()
        self.charger_commandes(chantier_id)

    def closeEvent(self, event):
        """Ferme proprement le client Sonepar"""
        self.sonepar_client.close()
        event.accept()
