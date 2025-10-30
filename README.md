# GESCO - Gestion de Chantiers v4.8.0

Application de gestion complète pour les chantiers de construction, développée en Python avec PySide6.

## 📋 Fonctionnalités principales

### Module Chantier (v4.8.0)
- Interface à deux volets : liste des chantiers + détails
- Recherche et filtrage des chantiers
- Indicateurs de suivi en temps réel :
  - Jours ouvrés estimés vs. réels
  - Budget chiffré vs. factures
  - Achats estimés vs. réalisés
- Barres de progression colorées
- Alertes de dépassement

### Autres modules
- **Achats** : Gestion des achats et approvisionnements
- **Main d'œuvre** : Suivi des heures et coûts par technicien
- **Tiers** : Gestion des contacts clients et fournisseurs
- **Factures** : Intégration avec l'API Axonaut
- **Archives** : Accès aux chantiers clôturés
- **Paramètres** : Configuration et gestion des techniciens

## 🚀 Installation

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. **Cloner le dépôt**
```bash
git clone https://github.com/Rich60500/GESCO.git
cd GESCO
```

2. **Créer un environnement virtuel** (recommandé)
```bash
python -m venv venv
```

3. **Activer l'environnement virtuel**
   - Windows :
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux :
     ```bash
     source venv/bin/activate
     ```

4. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

## ▶️ Démarrage

### Lancer l'application
```bash
python gesco_v4_8_0_MODULE_CHANTIER_FINAL.py
```

## 📁 Structure du projet

```
GESCO/
├── gesco_v4_8_0_MODULE_CHANTIER_FINAL.py  # Application principale
├── requirements.txt                        # Dépendances Python
├── data/                                   # Données de l'application (fichiers .pkl)
├── config/                                 # Configuration (API Axonaut, etc.)
├── docs/                                   # Documentation
└── README.md                               # Ce fichier
```

## 🔧 Configuration

### API Axonaut
Pour utiliser l'intégration de facturation Axonaut :
1. Créez un fichier `config/config.json`
2. Ajoutez vos identifiants API :
```json
{
  "axonaut": {
    "api_key": "votre_clé_api",
    "user_id": "votre_user_id"
  }
}
```

## 💾 Données

L'application stocke ses données dans des fichiers pickle (`.pkl`) dans le dossier `data/` :
- `chantiers.pkl` : Liste des chantiers
- `achats.pkl` : Achats et approvisionnements
- `heures.pkl` : Heures de main d'œuvre
- `contacts.pkl` : Contacts tiers
- `techniciens.pkl` : Liste des techniciens

## 🎨 Interface

Interface moderne avec design macOS :
- Fond gris doux
- Coins arrondis
- Couleurs pastel (#007AFF bleu, #34C759 vert, #FF3B30 rouge)
- Menu latéral avec icônes SVG personnalisées
- Tableaux interactifs avec tri et redimensionnement

## 📝 Version

**Version actuelle : 4.8.0**

Voir l'en-tête du fichier principal pour l'historique complet des versions.

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir une issue ou une pull request.

## 📄 Licence

Voir le fichier LICENSE pour plus de détails.