#!/usr/bin/env python3
"""
Script de test pour l'interface moderne GESCO v5.0
Ce script vérifie que tous les composants sont correctement importés
"""

import sys
print("🔍 Test de l'interface moderne GESCO v5.0\n")

# Test 1: Import du module principal
print("1. Test import du module gesco_modern_ui...")
try:
    from gesco_modern_ui import (
        DesignSystem,
        ModernLabel,
        ModernInput,
        ModernComboBox,
        ModernTextEdit,
        ModernButton,
        ModernCard,
        ResponsiveDialog,
        ModernChantierDialog
    )
    print("   ✅ Tous les composants importés avec succès\n")
except ImportError as e:
    print(f"   ❌ Erreur d'import: {e}\n")
    sys.exit(1)

# Test 2: Vérifier les constantes du Design System
print("2. Test du Design System...")
print(f"   - Couleur de fond: {DesignSystem.BACKGROUND}")
print(f"   - Couleur accent: {DesignSystem.ACCENT_BLUE}")
print(f"   - Taille de police: {DesignSystem.FONT_SIZE_BODY}px")
print(f"   - Espacement moyen: {DesignSystem.SPACING_MD}px")
print(f"   - Rayon des bordures: {DesignSystem.RADIUS_SM}px")
print("   ✅ Design System opérationnel\n")

# Test 3: Créer des composants (sans affichage)
print("3. Test création des composants...")
try:
    label = ModernLabel("Test Label")
    input_field = ModernInput(placeholder="Test")
    combo = ModernComboBox()
    text = ModernTextEdit()
    btn_primary = ModernButton("Test", "primary")
    btn_secondary = ModernButton("Test", "secondary")
    btn_success = ModernButton("Test", "success")
    btn_danger = ModernButton("Test", "danger")
    card = ModernCard()
    print("   ✅ Tous les composants créés avec succès\n")
except Exception as e:
    print(f"   ❌ Erreur de création: {e}\n")
    sys.exit(1)

# Test 4: Vérifier la démo
print("4. Test import de la démonstration...")
try:
    import demo_modern_ui
    print("   ✅ Module de démonstration importé\n")
except ImportError as e:
    print(f"   ❌ Erreur: {e}\n")
    sys.exit(1)

# Résumé
print("=" * 60)
print("✅ TOUS LES TESTS SONT PASSÉS !")
print("=" * 60)
print()
print("📋 Composants disponibles:")
print("   • ModernLabel (normal, bold, secondary)")
print("   • ModernInput (champs de saisie)")
print("   • ModernComboBox (listes déroulantes)")
print("   • ModernTextEdit (zones de texte)")
print("   • ModernButton (4 variantes)")
print("   • ModernCard (cartes conteneur)")
print("   • ResponsiveDialog (dialogues adaptatifs)")
print()
print("🚀 Pour lancer la démonstration graphique:")
print("   python demo_modern_ui.py")
print()
print("📚 Documentation:")
print("   - docs/NEW_UI_README.md : Introduction")
print("   - MIGRATION_GUIDE.md : Guide de migration")
print("   - docs/MODERN_UI_GUIDE.md : Guide complet")
print()
