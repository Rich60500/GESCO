"""
GESCO v5.0 - Module Factures
Gestion et visualisation des factures Axonaut
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem,
    QHeaderView, QMessageBox, QLabel, QPushButton, QComboBox,
    QProgressDialog, QAbstractItemView
)
from PySide6.QtCore import Qt, QSize, Signal
from PySide6.QtGui import QIcon, QColor, QFont
from datetime import datetime, timedelta
from typing import List, Optional

from ..design_system import DesignSystem, ModernLabel, ModernCard, ModernButton, ModernInput
from ..integrations.axonaut import AxonautClient, AxonautDatabase, AxonautConfig, Invoice


class FacturesWidget(QWidget):
    """Widget principal pour la gestion des factures"""

    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialisation des clients
        self.config = AxonautConfig()
        self.client = AxonautClient(self.config)
        self.db = AxonautDatabase()

        # État
        self.factures: List[Invoice] = []
        self.current_filter = "all"  # all, last_month, current_month, unpaid, overdue

        self.init_ui()
        self.load_factures()

    def init_ui(self):
        """Initialise l'interface utilisateur"""
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
        title = ModernLabel("Factures", "large")
        header_layout.addWidget(title)
        header_layout.addStretch()

        # Bouton Synchroniser
        sync_btn = self.create_icon_button("🔄", "Synchroniser avec Axonaut")
        sync_btn.clicked.connect(self.synchroniser_factures)
        header_layout.addWidget(sync_btn)

        layout.addLayout(header_layout)

        # Filtres
        filters_layout = QHBoxLayout()
        filters_layout.setSpacing(DesignSystem.SPACING_SM)

        # Boutons de filtre
        self.filter_all_btn = ModernButton("Toutes", "secondary")
        self.filter_all_btn.clicked.connect(lambda: self.apply_filter("all"))
        filters_layout.addWidget(self.filter_all_btn)

        self.filter_last_month_btn = ModernButton("Mois dernier", "secondary")
        self.filter_last_month_btn.clicked.connect(lambda: self.apply_filter("last_month"))
        filters_layout.addWidget(self.filter_last_month_btn)

        self.filter_current_month_btn = ModernButton("Mois en cours", "secondary")
        self.filter_current_month_btn.clicked.connect(lambda: self.apply_filter("current_month"))
        filters_layout.addWidget(self.filter_current_month_btn)

        self.filter_unpaid_btn = ModernButton("Non soldées", "secondary")
        self.filter_unpaid_btn.clicked.connect(lambda: self.apply_filter("unpaid"))
        filters_layout.addWidget(self.filter_unpaid_btn)

        self.filter_overdue_btn = ModernButton("En dépassement", "secondary")
        self.filter_overdue_btn.clicked.connect(lambda: self.apply_filter("overdue"))
        filters_layout.addWidget(self.filter_overdue_btn)

        filters_layout.addStretch()
        layout.addLayout(filters_layout)

        # Statistiques rapides
        self.stats_label = ModernLabel("", "secondary")
        layout.addWidget(self.stats_label)

        # Table des factures
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "Statut", "N° Facture", "Client", "Date émission",
            "Date échéance", "Montant TTC", "Payé", "Solde"
        ])

        # Configuration de la table
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        self.table.setShowGrid(False)

        # Hauteur des lignes
        self.table.verticalHeader().setDefaultSectionSize(44)

        # Colonnes
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)  # Statut
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)  # N° Facture
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)  # Client
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)  # Date émission
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)  # Date échéance
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents)  # Montant TTC
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.ResizeToContents)  # Payé
        header.setSectionResizeMode(7, QHeaderView.ResizeMode.ResizeToContents)  # Solde

        self.table.setColumnWidth(0, 80)

        # Style de la table
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
                padding: {DesignSystem.SPACING_SM}px;
                border: none;
                border-bottom: 1px solid {DesignSystem.BORDER_COLOR};
                font-weight: 600;
                color: {DesignSystem.TEXT_SECONDARY};
            }}
        """)

        layout.addWidget(self.table)

        # Style du widget principal
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {DesignSystem.BACKGROUND};
            }}
        """)

    def create_icon_button(self, icon: str, tooltip: str) -> QPushButton:
        """Crée un bouton compact avec icône"""
        btn = QPushButton(icon)
        btn.setFixedSize(36, 36)
        btn.setToolTip(tooltip)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setStyleSheet(f"""
            QPushButton {{
                background-color: {DesignSystem.SURFACE};
                border: 1px solid {DesignSystem.BORDER_COLOR};
                border-radius: {DesignSystem.RADIUS_SM}px;
                font-size: 16px;
            }}
            QPushButton:hover {{
                background-color: {DesignSystem.ACCENT_BLUE};
                color: white;
                border-color: {DesignSystem.ACCENT_BLUE};
            }}
        """)
        return btn

    def load_factures(self):
        """Charge les factures depuis la base locale"""
        try:
            # Charger depuis le 1er juillet 2025
            since_date = "2025-07-01"
            self.factures = self.db.get_invoices(since_date=since_date)
            self.apply_filter(self.current_filter)
        except Exception as e:
            QMessageBox.warning(
                self,
                "Erreur",
                f"Impossible de charger les factures: {str(e)}"
            )

    def synchroniser_factures(self):
        """Synchronise les factures depuis l'API Axonaut"""
        try:
            # Dialogue de progression
            progress = QProgressDialog(
                "Synchronisation des factures en cours...",
                "Annuler",
                0, 0,
                self
            )
            progress.setWindowModality(Qt.WindowModality.WindowModal)
            progress.setMinimumDuration(0)
            progress.show()

            # Récupérer depuis le 1er juillet 2025
            since_date = "2025-07-01"
            factures_api = self.client.get_invoices(since_date=since_date)

            # Sauvegarder en base locale
            for facture in factures_api:
                self.db.save_invoice(facture)

            progress.close()

            # Recharger l'affichage
            self.load_factures()

            QMessageBox.information(
                self,
                "Synchronisation réussie",
                f"{len(factures_api)} facture(s) synchronisée(s)"
            )

        except Exception as e:
            if 'progress' in locals():
                progress.close()
            QMessageBox.critical(
                self,
                "Erreur de synchronisation",
                f"Impossible de synchroniser les factures:\n{str(e)}"
            )

    def apply_filter(self, filter_type: str):
        """Applique un filtre sur les factures"""
        self.current_filter = filter_type

        # Réinitialiser le style des boutons
        for btn in [self.filter_all_btn, self.filter_last_month_btn,
                   self.filter_current_month_btn, self.filter_unpaid_btn,
                   self.filter_overdue_btn]:
            btn.setStyleSheet("")  # Reset to default (secondary style)

        # Filtrer les factures
        filtered = self.factures.copy()

        if filter_type == "last_month":
            # Mois dernier
            now = datetime.now()
            first_of_this_month = now.replace(day=1)
            last_month = first_of_this_month - timedelta(days=1)
            first_of_last_month = last_month.replace(day=1)

            filtered = [
                f for f in filtered
                if f.invoice_date and
                   first_of_last_month.isoformat() <= f.invoice_date < first_of_this_month.isoformat()
            ]
            self.filter_last_month_btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {DesignSystem.ACCENT_BLUE};
                    color: white;
                }}
            """)

        elif filter_type == "current_month":
            # Mois en cours
            now = datetime.now()
            first_of_this_month = now.replace(day=1)

            filtered = [
                f for f in filtered
                if f.invoice_date and f.invoice_date >= first_of_this_month.isoformat()
            ]
            self.filter_current_month_btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {DesignSystem.ACCENT_BLUE};
                    color: white;
                }}
            """)

        elif filter_type == "unpaid":
            # Factures non soldées
            filtered = [f for f in filtered if not f.is_paid]
            self.filter_unpaid_btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {DesignSystem.WARNING_ORANGE};
                    color: white;
                }}
            """)

        elif filter_type == "overdue":
            # Factures en dépassement
            filtered = [f for f in filtered if f.is_overdue]
            self.filter_overdue_btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {DesignSystem.ERROR_RED};
                    color: white;
                }}
            """)

        else:  # all
            self.filter_all_btn.setStyleSheet(f"""
                QPushButton {{
                    background-color: {DesignSystem.ACCENT_BLUE};
                    color: white;
                }}
            """)

        # Afficher les factures filtrées
        self.display_factures(filtered)

        # Mettre à jour les statistiques
        self.update_stats(filtered)

    def display_factures(self, factures: List[Invoice]):
        """Affiche les factures dans la table"""
        self.table.setRowCount(0)

        for row, facture in enumerate(factures):
            self.table.insertRow(row)

            # Colonne 0: Statut visuel
            status_item = QTableWidgetItem()
            status_color = facture.status_color
            status_label = facture.status_label

            # Créer un widget personnalisé pour le statut
            status_widget = QWidget()
            status_layout = QHBoxLayout(status_widget)
            status_layout.setContentsMargins(8, 4, 8, 4)

            status_badge = QLabel(status_label)
            status_badge.setAlignment(Qt.AlignmentFlag.AlignCenter)
            status_badge.setStyleSheet(f"""
                QLabel {{
                    background-color: {status_color};
                    color: white;
                    border-radius: 4px;
                    padding: 4px 8px;
                    font-size: {DesignSystem.FONT_SIZE_SMALL}px;
                    font-weight: 600;
                }}
            """)
            status_layout.addWidget(status_badge)

            self.table.setCellWidget(row, 0, status_widget)

            # Colonne 1: N° Facture
            self.table.setItem(row, 1, QTableWidgetItem(facture.invoice_number or "-"))

            # Colonne 2: Client
            self.table.setItem(row, 2, QTableWidgetItem(facture.company_name or "-"))

            # Colonne 3: Date émission
            date_emission = self.format_date(facture.invoice_date)
            self.table.setItem(row, 3, QTableWidgetItem(date_emission))

            # Colonne 4: Date échéance
            date_echeance = self.format_date(facture.due_date)
            due_item = QTableWidgetItem(date_echeance)
            # Colorer en rouge si en retard
            if facture.is_overdue:
                due_item.setForeground(QColor(DesignSystem.ERROR_RED))
                font = QFont()
                font.setBold(True)
                due_item.setFont(font)
            self.table.setItem(row, 4, due_item)

            # Colonne 5: Montant TTC
            montant_ttc = f"{facture.total_amount_tax_included:.2f} €"
            self.table.setItem(row, 5, QTableWidgetItem(montant_ttc))

            # Colonne 6: Payé
            paye = f"{facture.paid_amount:.2f} €"
            self.table.setItem(row, 6, QTableWidgetItem(paye))

            # Colonne 7: Solde
            solde = f"{facture.balance:.2f} €"
            solde_item = QTableWidgetItem(solde)
            # Colorer selon l'état
            if facture.is_paid:
                solde_item.setForeground(QColor(DesignSystem.SUCCESS_GREEN))
            elif facture.balance > 0:
                solde_item.setForeground(QColor(DesignSystem.ERROR_RED))
                font = QFont()
                font.setBold(True)
                solde_item.setFont(font)
            self.table.setItem(row, 7, solde_item)

            # Aligner les montants à droite
            for col in [5, 6, 7]:
                item = self.table.item(row, col)
                if item:
                    item.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

    def format_date(self, date_str: Optional[str]) -> str:
        """Formate une date ISO en format français"""
        if not date_str:
            return "-"

        try:
            # Essayer de parser la date
            if 'T' in date_str:
                date_str = date_str.split('T')[0]

            date = datetime.fromisoformat(date_str)
            return date.strftime("%d/%m/%Y")
        except:
            return date_str

    def update_stats(self, factures: List[Invoice]):
        """Met à jour les statistiques affichées"""
        total_count = len(factures)
        total_amount = sum(f.total_amount_tax_included for f in factures)
        total_paid = sum(f.paid_amount for f in factures)
        total_balance = total_amount - total_paid

        unpaid_count = len([f for f in factures if not f.is_paid])
        overdue_count = len([f for f in factures if f.is_overdue])

        stats_text = (
            f"{total_count} facture(s) • "
            f"Total: {total_amount:.2f} € • "
            f"Payé: {total_paid:.2f} € • "
            f"Solde: {total_balance:.2f} € • "
            f"Non soldées: {unpaid_count} • "
            f"En dépassement: {overdue_count}"
        )

        self.stats_label.setText(stats_text)
