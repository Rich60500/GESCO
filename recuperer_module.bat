@echo off
REM Script Windows pour récupérer le Module Chantier

echo =========================================
echo 🏗️  GESCO - Récupération du Module Chantier
echo =========================================
echo.

REM Vérifier si on est dans un dépôt git
if not exist ".git\" (
    echo ❌ Erreur: Vous n'êtes pas dans un dépôt Git
    echo.
    echo Exécutez d'abord :
    echo   git clone https://github.com/Rich60500/GESCO.git
    echo   cd GESCO
    echo   recuperer_module.bat
    pause
    exit /b 1
)

echo 📥 Récupération des dernières modifications...
git fetch origin

echo.
echo 🔄 Basculement sur la branche du module...
git checkout claude/getting-started-011CUe2LkzfAsTYAvr1744aw

echo.
echo ⬇️  Téléchargement des fichiers...
git pull origin claude/getting-started-011CUe2LkzfAsTYAvr1744aw

echo.
echo ✅ Vérification des fichiers...
echo.

if exist "module_chantier_complet.py" (
    echo ✅ module_chantier_complet.py présent
) else (
    echo ❌ module_chantier_complet.py MANQUANT
)

if exist "gesco_modern_ui.py" (
    echo ✅ gesco_modern_ui.py présent
) else (
    echo ❌ gesco_modern_ui.py MANQUANT
)

if exist "MODULE_CHANTIER_GUIDE.md" (
    echo ✅ MODULE_CHANTIER_GUIDE.md présent
) else (
    echo ❌ MODULE_CHANTIER_GUIDE.md MANQUANT
)

echo.
echo =========================================
echo 🎉 Récupération terminée !
echo.
echo Pour lancer le module :
echo   pip install -r requirements.txt
echo   python module_chantier_complet.py
echo.
pause
