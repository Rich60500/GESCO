"""
GESCO v5.0 - Design System
Système de design moderne inspiré de macOS Sonoma/Sequoia
"""

from PySide6.QtWidgets import (QLabel, QLineEdit, QTextEdit, QComboBox,
                               QPushButton, QWidget, QVBoxLayout, QHBoxLayout,
                               QFrame, QScrollArea, QDialog)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QPalette, QColor


class DesignSystem:
    """Constantes de design centralisées - style macOS Sonoma/Sequoia"""

    # Palette de couleurs Apple
    BACKGROUND = "#F5F5F7"  # Gris clair Apple
    SURFACE = "#FFFFFF"     # Blanc pur
    SURFACE_ELEVATED = "#FAFAFA"  # Blanc légèrement élevé

    TEXT_PRIMARY = "#1D1D1F"    # Noir Apple
    TEXT_SECONDARY = "#86868B"  # Gris moyen
    TEXT_TERTIARY = "#C7C7CC"   # Gris clair

    # Couleurs système Apple
    ACCENT_BLUE = "#007AFF"     # Bleu système
    SUCCESS_GREEN = "#34C759"   # Vert succès
    WARNING_ORANGE = "#FF9500"  # Orange attention
    ERROR_RED = "#FF3B30"       # Rouge erreur

    # États des chantiers
    ETAT_ACCEPTE = "#007AFF"    # Bleu
    ETAT_EN_COURS = "#FF9500"   # Orange
    ETAT_TERMINE = "#34C759"    # Vert
    ETAT_FACTURE = "#5856D6"    # Violet
    ETAT_CLOTURE = "#86868B"    # Gris

    # Bordures et ombres
    BORDER_COLOR = "#E5E5EA"
    SHADOW_LIGHT = "rgba(0, 0, 0, 0.05)"
    SHADOW_MEDIUM = "rgba(0, 0, 0, 0.1)"

    # Typographie SF Pro
    FONT_FAMILY = '"SF Pro Text", -apple-system, "Helvetica Neue", "Segoe UI", sans-serif'
    FONT_SIZE_SMALL = 11
    FONT_SIZE_BODY = 13
    FONT_SIZE_TITLE = 17
    FONT_SIZE_LARGE = 22

    # Espacements (système 4pt)
    SPACING_XS = 4
    SPACING_SM = 8
    SPACING_MD = 12
    SPACING_LG = 16
    SPACING_XL = 24
    SPACING_XXL = 32

    # Rayons de bordure
    RADIUS_SM = 8
    RADIUS_MD = 12
    RADIUS_LG = 16

    # Hauteurs des contrôles
    INPUT_HEIGHT = 36
    BUTTON_HEIGHT = 36

    @staticmethod
    def get_etat_color(etat: str) -> str:
        """Retourne la couleur associée à un état"""
        colors = {
            "Accepté": DesignSystem.ETAT_ACCEPTE,
            "En cours": DesignSystem.ETAT_EN_COURS,
            "Terminé": DesignSystem.ETAT_TERMINE,
            "Facturé": DesignSystem.ETAT_FACTURE,
            "Clôturé": DesignSystem.ETAT_CLOTURE
        }
        return colors.get(etat, DesignSystem.TEXT_SECONDARY)


class ModernLabel(QLabel):
    """Label moderne avec typographie macOS"""

    def __init__(self, text="", style="body", parent=None):
        super().__init__(text, parent)

        font = QFont(DesignSystem.FONT_FAMILY)

        if style == "title":
            font.setPointSize(DesignSystem.FONT_SIZE_TITLE)
            font.setWeight(QFont.Weight.DemiBold)
            color = DesignSystem.TEXT_PRIMARY
        elif style == "large":
            font.setPointSize(DesignSystem.FONT_SIZE_LARGE)
            font.setWeight(QFont.Weight.Bold)
            color = DesignSystem.TEXT_PRIMARY
        elif style == "secondary":
            font.setPointSize(DesignSystem.FONT_SIZE_BODY)
            color = DesignSystem.TEXT_SECONDARY
        else:  # body
            font.setPointSize(DesignSystem.FONT_SIZE_BODY)
            color = DesignSystem.TEXT_PRIMARY

        self.setFont(font)
        self.setStyleSheet(f"color: {color};")


class ModernInput(QLineEdit):
    """Champ de saisie moderne style macOS - sans bordures visibles"""

    def __init__(self, placeholder="", parent=None):
        super().__init__(parent)
        self.setPlaceholderText(placeholder)
        self.setMinimumHeight(DesignSystem.INPUT_HEIGHT)

        self.setStyleSheet(f"""
            QLineEdit {{
                background-color: {DesignSystem.SURFACE_ELEVATED};
                border: none;
                border-radius: {DesignSystem.RADIUS_SM}px;
                padding: 0 {DesignSystem.SPACING_MD}px;
                font-family: {DesignSystem.FONT_FAMILY};
                font-size: {DesignSystem.FONT_SIZE_BODY}px;
                color: {DesignSystem.TEXT_PRIMARY};
            }}
            QLineEdit:hover {{
                background-color: #F0F0F2;
            }}
            QLineEdit:focus {{
                background-color: {DesignSystem.SURFACE};
                border: 2px solid {DesignSystem.ACCENT_BLUE};
                padding: 0 {DesignSystem.SPACING_MD - 1}px;
            }}
            QLineEdit:disabled {{
                background-color: {DesignSystem.SURFACE_ELEVATED};
                color: {DesignSystem.TEXT_TERTIARY};
            }}
        """)


class ModernTextEdit(QTextEdit):
    """Zone de texte multiligne moderne - sans bordures visibles"""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet(f"""
            QTextEdit {{
                background-color: {DesignSystem.SURFACE_ELEVATED};
                border: none;
                border-radius: {DesignSystem.RADIUS_SM}px;
                padding: {DesignSystem.SPACING_SM}px;
                font-family: {DesignSystem.FONT_FAMILY};
                font-size: {DesignSystem.FONT_SIZE_BODY}px;
                color: {DesignSystem.TEXT_PRIMARY};
            }}
            QTextEdit:hover {{
                background-color: #F0F0F2;
            }}
            QTextEdit:focus {{
                background-color: {DesignSystem.SURFACE};
                border: 2px solid {DesignSystem.ACCENT_BLUE};
                padding: {DesignSystem.SPACING_SM - 1}px;
            }}
        """)


class ModernComboBox(QComboBox):
    """Liste déroulante moderne style macOS - sans bordures visibles"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumHeight(DesignSystem.INPUT_HEIGHT)

        self.setStyleSheet(f"""
            QComboBox {{
                background-color: {DesignSystem.SURFACE_ELEVATED};
                border: none;
                border-radius: {DesignSystem.RADIUS_SM}px;
                padding: 0 {DesignSystem.SPACING_MD}px;
                font-family: {DesignSystem.FONT_FAMILY};
                font-size: {DesignSystem.FONT_SIZE_BODY}px;
                color: {DesignSystem.TEXT_PRIMARY};
            }}
            QComboBox:hover {{
                background-color: #F0F0F2;
            }}
            QComboBox:focus {{
                background-color: {DesignSystem.SURFACE};
                border: 2px solid {DesignSystem.ACCENT_BLUE};
                padding: 0 {DesignSystem.SPACING_MD - 1}px;
            }}
            QComboBox::drop-down {{
                border: none;
                width: 24px;
            }}
            QComboBox::down-arrow {{
                image: none;
                border-left: 4px solid transparent;
                border-right: 4px solid transparent;
                border-top: 5px solid {DesignSystem.TEXT_SECONDARY};
                margin-right: 8px;
            }}
            QComboBox QAbstractItemView {{
                background-color: {DesignSystem.SURFACE};
                border: none;
                border-radius: {DesignSystem.RADIUS_MD}px;
                selection-background-color: {DesignSystem.ACCENT_BLUE};
                selection-color: white;
                padding: 4px;
                outline: none;
            }}
        """)


class ModernButton(QPushButton):
    """Bouton moderne style macOS"""

    def __init__(self, text="", style="primary", parent=None):
        super().__init__(text, parent)
        self.setMinimumHeight(DesignSystem.BUTTON_HEIGHT)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        if style == "primary":
            bg_color = DesignSystem.ACCENT_BLUE
            text_color = "white"
            hover_bg = "#0051D5"
        elif style == "success":
            bg_color = DesignSystem.SUCCESS_GREEN
            text_color = "white"
            hover_bg = "#2DA84E"
        elif style == "danger":
            bg_color = DesignSystem.ERROR_RED
            text_color = "white"
            hover_bg = "#D32F26"
        else:  # secondary
            bg_color = DesignSystem.SURFACE
            text_color = DesignSystem.TEXT_PRIMARY
            hover_bg = DesignSystem.SURFACE_ELEVATED

        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {bg_color};
                color: {text_color};
                border: {"1px solid " + DesignSystem.BORDER_COLOR if style == "secondary" else "none"};
                border-radius: {DesignSystem.RADIUS_SM}px;
                padding: 0 {DesignSystem.SPACING_LG}px;
                font-family: {DesignSystem.FONT_FAMILY};
                font-size: {DesignSystem.FONT_SIZE_BODY}px;
                font-weight: 500;
            }}
            QPushButton:hover {{
                background-color: {hover_bg};
            }}
            QPushButton:pressed {{
                background-color: {bg_color};
                transform: scale(0.98);
            }}
            QPushButton:disabled {{
                background-color: {DesignSystem.SURFACE_ELEVATED};
                color: {DesignSystem.TEXT_TERTIARY};
                border: 1px solid {DesignSystem.BORDER_COLOR};
            }}
        """)


class ModernCard(QFrame):
    """Carte moderne avec ombre et coins arrondis"""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setStyleSheet(f"""
            QFrame {{
                background-color: {DesignSystem.SURFACE};
                border: 1px solid {DesignSystem.BORDER_COLOR};
                border-radius: {DesignSystem.RADIUS_MD}px;
            }}
        """)

        # Layout interne avec marges
        self.card_layout = QVBoxLayout(self)
        self.card_layout.setContentsMargins(
            DesignSystem.SPACING_LG,
            DesignSystem.SPACING_LG,
            DesignSystem.SPACING_LG,
            DesignSystem.SPACING_LG
        )
        self.card_layout.setSpacing(DesignSystem.SPACING_MD)


class ResponsiveDialog(QDialog):
    """
    Dialogue responsive de base avec défilement automatique.
    Tous les champs sont toujours visibles grâce au QScrollArea.
    """

    def __init__(self, title="Dialog", width=600, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setMinimumWidth(width)

        # Layout principal
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Zone de défilement
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll.setStyleSheet(f"""
            QScrollArea {{
                border: none;
                background-color: {DesignSystem.BACKGROUND};
            }}
        """)

        # Widget de contenu
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setContentsMargins(
            DesignSystem.SPACING_XL,
            DesignSystem.SPACING_XL,
            DesignSystem.SPACING_XL,
            DesignSystem.SPACING_XL
        )
        self.content_layout.setSpacing(DesignSystem.SPACING_LG)

        scroll.setWidget(self.content_widget)
        main_layout.addWidget(scroll)

        # Style global
        self.setStyleSheet(f"""
            QDialog {{
                background-color: {DesignSystem.BACKGROUND};
            }}
        """)

    def add_section(self, title: str) -> QVBoxLayout:
        """Ajoute une section avec titre"""
        section_layout = QVBoxLayout()
        section_layout.setSpacing(DesignSystem.SPACING_SM)

        if title:
            title_label = ModernLabel(title, "title")
            section_layout.addWidget(title_label)

        self.content_layout.addLayout(section_layout)
        return section_layout

    def add_form_field(self, layout: QVBoxLayout, label: str, widget: QWidget):
        """Ajoute un champ de formulaire (label + widget)"""
        label_widget = ModernLabel(label)
        layout.addWidget(label_widget)
        layout.addWidget(widget)

    def add_button_bar(self, buttons: list):
        """Ajoute une barre de boutons en bas"""
        button_layout = QHBoxLayout()
        button_layout.setSpacing(DesignSystem.SPACING_SM)
        button_layout.addStretch()

        for button in buttons:
            button_layout.addWidget(button)

        self.content_layout.addLayout(button_layout)
