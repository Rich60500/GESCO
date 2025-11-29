"""
GESCO v5.0 - Application Principale
Système de gestion de chantiers moderne
"""

import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QStackedWidget, QPushButton, QLabel,
                               QFrame, QMessageBox)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QFont, QIcon

from design_system import DesignSystem, ModernLabel
from database import Database


class SidebarButton(QPushButton):
    """Bouton de la barre latérale"""

    def __init__(self, text: str, icon_text: str = "", parent=None):
        super().__init__(parent)
        self.setText(f"{icon_text}  {text}" if icon_text else text)
        self.setCheckable(True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.setStyleSheet(f"""
            QPushButton {{
                background-color: transparent;
                color: {DesignSystem.TEXT_PRIMARY};
                border: none;
                border-radius: {DesignSystem.RADIUS_SM}px;
                padding: {DesignSystem.SPACING_MD}px {DesignSystem.SPACING_LG}px;
                font-family: {DesignSystem.FONT_FAMILY};
                font-size: {DesignSystem.FONT_SIZE_BODY}px;
                text-align: left;
                min-height: 40px;
            }}
            QPushButton:hover {{
                background-color: rgba(0, 0, 0, 0.05);
            }}
            QPushButton:checked {{
                background-color: {DesignSystem.ACCENT_BLUE};
                color: white;
                font-weight: 600;
            }}
        """)


class ModernSidebar(QFrame):
    """Barre latérale moderne avec navigation"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(240)

        self.setStyleSheet(f"""
            QFrame {{
                background-color: {DesignSystem.SURFACE};
                border-right: 1px solid {DesignSystem.BORDER_COLOR};
            }}
        """)

        # Layout principal
        layout = QVBoxLayout(self)
        layout.setContentsMargins(
            DesignSystem.SPACING_LG,
            DesignSystem.SPACING_XL,
            DesignSystem.SPACING_LG,
            DesignSystem.SPACING_XL
        )
        layout.setSpacing(DesignSystem.SPACING_MD)

        # En-tête avec logo et titre
        header_layout = QVBoxLayout()
        header_layout.setSpacing(DesignSystem.SPACING_XS)

        logo_label = QLabel("⚡️")
        logo_label.setStyleSheet("font-size: 32px;")
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title_label = ModernLabel("GESCO", "large")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        version_label = ModernLabel("v5.0", "secondary")
        version_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        header_layout.addWidget(logo_label)
        header_layout.addWidget(title_label)
        header_layout.addWidget(version_label)

        layout.addLayout(header_layout)
        layout.addSpacing(DesignSystem.SPACING_XL)

        # Séparateur
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setStyleSheet(f"background-color: {DesignSystem.BORDER_COLOR};")
        separator.setFixedHeight(1)
        layout.addWidget(separator)

        layout.addSpacing(DesignSystem.SPACING_LG)

        # Boutons de navigation
        self.buttons = []

        # Module Chantiers (actif par défaut)
        btn_chantiers = SidebarButton("Chantiers", "🏗️")
        btn_chantiers.setChecked(True)
        self.buttons.append(btn_chantiers)
        layout.addWidget(btn_chantiers)

        # Module Achats (actif)
        btn_achats = SidebarButton("Achats", "🛒")
        self.buttons.append(btn_achats)
        layout.addWidget(btn_achats)

        # Module Tiers (actif)
        btn_tiers = SidebarButton("Tiers", "👥")
        self.buttons.append(btn_tiers)
        layout.addWidget(btn_tiers)

        # Module Factures (actif)
        btn_factures = SidebarButton("Factures", "💰")
        self.buttons.append(btn_factures)
        layout.addWidget(btn_factures)

        # Modules à venir (désactivés)
        modules_a_venir = [
            ("Main d'œuvre", "👷"),
            ("Archives", "📦"),
            ("Paramètres", "⚙️")
        ]

        for nom, icon in modules_a_venir:
            btn = SidebarButton(nom, icon)
            btn.setEnabled(False)
            btn.setStyleSheet(btn.styleSheet() + f"""
                QPushButton:disabled {{
                    color: {DesignSystem.TEXT_TERTIARY};
                }}
            """)
            self.buttons.append(btn)
            layout.addWidget(btn)

        # Espaceur pour pousser le footer en bas
        layout.addStretch()

        # Footer avec info
        footer_label = ModernLabel("Étape 3: Tiers & Factures", "secondary")
        footer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer_label.setWordWrap(True)
        layout.addWidget(footer_label)


class PlaceholderWidget(QWidget):
    """Widget placeholder pour les modules à venir"""

    def __init__(self, module_name: str, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        icon_label = QLabel("🚧")
        icon_label.setStyleSheet("font-size: 64px;")
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title_label = ModernLabel(f"Module {module_name}", "large")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        info_label = ModernLabel("Ce module sera disponible prochainement", "secondary")
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(icon_label)
        layout.addSpacing(DesignSystem.SPACING_LG)
        layout.addWidget(title_label)
        layout.addSpacing(DesignSystem.SPACING_SM)
        layout.addWidget(info_label)


class MainWindow(QMainWindow):
    """Fenêtre principale de GESCO v5.0"""

    def __init__(self):
        super().__init__()

        # Initialiser la base de données
        self.db = Database()

        self.setWindowTitle("GESCO v5.0 - Gestion de Chantiers")
        self.setMinimumSize(1200, 800)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal horizontal
        main_layout = QHBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Barre latérale
        self.sidebar = ModernSidebar()
        main_layout.addWidget(self.sidebar)

        # Zone de contenu avec QStackedWidget
        self.content_stack = QStackedWidget()
        self.content_stack.setStyleSheet(f"""
            QStackedWidget {{
                background-color: {DesignSystem.BACKGROUND};
            }}
        """)
        main_layout.addWidget(self.content_stack)

        # Importer et ajouter le module Chantiers
        try:
            from modules.chantiers import ModuleChantiers
            self.module_chantiers = ModuleChantiers(self.db)
            self.content_stack.addWidget(self.module_chantiers)
        except ImportError as e:
            # Si le module n'est pas encore créé, afficher un placeholder
            placeholder = PlaceholderWidget("Chantiers")
            self.content_stack.addWidget(placeholder)

        # Importer et ajouter le module Achats
        try:
            from modules.achats import ModuleAchats
            self.module_achats = ModuleAchats(self.db)
            self.content_stack.addWidget(self.module_achats)
        except ImportError as e:
            # Si le module n'est pas encore créé, afficher un placeholder
            placeholder = PlaceholderWidget("Achats")
            self.content_stack.addWidget(placeholder)

        # Importer et ajouter le module Tiers
        try:
            from modules.tiers import TiersModule
            self.module_tiers = TiersModule()
            self.content_stack.addWidget(self.module_tiers)
        except ImportError as e:
            # Si le module n'est pas encore créé, afficher un placeholder
            placeholder = PlaceholderWidget("Tiers")
            self.content_stack.addWidget(placeholder)

        # Importer et ajouter le module Factures
        try:
            from modules.factures import FacturesWidget
            self.module_factures = FacturesWidget()
            self.content_stack.addWidget(self.module_factures)
        except ImportError as e:
            # Si le module n'est pas encore créé, afficher un placeholder
            placeholder = PlaceholderWidget("Factures")
            self.content_stack.addWidget(placeholder)

        # Ajouter des placeholders pour les autres modules
        modules = ["Main d'œuvre", "Archives", "Paramètres"]
        for module in modules:
            placeholder = PlaceholderWidget(module)
            self.content_stack.addWidget(placeholder)

        # Connecter les boutons de navigation
        for i, button in enumerate(self.sidebar.buttons):
            button.clicked.connect(lambda checked, idx=i: self.switch_module(idx))

        # Style global de la fenêtre
        self.setStyleSheet(f"""
            QMainWindow {{
                background-color: {DesignSystem.BACKGROUND};
            }}
        """)

    def switch_module(self, index: int):
        """Change le module affiché"""
        # Décocher tous les boutons sauf celui cliqué
        for i, button in enumerate(self.sidebar.buttons):
            if i != index:
                button.setChecked(False)
            else:
                button.setChecked(True)

        # Changer le contenu affiché
        self.content_stack.setCurrentIndex(index)

    def closeEvent(self, event):
        """Gestion de la fermeture de l'application"""
        reply = QMessageBox.question(
            self,
            "Fermer GESCO",
            "Êtes-vous sûr de vouloir quitter l'application ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()


def main():
    """Point d'entrée de l'application"""
    app = QApplication(sys.argv)

    # Configuration de l'application
    app.setApplicationName("GESCO")
    app.setApplicationVersion("5.0")
    app.setOrganizationName("GESCO")

    # Police système
    font = QFont(DesignSystem.FONT_FAMILY, DesignSystem.FONT_SIZE_BODY)
    app.setFont(font)

    # Créer et afficher la fenêtre principale
    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
