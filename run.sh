#!/bin/bash
# Script de démarrage GESCO

echo "🚀 Démarrage de GESCO v4.8.0..."
echo ""

# Vérifier si l'environnement virtuel existe
if [ ! -d "venv" ]; then
    echo "⚠️  Environnement virtuel non trouvé."
    echo "   Création de l'environnement virtuel..."
    python3 -m venv venv
    echo "✅ Environnement virtuel créé."
    echo ""
fi

# Activer l'environnement virtuel
echo "🔧 Activation de l'environnement virtuel..."
source venv/bin/activate

# Vérifier si les dépendances sont installées
if ! python -c "import PySide6" 2>/dev/null; then
    echo "📦 Installation des dépendances..."
    pip install -r requirements.txt
    echo "✅ Dépendances installées."
    echo ""
fi

# Créer les dossiers de données s'ils n'existent pas
mkdir -p data config

# Lancer l'application
echo "▶️  Lancement de GESCO..."
echo ""
python gesco_v4_8_0_MODULE_CHANTIER_FINAL.py
