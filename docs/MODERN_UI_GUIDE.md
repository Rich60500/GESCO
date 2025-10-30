# Guide de l'Interface Moderne GESCO v5.0

## 🎨 Design System macOS Sonoma/Sequoia

### Vue d'ensemble

L'interface moderne de GESCO v5.0 s'inspire du design macOS Sonoma/Sequoia pour offrir une expérience utilisateur fluide, claire et professionnelle.

---

## ✨ Caractéristiques principales

### 1. Design 100% Responsive

Tous les dialogues s'adaptent automatiquement à la taille de l'écran :

- **Taille minimale** : 500x400 pixels
- **Taille par défaut** : 650x600 pixels
- **Redimensionnement** : Libre, avec scroll automatique
- **Adaptation** : Tous les éléments restent accessibles

### 2. Scroll Automatique avec QScrollArea

- Scroll vertical et horizontal selon les besoins
- Scrollbars style macOS (fines, transparentes, apparaissent au survol)
- Tous les champs toujours visibles, même sur petits écrans
- Pas de contenu coupé ou masqué

### 3. Typographie SF Pro

Polices utilisées :
- **Principale** : SF Pro Text
- **Alternative** : Helvetica Neue
- **Fallback** : Segoe UI, sans-serif

Tailles :
- **Petit texte** : 11px (labels secondaires)
- **Corps** : 13px (texte normal)
- **Titre** : 16px (titres de section)
- **Grand titre** : 22px (titre principal)

### 4. Palette de couleurs

#### Couleurs principales
```
Background:      #F5F5F7  (Gris clair Apple)
Surface:         #FFFFFF  (Blanc pur)
Surface Alt:     #FAFAFA  (Blanc cassé)
```

#### Texte
```
Primary:         #1D1D1F  (Noir Apple)
Secondary:       #86868B  (Gris moyen)
Tertiary:        #C7C7CC  (Gris clair)
```

#### Accents
```
Bleu (Primary):  #007AFF  (Bleu Apple)
Vert (Success):  #34C759  (Vert Apple)
Rouge (Danger):  #FF3B30  (Rouge Apple)
Orange:          #FF9500  (Orange Apple)
```

#### Bordures
```
Light:           rgba(0, 0, 0, 0.06)
Medium:          rgba(0, 0, 0, 0.12)
```

### 5. Espacements cohérents

```
XS:  4px   - Espacement très fin
SM:  8px   - Petit espacement
MD:  12px  - Espacement moyen
LG:  16px  - Grand espacement
XL:  24px  - Très grand espacement
XXL: 32px  - Espacement maximum
```

### 6. Bordures arrondies

```
SM: 8px   - Inputs, boutons
MD: 12px  - Éléments moyens
LG: 16px  - Cartes
```

---

## 🧩 Composants disponibles

### ModernLabel

Label avec style macOS moderne.

```python
# Label normal
label = ModernLabel("Mon texte")

# Label en gras
label_bold = ModernLabel("Texte important", bold=True)

# Label secondaire (gris)
label_secondary = ModernLabel("Texte secondaire", secondary=True)
```

**Propriétés :**
- Police SF Pro Text 13px
- Couleur automatique selon le type
- Pas de fond

### ModernInput

Champ de saisie style macOS.

```python
# Input simple
input = ModernInput()

# Input avec placeholder
input = ModernInput(placeholder="Saisir votre texte...")
```

**Propriétés :**
- Hauteur : 36px
- Bordure arrondie 8px
- Focus bleu Apple
- Selection bleu Apple
- Placeholder gris clair

### ModernComboBox

Liste déroulante style macOS.

```python
combo = ModernComboBox()
combo.addItems(["Option 1", "Option 2", "Option 3"])
```

**Propriétés :**
- Hauteur : 36px
- Flèche stylisée
- Menu déroulant arrondi
- Hover bleu clair
- Selection bleu Apple

### ModernTextEdit

Zone de texte multiligne.

```python
text = ModernTextEdit(placeholder="Vos notes...")
text.setMinimumHeight(120)
```

**Propriétés :**
- Bordure arrondie 8px
- Focus bleu Apple
- Scroll automatique
- Selection bleu Apple

### ModernButton

Bouton avec 4 variantes.

```python
# Bouton principal (bleu)
btn_primary = ModernButton("Valider", "primary")

# Bouton secondaire (gris)
btn_secondary = ModernButton("Annuler", "secondary")

# Bouton succès (vert)
btn_success = ModernButton("Créer", "success")

# Bouton danger (rouge)
btn_danger = ModernButton("Supprimer", "danger")
```

**Propriétés :**
- Hauteur : 36px
- Bordure arrondie 8px
- Curseur pointer
- Effet hover
- Effet pressed
- État disabled

### ModernCard

Carte conteneur avec style macOS.

```python
card = ModernCard()
layout = QVBoxLayout()
# ... ajouter du contenu
card.setLayout(layout)
```

**Propriétés :**
- Fond blanc
- Bordure fine grise
- Bordure arrondie 16px
- Ombre légère

---

## 📋 ResponsiveDialog

Classe de base pour tous les dialogues.

### Utilisation de base

```python
from gesco_modern_ui import ResponsiveDialog

class MonDialog(ResponsiveDialog):
    def __init__(self, parent=None):
        super().__init__("Titre du Dialog", parent)

        # Ajouter des sections
        section = self.add_form_section("Ma Section")

        # Ajouter des champs
        input = ModernInput()
        self.add_form_field(section, "Label", input)

        # Stretch
        self.content_layout.addStretch()

        # Boutons
        self.add_button_bar([
            ("Annuler", "secondary", self.reject),
            ("Valider", "primary", self.accept)
        ])
```

### Méthodes disponibles

#### `add_form_section(title=None)`

Ajoute une section de formulaire avec titre optionnel.

```python
section = self.add_form_section("Informations personnelles")
```

Retourne le layout de la carte où ajouter les champs.

#### `add_form_field(parent_layout, label_text, widget, required=False, help_text=None)`

Ajoute un champ avec label au layout.

```python
input = ModernInput(placeholder="Votre nom")
self.add_form_field(
    section,
    "Nom complet",
    input,
    required=True,
    help_text="Nom affiché sur les documents"
)
```

**Paramètres :**
- `parent_layout` : Layout parent (retourné par `add_form_section`)
- `label_text` : Texte du label
- `widget` : Widget de saisie
- `required` : Si True, ajoute un astérisque (*)
- `help_text` : Texte d'aide sous le champ (optionnel)

#### `add_button_bar(buttons)`

Ajoute une barre de boutons en bas du dialogue.

```python
self.add_button_bar([
    ("Réinitialiser", "danger", self.reset),
    ("Annuler", "secondary", self.reject),
    ("Enregistrer", "success", self.accept)
])
```

**Format :** Liste de tuples `(text, variant, callback)`

**Variantes :** `"primary"`, `"secondary"`, `"success"`, `"danger"`

---

## 📐 Layouts et espacement

### Bonnes pratiques

1. **Toujours utiliser les sections**
   ```python
   section = self.add_form_section("Titre de la section")
   ```

2. **Grouper les champs liés**
   ```python
   section1 = self.add_form_section("Informations de base")
   # ... champs de base

   section2 = self.add_form_section("Adresse")
   # ... champs d'adresse
   ```

3. **Ajouter un stretch avant les boutons**
   ```python
   self.content_layout.addStretch()
   self.add_button_bar([...])
   ```

4. **Utiliser les espacements du Design System**
   ```python
   from gesco_modern_ui import DesignSystem

   layout.setSpacing(DesignSystem.SPACING_MD)
   layout.setContentsMargins(
       DesignSystem.SPACING_XL,
       DesignSystem.SPACING_LG,
       DesignSystem.SPACING_XL,
       DesignSystem.SPACING_LG
   )
   ```

---

## 🎯 Exemples d'implémentation

### Dialog simple

```python
class SimpleDialog(ResponsiveDialog):
    def __init__(self, parent=None):
        super().__init__("Nouveau Contact", parent)

        section = self.add_form_section()

        self.nom_input = ModernInput(placeholder="Nom")
        self.add_form_field(section, "Nom", self.nom_input, required=True)

        self.email_input = ModernInput(placeholder="email@exemple.fr")
        self.add_form_field(section, "Email", self.email_input)

        self.content_layout.addStretch()

        self.add_button_bar([
            ("Annuler", "secondary", self.reject),
            ("Créer", "primary", self.accept)
        ])
```

### Dialog avec plusieurs sections

```python
class ComplexDialog(ResponsiveDialog):
    def __init__(self, parent=None):
        super().__init__("Informations Complètes", parent)

        # Section 1
        section1 = self.add_form_section("Identité")

        self.nom_input = ModernInput()
        self.add_form_field(section1, "Nom", self.nom_input, required=True)

        self.prenom_input = ModernInput()
        self.add_form_field(section1, "Prénom", self.prenom_input, required=True)

        # Section 2
        section2 = self.add_form_section("Contact")

        self.email_input = ModernInput(placeholder="email@exemple.fr")
        self.add_form_field(section2, "Email", self.email_input, required=True)

        self.tel_input = ModernInput(placeholder="+33 6 12 34 56 78")
        self.add_form_field(section2, "Téléphone", self.tel_input)

        # Section 3
        section3 = self.add_form_section("Commentaires")

        self.notes_text = ModernTextEdit()
        self.notes_text.setMinimumHeight(100)
        self.add_form_field(section3, "Notes", self.notes_text)

        self.content_layout.addStretch()

        self.add_button_bar([
            ("Annuler", "secondary", self.reject),
            ("Enregistrer", "success", self.accept)
        ])
```

### Dialog avec widgets complexes

```python
class AdvancedDialog(ResponsiveDialog):
    def __init__(self, parent=None):
        super().__init__("Configuration Avancée", parent)

        section = self.add_form_section("Paramètres")

        # ComboBox + bouton sur la même ligne
        client_container = QWidget()
        client_layout = QHBoxLayout()
        client_layout.setContentsMargins(0, 0, 0, 0)
        client_layout.setSpacing(DesignSystem.SPACING_SM)

        self.client_combo = ModernComboBox()
        client_layout.addWidget(self.client_combo)

        btn_new = ModernButton("Nouveau", "secondary")
        btn_new.setFixedWidth(100)
        client_layout.addWidget(btn_new)

        client_container.setLayout(client_layout)

        self.add_form_field(section, "Client", client_container, required=True)

        self.content_layout.addStretch()

        self.add_button_bar([
            ("Annuler", "secondary", self.reject),
            ("Valider", "primary", self.accept)
        ])
```

---

## 🔍 Responsive Design

### Comportements automatiques

1. **Taille minimale garantie**
   - Largeur min : 500px
   - Hauteur min : 400px

2. **Redimensionnement libre**
   - L'utilisateur peut agrandir/réduire
   - Les contraintes minimales sont respectées

3. **Scroll automatique**
   - Si contenu > taille fenêtre → scroll vertical
   - Tous les champs restent accessibles

4. **Adaptation des widgets**
   - Les inputs s'étendent horizontalement
   - Les labels gardent leur largeur
   - Les cartes s'adaptent

### Testez votre dialog

Pour vérifier le responsive :

1. Lancez votre dialog
2. Redimensionnez la fenêtre (petite, moyenne, grande)
3. Vérifiez que tous les champs sont visibles
4. Testez le scroll si nécessaire
5. Vérifiez l'espacement et l'alignement

---

## 🎨 Personnalisation

### Modifier les couleurs

```python
from gesco_modern_ui import DesignSystem

# Personnaliser une couleur
custom_blue = "#0066CC"

btn = ModernButton("Mon Bouton", "primary")
btn.setStyleSheet(f"""
    QPushButton {{
        background-color: {custom_blue};
        color: white;
        border-radius: {DesignSystem.RADIUS_SM}px;
    }}
""")
```

### Modifier les espacements

```python
# Utiliser les constantes
section_layout.setSpacing(DesignSystem.SPACING_LG)

# Ou personnaliser
custom_spacing = 20
section_layout.setSpacing(custom_spacing)
```

### Créer un nouveau composant

```python
from gesco_modern_ui import DesignSystem
from PySide6.QtWidgets import QWidget

class MonComposant(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Utiliser le Design System
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {DesignSystem.SURFACE};
                border: 1px solid {DesignSystem.BORDER_LIGHT};
                border-radius: {DesignSystem.RADIUS_MD}px;
                padding: {DesignSystem.SPACING_LG}px;
            }}
        """)
```

---

## 🚀 Performance

### Optimisations intégrées

1. **QScrollArea efficace**
   - Rendu uniquement de la partie visible
   - Pas de ralentissement avec beaucoup de champs

2. **Stylesheets optimisés**
   - Appliqués une seule fois
   - Pas de recalcul dynamique

3. **Layouts intelligents**
   - Redimensionnement rapide
   - Pas de flickering

---

## 📱 Accessibilité

1. **Champs requis marqués**
   - Astérisque (*) visible
   - Clarté pour l'utilisateur

2. **Textes d'aide**
   - Guidage contextuel
   - Améliore l'UX

3. **Contrastes respectés**
   - Texte noir sur fond clair
   - Lisibilité optimale

4. **Tailles de police**
   - 13px minimum pour le corps
   - Confortable pour la lecture

---

## 🐛 Débogage

### Problèmes courants

**Dialog trop petit**
```python
# Ajuster la taille par défaut
self.resize(700, 700)
```

**Scroll ne fonctionne pas**
```python
# Vérifier que vous héritez de ResponsiveDialog
class MonDialog(ResponsiveDialog):  # ✅
    ...

class MonDialog(QDialog):  # ❌ Pas de scroll automatique
    ...
```

**Champs mal alignés**
```python
# Utiliser add_form_field pour l'alignement automatique
self.add_form_field(section, "Label", widget)  # ✅

layout.addWidget(widget)  # ❌ Pas d'alignement automatique
```

**Boutons mal positionnés**
```python
# Toujours ajouter stretch avant les boutons
self.content_layout.addStretch()  # ✅
self.add_button_bar([...])
```

---

## 📚 Ressources

- **Module principal** : `gesco_modern_ui.py`
- **Démo interactive** : `demo_modern_ui.py`
- **Guide de migration** : `MIGRATION_GUIDE.md`
- **Ce guide** : `docs/MODERN_UI_GUIDE.md`

---

## 💡 Conseils finaux

1. Toujours hériter de `ResponsiveDialog`
2. Utiliser les composants modernes (ModernInput, ModernButton, etc.)
3. Organiser en sections logiques
4. Ajouter un stretch avant les boutons
5. Tester le redimensionnement
6. Utiliser les constantes du DesignSystem
7. Marquer les champs requis
8. Ajouter des textes d'aide quand nécessaire

---

**GESCO v5.0 - Interface Moderne Responsive** 🚀
