"""
GESCO v5.0.0 - Interface Moderne Responsive
Design System macOS Sonoma/Sequoia

✨ Améliorations majeures :
- Interface 100% responsive avec QScrollArea
- Design macOS Sonoma/Sequoia moderne
- Tous les champs toujours visibles
- Animations fluides et naturelles
- Typographie SF Pro cohérente
- Espaces blancs optimisés
"""

from PySide6.QtCore import Qt, QSize, QPropertyAnimation, QEasingCurve, QTimer
from PySide6.QtGui import QFont, QColor
from PySide6.QtWidgets import (
    QWidget, QDialog, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QLineEdit, QComboBox, QDateEdit, QTextEdit,
    QPushButton, QScrollArea, QFrame, QSizePolicy
)


# ============================================================================
# DESIGN SYSTEM - Constantes de design macOS moderne
# ============================================================================

class DesignSystem:
    """Système de design cohérent inspiré de macOS Sonoma/Sequoia"""

    # Couleurs
    BACKGROUND = "#F5F5F7"          # Fond principal
    SURFACE = "#FFFFFF"             # Surface des cartes
    SURFACE_SECONDARY = "#FAFAFA"   # Surface secondaire

    TEXT_PRIMARY = "#1D1D1F"        # Texte principal
    TEXT_SECONDARY = "#86868B"      # Texte secondaire
    TEXT_TERTIARY = "#C7C7CC"       # Texte tertiaire

    ACCENT_BLUE = "#007AFF"         # Accent bleu Apple
    ACCENT_GREEN = "#34C759"        # Accent vert
    ACCENT_RED = "#FF3B30"          # Accent rouge
    ACCENT_ORANGE = "#FF9500"       # Accent orange

    BORDER_LIGHT = "rgba(0, 0, 0, 0.06)"
    BORDER_MEDIUM = "rgba(0, 0, 0, 0.12)"

    # Typographie
    FONT_FAMILY = '"SF Pro Text", "Helvetica Neue", "Segoe UI", sans-serif'
    FONT_SIZE_SMALL = 11
    FONT_SIZE_BODY = 13
    FONT_SIZE_TITLE = 16
    FONT_SIZE_LARGE_TITLE = 22

    # Espacements
    SPACING_XS = 4
    SPACING_SM = 8
    SPACING_MD = 12
    SPACING_LG = 16
    SPACING_XL = 24
    SPACING_XXL = 32

    # Bordures
    RADIUS_SM = 8
    RADIUS_MD = 12
    RADIUS_LG = 16

    # Hauteurs de composants
    INPUT_HEIGHT = 36
    BUTTON_HEIGHT = 36

    @staticmethod
    def get_shadow():
        """Retourne le style d'ombre pour les cartes"""
        return """
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04),
                        0 2px 8px rgba(0, 0, 0, 0.02);
        """


# ============================================================================
# COMPOSANTS DE BASE - Widgets réutilisables
# ============================================================================

class ModernLabel(QLabel):
    """Label avec style macOS moderne"""

    def __init__(self, text="", bold=False, secondary=False, parent=None):
        super().__init__(text, parent)

        font = QFont(DesignSystem.FONT_FAMILY, DesignSystem.FONT_SIZE_BODY)
        if bold:
            font.setWeight(QFont.Weight.Bold)
        self.setFont(font)

        color = DesignSystem.TEXT_SECONDARY if secondary else DesignSystem.TEXT_PRIMARY
        self.setStyleSheet(f"""
            QLabel {{
                color: {color};
                background: transparent;
                padding: 0px;
            }}
        """)


class ModernInput(QLineEdit):
    """Champ de saisie avec style macOS moderne"""

    def __init__(self, placeholder="", parent=None):
        super().__init__(parent)

        if placeholder:
            self.setPlaceholderText(placeholder)

        self.setFont(QFont(DesignSystem.FONT_FAMILY, DesignSystem.FONT_SIZE_BODY))
        self.setMinimumHeight(DesignSystem.INPUT_HEIGHT)

        self.setStyleSheet(f"""
            QLineEdit {{
                background-color: {DesignSystem.SURFACE};
                color: {DesignSystem.TEXT_PRIMARY};
                border: 1px solid {DesignSystem.BORDER_LIGHT};
                border-radius: {DesignSystem.RADIUS_SM}px;
                padding: 0 {DesignSystem.SPACING_MD}px;
                font-size: {DesignSystem.FONT_SIZE_BODY}px;
                selection-background-color: {DesignSystem.ACCENT_BLUE};
            }}
            QLineEdit:focus {{
                border: 2px solid {DesignSystem.ACCENT_BLUE};
                background-color: {DesignSystem.SURFACE};
                outline: none;
            }}
            QLineEdit:disabled {{
                background-color: {DesignSystem.SURFACE_SECONDARY};
                color: {DesignSystem.TEXT_TERTIARY};
            }}
        """)


class ModernComboBox(QComboBox):
    """ComboBox avec style macOS moderne"""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setFont(QFont(DesignSystem.FONT_FAMILY, DesignSystem.FONT_SIZE_BODY))
        self.setMinimumHeight(DesignSystem.INPUT_HEIGHT)

        self.setStyleSheet(f"""
            QComboBox {{
                background-color: {DesignSystem.SURFACE};
                color: {DesignSystem.TEXT_PRIMARY};
                border: 1px solid {DesignSystem.BORDER_LIGHT};
                border-radius: {DesignSystem.RADIUS_SM}px;
                padding: 0 {DesignSystem.SPACING_MD}px;
                padding-right: 32px;
                font-size: {DesignSystem.FONT_SIZE_BODY}px;
            }}
            QComboBox:focus {{
                border: 2px solid {DesignSystem.ACCENT_BLUE};
                outline: none;
            }}
            QComboBox::drop-down {{
                border: none;
                padding-right: {DesignSystem.SPACING_MD}px;
                width: 24px;
            }}
            QComboBox::down-arrow {{
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 6px solid {DesignSystem.TEXT_PRIMARY};
                margin-right: {DesignSystem.SPACING_SM}px;
            }}
            QComboBox::down-arrow:hover {{
                border-top-color: {DesignSystem.ACCENT_BLUE};
            }}
            QComboBox QAbstractItemView {{
                background-color: {DesignSystem.SURFACE};
                border: 1px solid {DesignSystem.BORDER_MEDIUM};
                border-radius: {DesignSystem.RADIUS_SM}px;
                selection-background-color: {DesignSystem.ACCENT_BLUE};
                selection-color: white;
                padding: {DesignSystem.SPACING_XS}px;
                outline: none;
            }}
            QComboBox QAbstractItemView::item {{
                padding: {DesignSystem.SPACING_SM}px {DesignSystem.SPACING_MD}px;
                border-radius: {DesignSystem.RADIUS_SM - 2}px;
                min-height: 28px;
            }}
            QComboBox QAbstractItemView::item:hover {{
                background-color: rgba(0, 122, 255, 0.1);
            }}
        """)


class ModernTextEdit(QTextEdit):
    """Zone de texte avec style macOS moderne"""

    def __init__(self, placeholder="", parent=None):
        super().__init__(parent)

        if placeholder:
            self.setPlaceholderText(placeholder)

        self.setFont(QFont(DesignSystem.FONT_FAMILY, DesignSystem.FONT_SIZE_BODY))

        self.setStyleSheet(f"""
            QTextEdit {{
                background-color: {DesignSystem.SURFACE};
                color: {DesignSystem.TEXT_PRIMARY};
                border: 1px solid {DesignSystem.BORDER_LIGHT};
                border-radius: {DesignSystem.RADIUS_SM}px;
                padding: {DesignSystem.SPACING_SM}px {DesignSystem.SPACING_MD}px;
                font-size: {DesignSystem.FONT_SIZE_BODY}px;
                selection-background-color: {DesignSystem.ACCENT_BLUE};
            }}
            QTextEdit:focus {{
                border: 2px solid {DesignSystem.ACCENT_BLUE};
                outline: none;
            }}
        """)


class ModernButton(QPushButton):
    """Bouton avec style macOS moderne"""

    def __init__(self, text="", variant="primary", parent=None):
        super().__init__(text, parent)

        self.variant = variant
        self.setFont(QFont(DesignSystem.FONT_FAMILY, DesignSystem.FONT_SIZE_BODY, QFont.Weight.Medium))
        self.setMinimumHeight(DesignSystem.BUTTON_HEIGHT)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self._apply_style()

    def _apply_style(self):
        """Applique le style en fonction de la variante"""

        if self.variant == "primary":
            self.setStyleSheet(f"""
                QPushButton {{
                    background-color: {DesignSystem.ACCENT_BLUE};
                    color: white;
                    border: none;
                    border-radius: {DesignSystem.RADIUS_SM}px;
                    padding: 0 {DesignSystem.SPACING_LG}px;
                    font-weight: 600;
                }}
                QPushButton:hover {{
                    background-color: #0051D5;
                }}
                QPushButton:pressed {{
                    background-color: #004FC1;
                }}
                QPushButton:disabled {{
                    background-color: {DesignSystem.BORDER_LIGHT};
                    color: {DesignSystem.TEXT_TERTIARY};
                }}
            """)

        elif self.variant == "secondary":
            self.setStyleSheet(f"""
                QPushButton {{
                    background-color: {DesignSystem.SURFACE_SECONDARY};
                    color: {DesignSystem.TEXT_PRIMARY};
                    border: 1px solid {DesignSystem.BORDER_MEDIUM};
                    border-radius: {DesignSystem.RADIUS_SM}px;
                    padding: 0 {DesignSystem.SPACING_LG}px;
                    font-weight: 600;
                }}
                QPushButton:hover {{
                    background-color: #EFEFEF;
                    border-color: {DesignSystem.BORDER_MEDIUM};
                }}
                QPushButton:pressed {{
                    background-color: #E5E5E5;
                }}
            """)

        elif self.variant == "success":
            self.setStyleSheet(f"""
                QPushButton {{
                    background-color: {DesignSystem.ACCENT_GREEN};
                    color: white;
                    border: none;
                    border-radius: {DesignSystem.RADIUS_SM}px;
                    padding: 0 {DesignSystem.SPACING_LG}px;
                    font-weight: 600;
                }}
                QPushButton:hover {{
                    background-color: #2DB04A;
                }}
                QPushButton:pressed {{
                    background-color: #28A745;
                }}
            """)

        elif self.variant == "danger":
            self.setStyleSheet(f"""
                QPushButton {{
                    background-color: {DesignSystem.ACCENT_RED};
                    color: white;
                    border: none;
                    border-radius: {DesignSystem.RADIUS_SM}px;
                    padding: 0 {DesignSystem.SPACING_LG}px;
                    font-weight: 600;
                }}
                QPushButton:hover {{
                    background-color: #E6342A;
                }}
                QPushButton:pressed {{
                    background-color: #D92E24;
                }}
            """)


class ModernCard(QFrame):
    """Carte avec style macOS moderne"""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet(f"""
            QFrame {{
                background-color: {DesignSystem.SURFACE};
                border: 1px solid {DesignSystem.BORDER_LIGHT};
                border-radius: {DesignSystem.RADIUS_LG}px;
            }}
        """)


# ============================================================================
# DIALOG DE BASE RESPONSIVE
# ============================================================================

class ResponsiveDialog(QDialog):
    """
    Dialog moderne avec support du responsive design.
    Tous les dialogues doivent hériter de cette classe.
    """

    def __init__(self, title="Dialog", parent=None):
        super().__init__(parent)

        self.setWindowTitle(title)
        self.setModal(True)

        # Taille minimale et par défaut
        self.setMinimumSize(500, 400)
        self.resize(650, 600)

        # Layout principal
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Scroll Area pour le contenu
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        # Style de la scroll area
        scroll.setStyleSheet(f"""
            QScrollArea {{
                background-color: {DesignSystem.BACKGROUND};
                border: none;
            }}
            QScrollBar:vertical {{
                background-color: transparent;
                width: 8px;
                margin: 0px;
            }}
            QScrollBar::handle:vertical {{
                background-color: rgba(0, 0, 0, 0.15);
                border-radius: 4px;
                min-height: 30px;
            }}
            QScrollBar::handle:vertical:hover {{
                background-color: rgba(0, 0, 0, 0.25);
            }}
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
                height: 0px;
            }}
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
                background: none;
            }}
            QScrollBar:horizontal {{
                background-color: transparent;
                height: 8px;
                margin: 0px;
            }}
            QScrollBar::handle:horizontal {{
                background-color: rgba(0, 0, 0, 0.15);
                border-radius: 4px;
                min-width: 30px;
            }}
            QScrollBar::handle:horizontal:hover {{
                background-color: rgba(0, 0, 0, 0.25);
            }}
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{
                width: 0px;
            }}
            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {{
                background: none;
            }}
        """)

        # Widget de contenu
        self.content_widget = QWidget()
        self.content_widget.setStyleSheet(f"background-color: {DesignSystem.BACKGROUND};")

        # Layout du contenu
        self.content_layout = QVBoxLayout()
        self.content_layout.setContentsMargins(
            DesignSystem.SPACING_XXL,
            DesignSystem.SPACING_XL,
            DesignSystem.SPACING_XXL,
            DesignSystem.SPACING_XL
        )
        self.content_layout.setSpacing(DesignSystem.SPACING_XL)

        self.content_widget.setLayout(self.content_layout)
        scroll.setWidget(self.content_widget)

        main_layout.addWidget(scroll)
        self.setLayout(main_layout)

        # Appliquer le style général
        self.setStyleSheet(f"""
            QDialog {{
                background-color: {DesignSystem.BACKGROUND};
            }}
        """)

    def add_form_section(self, title=None):
        """Ajoute une section de formulaire avec titre optionnel"""

        section_widget = QWidget()
        section_layout = QVBoxLayout()
        section_layout.setContentsMargins(0, 0, 0, 0)
        section_layout.setSpacing(DesignSystem.SPACING_MD)

        if title:
            title_label = QLabel(title)
            title_label.setFont(QFont(DesignSystem.FONT_FAMILY, DesignSystem.FONT_SIZE_TITLE, QFont.Weight.Bold))
            title_label.setStyleSheet(f"color: {DesignSystem.TEXT_PRIMARY}; padding-bottom: {DesignSystem.SPACING_SM}px;")
            section_layout.addWidget(title_label)

        # Carte pour le formulaire
        card = ModernCard()
        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(
            DesignSystem.SPACING_XL,
            DesignSystem.SPACING_XL,
            DesignSystem.SPACING_XL,
            DesignSystem.SPACING_XL
        )
        card_layout.setSpacing(DesignSystem.SPACING_LG)
        card.setLayout(card_layout)

        section_layout.addWidget(card)
        section_widget.setLayout(section_layout)

        self.content_layout.addWidget(section_widget)

        return card_layout

    def add_form_field(self, parent_layout, label_text, widget, required=False, help_text=None):
        """Ajoute un champ de formulaire avec label"""

        field_layout = QVBoxLayout()
        field_layout.setSpacing(DesignSystem.SPACING_XS)

        # Label
        label = ModernLabel(label_text, bold=True)
        if required:
            label.setText(f"{label_text} *")
            label.setStyleSheet(f"""
                QLabel {{
                    color: {DesignSystem.TEXT_PRIMARY};
                    background: transparent;
                }}
            """)

        field_layout.addWidget(label)

        # Widget
        field_layout.addWidget(widget)

        # Texte d'aide optionnel
        if help_text:
            help_label = ModernLabel(help_text, secondary=True)
            help_label.setFont(QFont(DesignSystem.FONT_FAMILY, DesignSystem.FONT_SIZE_SMALL))
            field_layout.addWidget(help_label)

        parent_layout.addLayout(field_layout)

        return widget

    def add_button_bar(self, buttons):
        """
        Ajoute une barre de boutons en bas du dialogue

        Args:
            buttons: Liste de tuples (text, variant, callback)
                    Ex: [("Annuler", "secondary", self.reject), ("Créer", "primary", self.accept)]
        """

        # Séparateur
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setStyleSheet(f"background-color: {DesignSystem.BORDER_LIGHT}; max-height: 1px;")
        self.content_layout.addWidget(separator)

        # Barre de boutons
        button_layout = QHBoxLayout()
        button_layout.setSpacing(DesignSystem.SPACING_MD)
        button_layout.addStretch()

        for text, variant, callback in buttons:
            btn = ModernButton(text, variant)
            btn.clicked.connect(callback)
            button_layout.addWidget(btn)

        self.content_layout.addLayout(button_layout)


# ============================================================================
# EXEMPLE D'UTILISATION - Dialog Chantier Moderne
# ============================================================================

class ModernChantierDialog(ResponsiveDialog):
    """Dialog moderne pour créer un nouveau chantier"""

    def __init__(self, gestion, parent=None):
        super().__init__("Nouveau Chantier", parent)

        self.gestion = gestion

        # Section Informations générales
        section1 = self.add_form_section("Informations générales")

        # N° Commande Client
        self.num_commande_input = ModernInput(placeholder="Ex: CMD-2024-001")
        self.add_form_field(section1, "N° Commande Client", self.num_commande_input, required=True)

        # Client
        client_container = QWidget()
        client_layout = QHBoxLayout()
        client_layout.setContentsMargins(0, 0, 0, 0)
        client_layout.setSpacing(DesignSystem.SPACING_SM)

        self.client_combo = ModernComboBox()
        self.client_combo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        client_layout.addWidget(self.client_combo)

        btn_new_client = ModernButton("Nouveau", "secondary")
        btn_new_client.setFixedWidth(100)
        client_layout.addWidget(btn_new_client)

        client_container.setLayout(client_layout)
        self.add_form_field(section1, "Client", client_container, required=True)

        # Adresse Chantier
        address_container = QWidget()
        address_layout = QHBoxLayout()
        address_layout.setContentsMargins(0, 0, 0, 0)
        address_layout.setSpacing(DesignSystem.SPACING_SM)

        self.adresse_combo = ModernComboBox()
        self.adresse_combo.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        address_layout.addWidget(self.adresse_combo)

        btn_add_address = ModernButton("Ajouter", "secondary")
        btn_add_address.setFixedWidth(90)
        address_layout.addWidget(btn_add_address)

        btn_edit_address = ModernButton("Modifier", "secondary")
        btn_edit_address.setFixedWidth(90)
        address_layout.addWidget(btn_edit_address)

        address_container.setLayout(address_layout)
        self.add_form_field(section1, "Adresse du chantier", address_container, required=True)

        # Section Budget et durée
        section2 = self.add_form_section("Budget et durée")

        # Durée prévue
        self.duree_input = ModernInput(placeholder="30")
        self.add_form_field(
            section2,
            "Durée prévue (jours)",
            self.duree_input,
            help_text="Nombre de jours ouvrés estimés pour le chantier"
        )

        # Chiffrage Global
        self.chiffrage_input = ModernInput(placeholder="0.00")
        self.add_form_field(section2, "Chiffrage global (€)", self.chiffrage_input, required=True)

        # Section Coûts estimés
        section3 = self.add_form_section("Coûts estimés")

        # Coût Estimé Achats
        self.cout_achats_input = ModernInput(placeholder="0.00")
        self.add_form_field(section3, "Coût estimé achats (€)", self.cout_achats_input)

        # Coût Estimé Main d'Œuvre
        self.cout_mo_input = ModernInput(placeholder="0.00")
        self.add_form_field(section3, "Coût estimé main d'œuvre (€)", self.cout_mo_input)

        # Ajouter un stretch pour pousser le contenu vers le haut
        self.content_layout.addStretch()

        # Barre de boutons
        self.add_button_bar([
            ("Annuler", "secondary", self.reject),
            ("Créer le chantier", "primary", self.accept)
        ])


# ============================================================================
# EXPORT
# ============================================================================

__all__ = [
    'DesignSystem',
    'ModernLabel',
    'ModernInput',
    'ModernComboBox',
    'ModernTextEdit',
    'ModernButton',
    'ModernCard',
    'ResponsiveDialog',
    'ModernChantierDialog',
]
