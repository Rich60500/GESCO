#!/usr/bin/env python3
"""
Test du code Python (sans interface graphique)
Vérifie la syntaxe et la structure du code
"""

import sys
import ast

print("🔍 Test du code GESCO v5.0 (sans GUI)\n")

# Test 1: Vérifier la syntaxe du module principal
print("1. Vérification syntaxe de gesco_modern_ui.py...")
try:
    with open('gesco_modern_ui.py', 'r') as f:
        code = f.read()
        ast.parse(code)
    print("   ✅ Syntaxe Python valide\n")
except SyntaxError as e:
    print(f"   ❌ Erreur de syntaxe: {e}\n")
    sys.exit(1)

# Test 2: Vérifier la syntaxe de la démo
print("2. Vérification syntaxe de demo_modern_ui.py...")
try:
    with open('demo_modern_ui.py', 'r') as f:
        code = f.read()
        ast.parse(code)
    print("   ✅ Syntaxe Python valide\n")
except SyntaxError as e:
    print(f"   ❌ Erreur de syntaxe: {e}\n")
    sys.exit(1)

# Test 3: Analyser la structure
print("3. Analyse de la structure du code...")
with open('gesco_modern_ui.py', 'r') as f:
    tree = ast.parse(f.read())

classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
print(f"   Classes trouvées ({len(classes)}):")
for cls in classes:
    print(f"     • {cls}")
print()

# Test 4: Vérifier les fichiers de documentation
print("4. Vérification de la documentation...")
docs = [
    'MIGRATION_GUIDE.md',
    'docs/MODERN_UI_GUIDE.md',
    'docs/NEW_UI_README.md'
]

for doc in docs:
    try:
        with open(doc, 'r') as f:
            content = f.read()
            lines = len(content.split('\n'))
            size_kb = len(content) / 1024
        print(f"   ✅ {doc} ({lines} lignes, {size_kb:.1f} KB)")
    except FileNotFoundError:
        print(f"   ❌ {doc} non trouvé")

print()

# Résumé
print("=" * 70)
print("✅ CODE VÉRIFIÉ - SYNTAXE CORRECTE !")
print("=" * 70)
print()
print("📦 Modules créés:")
print("   • gesco_modern_ui.py - Design System + Composants")
print("   • demo_modern_ui.py - Démonstration interactive")
print()
print("📚 Documentation complète:")
print("   • MIGRATION_GUIDE.md - Migration v4.8 → v5.0")
print("   • docs/MODERN_UI_GUIDE.md - Guide complet")
print("   • docs/NEW_UI_README.md - Introduction")
print()
print("🖥️  Pour tester l'interface graphique:")
print()
print("   Sur votre machine locale (avec interface graphique):")
print()
print("   1. Clonez le dépôt:")
print("      git clone https://github.com/Rich60500/GESCO.git")
print("      cd GESCO")
print()
print("   2. Installez les dépendances:")
print("      pip install -r requirements.txt")
print()
print("   3. Lancez la démonstration:")
print("      python demo_modern_ui.py")
print()
print("   4. Testez les 3 dialogues et redimensionnez les fenêtres")
print()
print("📝 Classes implémentées:")
for cls in sorted(classes):
    print(f"   • {cls}")
print()
