"""
Démonstration de la nouvelle interface moderne GESCO v5.0

Ce fichier montre comment utiliser le nouveau système de design.
Lancez ce script pour voir les dialogues modernes en action.
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from gesco_modern_ui import (
    DesignSystem,
    ResponsiveDialog,
    ModernChantierDialog,
    ModernLabel,
    ModernInput,
    ModernButton,
    ModernComboBox,
    ModernTextEdit
)


class DemoMainWindow(QMainWindow):
    """Fenêtre de démonstration"""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("GESCO v5.0 - Démonstration Interface Moderne")
        self.setGeometry(100, 100, 800, 600)

        # Widget central
        central = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(20)

        # Titre
        title = ModernLabel("Démonstration du nouveau Design System", bold=True)
        title.setStyleSheet(f"""
            font-size: {DesignSystem.FONT_SIZE_LARGE_TITLE}px;
            color: {DesignSystem.TEXT_PRIMARY};
        """)
        layout.addWidget(title)

        # Description
        desc = ModernLabel("Testez les nouveaux dialogues responsives avec design macOS Sonoma/Sequoia", secondary=True)
        layout.addWidget(desc)

        layout.addSpacing(20)

        # Boutons de démonstration
        btn_chantier = ModernButton("Ouvrir Dialog Chantier", "primary")
        btn_chantier.clicked.connect(self.show_chantier_dialog)
        layout.addWidget(btn_chantier)

        btn_simple = ModernButton("Ouvrir Dialog Simple", "secondary")
        btn_simple.clicked.connect(self.show_simple_dialog)
        layout.addWidget(btn_simple)

        btn_complex = ModernButton("Ouvrir Dialog Complexe", "success")
        btn_complex.clicked.connect(self.show_complex_dialog)
        layout.addWidget(btn_complex)

        layout.addStretch()

        central.setLayout(layout)
        self.setCentralWidget(central)

        # Style de la fenêtre
        self.setStyleSheet(f"""
            QMainWindow {{
                background-color: {DesignSystem.BACKGROUND};
            }}
        """)

    def show_chantier_dialog(self):
        """Affiche le dialogue chantier moderne"""
        # Note: Besoin d'un objet gestion pour la vraie version
        # dialog = ModernChantierDialog(None, self)
        # dialog.exec()

        # Pour la démo, on utilise un dialog simple
        self.show_simple_dialog()

    def show_simple_dialog(self):
        """Affiche un dialogue simple"""
        dialog = ResponsiveDialog("Exemple de Dialog Simple", self)

        # Section unique
        section = dialog.add_form_section("Informations")

        # Champs
        name_input = ModernInput(placeholder="Votre nom")
        dialog.add_form_field(section, "Nom complet", name_input, required=True)

        email_input = ModernInput(placeholder="email@exemple.fr")
        dialog.add_form_field(section, "Email", email_input, required=True, help_text="Nous ne partagerons jamais votre email")

        phone_input = ModernInput(placeholder="+33 6 12 34 56 78")
        dialog.add_form_field(section, "Téléphone", phone_input)

        dialog.content_layout.addStretch()

        # Boutons
        dialog.add_button_bar([
            ("Annuler", "secondary", dialog.reject),
            ("Valider", "primary", dialog.accept)
        ])

        dialog.exec()

    def show_complex_dialog(self):
        """Affiche un dialogue complexe avec plusieurs sections"""
        dialog = ResponsiveDialog("Exemple de Dialog Complexe", self)
        dialog.resize(700, 700)

        # Section 1 : Informations personnelles
        section1 = dialog.add_form_section("Informations personnelles")

        nom_input = ModernInput(placeholder="Nom")
        dialog.add_form_field(section1, "Nom", nom_input, required=True)

        prenom_input = ModernInput(placeholder="Prénom")
        dialog.add_form_field(section1, "Prénom", prenom_input, required=True)

        email_input = ModernInput(placeholder="email@exemple.fr")
        dialog.add_form_field(section1, "Email", email_input, required=True)

        tel_input = ModernInput(placeholder="+33 6 12 34 56 78")
        dialog.add_form_field(section1, "Téléphone", tel_input)

        # Section 2 : Adresse
        section2 = dialog.add_form_section("Adresse")

        rue_input = ModernInput(placeholder="Numéro et nom de rue")
        dialog.add_form_field(section2, "Rue", rue_input, required=True)

        ville_input = ModernInput(placeholder="Ville")
        dialog.add_form_field(section2, "Ville", ville_input, required=True)

        cp_input = ModernInput(placeholder="Code postal")
        dialog.add_form_field(section2, "Code postal", cp_input, required=True)

        pays_combo = ModernComboBox()
        pays_combo.addItems(["France", "Belgique", "Suisse", "Luxembourg", "Canada"])
        dialog.add_form_field(section2, "Pays", pays_combo)

        # Section 3 : Informations complémentaires
        section3 = dialog.add_form_section("Informations complémentaires")

        societe_input = ModernInput(placeholder="Nom de la société")
        dialog.add_form_field(section3, "Société", societe_input)

        poste_input = ModernInput(placeholder="Votre poste")
        dialog.add_form_field(section3, "Poste", poste_input)

        notes_text = ModernTextEdit(placeholder="Vos notes...")
        notes_text.setMinimumHeight(100)
        dialog.add_form_field(section3, "Notes", notes_text, help_text="Informations complémentaires (optionnel)")

        # Section 4 : Préférences
        section4 = dialog.add_form_section("Préférences")

        langue_combo = ModernComboBox()
        langue_combo.addItems(["Français", "English", "Deutsch", "Español", "Italiano"])
        dialog.add_form_field(section4, "Langue préférée", langue_combo)

        timezone_combo = ModernComboBox()
        timezone_combo.addItems(["Europe/Paris", "Europe/Brussels", "Europe/Zurich", "America/Montreal"])
        dialog.add_form_field(section4, "Fuseau horaire", timezone_combo)

        dialog.content_layout.addStretch()

        # Boutons
        dialog.add_button_bar([
            ("Réinitialiser", "danger", lambda: print("Reset")),
            ("Annuler", "secondary", dialog.reject),
            ("Enregistrer", "success", dialog.accept)
        ])

        result = dialog.exec()
        if result:
            print("Dialog accepté !")
        else:
            print("Dialog annulé.")


def main():
    """Point d'entrée de la démo"""
    app = QApplication(sys.argv)

    # Configurer la police par défaut
    app.setFont(app.font())

    window = DemoMainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
