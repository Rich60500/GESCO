@echo off
REM Script de démarrage GESCO pour Windows

echo 🚀 Démarrage de GESCO v4.8.0...
echo.

REM Vérifier si l'environnement virtuel existe
if not exist "venv\" (
    echo ⚠️  Environnement virtuel non trouvé.
    echo    Création de l'environnement virtuel...
    python -m venv venv
    echo ✅ Environnement virtuel créé.
    echo.
)

REM Activer l'environnement virtuel
echo 🔧 Activation de l'environnement virtuel...
call venv\Scripts\activate.bat

REM Vérifier si les dépendances sont installées
python -c "import PySide6" 2>nul
if errorlevel 1 (
    echo 📦 Installation des dépendances...
    pip install -r requirements.txt
    echo ✅ Dépendances installées.
    echo.
)

REM Créer les dossiers de données s'ils n'existent pas
if not exist "data\" mkdir data
if not exist "config\" mkdir config

REM Lancer l'application
echo ▶️  Lancement de GESCO...
echo.
python gesco_v4_8_0_MODULE_CHANTIER_FINAL.py

pause
