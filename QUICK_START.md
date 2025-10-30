# 🚀 GESCO v5.0 - Démarrage Rapide

## En 3 minutes chrono ⏱️

### 1️⃣ Clonez et installez (1 minute)

```bash
git clone https://github.com/Rich60500/GESCO.git
cd GESCO
pip install -r requirements.txt
```

### 2️⃣ Testez la démo (30 secondes)

```bash
python demo_modern_ui.py
```

Une fenêtre s'ouvre avec 3 boutons pour tester les dialogues modernes !

### 3️⃣ Testez le responsive (1 minute)

1. Cliquez sur **"Ouvrir Dialog Complexe"**
2. **Redimensionnez** la fenêtre (petite, moyenne, grande)
3. Observez le **scroll automatique** quand vous réduisez
4. Tous les champs restent **toujours visibles** ✨

---

## 📱 Ce que vous allez voir

✅ Design macOS Sonoma/Sequoia moderne
✅ Interface 100% responsive
✅ Scroll automatique si besoin
✅ Champs toujours accessibles
✅ Composants élégants (inputs, boutons, cartes)

---

## 📚 Documentation

- **COMMENT_TESTER.md** : Guide complet de test
- **MIGRATION_GUIDE.md** : Migrer de v4.8 à v5.0
- **docs/MODERN_UI_GUIDE.md** : Documentation complète
- **docs/NEW_UI_README.md** : Introduction détaillée

---

## 💡 Créer votre premier dialogue

```python
from gesco_modern_ui import ResponsiveDialog, ModernInput

class MonDialog(ResponsiveDialog):
    def __init__(self, parent=None):
        super().__init__("Mon Dialog", parent)

        section = self.add_form_section("Informations")

        self.nom = ModernInput(placeholder="Nom")
        self.add_form_field(section, "Nom", self.nom, required=True)

        self.content_layout.addStretch()
        self.add_button_bar([
            ("Annuler", "secondary", self.reject),
            ("Valider", "primary", self.accept)
        ])

# Utiliser
dialog = MonDialog()
dialog.exec()
```

**C'est tout !** Dialog moderne, responsive, avec scroll automatique 🎉

---

## ⚡ TL;DR

```bash
# Installation
pip install -r requirements.txt

# Test
python demo_modern_ui.py

# Documentation
cat MIGRATION_GUIDE.md
```

**Interface moderne en 3 commandes !**

---

**Need help?** → Voir `COMMENT_TESTER.md`
