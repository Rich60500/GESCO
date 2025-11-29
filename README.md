# GESCO v5.0 - Gestion de Chantiers

⚡️ Application moderne de gestion de chantiers avec interface macOS Sonoma/Sequoia

## 🎯 Version Actuelle : Étape 2 - Achats & Sonepar

### Étape 1 : Fondations ✅
- ✅ Application principale avec menu moderne et sidebar
- ✅ Module Chantiers complet avec CRUD
- ✅ Base de données SQLite pour la persistance
- ✅ Design System moderne inspiré de macOS
- ✅ Interface responsive avec tous les champs toujours visibles

### Étape 2 : Achats & Intégration Sonepar ✅
- ✅ Module Achats complet avec interface à onglets
- ✅ Intégration complète de l'API Sonepar (fournisseur électrique)
- ✅ Recherche de produits dans le catalogue Sonepar
- ✅ Consultation des prix et stocks en temps réel
- ✅ Création de commandes liées aux chantiers
- ✅ Historique des commandes par chantier
- ✅ Rate limiting automatique pour respecter les limites API
- ✅ Gestion des bons de livraison

## 🚀 Démarrage Rapide

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Installation

1. **Cloner le dépôt**
```bash
git clone https://github.com/Rich60500/GESCO.git
cd GESCO
```

2. **Créer un environnement virtuel (recommandé)**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

### Lancer l'application

```bash
python src/main.py
```

## 📁 Structure du Projet

```
GESCO/
├── src/
│   ├── main.py                      # Application principale
│   ├── design_system.py             # Système de design moderne
│   ├── database.py                  # Gestionnaire SQLite
│   ├── modules/
│   │   ├── chantiers.py             # Module Chantiers
│   │   └── achats.py                # Module Achats
│   └── integrations/
│       └── sonepar/
│           ├── sonepar_models.py    # Modèles de données Sonepar
│           ├── sonepar_config.py    # Configuration API
│           ├── sonepar_client.py    # Client HTTP avec rate limiting
│           └── sonepar_database.py  # Liaison chantiers/commandes
├── data/                            # Base de données SQLite (créé automatiquement)
├── config/                          # Configuration (future)
├── requirements.txt                 # Dépendances Python
└── README.md
```

## ✨ Fonctionnalités du Module Chantiers

### Interface en 2 panneaux

- **Panneau gauche** : Liste de tous les chantiers
  - Affichage : Nom, N° Commande, Client, Date d'ouverture
  - Recherche en temps réel
  - Tri automatique (chantiers clôturés en fin de liste)
  - Indicateur coloré selon l'état

- **Panneau droit** : Détails du chantier sélectionné
  - Informations complètes
  - Changement d'état direct via ComboBox
  - Calcul automatique de l'écart budgétaire

### Gestion complète (CRUD)

- **Créer** un nouveau chantier
- **Lire** les détails d'un chantier
- **Modifier** un chantier existant
- **Supprimer** un chantier

### États des chantiers

- 🔵 **Accepté** - Nouveau chantier accepté
- 🟠 **En cours** - Travaux en cours
- 🟢 **Terminé** - Travaux terminés
- 🟣 **Facturé** - Facture émise
- ⚫ **Clôturé** - Chantier archivé (en fin de liste)

### Données gérées

- Nom du chantier
- Numéro de commande
- Client
- Adresse complète (adresse, code postal, ville)
- Contact (téléphone, email)
- Dates (ouverture, clôture)
- Budget (prévisionnel, réel, écart calculé)
- Notes et remarques

## 🛒 Fonctionnalités du Module Achats

### Intégration Sonepar API

Le module Achats s'intègre avec l'API Sonepar (fournisseur électrique) pour gérer les achats de matériel électrique directement liés aux chantiers.

**Identifiants API** :
- Client : DENIS EURL (API Key: 95791076)
- Code client : 4146EB1
- Organisation : 5QD
- Environnements : Test & Production

### Interface à 3 onglets

#### 1. 🔍 Catalogue Sonepar
- **Recherche de produits** : Par référence, EAN ou description
- **Affichage des résultats** :
  - Référence produit
  - Description complète
  - Marque
  - Code EAN
  - Conditionnement et unité
- **Consultation prix & stock** :
  - Prix net et brut
  - Taux de remise
  - Stock disponible
  - Type de stock (disponible, réservé, en commande)
  - Emplacement

#### 2. 📦 Commandes
- **Création de commandes** :
  - Sélection du chantier
  - Type de commande (Standard, Express, Dépôt)
  - Ajout de lignes de commande (référence + quantité)
  - Adresse de livraison optionnelle
  - Notes
- **Liste des commandes** :
  - Filtrage par chantier
  - Affichage : N° commande, Date, Chantier, Montant, Statut
  - Statuts colorés selon l'état
- **Liaison automatique** : Chaque commande est liée à un chantier GESCO

#### 3. 🚚 Livraisons
- **Suivi des bons de livraison**
- **Historique des livraisons par chantier**
- **Informations transporteur et tracking**

### Rate Limiting Automatique

Le client API respecte automatiquement les limites d'appels :
- **Général** : 10 appels par minute
- **Catalogue** : 5 appels par seconde
- **Retry automatique** : En cas d'échec avec backoff exponentiel (max 3 tentatives)

### Base de Données Intégrée

**Tables Sonepar** :
- `chantier_orders` : Commandes liées aux chantiers
- `chantier_products` : Produits commandés par chantier
- `chantier_delivery_notes` : Bons de livraison

**Fonctionnalités** :
- Statistiques d'achats par chantier
- Recherche de produits commandés
- Historique complet des commandes
- Liaison commandes ↔ chantiers ↔ livraisons

### Modèles de Données

Le système utilise des dataclasses Python pour une gestion typée :
- `Brand` : Marques de produits
- `Product` : Produits du catalogue
- `ProductWithPricing` : Produit avec prix et stock
- `Order` : Commandes avec lignes
- `OrderLine` : Ligne de commande individuelle
- `DeliveryNote` : Bon de livraison
- Enums : `ProductStatus`, `OrderType`, `StockType`, `OrderStatus`

## 🎨 Design System

Le design s'inspire de macOS Sonoma/Sequoia :

- **Typographie** : SF Pro Text
- **Couleurs** : Palette Apple (#007AFF, #34C759, #FF3B30, etc.)
- **Espacement** : Système 4pt
- **Coins arrondis** : 8-16px
- **Ombres subtiles** : Style Apple
- **Interface fluide** : Animations douces

## 🗄️ Base de Données

### SQLite

Les données sont stockées dans `data/gesco.db` (créé automatiquement).

**Table chantiers** :
- Informations générales (nom, client, n° commande)
- Localisation (adresse, CP, ville)
- Contact (téléphone, email)
- Dates (ouverture, clôture)
- État et budgets
- Métadonnées (created_at, updated_at)

**Index** pour performances :
- État
- Client
- Numéro de commande

## 🔄 Responsive Design

- Interface adaptative avec `QScrollArea`
- Tous les champs toujours visibles
- Défilement automatique si nécessaire
- Dialogues responsive pour tous les écrans

## 🛠️ Technologies

- **PySide6** : Framework Qt pour Python
- **SQLite** : Base de données légère et performante
- **Python 3.8+** : Langage moderne et efficace

## 📝 Modules à Venir

Les modules suivants seront développés dans les prochaines étapes :

- 🛒 **Achats** : Gestion des achats et integration Sonepar API
- 👷 **Main d'œuvre** : Gestion du personnel et des heures
- 👥 **Tiers** : Gestion des clients et fournisseurs
- 💰 **Factures** : Facturation et comptabilité
- 📦 **Archives** : Consultation des données historiques
- ⚙️ **Paramètres** : Configuration de l'application

## 🐛 Signaler un Problème

Ouvrez une issue sur GitHub : https://github.com/Rich60500/GESCO/issues

## 📜 Licence

Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

**Version actuelle** : v5.0 - Étape 1 (Fondations)
**Dernière mise à jour** : 2025-11-26
