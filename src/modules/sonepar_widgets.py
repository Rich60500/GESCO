"""
GESCO v5.0 - Widgets Sonepar réutilisables
Widgets pour l'intégration Sonepar : recherche, commandes, etc.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime
from typing import List, Optional

from PySide6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
                               QTableWidget, QTableWidgetItem, QHeaderView,
                               QMessageBox, QSpinBox, QAbstractItemView)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QColor

from design_system import (DesignSystem, ModernLabel, ModernInput, ModernComboBox,
                           ModernTextEdit, ModernButton, ResponsiveDialog)
from database import Database
from integrations.sonepar import (
    SoneParClient, SoneParConfig, SoneParDatabase,
    Product, ProductWithPricing, OrderType, OrderStatus
)


class RechercheSoneParWidget(QWidget):
    """Widget de recherche dans le catalogue Sonepar"""

    produit_selectionne = Signal(Product)  # Signal quand un produit est sélectionné

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

        btn_sync = ModernButton("⬇️ Sync Catalogue", "secondary")
        btn_sync.clicked.connect(self.synchroniser_catalogue)
        search_layout.addWidget(btn_sync)

        layout.addLayout(search_layout)

        # Info catalogue
        self.label_catalog_info = ModernLabel("", "secondary")
        layout.addWidget(self.label_catalog_info)
        self.update_catalog_info()

        # Info
        info_label = ModernLabel(
            "💡 Recherchez par référence, code EAN ou mots-clés dans la description",
            "secondary"
        )
        layout.addWidget(info_label)

        # Tableau des résultats
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "Référence", "Description", "Marque", "EAN", "Cond.", "Unité", "Prix", "Stock"
        ])

        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)

        # Ajuster les colonnes
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)  # Référence
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)  # Description
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)  # Marque
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)  # EAN
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)  # Cond.
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)  # Unité
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.ResizeToContents)  # Prix
        header.setSectionResizeMode(7, QHeaderView.ResizeMode.ResizeToContents)  # Stock

        self.table.setStyleSheet(f"""
            QTableWidget {{
                background-color: {DesignSystem.SURFACE};
                border: none;
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

        self.table.doubleClicked.connect(self.on_double_click)

        layout.addWidget(self.table)

        # Barre de statut
        status_layout = QHBoxLayout()
        status_layout.setSpacing(DesignSystem.SPACING_SM)

        self.label_results = ModernLabel("", "secondary")
        status_layout.addWidget(self.label_results)

        status_layout.addStretch()

        # Info prix/stock (vérifier si configuré)
        auth_configured = bool(self.client.config.user_id and self.client.config.user_password)
        if auth_configured:
            self.label_prix_stock = ModernLabel("✅ Prix/Stock : Actif", "secondary")
            self.label_prix_stock.setToolTip("Authentification configurée - Les prix et stocks s'affichent automatiquement")
        else:
            self.label_prix_stock = ModernLabel("ℹ️ Prix/Stock : Configuration requise", "secondary")
            self.label_prix_stock.setToolTip(
                "Pour afficher les prix et stocks, configurez les identifiants\n"
                "utilisateur Sonepar dans sonepar_config.py:\n"
                "- user_id\n"
                "- user_password"
            )
        status_layout.addWidget(self.label_prix_stock)

        layout.addLayout(status_layout)

    def update_catalog_info(self):
        """Met à jour l'info du catalogue"""
        try:
            info = self.client.get_catalog_info()
            product_count = info['product_count']
            last_sync = info['last_sync']

            if last_sync:
                last_sync_str = last_sync.strftime("%d/%m/%Y %H:%M")
                self.label_catalog_info.setText(
                    f"📚 Catalogue local: {product_count} produits | Dernière sync: {last_sync_str}"
                )
            else:
                self.label_catalog_info.setText(
                    f"📚 Catalogue local: {product_count} produits | Aucune synchronisation"
                )
        except:
            self.label_catalog_info.setText("📚 Catalogue local: Non disponible")

    def synchroniser_catalogue(self):
        """Synchronise le catalogue Sonepar"""
        from PySide6.QtWidgets import QProgressDialog
        from PySide6.QtCore import QTimer

        # Demander confirmation
        reply = QMessageBox.question(
            self,
            "Synchronisation du catalogue",
            "Cette opération peut prendre plusieurs minutes.\n\n"
            "Voulez-vous synchroniser le catalogue complet ?\n"
            "(Recommandé: 10 pages = ~10 000 produits)",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply != QMessageBox.StandardButton.Yes:
            return

        # Dialogue de progression
        progress = QProgressDialog(
            "Synchronisation du catalogue Sonepar en cours...",
            "Annuler",
            0,
            10,
            self
        )
        progress.setWindowTitle("Synchronisation")
        progress.setWindowModality(Qt.WindowModality.WindowModal)
        progress.show()

        # Callback de progression
        def update_progress(page, max_pages, total_products):
            progress.setValue(page)
            progress.setLabelText(
                f"Téléchargement page {page}/{max_pages}...\n"
                f"{total_products} produits synchronisés"
            )

        try:
            # Lancer la synchronisation
            result = self.client.sync_catalog(
                max_pages=10,
                progress_callback=update_progress
            )

            progress.close()

            # Mettre à jour l'affichage
            self.update_catalog_info()

            # Message de succès
            QMessageBox.information(
                self,
                "Synchronisation terminée",
                f"✓ Catalogue synchronisé avec succès !\n\n"
                f"Produits téléchargés: {result['total_products']}\n"
                f"Pages: {result['pages_downloaded']}\n"
                f"Durée: {result['duration']:.1f}s\n\n"
                f"Vous pouvez maintenant rechercher rapidement dans le catalogue local."
            )

        except Exception as e:
            progress.close()
            QMessageBox.critical(
                self,
                "Erreur de synchronisation",
                f"Impossible de synchroniser le catalogue:\n\n{str(e)}\n\n"
                f"Vérifiez votre connexion et vos identifiants API."
            )

    def rechercher_produits(self):
        """Recherche des produits dans le catalogue"""
        query = self.search_input.text().strip()

        if not query:
            QMessageBox.warning(self, "Champ vide", "Veuillez saisir un terme de recherche.")
            return

        try:
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

        # Vérifier si l'authentification est configurée pour charger prix/stocks
        auth_configured = bool(self.client.config.user_id and self.client.config.user_password)
        prix_stocks_data = {}

        # Charger les prix et stocks si authentification disponible
        if auth_configured and produits:
            try:
                # Limiter à 20 produits max pour éviter les délais (API limite à 100)
                product_ids = [p.id for p in produits[:20] if p.id]

                if product_ids:
                    self.label_prix_stock.setText("🔄 Chargement prix/stocks...")
                    pricing_results = self.client.get_prices_and_stocks(product_ids)

                    # Créer un dictionnaire pour accès rapide
                    for pricing in pricing_results:
                        prix_stocks_data[pricing.product.id] = pricing

                    self.label_prix_stock.setText("✅ Prix/Stock : Actif")
            except Exception as e:
                # En cas d'erreur, continuer sans prix/stocks
                self.label_prix_stock.setText(f"⚠️ Erreur prix/stock : {str(e)[:30]}...")

        # Afficher les produits
        for produit in produits:
            row = self.table.rowCount()
            self.table.insertRow(row)

            item_ref = QTableWidgetItem(produit.reference)
            item_ref.setData(Qt.ItemDataRole.UserRole, produit)

            item_desc = QTableWidgetItem(produit.description[:60] + "..." if len(produit.description) > 60 else produit.description)
            item_brand = QTableWidgetItem(produit.brand.name)
            item_ean = QTableWidgetItem(produit.ean)
            item_pack = QTableWidgetItem(str(produit.packaging))
            item_unit = QTableWidgetItem(produit.unit)

            # Prix et Stock
            pricing = prix_stocks_data.get(produit.id)
            if pricing and pricing.price:
                item_prix = QTableWidgetItem(f"{pricing.price.net_price:.2f} €")
                item_prix.setToolTip(f"Brut: {pricing.price.gross_price:.2f} € | Unité: {pricing.price.unit}")
            else:
                item_prix = QTableWidgetItem("-")
                item_prix.setToolTip("Non disponible" if auth_configured else "Configuration requise")

            if pricing and pricing.stock:
                item_stock = QTableWidgetItem(f"{pricing.stock.quantity}")
                item_stock.setToolTip(f"Disponible : {pricing.stock.location}")
                # Colorer en vert si dispo, rouge si rupture
                if pricing.stock.quantity > 0:
                    item_stock.setForeground(QColor(DesignSystem.SUCCESS_GREEN))
                else:
                    item_stock.setForeground(QColor(DesignSystem.ERROR_RED))
            else:
                item_stock = QTableWidgetItem("-")
                item_stock.setToolTip("Non disponible" if auth_configured else "Configuration requise")

            self.table.setItem(row, 0, item_ref)
            self.table.setItem(row, 1, item_desc)
            self.table.setItem(row, 2, item_brand)
            self.table.setItem(row, 3, item_ean)
            self.table.setItem(row, 4, item_pack)
            self.table.setItem(row, 5, item_unit)
            self.table.setItem(row, 6, item_prix)
            self.table.setItem(row, 7, item_stock)

    def on_double_click(self):
        """Double-clic : émet le signal de sélection"""
        selected_items = self.table.selectedItems()
        if selected_items:
            produit = self.table.item(selected_items[0].row(), 0).data(Qt.ItemDataRole.UserRole)
            self.produit_selectionne.emit(produit)


class CreerCommandeSoneParDialog(ResponsiveDialog):
    """Dialogue pour créer une commande Sonepar"""

    def __init__(self, db: Database, client: SoneParClient, parent=None):
        super().__init__("Nouvelle Commande Sonepar", 800, parent)

        self.db = db
        self.client = client
        self.lignes_commande = []

        # Section Chantier
        section_chantier = self.add_section("Chantier")

        self.combo_chantier = ModernComboBox()
        chantiers = [c for c in self.db.get_chantiers() if c['etat'] != 'Clôturé']
        for chantier in chantiers:
            self.combo_chantier.addItem(f"{chantier['nom']} - {chantier['client']}", chantier['id'])
        self.add_form_field(section_chantier, "Chantier *", self.combo_chantier)

        # Section Type de commande
        section_type = self.add_section("Type de commande")

        type_grid = QGridLayout()
        type_grid.setSpacing(DesignSystem.SPACING_MD)
        type_grid.setColumnStretch(0, 1)
        type_grid.setColumnStretch(1, 2)

        type_grid.addWidget(ModernLabel("Type *"), 0, 0)
        self.combo_type = ModernComboBox()
        self.combo_type.addItems(["STANDARD", "EXPRESS", "DEPOT"])
        type_grid.addWidget(self.combo_type, 1, 0)

        section_type.addLayout(type_grid)

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

        self.input_reference = ModernInput("Référence produit Sonepar")
        add_line_layout.addWidget(self.input_reference, 2)

        self.input_quantite = QSpinBox()
        self.input_quantite.setMinimum(1)
        self.input_quantite.setMaximum(9999)
        self.input_quantite.setValue(1)
        self.input_quantite.setPrefix("Qté: ")
        self.input_quantite.setStyleSheet(f"""
            QSpinBox {{
                background-color: {DesignSystem.SURFACE_ELEVATED};
                border: none;
                border-radius: {DesignSystem.RADIUS_SM}px;
                padding: 0 {DesignSystem.SPACING_MD}px;
                min-height: {DesignSystem.INPUT_HEIGHT}px;
            }}
            QSpinBox:hover {{
                background-color: #F0F0F2;
            }}
            QSpinBox:focus {{
                background-color: {DesignSystem.SURFACE};
                border: 2px solid {DesignSystem.ACCENT_BLUE};
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
        self.table_lignes.setStyleSheet(f"""
            QTableWidget {{
                background-color: {DesignSystem.SURFACE};
                border: none;
                border-radius: {DesignSystem.RADIUS_MD}px;
                gridline-color: {DesignSystem.BORDER_COLOR};
            }}
            QTableWidget::item {{
                padding: {DesignSystem.SPACING_SM}px;
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


class CommandesChantierWidget(QWidget):
    """Widget réutilisable pour afficher les commandes Sonepar d'un chantier"""

    def __init__(self, db: Database, sonepar_db: SoneParDatabase, chantier_id: Optional[int] = None, parent=None):
        super().__init__(parent)
        self.db = db
        self.sonepar_db = sonepar_db
        self.chantier_id = chantier_id

        # Layout principal
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(DesignSystem.SPACING_MD)

        # En-tête
        header_layout = QHBoxLayout()

        self.title_label = ModernLabel("Commandes Sonepar", "title")
        header_layout.addWidget(self.title_label)

        header_layout.addStretch()

        btn_refresh = ModernButton("🔄", "secondary")
        btn_refresh.setFixedWidth(40)
        btn_refresh.clicked.connect(self.charger_commandes)
        header_layout.addWidget(btn_refresh)

        layout.addLayout(header_layout)

        # Tableau des commandes
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels([
            "N° Commande", "Date", "Montant", "Statut", "Notes"
        ])

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)

        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setMaximumHeight(200)
        self.table.setStyleSheet(f"""
            QTableWidget {{
                background-color: {DesignSystem.SURFACE};
                border: none;
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
                padding: {DesignSystem.SPACING_SM}px;
                border: none;
                border-bottom: 1px solid {DesignSystem.BORDER_COLOR};
                font-weight: 600;
                font-size: {DesignSystem.FONT_SIZE_SMALL}px;
            }}
        """)

        layout.addWidget(self.table)

        # Total
        self.label_total = ModernLabel("Total : 0.00 €", "secondary")
        layout.addWidget(self.label_total)

        # Charger les commandes si un chantier est spécifié
        if self.chantier_id:
            self.charger_commandes()

    def set_chantier(self, chantier_id: int):
        """Change le chantier affiché"""
        self.chantier_id = chantier_id
        self.charger_commandes()

    def charger_commandes(self):
        """Charge les commandes du chantier"""
        if not self.chantier_id:
            self.table.setRowCount(0)
            self.label_total.setText("Aucun chantier sélectionné")
            return

        orders = self.sonepar_db.get_chantier_orders(self.chantier_id)

        self.table.setRowCount(0)
        total = 0.0

        for order in orders:
            row = self.table.rowCount()
            self.table.insertRow(row)

            self.table.setItem(row, 0, QTableWidgetItem(order.order_number))
            self.table.setItem(
                row, 1,
                QTableWidgetItem(order.order_date.strftime("%Y-%m-%d"))
            )
            self.table.setItem(
                row, 2,
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

            self.table.setItem(row, 3, status_item)
            self.table.setItem(row, 4, QTableWidgetItem(order.notes or ""))

            total += order.total_amount

        self.label_total.setText(f"Total : {total:.2f} €")
