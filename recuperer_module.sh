#!/bin/bash
# Script pour récupérer le Module Chantier sur votre PC local

echo "🏗️  GESCO - Récupération du Module Chantier"
echo "=========================================="
echo ""

# Vérifier si on est dans un dépôt git
if [ ! -d ".git" ]; then
    echo "❌ Erreur: Vous n'êtes pas dans un dépôt Git"
    echo ""
    echo "Exécutez d'abord :"
    echo "  git clone https://github.com/Rich60500/GESCO.git"
    echo "  cd GESCO"
    echo "  ./recuperer_module.sh"
    exit 1
fi

echo "📥 Récupération des dernières modifications..."
git fetch origin

echo ""
echo "🔄 Basculement sur la branche du module..."
git checkout claude/getting-started-011CUe2LkzfAsTYAvr1744aw

echo ""
echo "⬇️  Téléchargement des fichiers..."
git pull origin claude/getting-started-011CUe2LkzfAsTYAvr1744aw

echo ""
echo "✅ Vérification des fichiers..."
echo ""

if [ -f "module_chantier_complet.py" ]; then
    echo "✅ module_chantier_complet.py ($(du -h module_chantier_complet.py | cut -f1))"
else
    echo "❌ module_chantier_complet.py MANQUANT"
fi

if [ -f "gesco_modern_ui.py" ]; then
    echo "✅ gesco_modern_ui.py ($(du -h gesco_modern_ui.py | cut -f1))"
else
    echo "❌ gesco_modern_ui.py MANQUANT"
fi

if [ -f "MODULE_CHANTIER_GUIDE.md" ]; then
    echo "✅ MODULE_CHANTIER_GUIDE.md ($(du -h MODULE_CHANTIER_GUIDE.md | cut -f1))"
else
    echo "❌ MODULE_CHANTIER_GUIDE.md MANQUANT"
fi

echo ""
echo "=========================================="
echo "🎉 Récupération terminée !"
echo ""
echo "Pour lancer le module :"
echo "  pip install -r requirements.txt"
echo "  python module_chantier_complet.py"
echo ""
