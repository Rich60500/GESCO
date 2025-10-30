# Guide de Migration vers GESCO v5.0 - Interface Moderne

## 🎯 Vue d'ensemble

Ce guide vous explique comment migrer votre code GESCO v4.8 vers le nouveau système d'interface v5.0 avec design macOS Sonoma/Sequoia responsive.

## ✨ Principales améliorations

### Avant (v4.8)
- ❌ Dialogues à taille fixe
- ❌ Pas de scroll automatique
- ❌ Champs peuvent être masqués
- ❌ Style incohérent
- ❌ Non responsive

### Après (v5.0)
- ✅ Dialogues adaptatifs
- ✅ Scroll automatique avec QScrollArea
- ✅ Tous les champs toujours visibles
- ✅ Design system cohérent
- ✅ 100% responsive

---

## 📦 1. Import du nouveau module

```python
# Ancien (v4.8)
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

# Nouveau (v5.0)
from gesco_modern_ui import (
    ResponsiveDialog,
    DesignSystem,
    ModernLabel,
    ModernInput,
    ModernButton,
    ModernComboBox,
    ModernTextEdit,
    ModernCard
)
```

---

## 🔄 2. Migration d'un Dialog simple

### AVANT (v4.8)

```python
class ChantierDialog(QDialog):
    def __init__(self, gestion, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Nouveau Chantier")
        self.setModal(True)
        self.resize(650, 520)  # Taille fixe !

        layout = QVBoxLayout()
        layout.setSpacing(18)
        layout.setContentsMargins(25, 25, 25, 25)

        form = QGridLayout()
        form.setSpacing(12)

        # Labels avec largeur fixe
        label_commande = QLabel("N° Commande Client:")
        label_commande.setMinimumWidth(180)
        form.addWidget(label_commande, 0, 0)

        self.num_commande_entry = QLineEdit()
        self.num_commande_entry.setMinimumHeight(36)
        form.addWidget(self.num_commande_entry, 0, 1)

        layout.addLayout(form)

        # Boutons
        buttons = QHBoxLayout()
        btn_cancel = QPushButton("Annuler")
        btn_cancel.clicked.connect(self.reject)
        buttons.addWidget(btn_cancel)

        btn_ok = QPushButton("Créer")
        btn_ok.clicked.connect(self.accept)
        buttons.addWidget(btn_ok)

        layout.addLayout(buttons)
        self.setLayout(layout)
```

### APRÈS (v5.0)

```python
class ChantierDialog(ResponsiveDialog):
    def __init__(self, gestion, parent=None):
        super().__init__("Nouveau Chantier", parent)

        self.gestion = gestion

        # Section du formulaire
        section = self.add_form_section("Informations générales")

        # Champs
        self.num_commande_input = ModernInput(placeholder="Ex: CMD-2024-001")
        self.add_form_field(
            section,
            "N° Commande Client",
            self.num_commande_input,
            required=True
        )

        # Ajouter un stretch pour pousser le contenu vers le haut
        self.content_layout.addStretch()

        # Barre de boutons
        self.add_button_bar([
            ("Annuler", "secondary", self.reject),
            ("Créer le chantier", "primary", self.accept)
        ])
```

---

## 🎨 3. Utilisation des composants modernes

### Labels

```python
# Avant
label = QLabel("Mon texte")
label.setStyleSheet("color: #1D1D1F;")

# Après
label = ModernLabel("Mon texte")
label_bold = ModernLabel("Texte important", bold=True)
label_secondary = ModernLabel("Texte secondaire", secondary=True)
```

### Champs de saisie

```python
# Avant
input = QLineEdit()
input.setPlaceholderText("Saisir...")
input.setMinimumHeight(36)
input.setStyleSheet("...")  # Long stylesheet

# Après
input = ModernInput(placeholder="Saisir...")
```

### ComboBox

```python
# Avant
combo = QComboBox()
combo.setMinimumHeight(36)
combo.setStyleSheet("...")  # Long stylesheet

# Après
combo = ModernComboBox()
combo.addItems(["Option 1", "Option 2", "Option 3"])
```

### Boutons

```python
# Avant
btn = QPushButton("Valider")
btn.setStyleSheet("...")  # Long stylesheet

# Après
btn_primary = ModernButton("Valider", "primary")
btn_secondary = ModernButton("Annuler", "secondary")
btn_success = ModernButton("Créer", "success")
btn_danger = ModernButton("Supprimer", "danger")
```

---

## 📋 4. Migration d'un Dialog complexe avec plusieurs sections

```python
class ComplexDialog(ResponsiveDialog):
    def __init__(self, parent=None):
        super().__init__("Dialog Complexe", parent)

        # Section 1
        section1 = self.add_form_section("Informations de base")

        self.nom_input = ModernInput(placeholder="Nom")
        self.add_form_field(section1, "Nom", self.nom_input, required=True)

        self.email_input = ModernInput(placeholder="email@exemple.fr")
        self.add_form_field(
            section1,
            "Email",
            self.email_input,
            required=True,
            help_text="Nous ne partagerons jamais votre email"
        )

        # Section 2
        section2 = self.add_form_section("Adresse")

        self.ville_input = ModernInput(placeholder="Ville")
        self.add_form_field(section2, "Ville", self.ville_input)

        # Section 3
        section3 = self.add_form_section("Notes")

        self.notes_text = ModernTextEdit(placeholder="Vos notes...")
        self.notes_text.setMinimumHeight(120)
        self.add_form_field(section3, "Commentaires", self.notes_text)

        # Stretch
        self.content_layout.addStretch()

        # Boutons
        self.add_button_bar([
            ("Annuler", "secondary", self.reject),
            ("Enregistrer", "success", self.accept)
        ])
```

---

## 🔧 5. Utilisation du Design System

Toutes les constantes sont centralisées dans la classe `DesignSystem` :

```python
from gesco_modern_ui import DesignSystem

# Couleurs
bg_color = DesignSystem.BACKGROUND
text_color = DesignSystem.TEXT_PRIMARY
accent = DesignSystem.ACCENT_BLUE

# Espacements
small_spacing = DesignSystem.SPACING_SM  # 8px
medium_spacing = DesignSystem.SPACING_MD  # 12px
large_spacing = DesignSystem.SPACING_LG  # 16px

# Tailles de police
body_size = DesignSystem.FONT_SIZE_BODY  # 13px
title_size = DesignSystem.FONT_SIZE_TITLE  # 16px

# Bordures
radius = DesignSystem.RADIUS_MD  # 12px

# Composants
input_height = DesignSystem.INPUT_HEIGHT  # 36px
```

---

## 🚀 6. Avantages du nouveau système

### 1. Responsive automatique
```python
# Le dialog s'adapte automatiquement à la taille de l'écran
# Plus besoin de gérer manuellement resize()
dialog = ResponsiveDialog("Mon Dialog", parent)
# Taille minimale garantie, mais peut s'agrandir
```

### 2. Scroll automatique
```python
# Tous les champs sont toujours accessibles grâce au QScrollArea intégré
# Plus de problème de champs cachés !
section = dialog.add_form_section("Ma Section")
# Ajoutez autant de champs que nécessaire
```

### 3. Style cohérent
```python
# Plus besoin d'écrire des stylesheets manuellement
# Tout est géré par le Design System
input = ModernInput()  # Style macOS moderne automatique
```

### 4. Meilleure accessibilité
```python
# Support des champs requis
dialog.add_form_field(section, "Email", email_input, required=True)

# Support du texte d'aide
dialog.add_form_field(
    section,
    "Téléphone",
    phone_input,
    help_text="Format: +33 6 12 34 56 78"
)
```

---

## 📝 7. Checklist de migration

Pour chaque dialog à migrer :

- [ ] Hériter de `ResponsiveDialog` au lieu de `QDialog`
- [ ] Appeler `super().__init__(title, parent)` avec le titre
- [ ] Supprimer les appels à `resize()` et `setModal()`
- [ ] Remplacer les layouts manuels par `add_form_section()`
- [ ] Remplacer les widgets Qt par les composants modernes :
  - [ ] `QLabel` → `ModernLabel`
  - [ ] `QLineEdit` → `ModernInput`
  - [ ] `QComboBox` → `ModernComboBox`
  - [ ] `QTextEdit` → `ModernTextEdit`
  - [ ] `QPushButton` → `ModernButton`
- [ ] Remplacer les boutons manuels par `add_button_bar()`
- [ ] Ajouter `self.content_layout.addStretch()` avant les boutons
- [ ] Tester le dialog en redimensionnant la fenêtre

---

## 🎯 8. Exemple complet de migration

### Dialog Achat (Avant)

```python
class AchatDialog(QDialog):
    def __init__(self, gestion, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Nouvel Achat")
        self.resize(620, 480)

        layout = QVBoxLayout()
        form = QGridLayout()

        # Date
        label_date = QLabel("Date:")
        form.addWidget(label_date, 0, 0)
        self.date_edit = QDateEdit()
        form.addWidget(self.date_edit, 0, 1)

        # Fournisseur
        label_fournisseur = QLabel("Fournisseur:")
        form.addWidget(label_fournisseur, 1, 0)
        self.fournisseur_entry = QLineEdit()
        form.addWidget(self.fournisseur_entry, 1, 1)

        # Montant
        label_montant = QLabel("Montant:")
        form.addWidget(label_montant, 2, 0)
        self.montant_entry = QLineEdit()
        form.addWidget(self.montant_entry, 2, 1)

        layout.addLayout(form)

        # Boutons
        buttons = QHBoxLayout()
        btn_cancel = QPushButton("Annuler")
        btn_cancel.clicked.connect(self.reject)
        btn_ok = QPushButton("Créer")
        btn_ok.clicked.connect(self.accept)
        buttons.addWidget(btn_cancel)
        buttons.addWidget(btn_ok)

        layout.addLayout(buttons)
        self.setLayout(layout)
```

### Dialog Achat (Après)

```python
from PySide6.QtWidgets import QDateEdit
from gesco_modern_ui import (
    ResponsiveDialog,
    ModernInput,
    DesignSystem
)

class AchatDialog(ResponsiveDialog):
    def __init__(self, gestion, parent=None):
        super().__init__("Nouvel Achat", parent)

        self.gestion = gestion

        # Section principale
        section = self.add_form_section("Informations de l'achat")

        # Date
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setMinimumHeight(DesignSystem.INPUT_HEIGHT)
        # Appliquer un style moderne au QDateEdit si nécessaire
        self.add_form_field(section, "Date", self.date_edit, required=True)

        # Fournisseur
        self.fournisseur_input = ModernInput(placeholder="Nom du fournisseur")
        self.add_form_field(section, "Fournisseur", self.fournisseur_input, required=True)

        # Montant
        self.montant_input = ModernInput(placeholder="0.00")
        self.add_form_field(
            section,
            "Montant (€)",
            self.montant_input,
            required=True,
            help_text="Montant TTC de l'achat"
        )

        # Stretch
        self.content_layout.addStretch()

        # Boutons
        self.add_button_bar([
            ("Annuler", "secondary", self.reject),
            ("Créer l'achat", "success", self.accept)
        ])
```

---

## 🧪 9. Tester la migration

Pour tester vos dialogues migrés :

```bash
# Lancer la démo
python demo_modern_ui.py
```

Testez :
1. ✅ Redimensionnement de la fenêtre
2. ✅ Scroll vertical quand beaucoup de champs
3. ✅ Tous les champs restent visibles
4. ✅ Style cohérent macOS
5. ✅ Boutons fonctionnels

---

## 💡 10. Conseils et bonnes pratiques

1. **Toujours utiliser `add_form_section()`** pour organiser vos champs
2. **Grouper logiquement** les champs par section
3. **Utiliser `required=True`** pour les champs obligatoires
4. **Ajouter `help_text`** pour guider l'utilisateur
5. **Toujours ajouter `addStretch()`** avant la barre de boutons
6. **Utiliser les variantes de boutons** :
   - `primary` pour l'action principale
   - `secondary` pour annuler
   - `success` pour créer/enregistrer
   - `danger` pour supprimer

---

## 🆘 Support

En cas de problème lors de la migration :

1. Vérifiez que tous les imports sont corrects
2. Assurez-vous d'hériter de `ResponsiveDialog`
3. Consultez `demo_modern_ui.py` pour des exemples
4. Testez chaque dialog individuellement

---

## 📚 Ressources

- `gesco_modern_ui.py` - Module principal avec tous les composants
- `demo_modern_ui.py` - Exemples interactifs
- `MIGRATION_GUIDE.md` - Ce guide

Bonne migration ! 🚀
