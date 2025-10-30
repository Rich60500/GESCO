"""
✅ v4.8.0 - NOUVEAU MODULE CHANTIER
- ✅ Nouveau module "Chantier" avec interface à deux volets:
  * Volet gauche: Liste des chantiers avec recherche
  * Volet droit: Détails du chantier sélectionné
- ✅ Informations principales affichées:
  * Nom du chantier
  * Numéro de commande
  * Date d'ouverture
- ✅ Indicateurs de suivi en temps réel:
  * Jours ouvrés estimés vs. réels (basé sur module Main d'œuvre)
  * Budget chiffré vs. factures (prêt pour intégration module Facture)
  * Achats estimés vs. réalisés (basé sur module Achats)
- ✅ Interface moderne avec cartes colorées et barres de progression
- ✅ Icône SVG dédiée dans le menu latéral

✅ v4.7.10 - AMÉLIORATIONS ERGONOMIQUES DES TABLEAUX
- ✅ Toutes les colonnes de tous les tableaux sont redimensionnables manuellement
  * Mode Interactive activé sur toutes les colonnes
  * L'utilisateur peut ajuster la largeur selon ses besoins
- ✅ Module "Mes Chantiers" - Colonne État améliorée:
  * ComboBox avec style intégré ressemblant à une cellule
  * Visuellement plus harmonieux et professionnel
  * Changement d'état plus naturel et intuitif
- ✅ Sélection de texte sans encadrement gris:
  * Suppression de l'outline gênant lors de la sélection
  * Apparence plus propre et moderne
  * Amélioration globale de l'expérience utilisateur

HÉRITE DE v4.7.9:
- ✅ Tous les tableaux de l'application:
  * Couleur de sélection uniforme vert pastel sur toute la ligne
  * Tri activé sur toutes les colonnes (clic sur en-têtes)
  * Tableaux parfaitement adaptés à leur conteneur
- ✅ Tableaux concernés:
  * Techniciens (Paramètres)
  * Tiers
  * Achats
  * Heures (Main d'œuvre)
  * Chantiers
  * Archives
  * Factures

HÉRITE DE v4.7.8:
- ✅ Colonnes redimensionnables dynamiquement (mode Interactive)
- ✅ Tri activé sur toutes les colonnes
- ✅ Couleur de sélection changée à vert clair pastel

HÉRITE DE v4.7.7:
- ✅ Menu latéral:
  * Suppression de l'animation de glissement (affichage/masquage instantané)
  * Bouton Paramètres : espacement amélioré pour meilleure visibilité
- ✅ Titre GESCO:
  * Police augmentée de 16 à 22 pour meilleur impact visuel

HÉRITE DE v4.7.6:
- ✅ Menu latéral optimisé:
  * Largeur réduite de 240px à 200px
  * Espacement icône-texte ajusté à 2px supplémentaires
- ✅ Gestion des Techniciens dans Paramètres:
  * Nouvelle section Techniciens avec tableau CRUD
  * Ajout, modification et suppression de techniciens
  * Coût horaire personnalisable par technicien
  * Intégration automatique dans le popup Main d'œuvre
- ✅ Colonne État dans tableau Chantiers:
  * ComboBox pour changement rapide d'état
  * États disponibles: Validé, En cours, Terminé, Clôturé, Archivé
  * Mise à jour automatique du statut et de la date
- ✅ Chantiers archivés:
  * Lignes grisées dans le tableau Archives
  * Accès uniquement via clic droit
  * Différenciation visuelle claire

HÉRITE DE v4.7.5:
- ✅ Menu latéral visuellement distinct:
  * Fond sombre en dégradé (#2C2C2E → #1C1C1E)
  * Bordure droite subtile
  * Texte blanc pour meilleur contraste
- ✅ Icônes SVG personnalisées:
  * Achats: Symbole Euro
  * Main d'œuvre: Casque de chantier
  * Mes Chantiers: Bâtiment
  * Archives: Dossier zip
  * Tiers: Client/Personne
  * Factures: Documents
  * Paramètres: Roue crantée
- ✅ Menu cachable/affichable:
  * Bouton toggle en haut à gauche du contenu
  * État préservé pendant la session
- ✅ Largeur menu: 240px pour accommoder les icônes

HÉRITE DE v4.7.3:
- ✅ Menu Pilotage supprimé complètement
- ✅ Module Heure: Interface harmonisée avec le module Chantier
  * Labels avec largeur fixe (160px) pour alignement parfait
  * Champs de saisie avec hauteur minimale (36px)
  * Espacements harmonisés (spacing 18, marges 25)
  * Taille de fenêtre optimisée (620x540)
  * Bouton "Modifier" avec icône crayon pour cohérence
- ✅ Puces ComboBox améliorées:
  * Flèches plus visibles et plus grandes
  * Couleur dynamique (#1D1D1F par défaut, #007AFF au survol)
  * Meilleur contraste dans toutes les fenêtres popup

HÉRITE DE v4.7.1:
- ✅ Nouveaux boutons avec icônes:
  * ✚ (Plus vert) pour tous les boutons "Ajouter/Créer"
  * ✎ (Crayon bleu) pour tous les boutons "Modifier"
  * ✕ (Croix rouge) pour tous les boutons "Supprimer"
- ✅ Tailles de fenêtres optimisées et rationalisées
- ✅ Champs de saisie agrandis (hauteur 36px minimum)
- ✅ Espacements harmonisés dans tous les dialogues
- ✅ Labels avec largeur fixe pour meilleur alignement
- ✅ Interface cohérente et professionnelle dans tous les modules

HÉRITE DE v4.7:
- ✅ Ajout du champ "Coût Estimé Main d'Œuvre" dans le formulaire chantier
- ✅ Boutons "+ Ajouter" et "✏️ Modifier" pour gérer les adresses de chantier
- ✅ Création d'adresse de chantier directement depuis le popup Nouveau/Modifier chantier
- ✅ Modification d'adresse de chantier avec mise à jour automatique des chantiers et contacts

HÉRITE DE v4.6:
- ✅ Menu latéral compact: 240px → 180px (-25% largeur, +60px pour contenu)
- ✅ Sauvegarde automatique position splitter (préserve réglages utilisateur)
- ✅ Boutons adresses harmonisés: "✏️ Modifier" et "🗑 Supprimer" avec texte
- ✅ Cohérence parfaite de l'interface dans tous les modules

HÉRITE DE v4.5:
- ✅ Module Factures: API fonctionnelle avec gestion de la clé API
- ✅ Module Tiers: Interface améliorée avec liste/détails et gestion des contacts
- ✅ Différenciation Particulier/Professionnel
- ✅ Gestion de l'adresse principale
- ✅ CRUD des contacts associés
- ✅ Affichage de l'adresse dans la liste des tiers
- ✅ Espacements améliorés entre liste et cartes
- ✅ Boutons harmonisés dans l'interface
- ✅ Création de tiers directement depuis le module Chantier
- ✅ Rafraîchissement automatique après création de tiers
- ✅ Gestion complète des adresses de chantier (CRUD)
- ✅ Cartes resserrées avec padding et marges optimisés
- ✅ Carte contact optimisée avec boutons alignés horizontalement
- ✅ Hauteur de la liste des tiers réduite
- ✅ Espaces entre cartes réduits de 15px à 8px
- ✅ Association des contacts aux adresses de chantiers
- ✅ Sélection multiple d'adresses lors de la création/modification de contacts
- ✅ Affichage des adresses associées dans les cartes de contacts
"""

import sys
import os
import pickle
import uuid
from datetime import datetime
import requests
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QGridLayout, QLabel, QPushButton, QLineEdit, QComboBox, QStackedWidget,
    QScrollArea, QFrame, QMessageBox, QTableWidget, QTableWidgetItem,
    QHeaderView, QRadioButton, QButtonGroup, QDialog,
    QDateEdit, QTextEdit, QMenu, QSplitter, QCheckBox
)
from PySide6.QtCore import Qt, QDate, QLocale, QThread, Signal, QByteArray, QSize, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QFont, QColor, QAction, QIcon, QPainter, QPixmap
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtSvg import QSvgRenderer
import pandas as pd


# ===== ICÔNES SVG =====
SVG_ICONS = {
    'achats': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M17.728 20.517c-3.488 0-5.613-2.461-6.443-5.517h6.715l.333-2h-7.398c-.059-.664-.064-1.335-.014-2h7.746l.333-2h-7.755c.786-3.106 2.855-5.626 6.154-5.626 1.133 0 2.391.203 3.836.62l.765-3.162c-1.854-.552-3.616-.832-5.244-.832-5.959 0-9.541 4.152-10.594 9h-2.162l-.333 2h2.203c-.049.666-.051 1.334-.007 2h-2.53l-.333 2h3.145c1.033 4.848 4.664 9 11.085 9 1.5 0 3.004-.276 4.476-.821l-.883-3.23c-1.048.378-2.088.568-3.095.568z"/></svg>''',
    'main_oeuvre': '''<svg width="24" height="24" xmlns="http://www.w3.org/2000/svg" fill-rule="evenodd" clip-rule="evenodd"><path d="M2.178 11h-1.178v-2.209c.468 0 .774-.474.944-.997.587-1.803 1.59-4.513 4.056-6.212v3.418c0 .552.448 1 1 1s1-.448 1-1v-4.437c.868-.309 1.861-.516 3-.585v3.022c0 .552.448 1 1 1s1-.448 1-1v-3c1.134.094 2.128.327 3 .661v4.339c0 .552.448 1 1 1s1-.448 1-1v-3.269c2.391 1.7 3.463 4.304 4.057 6.063.175.52.475.997.943.997v2.209h-1.179c.575.459 1.179 1.36 1.179 3.131 0 1.63-.904 3.686-2.877 4.531-2.153 3.445-5.027 5.338-8.123 5.338-3.096 0-5.97-1.893-8.124-5.338-1.973-.845-2.876-2.901-2.876-4.531 0-1.771.603-2.672 1.178-3.131zm12.022 7.459h-4.4c.004.012.626 1.74 2.2 1.74 1.634 0 2.196-1.728 2.2-1.74zm4.517-7.459h-13.435l-.013.515c0 .668-.682 1.114-1.288.844-.169-.075-.43-.073-.617.049-.917.601-.819 3.864 1.425 4.629.916.313 2.364 3.103 3.93.398.542-.934 2.251-1.039 3.281-.297 1.029-.742 2.739-.637 3.28.297 1.566 2.705 3.014-.085 3.93-.398 2.244-.765 2.342-4.028 1.425-4.629-.215-.14-.487-.106-.616-.049-.606.271-1.289-.176-1.289-.844l-.013-.515zm-9.696.996c-.634 0-1.146.62-1.146 1.385s.512 1.385 1.146 1.385c.632 0 1.146-.62 1.146-1.385s-.514-1.385-1.146-1.385zm7.104 1.385c0 .765-.513 1.385-1.146 1.385-.633 0-1.146-.62-1.146-1.385s.513-1.385 1.146-1.385c.633 0 1.146.62 1.146 1.385z"/></svg>''',
    'chantiers': '''<svg width="24" height="24" xmlns="http://www.w3.org/2000/svg" fill-rule="evenodd" clip-rule="evenodd"><path d="M24 24h-11v-6h4v-4h7v10zm-12-22h9l3 3v2h-3v2h3v3h-7v-3h3v-2h-8v17h-6v-17h-1v2h-5v-7h6v-2h6v2zm5 18h-2v2h2v-2zm5 0h-3v2h3v-2zm-12 .052l-2 .952v.996h2v-1.948zm-2-1.821v1.773l2-.952v-1.774l-2 .953zm14-2.231h-3v2h3v-2zm-14-.628v1.859l2-.953v-1.858l-2 .952zm0-2.785v1.785l2-.952v-1.785l-2 .952zm0-2.768v1.768l2-.952v-1.768l-2 .952zm2-2.819h-2v1.819l2-.952v-.867zm10.017-3h-18.017v3h1v-2h18l-.983-1zm-10.017-3h-2v1h2v-1z"/></svg>''',
    'chantier_module': '''<svg width="24" height="24" xmlns="http://www.w3.org/2000/svg" fill-rule="evenodd" clip-rule="evenodd"><path d="M24 24h-11v-6h4v-4h7v10zm-12-22h9l3 3v2h-3v2h3v3h-7v-3h3v-2h-8v17h-6v-17h-1v2h-5v-7h6v-2h6v2zm5 18h-2v2h2v-2zm5 0h-3v2h3v-2zm-12 .052l-2 .952v.996h2v-1.948zm-2-1.821v1.773l2-.952v-1.774l-2 .953zm14-2.231h-3v2h3v-2zm-14-.628v1.859l2-.953v-1.858l-2 .952zm0-2.785v1.785l2-.952v-1.785l-2 .952zm0-2.768v1.768l2-.952v-1.768l-2 .952zm2-2.819h-2v1.819l2-.952v-.867zm10.017-3h-18.017v3h1v-2h18l-.983-1zm-10.017-3h-2v1h2v-1z"/></svg>''',
    'archives': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M10.997 19.06c0 1.277-2.996 1.268-2.996.003 0-1.314 2.996-1.344 2.996-.003zm11.003-8.06v13h-20v-24h8.409c4.857 0 3.335 8 3.335 8 3.009-.745 8.256-.419 8.256 3zm-14-4h3v-1h-3v1zm0-2h3v-1h-3v1zm0-2h3v-1h-3v1zm0 6h3v-1h-3v1zm0 2h3v-1h-3v1zm0 2h3v-1h-3v1zm3.925 5.5l-.925-4.5h-3l-.925 4.5c-.393 1.578.801 2.5 2.425 2.5 1.626 0 2.817-.924 2.425-2.5zm3.984-12.723c2.047-.478 4.805.279 6.091 1.179-1.494-1.998-5.23-5.708-7.432-6.881 1.156 1.168 1.563 4.234 1.341 5.702z"/></svg>''',
    'tiers': '''<svg width="24" height="24" xmlns="http://www.w3.org/2000/svg" fill-rule="evenodd" clip-rule="evenodd"><path d="M7 16.488l1.526-.723c1.792-.81 2.851-.344 4.349.232 1.716.661 2.365.883 3.077 1.164 1.278.506.688 2.177-.592 1.838-.778-.206-2.812-.795-3.38-.931-.64-.154-.93.602-.323.818 1.106.393 2.663.79 3.494 1.007.831.218 1.295-.145 1.881-.611.906-.72 2.968-2.909 2.968-2.909.842-.799 1.991-.135 1.991.72 0 .23-.083.474-.276.707-2.328 2.793-3.06 3.642-4.568 5.226-.623.655-1.342.974-2.204.974-.442 0-.922-.084-1.443-.25-1.825-.581-4.172-1.313-6.5-1.6v-5.662zm-1 6.538h-4v-8h4v8zm1-7.869v-1.714c-.006-1.557.062-2.447 1.854-2.861 1.963-.453 4.315-.859 3.384-2.577-2.761-5.092-.787-7.979 2.177-7.979 2.907 0 4.93 2.78 2.177 7.979-.904 1.708 1.378 2.114 3.384 2.577 1.799.415 1.859 1.311 1.853 2.879 0 .13-.011 1.171 0 1.665-.483-.309-1.442-.552-2.187.106-.535.472-.568.504-1.783 1.629-1.75-.831-4.456-1.883-6.214-2.478-.896-.304-2.04-.308-2.962.075l-1.683.699z"/></svg>''',
    'factures': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M15.602 4.075c2.201 1.174 4.904 3.254 6.398 5.252-1.286-.9-3.011-1.027-5.058-.549.222-1.469-.185-3.535-1.34-4.703zm-.825 6.925s1.522-7-3.335-7h-5.442v20h16v-10.629c0-3.42-4.214-3.116-7.223-2.371zm-.318-8l-1.459-1h-9v20h1v-19h9.459zm-2.443-2l-1.5-1h-8.516v20h1v-19h9.016z"/></svg>''',
    'parametres': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M24 13.616v-3.232c-1.651-.587-2.694-.752-3.219-2.019v-.001c-.527-1.271.1-2.134.847-3.707l-2.285-2.285c-1.561.742-2.433 1.375-3.707.847h-.001c-1.269-.526-1.435-1.576-2.019-3.219h-3.232c-.582 1.635-.749 2.692-2.019 3.219h-.001c-1.271.528-2.132-.098-3.707-.847l-2.285 2.285c.745 1.568 1.375 2.434.847 3.707-.527 1.271-1.584 1.438-3.219 2.02v3.232c1.632.58 2.692.749 3.219 2.019.53 1.282-.114 2.166-.847 3.707l2.285 2.286c1.562-.743 2.434-1.375 3.707-.847h.001c1.27.526 1.436 1.579 2.019 3.219h3.232c.582-1.636.75-2.69 2.027-3.222h.001c1.262-.524 2.12.101 3.698.851l2.285-2.286c-.744-1.563-1.375-2.433-.848-3.706.527-1.271 1.588-1.44 3.221-2.021zm-12 2.384c-2.209 0-4-1.791-4-4s1.791-4 4-4 4 1.791 4 4-1.791 4-4 4z"/></svg>''',
    'menu_toggle': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M24 6h-24v-4h24v4zm0 4h-24v4h24v-4zm0 8h-24v4h24v-4z"/></svg>'''
}


# ===== HELPER POUR ICÔNES SVG =====
class SVGIconHelper:
    """Helper pour créer des icônes à partir de SVG"""
    
    @staticmethod
    def create_icon(svg_string, color="#FFFFFF", size=20):
        """Crée un QIcon à partir d'une chaîne SVG"""
        # Remplacer le fill pour la couleur
        if 'fill=' not in svg_string and '<path' in svg_string:
            svg_string = svg_string.replace('<path', f'<path fill="{color}"')
        elif 'fill=' in svg_string:
            svg_string = svg_string.replace('fill="#000000"', f'fill="{color}"')
            svg_string = svg_string.replace('fill="#000"', f'fill="{color}"')
            svg_string = svg_string.replace('fill="black"', f'fill="{color}"')
        
        # Créer le renderer
        renderer = QSvgRenderer(QByteArray(svg_string.encode()))
        
        # Créer un pixmap
        pixmap = QPixmap(size, size)
        pixmap.fill(Qt.GlobalColor.transparent)
        
        # Dessiner le SVG
        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()
        
        return QIcon(pixmap)
    
    @staticmethod
    def create_pixmap(svg_string, color="#FFFFFF", size=20):
        """Crée un QPixmap à partir d'une chaîne SVG"""
        # Remplacer le fill pour la couleur
        if 'fill=' not in svg_string and '<path' in svg_string:
            svg_string = svg_string.replace('<path', f'<path fill="{color}"')
        elif 'fill=' in svg_string:
            svg_string = svg_string.replace('fill="#000000"', f'fill="{color}"')
            svg_string = svg_string.replace('fill="#000"', f'fill="{color}"')
            svg_string = svg_string.replace('fill="black"', f'fill="{color}"')
        
        # Créer le renderer
        renderer = QSvgRenderer(QByteArray(svg_string.encode()))
        
        # Créer un pixmap
        pixmap = QPixmap(size, size)
        pixmap.fill(Qt.GlobalColor.transparent)
        
        # Dessiner le SVG
        painter = QPainter(pixmap)
        renderer.render(painter)
        painter.end()
        
        return pixmap


# ===== HELPER POUR STYLE macOS MODERNE =====
class ModernMacOSStyleHelper:
    """Helper pour appliquer un style macOS moderne (Sonoma/Sequoia)"""
    
    @staticmethod
    def get_main_stylesheet():
        """Retourne le stylesheet principal pour l'application"""
        return """
            QMainWindow {
                background-color: #F5F5F7;
            }
            QWidget {
                background-color: #F5F5F7;
                color: #1D1D1F;
                font-family: "SF Pro Text", "Helvetica Neue", "Segoe UI", sans-serif;
                font-size: 13px;
            }
            QLabel {
                color: #1D1D1F;
                background-color: transparent;
            }
            QLineEdit, QComboBox, QDateEdit, QTextEdit {
                background-color: rgba(255, 255, 255, 0.7);
                color: #1D1D1F;
                border: 1px solid rgba(0, 0, 0, 0.08);
                border-radius: 8px;
                padding: 6px 12px;
                min-height: 28px;
                selection-background-color: #007AFF;
            }
            QLineEdit:focus, QComboBox:focus, QDateEdit:focus, QTextEdit:focus {
                border: 2px solid #007AFF;
                outline: none;
                background-color: rgba(255, 255, 255, 0.9);
            }
            QComboBox::drop-down {
                border: none;
                padding-right: 12px;
                width: 30px;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 6px solid transparent;
                border-right: 6px solid transparent;
                border-top: 8px solid #1D1D1F;
                margin-right: 8px;
            }
            QComboBox::down-arrow:hover {
                border-top-color: #007AFF;
            }
            QTableWidget {
                background-color: rgba(255, 255, 255, 0.6);
                color: #1D1D1F;
                gridline-color: rgba(0, 0, 0, 0.06);
                border: none;
                border-radius: 16px;
                selection-background-color: rgba(144, 238, 144, 0.4);
                selection-color: #1D1D1F;
            }
            QTableWidget::item {
                padding: 8px;
                min-height: 20px;
                border-bottom: 1px solid rgba(0, 0, 0, 0.04);
            }
            QTableWidget::item:selected {
                background-color: rgba(144, 238, 144, 0.4);
                color: #1D1D1F;
            }
            QTableWidget QTableCornerButton::section {
                background-color: rgba(255, 255, 255, 0.8);
                border: none;
            }
            QHeaderView::section {
                background-color: rgba(255, 255, 255, 0.8);
                color: #1D1D1F;
                padding: 12px;
                border: none;
                border-bottom: 1px solid rgba(0, 0, 0, 0.08);
                font-weight: 600;
                font-size: 12px;
            }
            QScrollBar:vertical {
                background-color: transparent;
                width: 6px;
                margin: 0px;
            }
            QScrollBar::handle:vertical {
                background-color: rgba(0, 0, 0, 0.1);
                border-radius: 3px;
                min-height: 30px;
            }
            QScrollBar::handle:vertical:hover {
                background-color: rgba(0, 0, 0, 0.2);
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
            QScrollBar:horizontal {
                background-color: transparent;
                height: 6px;
                margin: 0px;
            }
            QScrollBar::handle:horizontal {
                background-color: rgba(0, 0, 0, 0.1);
                border-radius: 3px;
                min-width: 30px;
            }
            QScrollBar::handle:horizontal:hover {
                background-color: rgba(0, 0, 0, 0.2);
            }
            QRadioButton {
                color: #1D1D1F;
                padding: 6px;
                spacing: 10px;
                background-color: transparent;
            }
            QRadioButton::indicator {
                width: 20px;
                height: 20px;
                border-radius: 10px;
                border: 2px solid #D2D2D7;
                background-color: rgba(255, 255, 255, 0.8);
            }
            QRadioButton::indicator:checked {
                background-color: #007AFF;
                border: 2px solid #007AFF;
            }
            QRadioButton::indicator:checked::after {
                content: "";
                width: 8px;
                height: 8px;
                border-radius: 4px;
                background-color: white;
            }
            QDialog {
                background-color: #F5F5F7;
            }
            QMenu {
                background-color: rgba(255, 255, 255, 0.95);
                color: #1D1D1F;
                border: 1px solid rgba(0, 0, 0, 0.1);
                border-radius: 12px;
                padding: 6px;
            }
            QMenu::item {
                padding: 8px 24px;
                border-radius: 6px;
            }
            QMenu::item:selected {
                background-color: #007AFF;
                color: white;
            }
            QFrame {
                background-color: transparent;
                border: none;
            }
            QCalendarWidget {
                background-color: rgba(255, 255, 255, 0.9);
                border-radius: 16px;
            }
            QCalendarWidget QToolButton {
                background-color: rgba(245, 245, 247, 0.8);
                color: #1D1D1F;
                border-radius: 8px;
                padding: 8px;
            }
            QCalendarWidget QToolButton:hover {
                background-color: rgba(229, 229, 234, 0.8);
            }
            QCalendarWidget QMenu {
                background-color: rgba(255, 255, 255, 0.95);
            }
            QCalendarWidget QSpinBox {
                background-color: rgba(255, 255, 255, 0.9);
                border: 1px solid rgba(0, 0, 0, 0.08);
                border-radius: 8px;
            }
            QScrollArea {
                border: none;
                background-color: transparent;
            }
            QSplitter::handle {
                background-color: rgba(0, 0, 0, 0.05);
                width: 2px;
            }
            QSplitter::handle:hover {
                background-color: rgba(0, 122, 255, 0.3);
            }
        """
    
    @staticmethod
    def get_sidebar_stylesheet():
        """Retourne le stylesheet de la barre latérale"""
        return """
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #2C2C2E, stop:1 #1C1C1E);
                border-right: 1px solid rgba(255, 255, 255, 0.1);
            }
            QPushButton {
                background-color: transparent;
                color: #FFFFFF;
                text-align: left;
                padding: 12px 20px 12px 52px;
                border: none;
                border-radius: 10px;
                font-size: 14px;
                font-weight: 500;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.1);
            }
            QPushButton:checked {
                background-color: #007AFF;
                color: white;
            }
            QLabel {
                color: #FFFFFF;
            }
        """
    
    @staticmethod
    def get_card_stylesheet():
        """Retourne le stylesheet pour les cartes"""
        return """
            QFrame {
                background-color: rgba(255, 255, 255, 0.8);
                border-radius: 16px;
                border: 1px solid rgba(0, 0, 0, 0.04);
            }
        """


# ===== GESTION DE LA CONFIGURATION =====
class ConfigManager:
    """Gestionnaire de configuration pour l'application"""
    
    CONFIG_FILE = "gesco_config.pkl"
    
    @staticmethod
    def load_config():
        """Charger la configuration depuis le fichier"""
        if os.path.exists(ConfigManager.CONFIG_FILE):
            try:
                with open(ConfigManager.CONFIG_FILE, 'rb') as f:
                    return pickle.load(f)
            except:
                pass
        return {}
    
    @staticmethod
    def save_config(config):
        """Sauvegarder la configuration dans le fichier"""
        with open(ConfigManager.CONFIG_FILE, 'wb') as f:
            pickle.dump(config, f)
    
    @staticmethod
    def get_api_key():
        """Récupérer la clé API Axonaut"""
        config = ConfigManager.load_config()
        return config.get('axonaut_api_key', '')
    
    @staticmethod
    def set_api_key(api_key):
        """Définir la clé API Axonaut"""
        config = ConfigManager.load_config()
        config['axonaut_api_key'] = api_key
        ConfigManager.save_config(config)


# ===== CONSTANTES AXONAUT (Pour les factures uniquement) =====
AXONAUT_API_URL = "https://axonaut.com/api/v2/invoices"

def get_axonaut_headers():
    """Retourne les headers pour l'API Axonaut avec la clé API actuelle"""
    return {
        "userApiKey": ConfigManager.get_api_key(),
        "Content-Type": "application/json"
    }


# ===== BOUTONS MODERNES macOS =====
class ModernMacOSButton(QPushButton):
    """Bouton macOS moderne de base"""
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFixedHeight(40)
        self.setMinimumWidth(120)
        self.setCursor(Qt.CursorShape.PointingHandCursor)


class ModernMacOSPrimaryButton(ModernMacOSButton):
    """Bouton primaire bleu"""
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            QPushButton {
                background-color: #007AFF;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px 24px;
                font-weight: 600;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #0051D5;
            }
            QPushButton:pressed {
                background-color: #003D99;
            }
        """)


class ModernMacOSSecondaryButton(ModernMacOSButton):
    """Bouton secondaire gris"""
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            QPushButton {
                background-color: rgba(120, 120, 128, 0.16);
                color: #1D1D1F;
                border: none;
                border-radius: 10px;
                padding: 10px 24px;
                font-weight: 600;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: rgba(120, 120, 128, 0.24);
            }
            QPushButton:pressed {
                background-color: rgba(120, 120, 128, 0.32);
            }
        """)


class ModernMacOSSuccessButton(ModernMacOSButton):
    """Bouton vert de succès"""
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            QPushButton {
                background-color: #34C759;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px 24px;
                font-weight: 600;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #248A3D;
            }
            QPushButton:pressed {
                background-color: #1F7A34;
            }
        """)


class ModernMacOSDangerButton(ModernMacOSButton):
    """Bouton rouge de danger"""
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setStyleSheet("""
            QPushButton {
                background-color: #FF3B30;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px 24px;
                font-weight: 600;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #D70015;
            }
            QPushButton:pressed {
                background-color: #B50012;
            }
        """)


class ModernMacOSSmallButton(QPushButton):
    """Petit bouton pour les actions"""
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFixedHeight(32)
        self.setMinimumWidth(80)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet("""
            QPushButton {
                background-color: rgba(120, 120, 128, 0.16);
                color: #1D1D1F;
                border: none;
                border-radius: 8px;
                padding: 6px 16px;
                font-weight: 500;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: rgba(120, 120, 128, 0.24);
            }
            QPushButton:pressed {
                background-color: rgba(120, 120, 128, 0.32);
            }
        """)


class ModernMacOSAddButton(ModernMacOSButton):
    """Bouton vert avec icône + pour ajouter"""
    def __init__(self, text="Ajouter", parent=None):
        super().__init__(f"✚  {text}", parent)
        self.setStyleSheet("""
            QPushButton {
                background-color: #34C759;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px 24px;
                font-weight: 600;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #248A3D;
            }
            QPushButton:pressed {
                background-color: #1F7A34;
            }
        """)


class ModernMacOSEditButton(ModernMacOSButton):
    """Bouton avec icône crayon pour modifier"""
    def __init__(self, text="Modifier", parent=None):
        super().__init__(f"✎  {text}", parent)
        self.setStyleSheet("""
            QPushButton {
                background-color: #007AFF;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px 24px;
                font-weight: 600;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #0051D5;
            }
            QPushButton:pressed {
                background-color: #003D99;
            }
        """)


class ModernMacOSDeleteButton(ModernMacOSButton):
    """Bouton rouge avec X pour supprimer"""
    def __init__(self, text="Supprimer", parent=None):
        super().__init__(f"✕  {text}", parent)
        self.setStyleSheet("""
            QPushButton {
                background-color: #FF3B30;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px 24px;
                font-weight: 600;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #D70015;
            }
            QPushButton:pressed {
                background-color: #B80012;
            }
        """)


class ModernMacOSSmallAddButton(QPushButton):
    """Petit bouton vert avec + pour ajouter"""
    def __init__(self, text="Ajouter", parent=None):
        super().__init__(f"✚ {text}", parent)
        self.setFixedHeight(32)
        self.setMinimumWidth(90)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet("""
            QPushButton {
                background-color: #34C759;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 6px 14px;
                font-weight: 600;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #248A3D;
            }
            QPushButton:pressed {
                background-color: #1F7A34;
            }
        """)


class ModernMacOSSmallEditButton(QPushButton):
    """Petit bouton avec icône crayon pour modifier"""
    def __init__(self, text="Modifier", parent=None):
        super().__init__(f"✎ {text}", parent)
        self.setFixedHeight(32)
        self.setMinimumWidth(95)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet("""
            QPushButton {
                background-color: #007AFF;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 6px 14px;
                font-weight: 600;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #0051D5;
            }
            QPushButton:pressed {
                background-color: #003D99;
            }
        """)


class ModernMacOSSmallDeleteButton(QPushButton):
    """Petit bouton rouge avec X pour supprimer"""
    def __init__(self, text="Supprimer", parent=None):
        super().__init__(f"✕ {text}", parent)
        self.setFixedHeight(32)
        self.setMinimumWidth(100)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet("""
            QPushButton {
                background-color: #FF3B30;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 6px 14px;
                font-weight: 600;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #D70015;
            }
            QPushButton:pressed {
                background-color: #B80012;
            }
        """)


class MenuButton(QPushButton):
    """Bouton de menu avec icône SVG"""
    def __init__(self, text, svg_key=None, parent=None):
        super().__init__(text, parent)
        self.svg_key = svg_key
        self.setCheckable(True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setFixedHeight(44)
        
        # Si une icône SVG est fournie, la créer
        if svg_key and svg_key in SVG_ICONS:
            self.update_icon()
    
    def update_icon(self, color="#FFFFFF"):
        """Met à jour l'icône avec la couleur spécifiée"""
        if self.svg_key and self.svg_key in SVG_ICONS:
            icon = SVGIconHelper.create_icon(SVG_ICONS[self.svg_key], color, 28)
            self.setIcon(icon)
            self.setIconSize(QSize(28, 28))
    
    def setChecked(self, checked):
        """Override pour changer la couleur de l'icône quand sélectionné"""
        super().setChecked(checked)
        if self.svg_key:
            color = "#FFFFFF" if checked else "#FFFFFF"
            self.update_icon(color)


# ===== FONCTION HELPER =====
def convert_timestamp_to_date(timestamp_value):
    """
    Convertit un timestamp en date française (JJ/MM/AAAA)
    """
    if (timestamp_value is None or 
        timestamp_value == '' or 
        timestamp_value == 0 or 
        timestamp_value == '0' or
        str(timestamp_value).lower() == 'null' or
        str(timestamp_value).strip() == ''):
        return 'N/A'
    
    try:
        if isinstance(timestamp_value, str) and '/' in timestamp_value:
            return timestamp_value
        
        if isinstance(timestamp_value, str):
            try:
                timestamp_value = float(timestamp_value)
            except (ValueError, TypeError):
                return 'N/A'
        
        if not isinstance(timestamp_value, (int, float)):
            return 'N/A'
        
        if timestamp_value > 10000000000:
            timestamp_value = timestamp_value / 1000
        
        if timestamp_value < 0 or timestamp_value > 4102444800:
            return 'N/A'
        
        date_obj = datetime.fromtimestamp(timestamp_value)
        return date_obj.strftime('%d/%m/%Y')
    
    except (ValueError, TypeError, OSError, OverflowError):
        return 'N/A'


# ===== THREAD DE CHARGEMENT ASYNCHRONE (FACTURES UNIQUEMENT) =====

class FacturesLoaderThread(QThread):
    """Thread pour charger les factures de manière asynchrone"""
    
    finished = Signal(list)
    error = Signal(str, int)
    progress = Signal(str)
    
    def __init__(self):
        super().__init__()
    
    def run(self):
        try:
            api_key = ConfigManager.get_api_key()
            
            if not api_key or api_key.strip() == '':
                self.error.emit("Clé API non configurée. Veuillez la configurer dans Paramètres.", 0)
                return
            
            self.progress.emit("Connexion à Axonaut...")
            
            response = requests.get(
                AXONAUT_API_URL,
                headers=get_axonaut_headers(),
                timeout=10
            )
            
            if response.status_code == 200:
                self.progress.emit("Traitement des données...")
                factures = response.json()
                self.finished.emit(factures)
            else:
                self.error.emit(
                    f"Erreur API (code {response.status_code})",
                    response.status_code
                )
        
        except requests.exceptions.Timeout:
            self.error.emit("Délai d'attente dépassé", 0)
        
        except requests.exceptions.ConnectionError:
            self.error.emit("Erreur de connexion", 0)
        
        except Exception as e:
            self.error.emit(f"Erreur inattendue: {str(e)}", 0)


# ===== DIALOGUE DE CONFIGURATION API =====

class ConfigAPIDialog(QDialog):
    """Dialogue pour configurer la clé API Axonaut et gérer les techniciens"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent_window = parent
        self.setWindowTitle("Paramètres")
        self.setModal(True)
        self.resize(800, 600)
        
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Créer les onglets
        tabs = QTabWidget()
        tabs.addTab(self.create_api_tab(), "🔑 Clé API")
        tabs.addTab(self.create_techniciens_tab(), "👷 Techniciens")
        
        layout.addWidget(tabs)
        self.setLayout(layout)
    
    def create_api_tab(self):
        """Onglet pour la configuration de la clé API"""
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Titre
        title = QLabel("Configuration de la clé API")
        title.setFont(QFont("SF Pro Text", 18, QFont.Weight.Bold))
        title.setStyleSheet("color: #1D1D1F;")
        layout.addWidget(title)
        
        # Instructions
        instructions = QLabel(
            "Pour accéder aux factures Axonaut, vous devez configurer votre clé API.\n\n"
            "Vous pouvez obtenir votre clé API depuis votre compte Axonaut :\n"
            "Paramètres → API → Générer une clé API"
        )
        instructions.setWordWrap(True)
        instructions.setStyleSheet("color: #86868B; font-size: 13px;")
        layout.addWidget(instructions)
        
        # Champ de saisie
        form = QGridLayout()
        form.setSpacing(15)
        
        form.addWidget(QLabel("Clé API:"), 0, 0)
        self.api_key_entry = QLineEdit()
        self.api_key_entry.setPlaceholderText("Entrez votre clé API Axonaut...")
        current_key = ConfigManager.get_api_key()
        if current_key:
            self.api_key_entry.setText(current_key)
        form.addWidget(self.api_key_entry, 0, 1)
        
        layout.addLayout(form)
        layout.addStretch()
        
        # Boutons
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(12)
        buttons_layout.addStretch()
        
        btn_save = ModernMacOSSuccessButton("Enregistrer")
        btn_save.clicked.connect(self.save_api_config)
        btn_save.setDefault(True)
        buttons_layout.addWidget(btn_save)
        
        layout.addLayout(buttons_layout)
        widget.setLayout(layout)
        return widget
    
    def create_techniciens_tab(self):
        """Onglet pour la gestion des techniciens"""
        widget = QWidget()
        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(30, 30, 30, 30)
        
        # Titre et bouton
        header = QHBoxLayout()
        title = QLabel("Gestion des Techniciens")
        title.setFont(QFont("SF Pro Text", 18, QFont.Weight.Bold))
        title.setStyleSheet("color: #1D1D1F;")
        header.addWidget(title)
        header.addStretch()
        
        btn_add_tech = ModernMacOSAddButton("+ Nouveau")
        btn_add_tech.clicked.connect(self.show_add_technicien_dialog)
        header.addWidget(btn_add_tech)
        layout.addLayout(header)
        
        # Table des techniciens
        self.techniciens_table = QTableWidget()
        self.techniciens_table.setColumnCount(3)
        self.techniciens_table.setHorizontalHeaderLabels(["Nom", "Coût Horaire (€)", "Actions"])
        # Configuration des colonnes pour adaptation optimale
        # Configuration des colonnes pour permettre le redimensionnement manuel
        header = self.techniciens_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Interactive)  # Nom redimensionnable
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive)  # Coût redimensionnable
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Interactive)  # Actions redimensionnable
        self.techniciens_table.setColumnWidth(2, 200)
        self.techniciens_table.verticalHeader().setVisible(False)
        self.techniciens_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.techniciens_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        # Activer le tri sur toutes les colonnes
        self.techniciens_table.setSortingEnabled(True)
        layout.addWidget(self.techniciens_table)
        
        self.refresh_techniciens_table()
        
        widget.setLayout(layout)
        return widget
    
    def refresh_techniciens_table(self):
        """Rafraîchir la table des techniciens"""
        self.techniciens_table.setRowCount(0)
        
        if not self.parent_window or not hasattr(self.parent_window, 'gestion'):
            return
        
        for idx, technicien in self.parent_window.gestion.techniciens.iterrows():
            row = self.techniciens_table.rowCount()
            self.techniciens_table.insertRow(row)
            
            # Nom
            self.techniciens_table.setItem(row, 0, QTableWidgetItem(technicien['Nom']))
            
            # Coût horaire
            cout_item = QTableWidgetItem(f"{technicien['Cout_Horaire_Defaut']:.2f} €")
            cout_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.techniciens_table.setItem(row, 1, cout_item)
            
            # Boutons d'action
            actions_widget = QWidget()
            actions_layout = QHBoxLayout(actions_widget)
            actions_layout.setContentsMargins(5, 2, 5, 2)
            actions_layout.setSpacing(5)
            
            btn_edit = ModernMacOSEditButton("Modifier")
            btn_edit.clicked.connect(lambda checked, tech_id=idx: self.show_edit_technicien_dialog(tech_id))
            actions_layout.addWidget(btn_edit)
            
            btn_delete = ModernMacOSDeleteButton("Supprimer")
            btn_delete.clicked.connect(lambda checked, tech_id=idx: self.delete_technicien(tech_id))
            actions_layout.addWidget(btn_delete)
            
            self.techniciens_table.setCellWidget(row, 2, actions_widget)
    
    def show_add_technicien_dialog(self):
        """Afficher le dialogue pour ajouter un technicien"""
        dialog = TechnicienDialog(self.parent_window.gestion, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_data()
            self.parent_window.gestion.ajouter_technicien(data)
            self.refresh_techniciens_table()
            QMessageBox.information(self, "Succès", "Technicien ajouté avec succès!")
    
    def show_edit_technicien_dialog(self, tech_id):
        """Afficher le dialogue pour modifier un technicien"""
        dialog = ModifierTechnicienDialog(self.parent_window.gestion, tech_id, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_data()
            self.parent_window.gestion.modifier_technicien(tech_id, data)
            self.refresh_techniciens_table()
            QMessageBox.information(self, "Succès", "Technicien modifié avec succès!")
    
    def delete_technicien(self, tech_id):
        """Supprimer un technicien"""
        reply = QMessageBox.question(
            self,
            "Confirmation",
            "Êtes-vous sûr de vouloir supprimer ce technicien ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.parent_window.gestion.supprimer_technicien(tech_id)
            self.refresh_techniciens_table()
            QMessageBox.information(self, "Succès", "Technicien supprimé avec succès!")
    
    def save_api_config(self):
        """Sauvegarder la configuration de l'API"""
        api_key = self.api_key_entry.text().strip()
        if api_key:
            ConfigManager.set_api_key(api_key)
            QMessageBox.information(self, "Succès", "Clé API enregistrée avec succès!")
        else:
            QMessageBox.warning(self, "Attention", "Veuillez entrer une clé API valide.")


class TechnicienDialog(QDialog):
    """Dialogue pour ajouter un technicien"""
    
    def __init__(self, gestion, parent=None):
        super().__init__(parent)
        self.gestion = gestion
        self.setWindowTitle("Nouveau Technicien")
        self.setModal(True)
        self.resize(500, 250)
        
        layout = QVBoxLayout()
        layout.setSpacing(18)
        layout.setContentsMargins(25, 25, 25, 25)
        
        form = QGridLayout()
        form.setSpacing(12)
        form.setColumnStretch(1, 1)
        
        # Nom
        label_nom = QLabel("Nom du technicien:")
        label_nom.setMinimumWidth(160)
        form.addWidget(label_nom, 0, 0)
        self.nom_entry = QLineEdit()
        self.nom_entry.setMinimumHeight(36)
        form.addWidget(self.nom_entry, 0, 1)
        
        # Coût horaire
        label_cout = QLabel("Coût horaire par défaut (€):")
        label_cout.setMinimumWidth(160)
        form.addWidget(label_cout, 1, 0)
        self.cout_entry = QLineEdit()
        self.cout_entry.setText("0.00")
        self.cout_entry.setMinimumHeight(36)
        form.addWidget(self.cout_entry, 1, 1)
        
        layout.addLayout(form)
        layout.addStretch()
        
        # Boutons
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(12)
        buttons_layout.addStretch()
        
        btn_cancel = ModernMacOSSecondaryButton("Annuler")
        btn_cancel.clicked.connect(self.reject)
        buttons_layout.addWidget(btn_cancel)
        
        btn_ok = ModernMacOSAddButton("Créer")
        btn_ok.clicked.connect(self.accept)
        btn_ok.setDefault(True)
        buttons_layout.addWidget(btn_ok)
        
        layout.addLayout(buttons_layout)
        self.setLayout(layout)
    
    def get_data(self):
        return {
            'Nom': self.nom_entry.text(),
            'Cout_Horaire_Defaut': float(self.cout_entry.text() or 0)
        }


class ModifierTechnicienDialog(TechnicienDialog):
    """Dialogue pour modifier un technicien"""
    
    def __init__(self, gestion, tech_id, parent=None):
        super().__init__(gestion, parent)
        self.tech_id = tech_id
        self.setWindowTitle("Modifier Technicien")
        
        technicien = gestion.techniciens.loc[tech_id]
        self.nom_entry.setText(technicien['Nom'])
        self.cout_entry.setText(str(float(technicien['Cout_Horaire_Defaut'])))
        
        # Changer le bouton
        for button in self.findChildren(ModernMacOSAddButton):
            button.setParent(None)
            button.deleteLater()
            
            btn_modifier = ModernMacOSEditButton("Modifier")
            btn_modifier.clicked.connect(self.accept)
            btn_modifier.setDefault(True)
            
            buttons_layout = self.layout().itemAt(self.layout().count() - 1).layout()
            buttons_layout.addWidget(btn_modifier)


# ===== GESTION DES DONNÉES =====

class GestionChantier:
    """Classe de gestion métier des chantiers"""
    
    def __init__(self):
        self.chantiers = pd.DataFrame(columns=[
            'ID_Chantier', 'Numero_Commande_Client', 'ID_Client', 'Nom_Client',
            'Adresse_Chantier', 'Date_Ouverture', 'Date_Cloture', 'Statut', 
            'Duree_Prevue_Jours', 'Chiffrage_Global', 'Cout_Estime_Achats', 'Cout_Estime_MO',
            'Avancement_Financier_Pourcentage', 'Avancement_Temporel_Pourcentage', 
            'Somme_Achats_Fournisseurs', 'Somme_Achats_Hors_Fournisseurs', 
            'Volume_Heure_Personnel'
        ])
        if not self.chantiers.empty:
            self.chantiers.set_index('ID_Chantier', inplace=True)
        
        self.achats = pd.DataFrame(columns=[
            'ID_Achat', 'ID_Chantier', 'Date', 'Fournisseur', 'Type_Achat', 
            'Montant', 'Description', 'Numero_BL'
        ])
        if not self.achats.empty:
            self.achats.set_index('ID_Achat', inplace=True)
        
        self.heures = pd.DataFrame(columns=[
            'ID_Heure', 'ID_Chantier', 'Date', 'Technicien', 'Heures', 'Cout_Horaire', 'Description'
        ])
        if not self.heures.empty:
            self.heures.set_index('ID_Heure', inplace=True)
        
        # NOUVEAU: Structure améliorée pour les tiers avec catégorie et adresse
        self.contacts = pd.DataFrame(columns=[
            'ID_Contact', 'Nom', 'Email', 'Telephone', 'Entreprise', 'Type', 
            'Categorie', 'Adresse_Principale', 'Adresses_Chantiers'
        ])
        if not self.contacts.empty:
            self.contacts.set_index('ID_Contact', inplace=True)
        
        # NOUVEAU: Table pour les contacts associés aux tiers
        self.contacts_associes = pd.DataFrame(columns=[
            'ID_Contact_Associe', 'ID_Tiers', 'Nom', 'Email', 'Telephone', 'Fonction', 'Adresses_Chantiers'
        ])
        if not self.contacts_associes.empty:
            self.contacts_associes.set_index('ID_Contact_Associe', inplace=True)
        
        self.techniciens = pd.DataFrame(columns=[
            'ID_Technicien', 'Nom', 'Cout_Horaire_Defaut', 'Telephone', 'Email'
        ])
        if not self.techniciens.empty:
            self.techniciens.set_index('ID_Technicien', inplace=True)
        
        self.load_data()

    def ajouter_chantier(self, data, client_name):
        new_id = f"CH-{str(uuid.uuid4())[:8].upper()}"
        data.update({
            'Nom_Client': client_name,
            'Statut': 'Actif',
            'Date_Cloture': None,
            'Somme_Achats_Fournisseurs': 0.0,
            'Somme_Achats_Hors_Fournisseurs': 0.0,
            'Volume_Heure_Personnel': 0.0,
            'Chiffrage_Global': float(data['Chiffrage_Global']),
            'Cout_Estime_Achats': float(data.get('Cout_Estime_Achats', 0)),
            'Cout_Estime_MO': float(data.get('Cout_Estime_MO', 0)),
            'Duree_Prevue_Jours': int(data.get('Duree_Prevue_Jours', 30)),
            'Avancement_Financier_Pourcentage': 0.0,
            'Avancement_Temporel_Pourcentage': 0.0,
            'Date_Ouverture': datetime.now().strftime('%Y-%m-%d'),
            'Adresse_Chantier': data.get('Adresse_Chantier', '')
        })
        self.chantiers.loc[new_id] = pd.Series(data, name=new_id)
        self.save_data()
        return new_id

    def ajouter_adresse_client(self, client_id, adresse):
        if client_id in self.contacts.index:
            adresses = self.contacts.loc[client_id, 'Adresses_Chantiers']
            if pd.isna(adresses) or adresses == '':
                adresses_list = []
            else:
                adresses_list = adresses.split('|||')
            
            if adresse and adresse.strip() and adresse not in adresses_list:
                adresses_list.append(adresse)
                self.contacts.loc[client_id, 'Adresses_Chantiers'] = '|||'.join(adresses_list)
                self.save_data()

    def modifier_adresse_client(self, client_id, ancienne_adresse, nouvelle_adresse):
        """Modifier une adresse de chantier existante pour un client"""
        if client_id in self.contacts.index:
            adresses = self.contacts.loc[client_id, 'Adresses_Chantiers']
            if pd.isna(adresses) or adresses == '':
                return
            
            adresses_list = adresses.split('|||')
            
            if ancienne_adresse in adresses_list and nouvelle_adresse and nouvelle_adresse.strip():
                # Remplacer l'ancienne adresse par la nouvelle
                index = adresses_list.index(ancienne_adresse)
                adresses_list[index] = nouvelle_adresse
                self.contacts.loc[client_id, 'Adresses_Chantiers'] = '|||'.join(adresses_list)
                
                # Mettre à jour les chantiers qui utilisent cette adresse
                for chantier_id in self.chantiers.index:
                    if self.chantiers.loc[chantier_id, 'Adresse_Chantier'] == ancienne_adresse:
                        self.chantiers.loc[chantier_id, 'Adresse_Chantier'] = nouvelle_adresse
                
                # Mettre à jour les contacts associés qui utilisent cette adresse
                for contact_id in self.contacts_associes.index:
                    adresses_contact = self.contacts_associes.loc[contact_id, 'Adresses_Chantiers']
                    if not pd.isna(adresses_contact) and adresses_contact != '':
                        adresses_contact_list = adresses_contact.split('|||')
                        if ancienne_adresse in adresses_contact_list:
                            index_contact = adresses_contact_list.index(ancienne_adresse)
                            adresses_contact_list[index_contact] = nouvelle_adresse
                            self.contacts_associes.loc[contact_id, 'Adresses_Chantiers'] = '|||'.join(adresses_contact_list)
                
                self.save_data()

    def get_adresses_client(self, client_id):
        if client_id in self.contacts.index:
            adresses = self.contacts.loc[client_id, 'Adresses_Chantiers']
            if pd.isna(adresses) or adresses == '':
                return []
            return adresses.split('|||')
        return []

    def cloturer_chantier(self, chantier_id):
        if chantier_id not in self.chantiers.index:
            raise ValueError("Chantier introuvable")
        self.chantiers.loc[chantier_id, 'Statut'] = 'Clôturé'
        self.chantiers.loc[chantier_id, 'Date_Cloture'] = datetime.now().strftime('%Y-%m-%d')
        self.save_data()

    def archiver_chantier(self, chantier_id):
        if chantier_id not in self.chantiers.index:
            raise ValueError("Chantier introuvable")
        self.chantiers.loc[chantier_id, 'Statut'] = 'Archivé'
        self.save_data()

    def desarchiver_chantier(self, chantier_id):
        if chantier_id not in self.chantiers.index:
            raise ValueError("Chantier introuvable")
        self.chantiers.loc[chantier_id, 'Statut'] = 'Actif'
        self.chantiers.loc[chantier_id, 'Date_Cloture'] = None
        self.save_data()

    def modifier_chantier(self, chantier_id, data):
        if chantier_id not in self.chantiers.index:
            raise ValueError("Chantier introuvable")
        
        self.chantiers.loc[chantier_id, 'Numero_Commande_Client'] = data['Numero_Commande_Client']
        self.chantiers.loc[chantier_id, 'Nom_Client'] = data['Nom_Client']
        self.chantiers.loc[chantier_id, 'Adresse_Chantier'] = data['Adresse_Chantier']
        self.chantiers.loc[chantier_id, 'Duree_Prevue_Jours'] = int(data['Duree_Prevue_Jours'])
        self.chantiers.loc[chantier_id, 'Chiffrage_Global'] = float(data['Chiffrage_Global'])
        self.chantiers.loc[chantier_id, 'Cout_Estime_Achats'] = float(data['Cout_Estime_Achats'])
        self.chantiers.loc[chantier_id, 'Cout_Estime_MO'] = float(data.get('Cout_Estime_MO', 0))
        
        self.calculer_avancement(chantier_id)
        self.save_data()

    def supprimer_chantier(self, chantier_id):
        if chantier_id not in self.chantiers.index:
            raise ValueError("Chantier introuvable")
        self.chantiers.drop(chantier_id, inplace=True)
        self.achats = self.achats[self.achats['ID_Chantier'] != chantier_id]
        self.heures = self.heures[self.heures['ID_Chantier'] != chantier_id]
        self.save_data()

    def ajouter_achat(self, data):
        new_id = f"AC-{str(uuid.uuid4())[:8].upper()}"
        self.achats.loc[new_id] = pd.Series(data, name=new_id)
        
        chantier_id = data['ID_Chantier']
        montant = float(data['Montant'])
        
        if data['Type_Achat'] == 'Fournisseur':
            self.chantiers.loc[chantier_id, 'Somme_Achats_Fournisseurs'] += montant
        else:
            self.chantiers.loc[chantier_id, 'Somme_Achats_Hors_Fournisseurs'] += montant
        
        self.calculer_avancement(chantier_id)
        self.save_data()
        return new_id

    def modifier_achat(self, achat_id, data):
        if achat_id not in self.achats.index:
            raise ValueError("Achat introuvable")
        
        ancien_achat = self.achats.loc[achat_id]
        ancien_montant = float(ancien_achat['Montant'])
        ancien_type = ancien_achat['Type_Achat']
        chantier_id = ancien_achat['ID_Chantier']
        
        if ancien_type == 'Fournisseur':
            self.chantiers.loc[chantier_id, 'Somme_Achats_Fournisseurs'] -= ancien_montant
        else:
            self.chantiers.loc[chantier_id, 'Somme_Achats_Hors_Fournisseurs'] -= ancien_montant
        
        self.achats.loc[achat_id, 'Date'] = data['Date']
        self.achats.loc[achat_id, 'Fournisseur'] = data['Fournisseur']
        self.achats.loc[achat_id, 'Type_Achat'] = data['Type_Achat']
        self.achats.loc[achat_id, 'Montant'] = float(data['Montant'])
        self.achats.loc[achat_id, 'Description'] = data['Description']
        self.achats.loc[achat_id, 'Numero_BL'] = data['Numero_BL']
        
        nouveau_montant = float(data['Montant'])
        if data['Type_Achat'] == 'Fournisseur':
            self.chantiers.loc[chantier_id, 'Somme_Achats_Fournisseurs'] += nouveau_montant
        else:
            self.chantiers.loc[chantier_id, 'Somme_Achats_Hors_Fournisseurs'] += nouveau_montant
        
        self.calculer_avancement(chantier_id)
        self.save_data()

    def supprimer_achat(self, achat_id):
        if achat_id not in self.achats.index:
            raise ValueError("Achat introuvable")
        
        achat = self.achats.loc[achat_id]
        chantier_id = achat['ID_Chantier']
        montant = float(achat['Montant'])
        
        if achat['Type_Achat'] == 'Fournisseur':
            self.chantiers.loc[chantier_id, 'Somme_Achats_Fournisseurs'] -= montant
        else:
            self.chantiers.loc[chantier_id, 'Somme_Achats_Hors_Fournisseurs'] -= montant
        
        self.achats.drop(achat_id, inplace=True)
        self.calculer_avancement(chantier_id)
        self.save_data()

    def ajouter_heures(self, data):
        new_id = f"HR-{str(uuid.uuid4())[:8].upper()}"
        self.heures.loc[new_id] = pd.Series(data, name=new_id)
        
        chantier_id = data['ID_Chantier']
        heures = float(data['Heures'])
        
        self.chantiers.loc[chantier_id, 'Volume_Heure_Personnel'] += heures
        
        self.calculer_avancement(chantier_id)
        self.save_data()
        return new_id

    def modifier_heures(self, heure_id, data):
        if heure_id not in self.heures.index:
            raise ValueError("Heures introuvables")
        
        ancienne_heure = self.heures.loc[heure_id]
        anciennes_heures = float(ancienne_heure['Heures'])
        chantier_id = ancienne_heure['ID_Chantier']
        
        self.chantiers.loc[chantier_id, 'Volume_Heure_Personnel'] -= anciennes_heures
        
        self.heures.loc[heure_id, 'Date'] = data['Date']
        self.heures.loc[heure_id, 'Technicien'] = data['Technicien']
        self.heures.loc[heure_id, 'Heures'] = float(data['Heures'])
        self.heures.loc[heure_id, 'Cout_Horaire'] = float(data['Cout_Horaire'])
        self.heures.loc[heure_id, 'Description'] = data['Description']
        
        nouvelles_heures = float(data['Heures'])
        self.chantiers.loc[chantier_id, 'Volume_Heure_Personnel'] += nouvelles_heures
        
        self.calculer_avancement(chantier_id)
        self.save_data()

    def supprimer_heures(self, heure_id):
        if heure_id not in self.heures.index:
            raise ValueError("Heures introuvables")
        
        heure = self.heures.loc[heure_id]
        chantier_id = heure['ID_Chantier']
        heures = float(heure['Heures'])
        
        self.chantiers.loc[chantier_id, 'Volume_Heure_Personnel'] -= heures
        
        self.heures.drop(heure_id, inplace=True)
        self.calculer_avancement(chantier_id)
        self.save_data()
    
    def ajouter_tiers(self, data):
        """Ajouter un tiers avec la nouvelle structure"""
        new_id = f"TI-{str(uuid.uuid4())[:8].upper()}"
        data.update({
            'Adresses_Chantiers': ''
        })
        self.contacts.loc[new_id] = pd.Series(data, name=new_id)
        self.save_data()
        return new_id
    
    def modifier_tiers(self, tiers_id, data):
        """Modifier un tiers existant"""
        if tiers_id not in self.contacts.index:
            raise ValueError("Tiers introuvable")
        
        # Conserver les adresses de chantiers existantes
        adresses_chantiers = self.contacts.loc[tiers_id, 'Adresses_Chantiers']
        data['Adresses_Chantiers'] = adresses_chantiers
        
        for key, value in data.items():
            self.contacts.loc[tiers_id, key] = value
        
        self.save_data()
    
    def supprimer_tiers(self, tiers_id):
        """Supprimer un tiers et ses contacts associés"""
        if tiers_id not in self.contacts.index:
            raise ValueError("Tiers introuvable")
        
        # Supprimer aussi tous les contacts associés
        contacts_associes = self.contacts_associes[
            self.contacts_associes['ID_Tiers'] == tiers_id
        ]
        for contact_id in contacts_associes.index:
            self.contacts_associes.drop(contact_id, inplace=True)
        
        self.contacts.drop(tiers_id, inplace=True)
        self.save_data()
    
    def ajouter_contact_associe(self, tiers_id, data):
        """Ajouter un contact associé à un tiers"""
        if tiers_id not in self.contacts.index:
            raise ValueError("Tiers introuvable")
        
        new_id = f"CA-{str(uuid.uuid4())[:8].upper()}"
        data['ID_Tiers'] = tiers_id
        self.contacts_associes.loc[new_id] = pd.Series(data, name=new_id)
        self.save_data()
        return new_id
    
    def modifier_contact_associe(self, contact_id, data):
        """Modifier un contact associé"""
        if contact_id not in self.contacts_associes.index:
            raise ValueError("Contact associé introuvable")
        
        # Conserver l'ID du tiers
        tiers_id = self.contacts_associes.loc[contact_id, 'ID_Tiers']
        data['ID_Tiers'] = tiers_id
        
        for key, value in data.items():
            self.contacts_associes.loc[contact_id, key] = value
        
        self.save_data()
    
    def supprimer_contact_associe(self, contact_id):
        """Supprimer un contact associé"""
        if contact_id not in self.contacts_associes.index:
            raise ValueError("Contact associé introuvable")
        
        self.contacts_associes.drop(contact_id, inplace=True)
        self.save_data()
    
    def get_contacts_associes(self, tiers_id):
        """Récupérer tous les contacts associés à un tiers"""
        if tiers_id not in self.contacts.index:
            return pd.DataFrame()
        
        return self.contacts_associes[
            self.contacts_associes['ID_Tiers'] == tiers_id
        ]

    def calculer_avancement(self, chantier_id):
        """Calculer l'avancement financier et temporel d'un chantier"""
        if chantier_id not in self.chantiers.index:
            return
        
        chantier = self.chantiers.loc[chantier_id]
        
        # Avancement financier
        total_depenses = float(chantier['Somme_Achats_Fournisseurs']) + float(chantier['Somme_Achats_Hors_Fournisseurs'])
        chiffrage = float(chantier['Chiffrage_Global'])
        
        if chiffrage > 0:
            avancement_financier = (total_depenses / chiffrage) * 100
            self.chantiers.loc[chantier_id, 'Avancement_Financier_Pourcentage'] = min(avancement_financier, 100)
        
        # Avancement temporel
        date_ouverture = datetime.strptime(chantier['Date_Ouverture'], '%Y-%m-%d')
        jours_ecoules = (datetime.now() - date_ouverture).days
        duree_prevue = int(chantier['Duree_Prevue_Jours'])
        
        if duree_prevue > 0:
            avancement_temporel = (jours_ecoules / duree_prevue) * 100
            self.chantiers.loc[chantier_id, 'Avancement_Temporel_Pourcentage'] = min(avancement_temporel, 100)

    def get_statut_budget(self, chantier_id):
        """Déterminer le statut budgétaire d'un chantier"""
        if chantier_id not in self.chantiers.index:
            return 'Normal'
        
        chantier = self.chantiers.loc[chantier_id]
        avancement_financier = float(chantier['Avancement_Financier_Pourcentage'])
        avancement_temporel = float(chantier['Avancement_Temporel_Pourcentage'])
        
        ecart = avancement_financier - avancement_temporel
        
        if ecart < -10:
            return 'Excellent'
        elif ecart < 5:
            return 'Normal'
        elif ecart < 15:
            return 'Attention'
        else:
            return 'Alerte'
    
    def get_statut_sami(self, chantier_id):
        """
        Déterminer le statut SAMI (Satisfaisant, Acceptable, Moyen, Insuffisant)
        basé sur l'accostage des données réelles vs estimées et l'avancement temporel
        """
        if chantier_id not in self.chantiers.index:
            return 'Moyen', '#FF9500'
        
        chantier = self.chantiers.loc[chantier_id]
        
        # Calcul de l'écart financier (dépenses réelles vs estimées)
        total_depenses = float(chantier['Somme_Achats_Fournisseurs']) + float(chantier['Somme_Achats_Hors_Fournisseurs'])
        cout_estime_total = float(chantier.get('Cout_Estime_Achats', 0)) + float(chantier.get('Cout_Estime_MO', 0))
        
        # Calcul de l'écart temporel
        avancement_financier = float(chantier['Avancement_Financier_Pourcentage'])
        avancement_temporel = float(chantier['Avancement_Temporel_Pourcentage'])
        
        # Score financier (0-100)
        if cout_estime_total > 0:
            ratio_financier = (total_depenses / cout_estime_total) * 100
            # Plus le ratio est bas, mieux c'est
            if ratio_financier <= 80:
                score_financier = 100
            elif ratio_financier <= 100:
                score_financier = 80
            elif ratio_financier <= 120:
                score_financier = 50
            else:
                score_financier = 20
        else:
            score_financier = 50  # Neutre si pas d'estimation
        
        # Score temporel (0-100)
        ecart_temporel = avancement_financier - avancement_temporel
        if ecart_temporel <= -10:
            score_temporel = 100  # Excellent : en avance
        elif ecart_temporel <= 0:
            score_temporel = 80   # Bon : dans les temps
        elif ecart_temporel <= 10:
            score_temporel = 50   # Moyen : léger retard
        else:
            score_temporel = 20   # Insuffisant : retard important
        
        # Score global (moyenne pondérée)
        score_global = (score_financier * 0.6) + (score_temporel * 0.4)
        
        # Attribution du statut SAMI
        if score_global >= 85:
            return 'Satisfaisant', '#34C759'  # Vert
        elif score_global >= 65:
            return 'Acceptable', '#007AFF'    # Bleu
        elif score_global >= 45:
            return 'Moyen', '#FF9500'         # Jaune
        else:
            return 'Insuffisant', '#FF3B30'   # Rouge

    def ajouter_technicien(self, data):
        """Ajouter un nouveau technicien"""
        new_id = f"TEC-{str(uuid.uuid4())[:8].upper()}"
        self.techniciens.loc[new_id] = {
            'Nom': data.get('Nom', ''),
            'Cout_Horaire_Defaut': float(data.get('Cout_Horaire_Defaut', 0)),
            'Telephone': data.get('Telephone', ''),
            'Email': data.get('Email', '')
        }
        self.save_data()
        return new_id
    
    def modifier_technicien(self, tech_id, data):
        """Modifier un technicien existant"""
        if tech_id in self.techniciens.index:
            self.techniciens.loc[tech_id, 'Nom'] = data.get('Nom', '')
            self.techniciens.loc[tech_id, 'Cout_Horaire_Defaut'] = float(data.get('Cout_Horaire_Defaut', 0))
            self.techniciens.loc[tech_id, 'Telephone'] = data.get('Telephone', '')
            self.techniciens.loc[tech_id, 'Email'] = data.get('Email', '')
            self.save_data()
    
    def supprimer_technicien(self, tech_id):
        """Supprimer un technicien"""
        if tech_id in self.techniciens.index:
            self.techniciens.drop(tech_id, inplace=True)
            self.save_data()

    def load_data(self):
        """Charger les données depuis les fichiers"""
        try:
            if os.path.exists('gesco_chantiers.pkl'):
                self.chantiers = pd.read_pickle('gesco_chantiers.pkl')
            if os.path.exists('gesco_achats.pkl'):
                self.achats = pd.read_pickle('gesco_achats.pkl')
            if os.path.exists('gesco_heures.pkl'):
                self.heures = pd.read_pickle('gesco_heures.pkl')
            if os.path.exists('gesco_contacts.pkl'):
                self.contacts = pd.read_pickle('gesco_contacts.pkl')
            if os.path.exists('gesco_contacts_associes.pkl'):
                self.contacts_associes = pd.read_pickle('gesco_contacts_associes.pkl')
            if os.path.exists('gesco_techniciens.pkl'):
                self.techniciens = pd.read_pickle('gesco_techniciens.pkl')
        except Exception as e:
            print(f"Erreur lors du chargement des données: {e}")

    def save_data(self):
        """Sauvegarder les données dans les fichiers"""
        try:
            self.chantiers.to_pickle('gesco_chantiers.pkl')
            self.achats.to_pickle('gesco_achats.pkl')
            self.heures.to_pickle('gesco_heures.pkl')
            self.contacts.to_pickle('gesco_contacts.pkl')
            self.contacts_associes.to_pickle('gesco_contacts_associes.pkl')
            self.techniciens.to_pickle('gesco_techniciens.pkl')
        except Exception as e:
            print(f"Erreur lors de la sauvegarde des données: {e}")


# ===== DIALOGUES =====

# (Les dialogues ChantierDialog, ModifierChantierDialog, AchatDialog, ModifierAchatDialog, 
# HeureDialog et ModifierHeureDialog restent identiques - je les inclus pour la complétude)

class ChantierDialog(QDialog):
    """Dialog pour créer un nouveau chantier"""
    
    def __init__(self, gestion, parent=None):
        super().__init__(parent)
        self.gestion = gestion
        self.parent_window = parent
        self.setWindowTitle("Nouveau Chantier")
        self.setModal(True)
        self.resize(650, 520)
        
        layout = QVBoxLayout()
        layout.setSpacing(18)
        layout.setContentsMargins(25, 25, 25, 25)
        
        form = QGridLayout()
        form.setSpacing(12)
        form.setColumnStretch(1, 1)
        
        # Largeur des labels
        label_width = 180
        
        # N° Commande Client
        label_commande = QLabel("N° Commande Client:")
        label_commande.setMinimumWidth(label_width)
        form.addWidget(label_commande, 0, 0)
        self.num_commande_entry = QLineEdit()
        self.num_commande_entry.setMinimumHeight(36)
        form.addWidget(self.num_commande_entry, 0, 1)
        
        # Client avec bouton pour créer un nouveau tiers
        label_client = QLabel("Client:")
        label_client.setMinimumWidth(label_width)
        form.addWidget(label_client, 1, 0)
        client_layout = QHBoxLayout()
        client_layout.setSpacing(8)
        
        self.client_combo = QComboBox()
        self.client_combo.setMinimumHeight(36)
        self.load_clients()
        client_layout.addWidget(self.client_combo, stretch=1)
        
        btn_new_client = ModernMacOSSmallAddButton("Nouveau")
        btn_new_client.setFixedWidth(100)
        btn_new_client.clicked.connect(self.create_new_tiers)
        client_layout.addWidget(btn_new_client)
        
        form.addLayout(client_layout, 1, 1)
        
        # Adresse Chantier avec boutons gérer les adresses
        label_adresse = QLabel("Adresse Chantier:")
        label_adresse.setMinimumWidth(label_width)
        form.addWidget(label_adresse, 2, 0)
        adresse_layout = QVBoxLayout()
        adresse_layout.setSpacing(8)
        
        # Combo + boutons sur la même ligne
        adresse_top_layout = QHBoxLayout()
        adresse_top_layout.setSpacing(8)
        
        self.adresse_chantier_combo = QComboBox()
        self.adresse_chantier_combo.setEditable(False)
        self.adresse_chantier_combo.setMinimumHeight(36)
        self.client_combo.currentIndexChanged.connect(self.load_client_addresses)
        self.load_client_addresses()
        adresse_top_layout.addWidget(self.adresse_chantier_combo, stretch=1)
        
        # Boutons pour gérer les adresses
        btn_new_address = ModernMacOSSmallAddButton("Ajouter")
        btn_new_address.setFixedWidth(95)
        btn_new_address.clicked.connect(self.create_new_address)
        adresse_top_layout.addWidget(btn_new_address)
        
        btn_edit_address = ModernMacOSSmallEditButton("Modifier")
        btn_edit_address.setFixedWidth(100)
        btn_edit_address.clicked.connect(self.edit_current_address)
        adresse_top_layout.addWidget(btn_edit_address)
        
        adresse_layout.addLayout(adresse_top_layout)
        form.addLayout(adresse_layout, 2, 1)
        
        # Durée prévue
        label_duree = QLabel("Durée prévue (jours):")
        label_duree.setMinimumWidth(label_width)
        form.addWidget(label_duree, 3, 0)
        self.duree_entry = QLineEdit()
        self.duree_entry.setText("30")
        self.duree_entry.setMinimumHeight(36)
        form.addWidget(self.duree_entry, 3, 1)
        
        # Chiffrage Global
        label_chiffrage = QLabel("Chiffrage Global (€):")
        label_chiffrage.setMinimumWidth(label_width)
        form.addWidget(label_chiffrage, 4, 0)
        self.chiffrage_entry = QLineEdit()
        self.chiffrage_entry.setMinimumHeight(36)
        form.addWidget(self.chiffrage_entry, 4, 1)
        
        # Coût Estimé Achats
        label_achats = QLabel("Coût Estimé Achats (€):")
        label_achats.setMinimumWidth(label_width)
        form.addWidget(label_achats, 5, 0)
        self.cout_achats_entry = QLineEdit()
        self.cout_achats_entry.setText("0")
        self.cout_achats_entry.setMinimumHeight(36)
        form.addWidget(self.cout_achats_entry, 5, 1)
        
        # Coût Estimé Main d'Œuvre
        label_mo = QLabel("Coût Estimé Main d'Œuvre (€):")
        label_mo.setMinimumWidth(label_width)
        form.addWidget(label_mo, 6, 0)
        self.cout_mo_entry = QLineEdit()
        self.cout_mo_entry.setText("0")
        self.cout_mo_entry.setMinimumHeight(36)
        form.addWidget(self.cout_mo_entry, 6, 1)
        
        layout.addLayout(form)
        
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(12)
        buttons_layout.addStretch()
        
        btn_cancel = ModernMacOSSecondaryButton("Annuler")
        btn_cancel.clicked.connect(self.reject)
        buttons_layout.addWidget(btn_cancel)
        
        btn_ok = ModernMacOSAddButton("Créer")
        btn_ok.clicked.connect(self.accept)
        btn_ok.setDefault(True)
        buttons_layout.addWidget(btn_ok)
        
        layout.addLayout(buttons_layout)
        
        self.setLayout(layout)
    
    def load_clients(self):
        """Charger la liste des clients"""
        self.client_combo.clear()
        if not self.gestion.contacts.empty:
            # Filtrer uniquement les clients
            for idx, contact in self.gestion.contacts.iterrows():
                if contact['Type'] == 'Client':
                    display_text = contact['Nom']
                    if contact.get('Entreprise'):
                        display_text += f" ({contact['Entreprise']})"
                    self.client_combo.addItem(display_text, userData=idx)
    
    def create_new_tiers(self):
        """Créer un nouveau tiers depuis le popup chantier"""
        dialog = TiersDialog(self.gestion, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_data()
            
            if not data['Nom']:
                QMessageBox.critical(self, "Erreur", "Le nom est obligatoire")
                return
            
            # Forcer le type à "Client"
            data['Type'] = 'Client'
            
            try:
                new_id = self.gestion.ajouter_tiers(data)
                QMessageBox.information(self, "Succès", "Client créé avec succès !")
                
                # Recharger la liste des clients
                self.load_clients()
                
                # Sélectionner le nouveau client
                for i in range(self.client_combo.count()):
                    if self.client_combo.itemData(i) == new_id:
                        self.client_combo.setCurrentIndex(i)
                        break
                
                # Rafraîchir aussi la fenêtre parente si elle existe
                if hasattr(self.parent_window, 'refresh_tiers_list'):
                    self.parent_window.refresh_tiers_list()
                    
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur lors de la création: {e}")
    
    def load_client_addresses(self):
        self.adresse_chantier_combo.clear()
        client_id = self.client_combo.currentData()
        if client_id:
            adresses = self.gestion.get_adresses_client(client_id)
            self.adresse_chantier_combo.addItems(adresses)
    
    def create_new_address(self):
        """Créer une nouvelle adresse de chantier pour le client sélectionné"""
        client_id = self.client_combo.currentData()
        if not client_id:
            QMessageBox.warning(self, "Attention", "Veuillez d'abord sélectionner un client.")
            return
        
        dialog = AdresseChantierDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            nouvelle_adresse = dialog.get_adresse()
            if nouvelle_adresse:
                # Ajouter l'adresse au client
                self.gestion.ajouter_adresse_client(client_id, nouvelle_adresse)
                # Recharger la liste des adresses
                self.load_client_addresses()
                # Sélectionner la nouvelle adresse
                index = self.adresse_chantier_combo.findText(nouvelle_adresse)
                if index >= 0:
                    self.adresse_chantier_combo.setCurrentIndex(index)
                QMessageBox.information(self, "Succès", "Adresse de chantier créée avec succès !")
    
    def edit_current_address(self):
        """Modifier l'adresse de chantier sélectionnée"""
        client_id = self.client_combo.currentData()
        if not client_id:
            QMessageBox.warning(self, "Attention", "Veuillez d'abord sélectionner un client.")
            return
        
        current_address = self.adresse_chantier_combo.currentText()
        if not current_address:
            QMessageBox.warning(self, "Attention", "Aucune adresse sélectionnée.")
            return
        
        dialog = AdresseChantierDialog(self, adresse_existante=current_address)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            nouvelle_adresse = dialog.get_adresse()
            if nouvelle_adresse:
                # Modifier l'adresse du client
                self.gestion.modifier_adresse_client(client_id, current_address, nouvelle_adresse)
                # Recharger la liste des adresses
                self.load_client_addresses()
                # Sélectionner l'adresse modifiée
                index = self.adresse_chantier_combo.findText(nouvelle_adresse)
                if index >= 0:
                    self.adresse_chantier_combo.setCurrentIndex(index)
                QMessageBox.information(self, "Succès", "Adresse de chantier modifiée avec succès !")
    
    def get_data(self):
        return {
            'Numero_Commande_Client': self.num_commande_entry.text(),
            'ID_Client': self.client_combo.currentData(),
            'Adresse_Chantier': self.adresse_chantier_combo.currentText(),
            'Duree_Prevue_Jours': self.duree_entry.text(),
            'Chiffrage_Global': self.chiffrage_entry.text(),
            'Cout_Estime_Achats': self.cout_achats_entry.text(),
            'Cout_Estime_MO': self.cout_mo_entry.text()
        }


class ModifierChantierDialog(ChantierDialog):
    """Dialog pour modifier un chantier existant"""
    
    def __init__(self, gestion, chantier_id, parent=None):
        super().__init__(gestion, parent)
        self.chantier_id = chantier_id
        self.setWindowTitle("Modifier Chantier")
        
        chantier = gestion.chantiers.loc[chantier_id]
        
        self.num_commande_entry.setText(chantier['Numero_Commande_Client'])
        
        # Sélectionner le client correspondant
        for i in range(self.client_combo.count()):
            if self.client_combo.itemData(i) == chantier['ID_Client']:
                self.client_combo.setCurrentIndex(i)
                break
        
        self.adresse_chantier_combo.setCurrentText(chantier['Adresse_Chantier'])
        self.duree_entry.setText(str(int(chantier['Duree_Prevue_Jours'])))
        self.chiffrage_entry.setText(str(float(chantier['Chiffrage_Global'])))
        self.cout_achats_entry.setText(str(float(chantier['Cout_Estime_Achats'])))
        self.cout_mo_entry.setText(str(float(chantier.get('Cout_Estime_MO', 0))))
        
        # Remplacer le bouton "Créer" par "Modifier" avec icône crayon
        for button in self.findChildren(ModernMacOSAddButton):
            # Supprimer l'ancien bouton
            button.setParent(None)
            button.deleteLater()
            
            # Créer le nouveau bouton Modifier
            btn_modifier = ModernMacOSEditButton("Modifier")
            btn_modifier.clicked.connect(self.accept)
            btn_modifier.setDefault(True)
            
            # Trouver le layout des boutons et ajouter le nouveau
            buttons_layout = self.layout().itemAt(self.layout().count() - 1).layout()
            buttons_layout.addWidget(btn_modifier)


class AchatDialog(QDialog):
    """Dialog pour ajouter un achat"""
    
    def __init__(self, gestion, parent=None):
        super().__init__(parent)
        self.gestion = gestion
        self.setWindowTitle("Nouvel Achat")
        self.setModal(True)
        self.resize(500, 450)
        
        layout = QVBoxLayout()
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)
        
        form = QGridLayout()
        form.setSpacing(15)
        
        form.addWidget(QLabel("Chantier:"), 0, 0)
        self.chantier_combo = QComboBox()
        chantiers_actifs = gestion.chantiers[gestion.chantiers['Statut'] == 'Actif']
        for idx, chantier in chantiers_actifs.iterrows():
            label = f"{chantier['Numero_Commande_Client']} - {chantier['Nom_Client']}"
            self.chantier_combo.addItem(label, userData=idx)
        form.addWidget(self.chantier_combo, 0, 1)
        
        form.addWidget(QLabel("Date:"), 1, 0)
        self.date_edit = QDateEdit()
        self.date_edit.setDate(QDate.currentDate())
        self.date_edit.setCalendarPopup(True)
        form.addWidget(self.date_edit, 1, 1)
        
        form.addWidget(QLabel("Fournisseur:"), 2, 0)
        self.fournisseur_entry = QLineEdit()
        form.addWidget(self.fournisseur_entry, 2, 1)
        
        form.addWidget(QLabel("Type d'achat:"), 3, 0)
        self.type_combo = QComboBox()
        self.type_combo.addItems(["Fournisseur", "Hors Fournisseur"])
        form.addWidget(self.type_combo, 3, 1)
        
        form.addWidget(QLabel("Montant (€):"), 4, 0)
        self.montant_entry = QLineEdit()
        form.addWidget(self.montant_entry, 4, 1)
        
        form.addWidget(QLabel("Description:"), 5, 0)
        self.description_entry = QTextEdit()
        self.description_entry.setMaximumHeight(80)
        form.addWidget(self.description_entry, 5, 1)
        
        form.addWidget(QLabel("N° BL:"), 6, 0)
        self.bl_entry = QLineEdit()
        form.addWidget(self.bl_entry, 6, 1)
        
        layout.addLayout(form)
        
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(12)
        buttons_layout.addStretch()
        
        btn_cancel = ModernMacOSSecondaryButton("Annuler")
        btn_cancel.clicked.connect(self.reject)
        buttons_layout.addWidget(btn_cancel)
        
        btn_ok = ModernMacOSSuccessButton("Ajouter")
        btn_ok.clicked.connect(self.accept)
        btn_ok.setDefault(True)
        buttons_layout.addWidget(btn_ok)
        
        layout.addLayout(buttons_layout)
        
        self.setLayout(layout)
    
    def get_data(self):
        return {
            'ID_Chantier': self.chantier_combo.currentData(),
            'Date': self.date_edit.date().toString('yyyy-MM-dd'),
            'Fournisseur': self.fournisseur_entry.text(),
            'Type_Achat': self.type_combo.currentText(),
            'Montant': self.montant_entry.text(),
            'Description': self.description_entry.toPlainText(),
            'Numero_BL': self.bl_entry.text()
        }


class ModifierAchatDialog(AchatDialog):
    """Dialog pour modifier un achat existant"""
    
    def __init__(self, gestion, achat_id, parent=None):
        super().__init__(gestion, parent)
        self.achat_id = achat_id
        self.setWindowTitle("Modifier Achat")
        
        achat = gestion.achats.loc[achat_id]
        
        # Sélectionner le chantier correspondant
        for i in range(self.chantier_combo.count()):
            if self.chantier_combo.itemData(i) == achat['ID_Chantier']:
                self.chantier_combo.setCurrentIndex(i)
                break
        
        date_obj = datetime.strptime(str(achat['Date']), '%Y-%m-%d')
        self.date_edit.setDate(QDate(date_obj.year, date_obj.month, date_obj.day))
        
        self.fournisseur_entry.setText(achat['Fournisseur'])
        self.type_combo.setCurrentText(achat['Type_Achat'])
        self.montant_entry.setText(str(float(achat['Montant'])))
        self.description_entry.setPlainText(achat['Description'])
        self.bl_entry.setText(achat['Numero_BL'])
        
        # Changer le texte du bouton
        for button in self.findChildren(ModernMacOSSuccessButton):
            button.setText("Modifier")


class HeureDialog(QDialog):
    """Dialog pour ajouter des heures"""
    
    def __init__(self, gestion, parent=None):
        super().__init__(parent)
        self.gestion = gestion
        self.setWindowTitle("Nouvelles Heures")
        self.setModal(True)
        self.resize(620, 540)
        
        layout = QVBoxLayout()
        layout.setSpacing(18)
        layout.setContentsMargins(25, 25, 25, 25)
        
        form = QGridLayout()
        form.setSpacing(12)
        form.setColumnStretch(1, 1)
        
        # Largeur des labels
        label_width = 160
        
        # Chantier
        label_chantier = QLabel("Chantier:")
        label_chantier.setMinimumWidth(label_width)
        form.addWidget(label_chantier, 0, 0)
        self.chantier_combo = QComboBox()
        self.chantier_combo.setMinimumHeight(36)
        chantiers_actifs = gestion.chantiers[gestion.chantiers['Statut'] == 'Actif']
        for idx, chantier in chantiers_actifs.iterrows():
            label = f"{chantier['Numero_Commande_Client']} - {chantier['Nom_Client']}"
            self.chantier_combo.addItem(label, userData=idx)
        form.addWidget(self.chantier_combo, 0, 1)
        
        # Date
        label_date = QLabel("Date:")
        label_date.setMinimumWidth(label_width)
        form.addWidget(label_date, 1, 0)
        self.date_edit = QDateEdit()
        self.date_edit.setDate(QDate.currentDate())
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setMinimumHeight(36)
        form.addWidget(self.date_edit, 1, 1)
        
        # Technicien
        label_technicien = QLabel("Technicien:")
        label_technicien.setMinimumWidth(label_width)
        form.addWidget(label_technicien, 2, 0)
        self.technicien_combo = QComboBox()
        self.technicien_combo.setEditable(True)
        self.technicien_combo.setMinimumHeight(36)
        if not gestion.techniciens.empty:
            for idx, tech in gestion.techniciens.iterrows():
                self.technicien_combo.addItem(tech['Nom'], userData=idx)
        self.technicien_combo.currentIndexChanged.connect(self.load_cout_horaire)
        form.addWidget(self.technicien_combo, 2, 1)
        
        # Heures
        label_heures = QLabel("Heures:")
        label_heures.setMinimumWidth(label_width)
        form.addWidget(label_heures, 3, 0)
        self.heures_entry = QLineEdit()
        self.heures_entry.setMinimumHeight(36)
        form.addWidget(self.heures_entry, 3, 1)
        
        # Coût Horaire
        label_cout = QLabel("Coût Horaire (€):")
        label_cout.setMinimumWidth(label_width)
        form.addWidget(label_cout, 4, 0)
        self.cout_entry = QLineEdit()
        self.cout_entry.setText("0")
        self.cout_entry.setMinimumHeight(36)
        form.addWidget(self.cout_entry, 4, 1)
        
        # Description
        label_description = QLabel("Description:")
        label_description.setMinimumWidth(label_width)
        form.addWidget(label_description, 5, 0, Qt.AlignmentFlag.AlignTop)
        self.description_entry = QTextEdit()
        self.description_entry.setMaximumHeight(85)
        form.addWidget(self.description_entry, 5, 1)
        
        layout.addLayout(form)
        
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(12)
        buttons_layout.addStretch()
        
        btn_cancel = ModernMacOSSecondaryButton("Annuler")
        btn_cancel.clicked.connect(self.reject)
        buttons_layout.addWidget(btn_cancel)
        
        btn_ok = ModernMacOSAddButton("Créer")
        btn_ok.clicked.connect(self.accept)
        btn_ok.setDefault(True)
        buttons_layout.addWidget(btn_ok)
        
        layout.addLayout(buttons_layout)
        
        self.setLayout(layout)
    
    def load_cout_horaire(self):
        tech_id = self.technicien_combo.currentData()
        if tech_id and tech_id in self.gestion.techniciens.index:
            cout = self.gestion.techniciens.loc[tech_id, 'Cout_Horaire_Defaut']
            self.cout_entry.setText(str(float(cout)))
    
    def get_data(self):
        return {
            'ID_Chantier': self.chantier_combo.currentData(),
            'Date': self.date_edit.date().toString('yyyy-MM-dd'),
            'Technicien': self.technicien_combo.currentText(),
            'Heures': self.heures_entry.text(),
            'Cout_Horaire': self.cout_entry.text(),
            'Description': self.description_entry.toPlainText()
        }


class ModifierHeureDialog(HeureDialog):
    """Dialog pour modifier des heures existantes"""
    
    def __init__(self, gestion, heure_id, parent=None):
        super().__init__(gestion, parent)
        self.heure_id = heure_id
        self.setWindowTitle("Modifier Heures")
        
        heure = gestion.heures.loc[heure_id]
        
        # Sélectionner le chantier correspondant
        for i in range(self.chantier_combo.count()):
            if self.chantier_combo.itemData(i) == heure['ID_Chantier']:
                self.chantier_combo.setCurrentIndex(i)
                break
        
        date_obj = datetime.strptime(str(heure['Date']), '%Y-%m-%d')
        self.date_edit.setDate(QDate(date_obj.year, date_obj.month, date_obj.day))
        
        self.technicien_combo.setCurrentText(heure['Technicien'])
        self.heures_entry.setText(str(float(heure['Heures'])))
        self.cout_entry.setText(str(float(heure['Cout_Horaire'])))
        self.description_entry.setPlainText(heure['Description'])
        
        # Remplacer le bouton "Créer" par "Modifier" avec icône crayon
        for button in self.findChildren(ModernMacOSAddButton):
            button.setParent(None)
            button.deleteLater()
            
            btn_modifier = ModernMacOSEditButton("Modifier")
            btn_modifier.clicked.connect(self.accept)
            btn_modifier.setDefault(True)
            
            buttons_layout = self.layout().itemAt(self.layout().count() - 1).layout()
            buttons_layout.addWidget(btn_modifier)


# ===== NOUVEAUX DIALOGUES POUR LES TIERS =====

class TiersDialog(QDialog):
    """Dialog pour créer/modifier un tiers avec les nouveaux champs"""
    
    def __init__(self, gestion, parent=None):
        super().__init__(parent)
        self.gestion = gestion
        self.setWindowTitle("Nouveau Tiers")
        self.setModal(True)
        self.resize(620, 540)
        
        layout = QVBoxLayout()
        layout.setSpacing(18)
        layout.setContentsMargins(25, 25, 25, 25)
        
        form = QGridLayout()
        form.setSpacing(12)
        form.setColumnStretch(1, 1)
        
        # Largeur des labels
        label_width = 160
        
        # Nom
        label_nom = QLabel("Nom:")
        label_nom.setMinimumWidth(label_width)
        form.addWidget(label_nom, 0, 0)
        self.nom_entry = QLineEdit()
        self.nom_entry.setMinimumHeight(36)
        form.addWidget(self.nom_entry, 0, 1)
        
        # Catégorie
        label_cat = QLabel("Catégorie:")
        label_cat.setMinimumWidth(label_width)
        form.addWidget(label_cat, 1, 0)
        self.categorie_combo = QComboBox()
        self.categorie_combo.addItems(["Particulier", "Professionnel"])
        self.categorie_combo.setMinimumHeight(36)
        form.addWidget(self.categorie_combo, 1, 1)
        
        # Entreprise
        label_entreprise = QLabel("Entreprise:")
        label_entreprise.setMinimumWidth(label_width)
        form.addWidget(label_entreprise, 2, 0)
        self.entreprise_entry = QLineEdit()
        self.entreprise_entry.setMinimumHeight(36)
        form.addWidget(self.entreprise_entry, 2, 1)
        
        # Email
        label_email = QLabel("Email:")
        label_email.setMinimumWidth(label_width)
        form.addWidget(label_email, 3, 0)
        self.email_entry = QLineEdit()
        self.email_entry.setMinimumHeight(36)
        form.addWidget(self.email_entry, 3, 1)
        
        # Téléphone
        label_tel = QLabel("Téléphone:")
        label_tel.setMinimumWidth(label_width)
        form.addWidget(label_tel, 4, 0)
        self.tel_entry = QLineEdit()
        self.tel_entry.setMinimumHeight(36)
        form.addWidget(self.tel_entry, 4, 1)
        
        # Adresse principale
        label_adresse = QLabel("Adresse principale:")
        label_adresse.setMinimumWidth(label_width)
        form.addWidget(label_adresse, 5, 0, Qt.AlignmentFlag.AlignTop)
        self.adresse_entry = QTextEdit()
        self.adresse_entry.setMaximumHeight(85)
        form.addWidget(self.adresse_entry, 5, 1)
        
        # Type
        label_type = QLabel("Type:")
        label_type.setMinimumWidth(label_width)
        form.addWidget(label_type, 6, 0)
        self.type_combo = QComboBox()
        self.type_combo.addItems(["Client", "Fournisseur", "Prospect", "Autre"])
        self.type_combo.setMinimumHeight(36)
        form.addWidget(self.type_combo, 6, 1)
        
        layout.addLayout(form)
        
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(12)
        buttons_layout.addStretch()
        
        btn_cancel = ModernMacOSSecondaryButton("Annuler")
        btn_cancel.clicked.connect(self.reject)
        buttons_layout.addWidget(btn_cancel)
        
        btn_ok = ModernMacOSAddButton("Créer")
        btn_ok.clicked.connect(self.accept)
        btn_ok.setDefault(True)
        buttons_layout.addWidget(btn_ok)
        
        layout.addLayout(buttons_layout)
        
        self.setLayout(layout)
    
    def get_data(self):
        return {
            'Nom': self.nom_entry.text(),
            'Categorie': self.categorie_combo.currentText(),
            'Email': self.email_entry.text(),
            'Telephone': self.tel_entry.text(),
            'Entreprise': self.entreprise_entry.text(),
            'Adresse_Principale': self.adresse_entry.toPlainText(),
            'Type': self.type_combo.currentText()
        }


class ModifierTiersDialog(TiersDialog):
    """Dialog pour modifier un tiers existant"""
    
    def __init__(self, gestion, tiers_id, parent=None):
        super().__init__(gestion, parent)
        self.tiers_id = tiers_id
        self.setWindowTitle("Modifier Tiers")
        
        tiers = gestion.contacts.loc[tiers_id]
        
        self.nom_entry.setText(tiers['Nom'])
        self.categorie_combo.setCurrentText(tiers.get('Categorie', 'Particulier'))
        self.entreprise_entry.setText(tiers.get('Entreprise', ''))
        self.email_entry.setText(tiers.get('Email', ''))
        self.tel_entry.setText(tiers.get('Telephone', ''))
        self.adresse_entry.setPlainText(tiers.get('Adresse_Principale', ''))
        self.type_combo.setCurrentText(tiers['Type'])
        
        # Remplacer le bouton "Créer" par "Modifier" avec icône crayon
        for button in self.findChildren(ModernMacOSAddButton):
            button.setParent(None)
            button.deleteLater()
            
            btn_modifier = ModernMacOSEditButton("Modifier")
            btn_modifier.clicked.connect(self.accept)
            btn_modifier.setDefault(True)
            
            buttons_layout = self.layout().itemAt(self.layout().count() - 1).layout()
            buttons_layout.addWidget(btn_modifier)


class ContactAssocieDialog(QDialog):
    """Dialog pour créer/modifier un contact associé"""
    
    def __init__(self, gestion, tiers_id, parent=None):
        super().__init__(parent)
        self.gestion = gestion
        self.tiers_id = tiers_id
        self.setWindowTitle("Nouveau Contact Associé")
        self.setModal(True)
        self.resize(580, 520)
        
        layout = QVBoxLayout()
        layout.setSpacing(18)
        layout.setContentsMargins(25, 25, 25, 25)
        
        form = QGridLayout()
        form.setSpacing(12)
        form.setColumnStretch(1, 1)
        
        # Largeur des labels
        label_width = 120
        
        # Nom
        label_nom = QLabel("Nom:")
        label_nom.setMinimumWidth(label_width)
        form.addWidget(label_nom, 0, 0)
        self.nom_entry = QLineEdit()
        self.nom_entry.setMinimumHeight(36)
        form.addWidget(self.nom_entry, 0, 1)
        
        # Email
        label_email = QLabel("Email:")
        label_email.setMinimumWidth(label_width)
        form.addWidget(label_email, 1, 0)
        self.email_entry = QLineEdit()
        self.email_entry.setMinimumHeight(36)
        form.addWidget(self.email_entry, 1, 1)
        
        # Téléphone
        label_tel = QLabel("Téléphone:")
        label_tel.setMinimumWidth(label_width)
        form.addWidget(label_tel, 2, 0)
        self.tel_entry = QLineEdit()
        self.tel_entry.setMinimumHeight(36)
        form.addWidget(self.tel_entry, 2, 1)
        
        # Fonction
        label_fonction = QLabel("Fonction:")
        label_fonction.setMinimumWidth(label_width)
        form.addWidget(label_fonction, 3, 0)
        self.fonction_entry = QLineEdit()
        self.fonction_entry.setMinimumHeight(36)
        form.addWidget(self.fonction_entry, 3, 1)
        
        layout.addLayout(form)
        
        # Section pour les adresses de chantiers
        adresses_section = QVBoxLayout()
        adresses_section.setSpacing(10)
        
        adresses_label = QLabel("Adresses de chantiers associées:")
        adresses_label.setFont(QFont("SF Pro Text", 13, QFont.Weight.DemiBold))
        adresses_section.addWidget(adresses_label)
        
        info_label = QLabel("Ce contact recevra les emails pour les chantiers sélectionnés")
        info_label.setStyleSheet("color: #86868B; font-size: 11px; font-style: italic;")
        adresses_section.addWidget(info_label)
        
        # Scroll area pour les checkboxes des adresses
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setMaximumHeight(145)
        scroll.setStyleSheet("""
            QScrollArea {
                background-color: rgba(0, 0, 0, 0.02);
                border: 1px solid rgba(0, 0, 0, 0.08);
                border-radius: 8px;
            }
        """)
        
        scroll_widget = QWidget()
        self.adresses_layout = QVBoxLayout()
        self.adresses_layout.setSpacing(5)
        self.adresses_layout.setContentsMargins(10, 10, 10, 10)
        scroll_widget.setLayout(self.adresses_layout)
        scroll.setWidget(scroll_widget)
        
        # Charger les adresses disponibles
        self.adresses_checkboxes = {}
        adresses = self.gestion.get_adresses_client(tiers_id)
        
        if not adresses:
            no_addr_label = QLabel("Aucune adresse de chantier disponible")
            no_addr_label.setStyleSheet("color: #86868B; font-style: italic; padding: 10px;")
            no_addr_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.adresses_layout.addWidget(no_addr_label)
        else:
            for i, adresse in enumerate(adresses):
                checkbox = QCheckBox(adresse)
                checkbox.setStyleSheet("QCheckBox { padding: 5px; }")
                self.adresses_checkboxes[i] = checkbox
                self.adresses_layout.addWidget(checkbox)
        
        self.adresses_layout.addStretch()
        adresses_section.addWidget(scroll)
        
        layout.addLayout(adresses_section)
        
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(12)
        buttons_layout.addStretch()
        
        btn_cancel = ModernMacOSSecondaryButton("Annuler")
        btn_cancel.clicked.connect(self.reject)
        buttons_layout.addWidget(btn_cancel)
        
        btn_ok = ModernMacOSAddButton("Ajouter")
        btn_ok.clicked.connect(self.accept)
        btn_ok.setDefault(True)
        buttons_layout.addWidget(btn_ok)
        
        layout.addLayout(buttons_layout)
        
        self.setLayout(layout)
    
    def get_data(self):
        # Récupérer les adresses sélectionnées
        adresses_selectionnees = []
        for idx, checkbox in self.adresses_checkboxes.items():
            if checkbox.isChecked():
                adresses = self.gestion.get_adresses_client(self.tiers_id)
                if idx < len(adresses):
                    adresses_selectionnees.append(adresses[idx])
        
        return {
            'Nom': self.nom_entry.text(),
            'Email': self.email_entry.text(),
            'Telephone': self.tel_entry.text(),
            'Fonction': self.fonction_entry.text(),
            'Adresses_Chantiers': '|||'.join(adresses_selectionnees) if adresses_selectionnees else ''
        }


class ModifierContactAssocieDialog(ContactAssocieDialog):
    """Dialog pour modifier un contact associé existant"""
    
    def __init__(self, gestion, tiers_id, contact_id, parent=None):
        super().__init__(gestion, tiers_id, parent)
        self.contact_id = contact_id
        self.setWindowTitle("Modifier Contact Associé")
        
        contact = gestion.contacts_associes.loc[contact_id]
        
        self.nom_entry.setText(contact['Nom'])
        self.email_entry.setText(contact.get('Email', ''))
        self.tel_entry.setText(contact.get('Telephone', ''))
        self.fonction_entry.setText(contact.get('Fonction', ''))
        
        # Cocher les adresses déjà associées
        adresses_associees = contact.get('Adresses_Chantiers', '')
        if adresses_associees and adresses_associees != '':
            adresses_list = adresses_associees.split('|||')
            adresses_disponibles = gestion.get_adresses_client(tiers_id)
            
            for idx, checkbox in self.adresses_checkboxes.items():
                if idx < len(adresses_disponibles) and adresses_disponibles[idx] in adresses_list:
                    checkbox.setChecked(True)
        
        # Remplacer le bouton "Ajouter" par "Modifier" avec icône crayon
        for button in self.findChildren(ModernMacOSAddButton):
            button.setParent(None)
            button.deleteLater()
            
            btn_modifier = ModernMacOSEditButton("Modifier")
            btn_modifier.clicked.connect(self.accept)
            btn_modifier.setDefault(True)
            
            buttons_layout = self.layout().itemAt(self.layout().count() - 1).layout()
            buttons_layout.addWidget(btn_modifier)


class AdresseChantierDialog(QDialog):
    """Dialog pour créer/modifier une adresse de chantier"""
    
    def __init__(self, parent=None, adresse_existante=None):
        super().__init__(parent)
        self.setWindowTitle("Adresse de Chantier")
        self.setModal(True)
        self.resize(520, 240)
        
        layout = QVBoxLayout()
        layout.setSpacing(18)
        layout.setContentsMargins(25, 25, 25, 25)
        
        form = QVBoxLayout()
        form.setSpacing(12)
        
        label_adresse = QLabel("Adresse complète:")
        label_adresse.setFont(QFont("SF Pro Text", 13, QFont.Weight.DemiBold))
        form.addWidget(label_adresse)
        
        self.adresse_entry = QTextEdit()
        self.adresse_entry.setMaximumHeight(95)
        self.adresse_entry.setPlaceholderText("Ex: 123 Rue de la République, 75001 Paris")
        
        if adresse_existante:
            self.adresse_entry.setPlainText(adresse_existante)
        
        form.addWidget(self.adresse_entry)
        
        layout.addLayout(form)
        
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(12)
        buttons_layout.addStretch()
        
        btn_cancel = ModernMacOSSecondaryButton("Annuler")
        btn_cancel.clicked.connect(self.reject)
        buttons_layout.addWidget(btn_cancel)
        
        if adresse_existante:
            btn_ok = ModernMacOSEditButton("Enregistrer")
        else:
            btn_ok = ModernMacOSAddButton("Ajouter")
        btn_ok.clicked.connect(self.accept)
        btn_ok.setDefault(True)
        buttons_layout.addWidget(btn_ok)
        
        layout.addLayout(buttons_layout)
        
        self.setLayout(layout)
    
    def get_adresse(self):
        return self.adresse_entry.toPlainText().strip()


# Je continue le fichier dans la prochaine partie...

# ===== FENÊTRE PRINCIPALE =====

class GescoMainWindow(QMainWindow):
    """Fenêtre principale de l'application"""
    
    def __init__(self):
        super().__init__()
        self.gestion = GestionChantier()
        
        # Variable pour tracker le premier chargement des factures
        self.factures_first_load = False
        
        # Variable pour tracker le tiers sélectionné
        self.selected_tiers_id = None
        
        # Variable pour tracker l'état du sidebar
        self.sidebar_visible = True
        
        self.setWindowTitle("GESCO - Gestion de Chantier")
        self.resize(1400, 900)
        
        self.setStyleSheet(ModernMacOSStyleHelper.get_main_stylesheet())
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QHBoxLayout()
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        central_widget.setLayout(main_layout)
        
        # Menu latéral (stocker comme attribut pour pouvoir le cacher/afficher)
        self.sidebar = self.create_sidebar()
        main_layout.addWidget(self.sidebar)
        
        # Zone de contenu
        content_area = QWidget()
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(40, 40, 40, 40)
        content_area.setLayout(content_layout)
        
        # Bouton toggle menu en haut à gauche
        toggle_layout = QHBoxLayout()
        toggle_layout.setContentsMargins(0, 0, 0, 20)
        
        self.btn_toggle_menu = QPushButton()
        self.btn_toggle_menu.setIcon(SVGIconHelper.create_icon(SVG_ICONS['menu_toggle'], "#1D1D1F", 20))
        self.btn_toggle_menu.setIconSize(QSize(20, 20))
        self.btn_toggle_menu.setFixedSize(40, 40)
        self.btn_toggle_menu.clicked.connect(self.toggle_sidebar)
        self.btn_toggle_menu.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_toggle_menu.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: rgba(0, 0, 0, 0.05);
            }
        """)
        toggle_layout.addWidget(self.btn_toggle_menu)
        toggle_layout.addStretch()
        content_layout.addLayout(toggle_layout)
        
        self.stacked_widget = QStackedWidget()
        content_layout.addWidget(self.stacked_widget)
        
        # Ajouter les pages
        self.stacked_widget.addWidget(self.create_achats_page())  # 0
        self.stacked_widget.addWidget(self.create_heures_page())  # 1
        self.stacked_widget.addWidget(self.create_chantier_module_page())  # 2 - NOUVEAU MODULE
        self.stacked_widget.addWidget(self.create_archives_page())  # 3
        self.stacked_widget.addWidget(self.create_tiers_page())  # 4
        self.stacked_widget.addWidget(self.create_factures_page())  # 5
        
        main_layout.addWidget(content_area, stretch=1)
    
    def create_sidebar(self):
        """Création du menu latéral macOS moderne avec icônes SVG"""
        sidebar = QFrame()
        sidebar.setFixedWidth(200)  # Largeur réduite de 240px à 200px
        sidebar.setStyleSheet(ModernMacOSStyleHelper.get_sidebar_stylesheet())
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 30, 0, 20)
        layout.setSpacing(6)
        
        # Logo / Titre (centré, sans icône, police 22)
        logo = QLabel("GESCO")
        logo.setFont(QFont("SF Pro Text", 22, QFont.Weight.Bold))
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo.setStyleSheet("padding: 20px; color: #FFFFFF;")
        layout.addWidget(logo)
        
        layout.addSpacing(20)
        
        # Boutons de menu avec icônes SVG
        self.menu_buttons = []
        
        menus = [
            ("Achats", 0, 'achats'),
            ("Main d'œuvre", 1, 'main_oeuvre'),
            ("Mes Chantiers", 2, 'chantier_module'),  # NOUVEAU MODULE ICI
            ("Archives", 3, 'archives'),
            ("Tiers", 4, 'tiers'),
            ("Factures", 5, 'factures')
        ]
        
        for text, index, icon_key in menus:
            btn = MenuButton(text, icon_key)
            btn.clicked.connect(lambda checked, i=index: self.switch_page(i))
            self.menu_buttons.append(btn)
            layout.addWidget(btn)
        
        self.menu_buttons[0].setChecked(True)
        
        # Espacement pour pousser les éléments en bas
        layout.addStretch()
        
        # Espacement avant les paramètres
        layout.addSpacing(10)
        
        # Bouton paramètres en bas (identique aux autres menus)
        btn_settings = MenuButton("Paramètres", 'parametres')
        btn_settings.clicked.connect(self.show_settings_dialog)
        btn_settings.setCursor(Qt.CursorShape.PointingHandCursor)
        layout.addWidget(btn_settings)
        
        # Version en bas du menu
        version_label = QLabel("v4.7.7")
        version_label.setFont(QFont("SF Pro Text", 10))
        version_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        version_label.setStyleSheet("color: rgba(255, 255, 255, 0.5); padding-top: 10px;")
        layout.addWidget(version_label)
        
        sidebar.setLayout(layout)
        
        return sidebar
    
    def toggle_sidebar(self):
        """Afficher/masquer le menu latéral sans animation"""
        self.sidebar_visible = not self.sidebar_visible
        
        if self.sidebar_visible:
            self.sidebar.show()
        else:
            self.sidebar.hide()
    
    def switch_page(self, index):
        """Change de page et actualise selon les règles"""
        self.stacked_widget.setCurrentIndex(index)
        
        # Désélectionner tous les boutons sauf celui cliqué
        for i, btn in enumerate(self.menu_buttons):
            btn.setChecked(i == index)
        
        # Actualiser selon la page
        if index == 0:  # Achats
            self.refresh_achats_list()
        elif index == 1:  # Heures
            self.refresh_heures_list()
        elif index == 2:  # Mes Chantiers (NOUVEAU MODULE)
            self.refresh_chantier_module_list()
        elif index == 3:  # Archives
            self.refresh_archives()
        elif index == 4:  # Tiers
            self.refresh_tiers_list()
        elif index == 5:  # Factures
            if not self.factures_first_load:
                self.refresh_factures()
                self.factures_first_load = True
    
    def show_settings_dialog(self):
        """Afficher le dialogue de paramètres"""
        dialog = ConfigAPIDialog(self)
        dialog.exec()
    
    def create_tiers_page(self):
        """NOUVEAU: Page tiers avec interface liste/détails"""
        page = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)
        page.setLayout(layout)
        
        # SPLITTER pour diviser en deux parties
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setHandleWidth(1)
        
        # v4.6: Sauvegarder la position du splitter quand elle change
        splitter.splitterMoved.connect(lambda: self.save_splitter_position(splitter))
        
        # === PARTIE GAUCHE: Liste des tiers (30%) ===
        left_widget = QWidget()
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(0, 0, 20, 0)  # Marge à droite pour éviter collision
        left_layout.setSpacing(15)
        left_widget.setLayout(left_layout)
        
        # Barre de recherche et bouton
        search_layout = QHBoxLayout()
        search_layout.setSpacing(10)
        
        self.tiers_search_entry = QLineEdit()
        self.tiers_search_entry.setPlaceholderText("🔍 Rechercher...")
        self.tiers_search_entry.textChanged.connect(self.refresh_tiers_list)
        search_layout.addWidget(self.tiers_search_entry)
        
        btn_add_tiers = ModernMacOSPrimaryButton("+ Nouveau")
        btn_add_tiers.clicked.connect(self.show_tiers_dialog)
        search_layout.addWidget(btn_add_tiers)
        
        left_layout.addLayout(search_layout)
        
        # Compteur
        self.tiers_count_label = QLabel("Total: 0 tiers")
        self.tiers_count_label.setFont(QFont("SF Pro Text", 12, QFont.Weight.Bold))
        self.tiers_count_label.setStyleSheet("color: #86868B; padding: 5px 0;")
        left_layout.addWidget(self.tiers_count_label)
        
        # Liste des tiers avec adresse
        self.tiers_list = QTableWidget()
        self.tiers_list.setColumnCount(3)
        self.tiers_list.setHorizontalHeaderLabels(["Nom", "Type", "Adresse"])
        # Configuration des colonnes pour adaptation optimale
        # Configuration des colonnes pour permettre le redimensionnement manuel
        header = self.tiers_list.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Interactive)  # Nom redimensionnable
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive)  # Type redimensionnable
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Interactive)  # Adresse redimensionnable
        self.tiers_list.setColumnWidth(0, 200)
        self.tiers_list.verticalHeader().setVisible(False)
        self.tiers_list.verticalHeader().setDefaultSectionSize(38)
        self.tiers_list.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.tiers_list.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.tiers_list.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        # Activer le tri sur toutes les colonnes
        self.tiers_list.setSortingEnabled(True)
        self.tiers_list.itemSelectionChanged.connect(self.on_tiers_selection_changed)
        left_layout.addWidget(self.tiers_list)
        
        splitter.addWidget(left_widget)
        
        # === PARTIE DROITE: Détails du tiers (70%) ===
        right_widget = QWidget()
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(20, 0, 0, 0)  # Marge à gauche pour éviter collision
        right_layout.setSpacing(20)
        right_widget.setLayout(right_layout)
        
        # Scroll area pour les détails
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; }")
        
        details_container = QWidget()
        self.tiers_details_layout = QVBoxLayout()
        self.tiers_details_layout.setSpacing(20)
        self.tiers_details_layout.setContentsMargins(0, 0, 0, 0)
        details_container.setLayout(self.tiers_details_layout)
        
        scroll.setWidget(details_container)
        right_layout.addWidget(scroll)
        
        splitter.addWidget(right_widget)
        
        # v4.6: Charger la position sauvegardée ou définir les proportions par défaut (30% - 70%)
        saved_sizes = self.load_splitter_position()
        if saved_sizes:
            splitter.setSizes(saved_sizes)
        else:
            splitter.setSizes([300, 700])  # Par défaut
        
        layout.addWidget(splitter)
        
        return page
    
    def save_splitter_position(self, splitter):
        """v4.6: Sauvegarder la position du splitter dans un fichier"""
        try:
            sizes = splitter.sizes()
            with open('gesco_splitter_pos.pkl', 'wb') as f:
                pickle.dump(sizes, f)
        except Exception as e:
            print(f"Erreur lors de la sauvegarde de la position du splitter: {e}")
    
    def load_splitter_position(self):
        """v4.6: Charger la position sauvegardée du splitter"""
        try:
            if os.path.exists('gesco_splitter_pos.pkl'):
                with open('gesco_splitter_pos.pkl', 'rb') as f:
                    return pickle.load(f)
        except Exception as e:
            print(f"Erreur lors du chargement de la position du splitter: {e}")
        return None
    
    def refresh_tiers_list(self):
        """Actualiser la liste des tiers"""
        self.tiers_list.setRowCount(0)
        
        if self.gestion.contacts.empty:
            self.tiers_count_label.setText("Total: 0 tiers")
            self.clear_tiers_details()
            return
        
        search_term = self.tiers_search_entry.text().lower()
        
        type_colors = {
            'Client': '#34C759',
            'Fournisseur': '#007AFF',
            'Prospect': '#FF9500',
            'Autre': '#86868B'
        }
        
        count = 0
        for idx, contact in self.gestion.contacts.iterrows():
            # Filtrage
            if search_term:
                nom_lower = str(contact['Nom']).lower()
                entreprise_lower = str(contact.get('Entreprise', '')).lower()
                adresse_lower = str(contact.get('Adresse_Principale', '')).lower()
                if (search_term not in nom_lower and 
                    search_term not in entreprise_lower and 
                    search_term not in adresse_lower):
                    continue
            
            row = self.tiers_list.rowCount()
            self.tiers_list.insertRow(row)
            
            # Nom
            item_nom = QTableWidgetItem(contact['Nom'])
            item_nom.setData(Qt.ItemDataRole.UserRole, idx)
            item_nom.setFont(QFont("SF Pro Text", 13, QFont.Weight.DemiBold))
            self.tiers_list.setItem(row, 0, item_nom)
            
            # Type
            item_type = QTableWidgetItem(contact['Type'])
            item_type.setForeground(QColor(type_colors.get(contact['Type'], '#1D1D1F')))
            item_type.setFont(QFont("SF Pro Text", 11))
            self.tiers_list.setItem(row, 1, item_type)
            
            # Adresse (tronquée si trop longue)
            adresse = contact.get('Adresse_Principale', '')
            if len(adresse) > 50:
                adresse = adresse[:47] + "..."
            item_adresse = QTableWidgetItem(adresse)
            item_adresse.setFont(QFont("SF Pro Text", 11))
            item_adresse.setForeground(QColor("#86868B"))
            self.tiers_list.setItem(row, 2, item_adresse)
            
            count += 1
        
        self.tiers_count_label.setText(f"Total: {count} tiers")
    
    def on_tiers_selection_changed(self):
        """Quand un tiers est sélectionné dans la liste"""
        selected_items = self.tiers_list.selectedItems()
        if not selected_items:
            self.clear_tiers_details()
            return
        
        # Récupérer l'ID du tiers sélectionné
        row = selected_items[0].row()
        item = self.tiers_list.item(row, 0)
        self.selected_tiers_id = item.data(Qt.ItemDataRole.UserRole)
        
        # Afficher les détails
        self.show_tiers_details(self.selected_tiers_id)
    
    def clear_tiers_details(self):
        """Effacer les détails du tiers"""
        while self.tiers_details_layout.count():
            child = self.tiers_details_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        # Message par défaut
        label = QLabel("Sélectionnez un tiers dans la liste pour voir les détails")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("color: #86868B; font-size: 14px; padding: 100px;")
        self.tiers_details_layout.addWidget(label)
    
    def show_tiers_details(self, tiers_id):
        """Afficher les détails d'un tiers"""
        # Effacer l'ancien contenu
        while self.tiers_details_layout.count():
            child = self.tiers_details_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        if tiers_id not in self.gestion.contacts.index:
            self.clear_tiers_details()
            return
        
        tiers = self.gestion.contacts.loc[tiers_id]
        
        # === EN-TÊTE ===
        header_frame = QFrame()
        header_frame.setStyleSheet(ModernMacOSStyleHelper.get_card_stylesheet() + 
                                   "QFrame { margin-bottom: 15px; }")
        header_layout = QVBoxLayout()
        header_layout.setContentsMargins(20, 20, 20, 20)
        header_layout.setSpacing(10)
        header_frame.setLayout(header_layout)
        
        # Ligne 1: Nom et boutons d'action
        title_layout = QHBoxLayout()
        
        nom_label = QLabel(tiers['Nom'])
        nom_label.setFont(QFont("SF Pro Text", 24, QFont.Weight.Bold))
        nom_label.setStyleSheet("color: #1D1D1F;")
        title_layout.addWidget(nom_label)
        
        title_layout.addStretch()
        
        btn_modifier = ModernMacOSSmallButton("✏️ Modifier")
        btn_modifier.clicked.connect(lambda: self.modifier_tiers(tiers_id))
        title_layout.addWidget(btn_modifier)
        
        btn_supprimer = ModernMacOSSmallButton("🗑 Supprimer")
        btn_supprimer.clicked.connect(lambda: self.supprimer_tiers(tiers_id))
        btn_supprimer.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 59, 48, 0.1);
                color: #FF3B30;
                border: none;
                border-radius: 8px;
                padding: 6px 16px;
                font-weight: 500;
                font-size: 13px;
            }
            QPushButton:hover {
                background-color: rgba(255, 59, 48, 0.2);
            }
        """)
        title_layout.addWidget(btn_supprimer)
        
        header_layout.addLayout(title_layout)
        
        # Ligne 2: Catégorie et Type
        badges_layout = QHBoxLayout()
        badges_layout.setSpacing(10)
        
        categorie_badge = QLabel(tiers.get('Categorie', 'Particulier'))
        categorie_badge.setStyleSheet("""
            QLabel {
                background-color: rgba(0, 122, 255, 0.15);
                color: #007AFF;
                border-radius: 8px;
                padding: 6px 12px;
                font-weight: 600;
                font-size: 12px;
            }
        """)
        badges_layout.addWidget(categorie_badge)
        
        type_colors = {
            'Client': ('#34C759', 'rgba(52, 199, 89, 0.15)'),
            'Fournisseur': ('#007AFF', 'rgba(0, 122, 255, 0.15)'),
            'Prospect': ('#FF9500', 'rgba(255, 149, 0, 0.15)'),
            'Autre': ('#86868B', 'rgba(134, 134, 139, 0.15)')
        }
        
        type_tiers = tiers['Type']
        color, bg_color = type_colors.get(type_tiers, ('#86868B', 'rgba(134, 134, 139, 0.15)'))
        
        type_badge = QLabel(type_tiers)
        type_badge.setStyleSheet(f"""
            QLabel {{
                background-color: {bg_color};
                color: {color};
                border-radius: 8px;
                padding: 6px 12px;
                font-weight: 600;
                font-size: 12px;
            }}
        """)
        badges_layout.addWidget(type_badge)
        
        badges_layout.addStretch()
        
        header_layout.addLayout(badges_layout)
        
        self.tiers_details_layout.addWidget(header_frame)
        
        # === INFORMATIONS GÉNÉRALES ===
        info_frame = QFrame()
        info_frame.setStyleSheet(ModernMacOSStyleHelper.get_card_stylesheet() + 
                                "QFrame { margin-bottom: 8px; }")  # Réduit de 15px à 8px
        info_layout = QVBoxLayout()
        info_layout.setContentsMargins(15, 15, 15, 15)  # Réduit de 20 à 15
        info_layout.setSpacing(12)  # Réduit de 15 à 12
        info_frame.setLayout(info_layout)
        
        info_title = QLabel("Informations générales")
        info_title.setFont(QFont("SF Pro Text", 15, QFont.Weight.Bold))  # Réduit de 16 à 15
        info_layout.addWidget(info_title)
        
        info_grid = QGridLayout()
        info_grid.setSpacing(12)  # Réduit de 15 à 12
        info_grid.setColumnStretch(1, 1)
        
        row = 0
        
        if tiers.get('Entreprise'):
            info_grid.addWidget(QLabel("🏢 Entreprise:"), row, 0)
            entreprise_label = QLabel(tiers['Entreprise'])
            entreprise_label.setStyleSheet("color: #1D1D1F; font-size: 14px;")
            info_grid.addWidget(entreprise_label, row, 1)
            row += 1
        
        if tiers.get('Email'):
            info_grid.addWidget(QLabel("📧 Email:"), row, 0)
            email_label = QLabel(tiers['Email'])
            email_label.setStyleSheet("color: #007AFF; font-size: 14px;")
            email_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
            info_grid.addWidget(email_label, row, 1)
            row += 1
        
        if tiers.get('Telephone'):
            info_grid.addWidget(QLabel("📱 Téléphone:"), row, 0)
            tel_label = QLabel(tiers['Telephone'])
            tel_label.setStyleSheet("color: #1D1D1F; font-size: 14px;")
            tel_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
            info_grid.addWidget(tel_label, row, 1)
            row += 1
        
        if tiers.get('Adresse_Principale'):
            info_grid.addWidget(QLabel("📍 Adresse:"), row, 0, Qt.AlignmentFlag.AlignTop)
            adresse_label = QLabel(tiers['Adresse_Principale'])
            adresse_label.setWordWrap(True)
            adresse_label.setStyleSheet("color: #1D1D1F; font-size: 14px;")
            adresse_label.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
            info_grid.addWidget(adresse_label, row, 1)
            row += 1
        
        info_layout.addLayout(info_grid)
        self.tiers_details_layout.addWidget(info_frame)
        
        # === CONTACTS ASSOCIÉS ===
        contacts_frame = QFrame()
        contacts_frame.setStyleSheet(ModernMacOSStyleHelper.get_card_stylesheet() + 
                                    "QFrame { margin-bottom: 8px; }")  # Réduit de 15px à 8px
        contacts_layout = QVBoxLayout()
        contacts_layout.setContentsMargins(15, 15, 15, 15)  # Réduit de 20 à 15
        contacts_layout.setSpacing(10)  # Réduit de 15 à 10
        contacts_frame.setLayout(contacts_layout)
        
        # Titre et bouton
        contacts_title_layout = QHBoxLayout()
        
        contacts_title = QLabel("Contacts associés")
        contacts_title.setFont(QFont("SF Pro Text", 15, QFont.Weight.Bold))  # Réduit de 16 à 15
        contacts_title_layout.addWidget(contacts_title)
        
        contacts_title_layout.addStretch()
        
        btn_add_contact = ModernMacOSSmallButton("+ Ajouter")
        btn_add_contact.clicked.connect(lambda: self.show_contact_associe_dialog(tiers_id))
        contacts_title_layout.addWidget(btn_add_contact)
        
        contacts_layout.addLayout(contacts_title_layout)
        
        # Liste des contacts
        contacts_associes = self.gestion.get_contacts_associes(tiers_id)
        
        if contacts_associes.empty:
            no_contacts = QLabel("Aucun contact associé")
            no_contacts.setStyleSheet("color: #86868B; font-style: italic; padding: 20px;")
            no_contacts.setAlignment(Qt.AlignmentFlag.AlignCenter)
            contacts_layout.addWidget(no_contacts)
        else:
            for idx, contact in contacts_associes.iterrows():
                contact_item = QFrame()
                contact_item.setStyleSheet("""
                    QFrame {
                        background-color: rgba(0, 0, 0, 0.02);
                        border-radius: 8px;
                        padding: 8px;
                    }
                """)
                contact_item_layout = QHBoxLayout()
                contact_item_layout.setContentsMargins(8, 8, 8, 8)  # Réduit de 10 à 8
                contact_item_layout.setSpacing(12)
                contact_item.setLayout(contact_item_layout)
                
                # Infos du contact
                contact_info = QVBoxLayout()
                contact_info.setSpacing(4)  # Réduit de 5 à 4
                
                # v4.6: Header du contact avec nom et boutons sur la même ligne
                contact_header = QHBoxLayout()
                contact_header.setSpacing(10)
                
                nom_contact = QLabel(contact['Nom'])
                nom_contact.setFont(QFont("SF Pro Text", 13, QFont.Weight.DemiBold))  # Réduit de 14 à 13
                contact_header.addWidget(nom_contact)
                
                contact_header.addStretch()
                
                # v4.6: Boutons d'action alignés avec le nom
                btn_edit = ModernMacOSSmallButton("✏️ Modifier")
                btn_edit.clicked.connect(lambda checked, c_id=idx: self.modifier_contact_associe(tiers_id, c_id))
                contact_header.addWidget(btn_edit)
                
                btn_delete = ModernMacOSSmallButton("🗑 Supprimer")
                btn_delete.setStyleSheet("""
                    QPushButton {
                        background-color: rgba(255, 59, 48, 0.1);
                        color: #FF3B30;
                        border: none;
                        border-radius: 8px;
                        padding: 6px 16px;
                        font-weight: 500;
                        font-size: 13px;
                    }
                    QPushButton:hover {
                        background-color: rgba(255, 59, 48, 0.2);
                    }
                """)
                btn_delete.clicked.connect(lambda checked, c_id=idx: self.supprimer_contact_associe(c_id))
                contact_header.addWidget(btn_delete)
                
                contact_info.addLayout(contact_header)
                
                if contact.get('Fonction'):
                    fonction = QLabel(contact['Fonction'])
                    fonction.setStyleSheet("color: #86868B; font-size: 11px;")  # Réduit de 12 à 11
                    contact_info.addWidget(fonction)
                
                details_layout = QHBoxLayout()
                details_layout.setSpacing(15)  # Réduit de 20 à 15
                
                if contact.get('Email'):
                    email = QLabel(f"📧 {contact['Email']}")
                    email.setStyleSheet("color: #007AFF; font-size: 11px;")  # Réduit de 12 à 11
                    details_layout.addWidget(email)
                
                if contact.get('Telephone'):
                    tel = QLabel(f"📱 {contact['Telephone']}")
                    tel.setStyleSheet("color: #1D1D1F; font-size: 11px;")  # Réduit de 12 à 11
                    details_layout.addWidget(tel)
                
                details_layout.addStretch()
                contact_info.addLayout(details_layout)
                
                # Afficher les adresses de chantiers associées
                adresses_associees = contact.get('Adresses_Chantiers', '')
                if adresses_associees and adresses_associees != '':
                    adresses_list = adresses_associees.split('|||')
                    if adresses_list:
                        adresses_label = QLabel(f"📍 {len(adresses_list)} adresse(s) de chantier")
                        adresses_label.setStyleSheet("color: #34C759; font-size: 11px; font-weight: 600;")
                        adresses_label.setToolTip("\n".join(adresses_list))
                        contact_info.addWidget(adresses_label)
                
                contact_item_layout.addLayout(contact_info)
                
                contacts_layout.addWidget(contact_item)
        
        self.tiers_details_layout.addWidget(contacts_frame)
        
        # === ADRESSES DE CHANTIERS ===
        adresses_frame = QFrame()
        adresses_frame.setStyleSheet(ModernMacOSStyleHelper.get_card_stylesheet() + 
                                    "QFrame { margin-bottom: 8px; }")  # Espacé comme les autres cartes
        adresses_layout = QVBoxLayout()
        adresses_layout.setContentsMargins(15, 15, 15, 15)  # Cohérent avec les autres cartes
        adresses_layout.setSpacing(10)
        adresses_frame.setLayout(adresses_layout)
        
        # Titre et bouton
        adresses_title_layout = QHBoxLayout()
        
        adresses_title = QLabel("Adresses de chantiers")
        adresses_title.setFont(QFont("SF Pro Text", 15, QFont.Weight.Bold))
        adresses_title_layout.addWidget(adresses_title)
        
        adresses_title_layout.addStretch()
        
        btn_add_adresse = ModernMacOSSmallButton("+ Ajouter")
        btn_add_adresse.clicked.connect(lambda: self.show_adresse_chantier_dialog(tiers_id))
        adresses_title_layout.addWidget(btn_add_adresse)
        
        adresses_layout.addLayout(adresses_title_layout)
        
        # Liste des adresses
        adresses = self.gestion.get_adresses_client(tiers_id)
        
        if not adresses:
            no_adresses = QLabel("Aucune adresse de chantier")
            no_adresses.setStyleSheet("color: #86868B; font-style: italic; padding: 20px;")
            no_adresses.setAlignment(Qt.AlignmentFlag.AlignCenter)
            adresses_layout.addWidget(no_adresses)
        else:
            for i, adresse in enumerate(adresses):
                adresse_item = QFrame()
                adresse_item.setStyleSheet("""
                    QFrame {
                        background-color: rgba(0, 0, 0, 0.02);
                        border-radius: 8px;
                        padding: 8px;
                    }
                """)
                adresse_item_layout = QHBoxLayout()
                adresse_item_layout.setContentsMargins(8, 8, 8, 8)
                adresse_item_layout.setSpacing(12)
                adresse_item.setLayout(adresse_item_layout)
                
                # v4.6: Icône et texte de l'adresse
                icon_label = QLabel("📍")
                icon_label.setStyleSheet("font-size: 16px;")
                adresse_item_layout.addWidget(icon_label)
                
                adresse_text = QLabel(adresse)
                adresse_text.setStyleSheet("color: #1D1D1F; font-size: 12px;")
                adresse_text.setWordWrap(True)
                adresse_item_layout.addWidget(adresse_text, stretch=1)
                
                # v4.6: Boutons d'action alignés sur la même ligne
                btn_edit_adresse = ModernMacOSSmallButton("✏️ Modifier")
                btn_edit_adresse.clicked.connect(lambda checked, idx=i, addr=adresse: self.modifier_adresse_chantier(tiers_id, idx, addr))
                adresse_item_layout.addWidget(btn_edit_adresse)
                
                btn_delete_adresse = ModernMacOSSmallButton("🗑 Supprimer")
                btn_delete_adresse.setStyleSheet("""
                    QPushButton {
                        background-color: rgba(255, 59, 48, 0.1);
                        color: #FF3B30;
                        border: none;
                        border-radius: 8px;
                        padding: 6px 16px;
                        font-weight: 500;
                        font-size: 13px;
                    }
                    QPushButton:hover {
                        background-color: rgba(255, 59, 48, 0.2);
                    }
                """)
                btn_delete_adresse.clicked.connect(lambda checked, idx=i: self.supprimer_adresse_chantier(tiers_id, idx))
                adresse_item_layout.addWidget(btn_delete_adresse)
                
                adresses_layout.addWidget(adresse_item)
        
        self.tiers_details_layout.addWidget(adresses_frame)
        
        self.tiers_details_layout.addStretch()
    
    # Méthodes pour gérer les tiers
    
    def show_tiers_dialog(self):
        """Afficher le dialogue d'ajout de tiers"""
        dialog = TiersDialog(self.gestion, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_data()
            
            if not data['Nom']:
                QMessageBox.critical(self, "Erreur", "Le nom est obligatoire")
                return
            
            new_id = self.gestion.ajouter_tiers(data)
            self.refresh_tiers_list()
            QMessageBox.information(self, "Succès", f"Tiers ajouté avec l'ID: {new_id}")
    
    def modifier_tiers(self, tiers_id):
        """Modifier un tiers existant"""
        dialog = ModifierTiersDialog(self.gestion, tiers_id, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_data()
            
            if not data['Nom']:
                QMessageBox.critical(self, "Erreur", "Le nom est obligatoire")
                return
            
            try:
                self.gestion.modifier_tiers(tiers_id, data)
                self.refresh_tiers_list()
                self.show_tiers_details(tiers_id)
                QMessageBox.information(self, "Succès", "Tiers modifié!")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur: {e}")
    
    def supprimer_tiers(self, tiers_id):
        """Supprimer un tiers"""
        reply = QMessageBox.question(
            self,
            "Confirmation",
            "Êtes-vous sûr de vouloir supprimer ce tiers et tous ses contacts associés ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                self.gestion.supprimer_tiers(tiers_id)
                self.refresh_tiers_list()
                self.clear_tiers_details()
                QMessageBox.information(self, "Succès", "Tiers supprimé!")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur: {e}")
    
    def show_contact_associe_dialog(self, tiers_id):
        """Afficher le dialogue d'ajout de contact associé"""
        dialog = ContactAssocieDialog(self.gestion, tiers_id, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_data()
            
            if not data['Nom']:
                QMessageBox.critical(self, "Erreur", "Le nom est obligatoire")
                return
            
            try:
                new_id = self.gestion.ajouter_contact_associe(tiers_id, data)
                self.show_tiers_details(tiers_id)
                QMessageBox.information(self, "Succès", f"Contact ajouté avec l'ID: {new_id}")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur: {e}")
    
    def modifier_contact_associe(self, tiers_id, contact_id):
        """Modifier un contact associé"""
        dialog = ModifierContactAssocieDialog(self.gestion, tiers_id, contact_id, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_data()
            
            if not data['Nom']:
                QMessageBox.critical(self, "Erreur", "Le nom est obligatoire")
                return
            
            try:
                self.gestion.modifier_contact_associe(contact_id, data)
                self.show_tiers_details(tiers_id)
                QMessageBox.information(self, "Succès", "Contact modifié!")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur: {e}")
    
    def supprimer_contact_associe(self, contact_id):
        """Supprimer un contact associé"""
        reply = QMessageBox.question(
            self,
            "Confirmation",
            "Êtes-vous sûr de vouloir supprimer ce contact ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                # Récupérer le tiers_id avant de supprimer
                tiers_id = self.gestion.contacts_associes.loc[contact_id, 'ID_Tiers']
                self.gestion.supprimer_contact_associe(contact_id)
                self.show_tiers_details(tiers_id)
                QMessageBox.information(self, "Succès", "Contact supprimé!")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur: {e}")
    
    def show_adresse_chantier_dialog(self, tiers_id):
        """Afficher le dialogue d'ajout d'adresse de chantier"""
        dialog = AdresseChantierDialog(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            nouvelle_adresse = dialog.get_adresse()
            
            if not nouvelle_adresse.strip():
                QMessageBox.critical(self, "Erreur", "L'adresse ne peut pas être vide")
                return
            
            try:
                # Ajouter l'adresse via la méthode appropriée
                self.gestion.ajouter_adresse_client(tiers_id, nouvelle_adresse)
                
                self.show_tiers_details(tiers_id)
                QMessageBox.information(self, "Succès", "Adresse de chantier ajoutée!")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur: {e}")
    
    def modifier_adresse_chantier(self, tiers_id, index, adresse_actuelle):
        """Modifier une adresse de chantier"""
        dialog = AdresseChantierDialog(self, adresse_actuelle)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            nouvelle_adresse = dialog.get_adresse()
            
            if not nouvelle_adresse.strip():
                QMessageBox.critical(self, "Erreur", "L'adresse ne peut pas être vide")
                return
            
            try:
                # Récupérer et modifier les adresses
                adresses = self.gestion.get_adresses_client(tiers_id)
                if index < len(adresses):
                    adresses[index] = nouvelle_adresse
                    
                    # Sauvegarder dans contacts
                    self.gestion.contacts.loc[tiers_id, 'Adresses_Chantiers'] = '|||'.join(adresses)
                    self.gestion.save_data()
                    
                    self.show_tiers_details(tiers_id)
                    QMessageBox.information(self, "Succès", "Adresse modifiée!")
                else:
                    QMessageBox.critical(self, "Erreur", "Index d'adresse invalide")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur: {e}")
    
    def supprimer_adresse_chantier(self, tiers_id, index):
        """Supprimer une adresse de chantier"""
        reply = QMessageBox.question(
            self,
            "Confirmation",
            "Êtes-vous sûr de vouloir supprimer cette adresse de chantier ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                # Récupérer et supprimer l'adresse
                adresses = self.gestion.get_adresses_client(tiers_id)
                if index < len(adresses):
                    adresses.pop(index)
                    
                    # Sauvegarder dans contacts
                    if adresses:
                        self.gestion.contacts.loc[tiers_id, 'Adresses_Chantiers'] = '|||'.join(adresses)
                    else:
                        self.gestion.contacts.loc[tiers_id, 'Adresses_Chantiers'] = ''
                    self.gestion.save_data()
                    
                    self.show_tiers_details(tiers_id)
                    QMessageBox.information(self, "Succès", "Adresse supprimée!")
                else:
                    QMessageBox.critical(self, "Erreur", "Index d'adresse invalide")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur: {e}")


    # Les méthodes create_achats_page, create_heures_page, 
    # create_chantiers_page et create_archives_page restent identiques
    
    def create_achats_page(self):
        """Page achats avec interface liste/détails (modèle Tiers)"""
        page = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)
        page.setLayout(layout)
        
        # SPLITTER pour diviser en deux parties
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setHandleWidth(1)
        
        # === PARTIE GAUCHE: Liste des achats (40%) ===
        left_widget = QWidget()
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(0, 0, 20, 0)
        left_layout.setSpacing(15)
        left_widget.setLayout(left_layout)
        
        # Barre de recherche et bouton
        search_layout = QHBoxLayout()
        search_layout.setSpacing(10)
        
        self.achats_search_entry = QLineEdit()
        self.achats_search_entry.setPlaceholderText("🔍 Rechercher...")
        self.achats_search_entry.textChanged.connect(self.refresh_achats_list)
        search_layout.addWidget(self.achats_search_entry)
        
        btn_add_achat = ModernMacOSPrimaryButton("+ Nouvel Achat")
        btn_add_achat.clicked.connect(self.show_achat_dialog)
        search_layout.addWidget(btn_add_achat)
        
        left_layout.addLayout(search_layout)
        
        # Compteur et total
        stats_layout = QHBoxLayout()
        stats_layout.setSpacing(15)
        
        self.achats_count_label = QLabel("Total: 0 achats")
        self.achats_count_label.setFont(QFont("SF Pro Text", 11))
        self.achats_count_label.setStyleSheet("color: #86868B;")
        stats_layout.addWidget(self.achats_count_label)
        
        stats_layout.addStretch()
        
        self.achats_sum_label = QLabel("0.00 €")
        self.achats_sum_label.setFont(QFont("SF Pro Text", 14, QFont.Weight.Bold))
        self.achats_sum_label.setStyleSheet("color: #007AFF;")
        stats_layout.addWidget(self.achats_sum_label)
        
        left_layout.addLayout(stats_layout)
        
        # Liste des achats
        self.achats_list = QTableWidget()
        self.achats_list.setColumnCount(4)
        self.achats_list.setHorizontalHeaderLabels(["Date", "Chantier", "Fournisseur", "Montant"])
        # Configuration des colonnes pour permettre le redimensionnement manuel
        header = self.achats_list.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Interactive)  # Date redimensionnable
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive)  # Chantier redimensionnable
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Interactive)  # Fournisseur redimensionnable
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Interactive)  # Montant redimensionnable
        self.achats_list.setColumnWidth(2, 180)
        self.achats_list.verticalHeader().setVisible(False)
        self.achats_list.verticalHeader().setDefaultSectionSize(38)
        self.achats_list.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.achats_list.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.achats_list.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        # Activer le tri sur toutes les colonnes
        self.achats_list.setSortingEnabled(True)
        self.achats_list.itemSelectionChanged.connect(self.on_achat_selection_changed)
        self.achats_list.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.achats_list.customContextMenuRequested.connect(self.show_achat_context_menu)
        left_layout.addWidget(self.achats_list)
        
        splitter.addWidget(left_widget)
        
        # === PARTIE DROITE: Détails de l'achat (60%) ===
        right_widget = QWidget()
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(20, 0, 0, 0)
        right_layout.setSpacing(20)
        right_widget.setLayout(right_layout)
        
        # Scroll area pour les détails
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; }")
        
        details_container = QWidget()
        self.achats_details_layout = QVBoxLayout()
        self.achats_details_layout.setSpacing(20)
        self.achats_details_layout.setContentsMargins(0, 0, 0, 0)
        details_container.setLayout(self.achats_details_layout)
        
        scroll.setWidget(details_container)
        right_layout.addWidget(scroll)
        
        splitter.addWidget(right_widget)
        
        # Proportions par défaut (40% - 60%)
        splitter.setSizes([400, 600])
        
        layout.addWidget(splitter)
        
        return page
    
    def create_heures_page(self):
        """Page heures avec interface liste/détails (modèle Tiers)"""
        page = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)
        page.setLayout(layout)
        
        # SPLITTER pour diviser en deux parties
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setHandleWidth(1)
        
        # === PARTIE GAUCHE: Liste des heures (40%) ===
        left_widget = QWidget()
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(0, 0, 20, 0)
        left_layout.setSpacing(15)
        left_widget.setLayout(left_layout)
        
        # Barre de recherche et bouton
        search_layout = QHBoxLayout()
        search_layout.setSpacing(10)
        
        self.heures_search_entry = QLineEdit()
        self.heures_search_entry.setPlaceholderText("🔍 Rechercher...")
        self.heures_search_entry.textChanged.connect(self.refresh_heures_list)
        search_layout.addWidget(self.heures_search_entry)
        
        btn_add_heure = ModernMacOSPrimaryButton("+ Nouvelles Heures")
        btn_add_heure.clicked.connect(self.show_heure_dialog)
        search_layout.addWidget(btn_add_heure)
        
        left_layout.addLayout(search_layout)
        
        # Compteur et total
        stats_layout = QHBoxLayout()
        stats_layout.setSpacing(15)
        
        self.heures_count_label = QLabel("Total: 0 heures")
        self.heures_count_label.setFont(QFont("SF Pro Text", 11))
        self.heures_count_label.setStyleSheet("color: #86868B;")
        stats_layout.addWidget(self.heures_count_label)
        
        stats_layout.addStretch()
        
        self.heures_sum_label = QLabel("0.0h | 0.00 €")
        self.heures_sum_label.setFont(QFont("SF Pro Text", 14, QFont.Weight.Bold))
        self.heures_sum_label.setStyleSheet("color: #007AFF;")
        stats_layout.addWidget(self.heures_sum_label)
        
        left_layout.addLayout(stats_layout)
        
        # Liste des heures
        self.heures_list = QTableWidget()
        self.heures_list.setColumnCount(4)
        self.heures_list.setHorizontalHeaderLabels(["Date", "Chantier", "Technicien", "Heures"])
        # Configuration des colonnes pour permettre le redimensionnement manuel
        header = self.heures_list.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Interactive)  # Date redimensionnable
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive)  # Chantier redimensionnable
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Interactive)  # Technicien redimensionnable
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Interactive)  # Heures redimensionnable
        self.heures_list.setColumnWidth(2, 180)
        self.heures_list.verticalHeader().setVisible(False)
        self.heures_list.verticalHeader().setDefaultSectionSize(38)
        self.heures_list.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.heures_list.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.heures_list.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        # Activer le tri sur toutes les colonnes
        self.heures_list.setSortingEnabled(True)
        self.heures_list.itemSelectionChanged.connect(self.on_heure_selection_changed)
        self.heures_list.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.heures_list.customContextMenuRequested.connect(self.show_heure_context_menu)
        left_layout.addWidget(self.heures_list)
        
        splitter.addWidget(left_widget)
        
        # === PARTIE DROITE: Détails de l'heure (60%) ===
        right_widget = QWidget()
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(20, 0, 0, 0)
        right_layout.setSpacing(20)
        right_widget.setLayout(right_layout)
        
        # Scroll area pour les détails
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; }")
        
        details_container = QWidget()
        self.heures_details_layout = QVBoxLayout()
        self.heures_details_layout.setSpacing(20)
        self.heures_details_layout.setContentsMargins(0, 0, 0, 0)
        details_container.setLayout(self.heures_details_layout)
        
        scroll.setWidget(details_container)
        right_layout.addWidget(scroll)
        
        splitter.addWidget(right_widget)
        
        # Proportions par défaut (40% - 60%)
        splitter.setSizes([400, 600])
        
        layout.addWidget(splitter)
        
        return page
    
    def create_chantiers_page(self):
        """Page chantiers avec barre d'actions"""
        page = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)
        page.setLayout(layout)
        
        # Barre d'actions
        actions_frame = QFrame()
        actions_frame.setStyleSheet("QFrame { background-color: transparent; border: none; }")
        actions_layout = QHBoxLayout()
        actions_layout.setSpacing(12)
        actions_layout.setContentsMargins(0, 0, 0, 0)
        actions_frame.setLayout(actions_layout)
        
        btn_add = ModernMacOSPrimaryButton("+ Nouveau Chantier")
        btn_add.clicked.connect(self.show_chantier_dialog)
        actions_layout.addWidget(btn_add)
        
        self.search_entry = QLineEdit()
        self.search_entry.setPlaceholderText("🔍 Rechercher...")
        self.search_entry.setMaximumWidth(400)
        self.search_entry.textChanged.connect(self.refresh_chantiers)
        actions_layout.addWidget(self.search_entry)
        
        # Filtres radio
        filter_widget = QWidget()
        filter_widget.setStyleSheet("QWidget { background-color: transparent; }")
        filter_layout = QHBoxLayout()
        filter_layout.setSpacing(8)
        filter_layout.setContentsMargins(0, 0, 0, 0)
        filter_widget.setLayout(filter_layout)
        
        filter_label = QLabel("Statut budget:")
        filter_label.setStyleSheet("color: #86868B; font-size: 12px;")
        filter_layout.addWidget(filter_label)
        
        self.filter_group = QButtonGroup()
        
        statuts = ["Tous", "Excellent", "Normal", "Attention", "Alerte"]
        for statut in statuts:
            radio = QRadioButton(statut)
            radio.toggled.connect(self.refresh_chantiers)
            self.filter_group.addButton(radio)
            filter_layout.addWidget(radio)
        
        self.filter_group.buttons()[0].setChecked(True)
        
        actions_layout.addWidget(filter_widget)
        actions_layout.addStretch()
        
        layout.addWidget(actions_frame)
        
        self.chantiers_table = QTableWidget()
        self.chantiers_table.setColumnCount(10)
        self.chantiers_table.setHorizontalHeaderLabels([
            "Client", "N° Commande", "Adresse", "Ouverture", 
            "Durée", "Chiffrage", "Achats Est.", "Dépenses", "Heures", "État"
        ])
        
        # Configuration des colonnes pour permettre le redimensionnement manuel
        header = self.chantiers_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Interactive)  # Client redimensionnable
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive)  # N° Commande redimensionnable
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Interactive)  # Adresse redimensionnable
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Interactive)  # Ouverture redimensionnable
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Interactive)  # Durée redimensionnable
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.Interactive)  # Chiffrage redimensionnable
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.Interactive)  # Achats Est. redimensionnable
        header.setSectionResizeMode(7, QHeaderView.ResizeMode.Interactive)  # Dépenses redimensionnable
        header.setSectionResizeMode(8, QHeaderView.ResizeMode.Interactive)  # Heures redimensionnable
        header.setSectionResizeMode(9, QHeaderView.ResizeMode.Interactive)  # État redimensionnable
        self.chantiers_table.setColumnWidth(0, 150)
        
        self.chantiers_table.verticalHeader().setVisible(False)
        self.chantiers_table.verticalHeader().setDefaultSectionSize(24)
        self.chantiers_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        # Activer le tri sur toutes les colonnes
        self.chantiers_table.setSortingEnabled(True)
        self.chantiers_table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.chantiers_table.customContextMenuRequested.connect(self.show_chantier_context_menu)
        
        # Style pour améliorer l'apparence et réduire les bordures de grille
        self.chantiers_table.setStyleSheet("""
            QTableWidget {
                gridline-color: rgba(0, 0, 0, 0.05);
                background-color: white;
            }
            QTableWidget::item {
                border: none;
                padding: 4px;
            }
        """)
        
        layout.addWidget(self.chantiers_table)
        
        return page
    
    def create_archives_page(self):
        """Page archives avec barre d'actions"""
        page = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)
        page.setLayout(layout)
        
        # Barre d'actions
        actions_frame = QFrame()
        actions_frame.setStyleSheet("QFrame { background-color: transparent; border: none; }")
        actions_layout = QHBoxLayout()
        actions_layout.setSpacing(12)
        actions_layout.setContentsMargins(0, 0, 0, 0)
        actions_frame.setLayout(actions_layout)
        
        self.archives_search_entry = QLineEdit()
        self.archives_search_entry.setPlaceholderText("🔍 Rechercher dans les archives...")
        self.archives_search_entry.setMaximumWidth(400)
        self.archives_search_entry.textChanged.connect(self.refresh_archives)
        actions_layout.addWidget(self.archives_search_entry)
        
        actions_layout.addStretch()
        
        layout.addWidget(actions_frame)
        
        self.archives_table = QTableWidget()
        self.archives_table.setColumnCount(10)
        self.archives_table.setHorizontalHeaderLabels([
            "Client", "N° Commande", "Adresse", "Ouverture", 
            "Clôture", "Statut", "Durée", "Chiffrage", "Dépenses", "Heures"
        ])
        
        # Configuration des colonnes pour permettre le redimensionnement manuel
        header = self.archives_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Interactive)  # Client redimensionnable
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive)  # N° Commande redimensionnable
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Interactive)  # Adresse redimensionnable
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Interactive)  # Ouverture redimensionnable
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Interactive)  # Clôture redimensionnable
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.Interactive)  # Statut redimensionnable
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.Interactive)  # Durée redimensionnable
        header.setSectionResizeMode(7, QHeaderView.ResizeMode.Interactive)  # Chiffrage redimensionnable
        header.setSectionResizeMode(8, QHeaderView.ResizeMode.Interactive)  # Dépenses redimensionnable
        header.setSectionResizeMode(9, QHeaderView.ResizeMode.Interactive)  # Heures redimensionnable
        self.archives_table.setColumnWidth(0, 150)
        
        self.archives_table.verticalHeader().setVisible(False)
        self.archives_table.verticalHeader().setDefaultSectionSize(28)
        self.archives_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        # Activer le tri sur toutes les colonnes
        self.archives_table.setSortingEnabled(True)
        self.archives_table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.archives_table.customContextMenuRequested.connect(self.show_archive_context_menu)
        
        layout.addWidget(self.archives_table)
        
        return page
    
    def create_factures_page(self):
        """Page factures avec barre d'actions à fond transparent"""
        page = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(20)
        page.setLayout(layout)
        
        # Barre d'actions avec fond transparent
        actions_frame = QFrame()
        actions_frame.setStyleSheet("QFrame { background-color: transparent; border: none; }")
        actions_layout = QHBoxLayout()
        actions_layout.setSpacing(12)
        actions_layout.setContentsMargins(0, 0, 0, 0)
        actions_frame.setLayout(actions_layout)
        
        # Bouton actualiser pour les factures
        self.btn_refresh_factures = ModernMacOSSecondaryButton("🔄 Actualiser")
        self.btn_refresh_factures.clicked.connect(self.refresh_factures)
        actions_layout.addWidget(self.btn_refresh_factures)
        
        actions_layout.addStretch()
        
        # Label de statut SANS fond coloré
        self.factures_status_label = QLabel("Chargement...")
        self.factures_status_label.setFont(QFont("SF Pro Text", 12))
        self.factures_status_label.setStyleSheet("color: #86868B;")
        actions_layout.addWidget(self.factures_status_label)
        
        self.factures_sum_label = QLabel("Total: 0.00 €")
        self.factures_sum_label.setFont(QFont("SF Pro Text", 14, QFont.Weight.Bold))
        self.factures_sum_label.setStyleSheet("""
            background-color: #007AFF; 
            padding: 8px 20px; 
            border-radius: 8px;
            color: white;
        """)
        actions_layout.addWidget(self.factures_sum_label)
        
        layout.addWidget(actions_frame)
        
        self.factures_table = QTableWidget()
        self.factures_table.setColumnCount(10)
        self.factures_table.setHorizontalHeaderLabels([
            "N° Facture", "Date", "Client", "Montant HT", "Montant TVA", 
            "Total TTC", "Date échéance", "Statut paiement", "Devise", "Liens PDF"
        ])
        
        # Configuration des colonnes pour permettre le redimensionnement manuel
        header = self.factures_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Interactive)  # N° Facture redimensionnable
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive)  # Date redimensionnable
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Interactive)  # Client redimensionnable
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Interactive)  # Montant HT redimensionnable
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Interactive)  # Montant TVA redimensionnable
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.Interactive)  # Total TTC redimensionnable
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.Interactive)  # Date échéance redimensionnable
        header.setSectionResizeMode(7, QHeaderView.ResizeMode.Interactive)  # Statut redimensionnable
        header.setSectionResizeMode(8, QHeaderView.ResizeMode.Interactive)  # Devise redimensionnable
        header.setSectionResizeMode(9, QHeaderView.ResizeMode.Interactive)  # Liens PDF redimensionnable
        self.factures_table.setColumnWidth(9, 100)
        
        self.factures_table.verticalHeader().setVisible(False)
        self.factures_table.verticalHeader().setDefaultSectionSize(28)
        self.factures_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        # Activer le tri sur toutes les colonnes
        self.factures_table.setSortingEnabled(True)
        
        layout.addWidget(self.factures_table)
        
        return page
    
    # Méthodes de menu contextuel (identiques)
    
    def show_achat_context_menu(self, position):
        """Menu contextuel achats"""
        row = self.achats_table.rowAt(position.y())
        if row < 0:
            return
        
        item = self.achats_table.item(row, 0)
        if not item:
            return
        
        achat_id = item.data(Qt.ItemDataRole.UserRole)
        if not achat_id or achat_id not in self.gestion.achats.index:
            return
        
        menu = QMenu(self)
        
        action_modifier = QAction("✏️ Modifier", self)
        action_modifier.triggered.connect(lambda: self.modifier_achat(achat_id))
        menu.addAction(action_modifier)
        
        menu.addSeparator()
        
        action_supprimer = QAction("🗑 Supprimer", self)
        action_supprimer.triggered.connect(lambda: self.supprimer_achat(achat_id))
        menu.addAction(action_supprimer)
        
        menu.exec(self.achats_table.mapToGlobal(position))
    
    def show_heure_context_menu(self, position):
        """Menu contextuel heures"""
        row = self.heures_table.rowAt(position.y())
        if row < 0:
            return
        
        item = self.heures_table.item(row, 0)
        if not item:
            return
        
        heure_id = item.data(Qt.ItemDataRole.UserRole)
        if not heure_id or heure_id not in self.gestion.heures.index:
            return
        
        menu = QMenu(self)
        
        action_modifier = QAction("✏️ Modifier", self)
        action_modifier.triggered.connect(lambda: self.modifier_heures(heure_id))
        menu.addAction(action_modifier)
        
        menu.addSeparator()
        
        action_supprimer = QAction("🗑 Supprimer", self)
        action_supprimer.triggered.connect(lambda: self.supprimer_heures(heure_id))
        menu.addAction(action_supprimer)
        
        menu.exec(self.heures_table.mapToGlobal(position))
    
    def show_chantier_context_menu(self, position):
        """Menu contextuel chantiers"""
        row = self.chantiers_table.rowAt(position.y())
        if row < 0:
            return
        
        item = self.chantiers_table.item(row, 0)
        if not item:
            return
        
        chantier_id = item.data(Qt.ItemDataRole.UserRole)
        if not chantier_id or chantier_id not in self.gestion.chantiers.index:
            return
        
        menu = QMenu(self)
        
        action_modifier = QAction("✏️ Modifier", self)
        action_modifier.triggered.connect(lambda: self.modifier_chantier(chantier_id))
        menu.addAction(action_modifier)
        
        action_cloturer = QAction("🔒 Clôturer", self)
        action_cloturer.triggered.connect(lambda: self.cloturer_chantier(chantier_id))
        menu.addAction(action_cloturer)
        
        action_archiver = QAction("📦 Archiver", self)
        action_archiver.triggered.connect(lambda: self.archiver_chantier(chantier_id))
        menu.addAction(action_archiver)
        
        menu.addSeparator()
        
        action_supprimer = QAction("🗑 Supprimer", self)
        action_supprimer.triggered.connect(lambda: self.supprimer_chantier(chantier_id))
        menu.addAction(action_supprimer)
        
        menu.exec(self.chantiers_table.mapToGlobal(position))
    
    def show_archive_context_menu(self, position):
        """Menu contextuel archives"""
        row = self.archives_table.rowAt(position.y())
        if row < 0:
            return
        
        item = self.archives_table.item(row, 0)
        if not item:
            return
        
        chantier_id = item.data(Qt.ItemDataRole.UserRole)
        if not chantier_id or chantier_id not in self.gestion.chantiers.index:
            return
        
        menu = QMenu(self)
        
        action_desarchiver = QAction("♻️ Désarchiver", self)
        action_desarchiver.triggered.connect(lambda: self.desarchiver_chantier(chantier_id))
        menu.addAction(action_desarchiver)
        
        menu.addSeparator()
        
        action_supprimer = QAction("🗑 Supprimer", self)
        action_supprimer.triggered.connect(lambda: self.supprimer_chantier(chantier_id))
        menu.addAction(action_supprimer)
        
        menu.exec(self.archives_table.mapToGlobal(position))
    
    # Méthodes de modification/suppression
    
    def modifier_achat(self, achat_id):
        """Modifier un achat existant"""
        dialog = ModifierAchatDialog(self.gestion, achat_id, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_data()
            
            if not data['ID_Chantier']:
                QMessageBox.critical(self, "Erreur", "Chantier invalide")
                return
            
            try:
                montant = float(data['Montant'])
                if montant <= 0:
                    raise ValueError()
            except:
                QMessageBox.critical(self, "Erreur", "Le montant doit être un nombre positif")
                return
            
            try:
                self.gestion.modifier_achat(achat_id, data)
                self.refresh_achats_list()
                QMessageBox.information(self, "Succès", "Achat modifié!")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur: {e}")
    
    def supprimer_achat(self, achat_id):
        """Supprimer un achat"""
        reply = QMessageBox.question(
            self,
            "Confirmation",
            "Êtes-vous sûr de vouloir supprimer cet achat ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                self.gestion.supprimer_achat(achat_id)
                self.refresh_achats_list()
                QMessageBox.information(self, "Succès", "Achat supprimé!")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur: {e}")
    
    def modifier_heures(self, heure_id):
        """Modifier des heures existantes"""
        dialog = ModifierHeureDialog(self.gestion, heure_id, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_data()
            
            if not data['ID_Chantier']:
                QMessageBox.critical(self, "Erreur", "Chantier invalide")
                return
            
            try:
                heures = float(data['Heures'])
                if heures <= 0:
                    raise ValueError()
            except:
                QMessageBox.critical(self, "Erreur", "Les heures doivent être un nombre positif")
                return
            
            try:
                self.gestion.modifier_heures(heure_id, data)
                self.refresh_heures_list()
                QMessageBox.information(self, "Succès", "Heures modifiées!")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur: {e}")
    
    def supprimer_heures(self, heure_id):
        """Supprimer des heures"""
        reply = QMessageBox.question(
            self,
            "Confirmation",
            "Êtes-vous sûr de vouloir supprimer ces heures ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                self.gestion.supprimer_heures(heure_id)
                self.refresh_heures_list()
                QMessageBox.information(self, "Succès", "Heures supprimées!")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur: {e}")
    
    def modifier_chantier(self, chantier_id):
        """Modifier un chantier existant"""
        dialog = ModifierChantierDialog(self.gestion, chantier_id, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_data()
            
            if not data['Numero_Commande_Client']:
                QMessageBox.critical(self, "Erreur", "Le numéro de commande est obligatoire")
                return
            
            try:
                chiffrage = float(data['Chiffrage_Global'])
                if chiffrage <= 0:
                    raise ValueError()
            except:
                QMessageBox.critical(self, "Erreur", "Le chiffrage global doit être un nombre positif")
                return
            
            try:
                duree = int(data['Duree_Prevue_Jours'])
                if duree <= 0:
                    raise ValueError()
            except:
                QMessageBox.critical(self, "Erreur", "La durée doit être un nombre entier positif")
                return
            
            client_name = dialog.client_combo.currentText()
            data['Nom_Client'] = client_name
            
            try:
                self.gestion.modifier_chantier(chantier_id, data)
                
                if data['Adresse_Chantier']:
                    self.gestion.ajouter_adresse_client(data['ID_Client'], data['Adresse_Chantier'])
                    
                    # Rafraîchir les détails du tiers si c'est le tiers sélectionné
                    if hasattr(self, 'selected_tiers_id') and self.selected_tiers_id == data['ID_Client']:
                        self.show_tiers_details(self.selected_tiers_id)
                
                self.refresh_chantiers()
                QMessageBox.information(self, "Succès", "Chantier modifié!")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur: {e}")
    
    def cloturer_chantier(self, chantier_id):
        """Clôturer un chantier"""
        reply = QMessageBox.question(
            self,
            "Confirmation",
            "Êtes-vous sûr de vouloir clôturer ce chantier ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                self.gestion.cloturer_chantier(chantier_id)
                self.refresh_chantiers()
                QMessageBox.information(self, "Succès", "Chantier clôturé!")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur: {e}")
    
    def archiver_chantier(self, chantier_id):
        """Archiver un chantier"""
        reply = QMessageBox.question(
            self,
            "Confirmation",
            "Êtes-vous sûr de vouloir archiver ce chantier ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                self.gestion.archiver_chantier(chantier_id)
                self.refresh_chantiers()
                QMessageBox.information(self, "Succès", "Chantier archivé!")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur: {e}")
    
    def desarchiver_chantier(self, chantier_id):
        """Désarchiver un chantier"""
        reply = QMessageBox.question(
            self,
            "Confirmation",
            "Êtes-vous sûr de vouloir désarchiver ce chantier ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                self.gestion.desarchiver_chantier(chantier_id)
                self.refresh_archives()
                QMessageBox.information(self, "Succès", "Chantier désarchivé!")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur: {e}")
    
    def supprimer_chantier(self, chantier_id):
        """Supprimer un chantier"""
        reply = QMessageBox.question(
            self,
            "Confirmation",
            "Êtes-vous sûr de vouloir supprimer ce chantier ?\nToutes les données associées (achats, heures) seront également supprimées.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            try:
                self.gestion.supprimer_chantier(chantier_id)
                self.refresh_chantiers()
                self.refresh_archives()
                QMessageBox.information(self, "Succès", "Chantier supprimé!")
            except Exception as e:
                QMessageBox.critical(self, "Erreur", f"Erreur: {e}")
    
    # Dialogs
    
    def show_chantier_dialog(self):
        """Afficher le dialog de création de chantier"""
        dialog = ChantierDialog(self.gestion, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_data()
            
            if not data['Numero_Commande_Client']:
                QMessageBox.critical(self, "Erreur", "Le numéro de commande est obligatoire")
                return
            
            if not data['ID_Client']:
                QMessageBox.critical(self, "Erreur", "Le client est obligatoire")
                return
            
            try:
                chiffrage = float(data['Chiffrage_Global'])
                if chiffrage <= 0:
                    raise ValueError()
            except:
                QMessageBox.critical(self, "Erreur", "Le chiffrage global doit être un nombre positif")
                return
            
            try:
                duree = int(data['Duree_Prevue_Jours'])
                if duree <= 0:
                    raise ValueError()
            except:
                QMessageBox.critical(self, "Erreur", "La durée doit être un nombre entier positif")
                return
            
            client_name = dialog.client_combo.currentText()
            new_id = self.gestion.ajouter_chantier(data, client_name)
            
            if data['Adresse_Chantier']:
                self.gestion.ajouter_adresse_client(data['ID_Client'], data['Adresse_Chantier'])
                
                # Rafraîchir les détails du tiers si c'est le tiers sélectionné
                if hasattr(self, 'selected_tiers_id') and self.selected_tiers_id == data['ID_Client']:
                    self.show_tiers_details(self.selected_tiers_id)
            
            self.refresh_chantiers()
            QMessageBox.information(self, "Succès", f"Chantier créé avec l'ID: {new_id}")
    
    def show_achat_dialog(self):
        """Afficher le dialog d'ajout d'achat"""
        if self.gestion.chantiers.empty:
            QMessageBox.warning(self, "Attention", "Veuillez d'abord créer un chantier")
            return
        
        dialog = AchatDialog(self.gestion, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_data()
            
            if not data['ID_Chantier']:
                QMessageBox.critical(self, "Erreur", "Chantier invalide")
                return
            
            try:
                montant = float(data['Montant'])
                if montant <= 0:
                    raise ValueError()
            except:
                QMessageBox.critical(self, "Erreur", "Le montant doit être un nombre positif")
                return
            
            new_id = self.gestion.ajouter_achat(data)
            
            # Basculer vers la page Achats (index 1)
            self.switch_page(1)
            
            # Rafraîchir l'affichage
            QMessageBox.information(self, "Succès", f"Achat ajouté avec l'ID: {new_id}")
    
    def show_heure_dialog(self):
        """Afficher le dialog d'ajout d'heures"""
        if self.gestion.chantiers.empty:
            QMessageBox.warning(self, "Attention", "Veuillez d'abord créer un chantier")
            return
        
        dialog = HeureDialog(self.gestion, self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            data = dialog.get_data()
            
            if not data['ID_Chantier']:
                QMessageBox.critical(self, "Erreur", "Chantier invalide")
                return
            
            try:
                heures = float(data['Heures'])
                if heures <= 0:
                    raise ValueError()
            except:
                QMessageBox.critical(self, "Erreur", "Les heures doivent être un nombre positif")
                return
            
            new_id = self.gestion.ajouter_heures(data)
            
            # Basculer vers la page Heures (index 2)
            self.switch_page(2)
            
            # Rafraîchir l'affichage
            QMessageBox.information(self, "Succès", f"Heures ajoutées avec l'ID: {new_id}")

    
    # Méthodes d'actualisation
    
    def format_date_francais(self, date_str):
        """Formater une date au format français"""
        if not date_str or date_str == '':
            return 'N/A'
        try:
            date_obj = datetime.strptime(str(date_str), '%Y-%m-%d')
            return date_obj.strftime('%d/%m/%Y')
        except:
            return str(date_str)
    
    def create_info_row(self, label_text, value_text):
        """Créer une ligne d'information avec label et valeur"""
        row_layout = QHBoxLayout()
        row_layout.setSpacing(10)
        
        label = QLabel(label_text)
        label.setFont(QFont("SF Pro Text", 12, QFont.Weight.DemiBold))
        label.setStyleSheet("color: #86868B;")
        label.setMinimumWidth(150)
        row_layout.addWidget(label)
        
        value = QLabel(value_text)
        value.setFont(QFont("SF Pro Text", 13))
        value.setStyleSheet("color: #1D1D1F;")
        value.setWordWrap(True)
        row_layout.addWidget(value, stretch=1)
        
        return row_layout
    
    def create_stat_card(self, title, value, color):
        """Créer une carte de statistique"""
        card = QFrame()
        card.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.8);
                border-radius: 16px;
                border: 1px solid rgba(0, 0, 0, 0.04);
                padding: 20px;
            }
        """)
        
        layout = QVBoxLayout()
        layout.setSpacing(10)
        card.setLayout(layout)
        
        title_label = QLabel(title)
        title_label.setFont(QFont("SF Pro Text", 13))
        title_label.setStyleSheet("color: #86868B;")
        layout.addWidget(title_label)
        
        value_label = QLabel(value)
        value_label.setFont(QFont("SF Pro Text", 32, QFont.Weight.Bold))
        value_label.setStyleSheet(f"color: {color};")
        layout.addWidget(value_label)
        
        return card
    
    def refresh_achats_list(self):
        """Actualiser la liste des achats"""
        if not hasattr(self, 'achats_list'):
            return
        
        self.achats_list.setRowCount(0)
        
        if self.gestion.achats.empty:
            self.achats_count_label.setText("Total: 0 achats")
            self.achats_sum_label.setText("0.00 €")
            self.clear_achats_details()
            return
        
        search_term = self.achats_search_entry.text().lower()
        
        count = 0
        total_montant = 0.0
        
        for idx, achat in self.gestion.achats.iterrows():
            # Filtrage
            if search_term:
                fournisseur_lower = str(achat['Fournisseur']).lower()
                desc_lower = str(achat['Description']).lower()
                if search_term not in fournisseur_lower and search_term not in desc_lower:
                    continue
            
            row = self.achats_list.rowCount()
            self.achats_list.insertRow(row)
            
            # Date
            date_fr = self.format_date_francais(str(achat['Date']))
            item_date = QTableWidgetItem(date_fr)
            item_date.setData(Qt.ItemDataRole.UserRole, idx)
            item_date.setFont(QFont("SF Pro Text", 11))
            self.achats_list.setItem(row, 0, item_date)
            
            # Chantier
            try:
                chantier = self.gestion.chantiers.loc[achat['ID_Chantier']]
                item_chantier = QTableWidgetItem(chantier['Numero_Commande_Client'])
            except:
                item_chantier = QTableWidgetItem("N/A")
            item_chantier.setFont(QFont("SF Pro Text", 11))
            self.achats_list.setItem(row, 1, item_chantier)
            
            # Fournisseur
            item_fournisseur = QTableWidgetItem(achat['Fournisseur'])
            item_fournisseur.setFont(QFont("SF Pro Text", 11, QFont.Weight.DemiBold))
            self.achats_list.setItem(row, 2, item_fournisseur)
            
            # Montant
            montant = float(achat['Montant'])
            item_montant = QTableWidgetItem(f"{montant:.2f}€")
            item_montant.setFont(QFont("SF Pro Text", 11, QFont.Weight.Bold))
            item_montant.setForeground(QColor("#007AFF"))
            item_montant.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            self.achats_list.setItem(row, 3, item_montant)
            
            count += 1
            total_montant += montant
        
        self.achats_count_label.setText(f"Total: {count} achats")
        self.achats_sum_label.setText(f"{total_montant:,.2f} €")
    
    def on_achat_selection_changed(self):
        """Quand un achat est sélectionné dans la liste"""
        selected_items = self.achats_list.selectedItems()
        if not selected_items:
            self.clear_achats_details()
            return
        
        # Récupérer l'ID de l'achat sélectionné
        row = selected_items[0].row()
        item = self.achats_list.item(row, 0)
        achat_id = item.data(Qt.ItemDataRole.UserRole)
        
        # Afficher les détails
        self.show_achat_details(achat_id)
    
    def clear_achats_details(self):
        """Effacer les détails de l'achat"""
        while self.achats_details_layout.count():
            child = self.achats_details_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        # Message par défaut
        label = QLabel("Sélectionnez un achat dans la liste pour voir les détails")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("color: #86868B; font-size: 14px; padding: 100px;")
        self.achats_details_layout.addWidget(label)
    
    def show_achat_details(self, achat_id):
        """Afficher les détails d'un achat"""
        # Effacer l'ancien contenu
        while self.achats_details_layout.count():
            child = self.achats_details_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        if achat_id not in self.gestion.achats.index:
            self.clear_achats_details()
            return
        
        achat = self.gestion.achats.loc[achat_id]
        
        # === EN-TÊTE ===
        header_frame = QFrame()
        header_frame.setStyleSheet(ModernMacOSStyleHelper.get_card_stylesheet())
        header_layout = QVBoxLayout()
        header_layout.setContentsMargins(20, 20, 20, 20)
        header_layout.setSpacing(15)
        header_frame.setLayout(header_layout)
        
        # Titre
        title_label = QLabel(achat['Fournisseur'])
        title_label.setFont(QFont("SF Pro Text", 20, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #1D1D1F;")
        header_layout.addWidget(title_label)
        
        # Type d'achat
        type_label = QLabel(f"Type: {achat['Type_Achat']}")
        type_label.setFont(QFont("SF Pro Text", 12))
        type_label.setStyleSheet("color: #86868B;")
        header_layout.addWidget(type_label)
        
        # Montant en gros
        montant_label = QLabel(f"{float(achat['Montant']):.2f} €")
        montant_label.setFont(QFont("SF Pro Text", 32, QFont.Weight.Bold))
        montant_label.setStyleSheet("color: #007AFF;")
        header_layout.addWidget(montant_label)
        
        # Boutons d'action
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(10)
        
        btn_modifier = ModernMacOSSecondaryButton("✏️ Modifier")
        btn_modifier.clicked.connect(lambda: self.modifier_achat(achat_id))
        buttons_layout.addWidget(btn_modifier)
        
        btn_supprimer = QPushButton("🗑 Supprimer")
        btn_supprimer.setStyleSheet("""
            QPushButton {
                background-color: #FF3B30;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 13px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #D72B21;
            }
        """)
        btn_supprimer.clicked.connect(lambda: self.supprimer_achat(achat_id))
        buttons_layout.addWidget(btn_supprimer)
        
        buttons_layout.addStretch()
        
        header_layout.addLayout(buttons_layout)
        
        self.achats_details_layout.addWidget(header_frame)
        
        # === INFORMATIONS ===
        info_frame = QFrame()
        info_frame.setStyleSheet(ModernMacOSStyleHelper.get_card_stylesheet())
        info_layout = QVBoxLayout()
        info_layout.setContentsMargins(20, 20, 20, 20)
        info_layout.setSpacing(12)
        info_frame.setLayout(info_layout)
        
        # Titre de section
        section_title = QLabel("📋 Informations")
        section_title.setFont(QFont("SF Pro Text", 16, QFont.Weight.Bold))
        section_title.setStyleSheet("color: #1D1D1F; margin-bottom: 10px;")
        info_layout.addWidget(section_title)
        
        # Date
        date_fr = self.format_date_francais(str(achat['Date']))
        date_row = self.create_info_row("Date:", date_fr)
        info_layout.addLayout(date_row)
        
        # Chantier
        try:
            chantier = self.gestion.chantiers.loc[achat['ID_Chantier']]
            chantier_text = f"{chantier['Numero_Commande_Client']}"
        except:
            chantier_text = "N/A"
        chantier_row = self.create_info_row("Chantier:", chantier_text)
        info_layout.addLayout(chantier_row)
        
        # N° BL
        bl_row = self.create_info_row("N° Bon de Livraison:", achat['Numero_BL'])
        info_layout.addLayout(bl_row)
        
        self.achats_details_layout.addWidget(info_frame)
        
        # === DESCRIPTION ===
        if achat['Description']:
            desc_frame = QFrame()
            desc_frame.setStyleSheet(ModernMacOSStyleHelper.get_card_stylesheet())
            desc_layout = QVBoxLayout()
            desc_layout.setContentsMargins(20, 20, 20, 20)
            desc_layout.setSpacing(12)
            desc_frame.setLayout(desc_layout)
            
            desc_title = QLabel("📝 Description")
            desc_title.setFont(QFont("SF Pro Text", 16, QFont.Weight.Bold))
            desc_title.setStyleSheet("color: #1D1D1F; margin-bottom: 10px;")
            desc_layout.addWidget(desc_title)
            
            desc_text = QLabel(achat['Description'])
            desc_text.setWordWrap(True)
            desc_text.setFont(QFont("SF Pro Text", 13))
            desc_text.setStyleSheet("color: #1D1D1F; line-height: 1.5;")
            desc_layout.addWidget(desc_text)
            
            self.achats_details_layout.addWidget(desc_frame)
        
        self.achats_details_layout.addStretch()
    
    def refresh_heures_list(self):
        """Actualiser la liste des heures"""
        if not hasattr(self, 'heures_list'):
            return
        
        self.heures_list.setRowCount(0)
        
        if self.gestion.heures.empty:
            self.heures_count_label.setText("Total: 0 heures")
            self.heures_sum_label.setText("0.0h | 0.00 €")
            self.clear_heures_details()
            return
        
        search_term = self.heures_search_entry.text().lower()
        
        count = 0
        total_heures = 0.0
        total_cout = 0.0
        
        for idx, heure in self.gestion.heures.iterrows():
            # Filtrage
            if search_term:
                technicien_lower = str(heure['Technicien']).lower()
                desc_lower = str(heure['Description']).lower()
                if search_term not in technicien_lower and search_term not in desc_lower:
                    continue
            
            row = self.heures_list.rowCount()
            self.heures_list.insertRow(row)
            
            # Date
            date_fr = self.format_date_francais(str(heure['Date']))
            item_date = QTableWidgetItem(date_fr)
            item_date.setData(Qt.ItemDataRole.UserRole, idx)
            item_date.setFont(QFont("SF Pro Text", 11))
            self.heures_list.setItem(row, 0, item_date)
            
            # Chantier
            try:
                chantier = self.gestion.chantiers.loc[heure['ID_Chantier']]
                item_chantier = QTableWidgetItem(chantier['Numero_Commande_Client'])
            except:
                item_chantier = QTableWidgetItem("N/A")
            item_chantier.setFont(QFont("SF Pro Text", 11))
            self.heures_list.setItem(row, 1, item_chantier)
            
            # Technicien
            item_technicien = QTableWidgetItem(heure['Technicien'])
            item_technicien.setFont(QFont("SF Pro Text", 11, QFont.Weight.DemiBold))
            self.heures_list.setItem(row, 2, item_technicien)
            
            # Heures
            nb_heures = float(heure['Heures'])
            item_heures = QTableWidgetItem(f"{nb_heures:.1f}h")
            item_heures.setFont(QFont("SF Pro Text", 11, QFont.Weight.Bold))
            item_heures.setForeground(QColor("#007AFF"))
            item_heures.setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            self.heures_list.setItem(row, 3, item_heures)
            
            count += 1
            total_heures += nb_heures
            cout_horaire = heure.get('Cout_Horaire', 0)
            total_cout += nb_heures * float(cout_horaire)
        
        self.heures_count_label.setText(f"Total: {count} heures")
        self.heures_sum_label.setText(f"{total_heures:.1f}h | {total_cout:,.2f} €")
    
    def on_heure_selection_changed(self):
        """Quand une heure est sélectionnée dans la liste"""
        selected_items = self.heures_list.selectedItems()
        if not selected_items:
            self.clear_heures_details()
            return
        
        # Récupérer l'ID de l'heure sélectionnée
        row = selected_items[0].row()
        item = self.heures_list.item(row, 0)
        heure_id = item.data(Qt.ItemDataRole.UserRole)
        
        # Afficher les détails
        self.show_heure_details(heure_id)
    
    def clear_heures_details(self):
        """Effacer les détails de l'heure"""
        while self.heures_details_layout.count():
            child = self.heures_details_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        # Message par défaut
        label = QLabel("Sélectionnez une entrée dans la liste pour voir les détails")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("color: #86868B; font-size: 14px; padding: 100px;")
        self.heures_details_layout.addWidget(label)
    
    def show_heure_details(self, heure_id):
        """Afficher les détails d'une heure"""
        # Effacer l'ancien contenu
        while self.heures_details_layout.count():
            child = self.heures_details_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        if heure_id not in self.gestion.heures.index:
            self.clear_heures_details()
            return
        
        heure = self.gestion.heures.loc[heure_id]
        
        # === EN-TÊTE ===
        header_frame = QFrame()
        header_frame.setStyleSheet(ModernMacOSStyleHelper.get_card_stylesheet())
        header_layout = QVBoxLayout()
        header_layout.setContentsMargins(20, 20, 20, 20)
        header_layout.setSpacing(15)
        header_frame.setLayout(header_layout)
        
        # Titre
        title_label = QLabel(heure['Technicien'])
        title_label.setFont(QFont("SF Pro Text", 20, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #1D1D1F;")
        header_layout.addWidget(title_label)
        
        # Heures en gros
        nb_heures = float(heure['Heures'])
        heures_label = QLabel(f"{nb_heures:.1f} heures")
        heures_label.setFont(QFont("SF Pro Text", 32, QFont.Weight.Bold))
        heures_label.setStyleSheet("color: #007AFF;")
        header_layout.addWidget(heures_label)
        
        # Coût
        cout_horaire = float(heure.get('Cout_Horaire', 0))
        if cout_horaire > 0:
            cout_total = nb_heures * cout_horaire
            cout_label = QLabel(f"Coût: {cout_total:.2f} € ({cout_horaire:.2f} €/h)")
            cout_label.setFont(QFont("SF Pro Text", 14))
            cout_label.setStyleSheet("color: #86868B;")
            header_layout.addWidget(cout_label)
        
        # Boutons d'action
        buttons_layout = QHBoxLayout()
        buttons_layout.setSpacing(10)
        
        btn_modifier = ModernMacOSSecondaryButton("✏️ Modifier")
        btn_modifier.clicked.connect(lambda: self.modifier_heures(heure_id))
        buttons_layout.addWidget(btn_modifier)
        
        btn_supprimer = QPushButton("🗑 Supprimer")
        btn_supprimer.setStyleSheet("""
            QPushButton {
                background-color: #FF3B30;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px 16px;
                font-size: 13px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #D72B21;
            }
        """)
        btn_supprimer.clicked.connect(lambda: self.supprimer_heures(heure_id))
        buttons_layout.addWidget(btn_supprimer)
        
        buttons_layout.addStretch()
        
        header_layout.addLayout(buttons_layout)
        
        self.heures_details_layout.addWidget(header_frame)
        
        # === INFORMATIONS ===
        info_frame = QFrame()
        info_frame.setStyleSheet(ModernMacOSStyleHelper.get_card_stylesheet())
        info_layout = QVBoxLayout()
        info_layout.setContentsMargins(20, 20, 20, 20)
        info_layout.setSpacing(12)
        info_frame.setLayout(info_layout)
        
        # Titre de section
        section_title = QLabel("📋 Informations")
        section_title.setFont(QFont("SF Pro Text", 16, QFont.Weight.Bold))
        section_title.setStyleSheet("color: #1D1D1F; margin-bottom: 10px;")
        info_layout.addWidget(section_title)
        
        # Date
        date_fr = self.format_date_francais(str(heure['Date']))
        date_row = self.create_info_row("Date:", date_fr)
        info_layout.addLayout(date_row)
        
        # Chantier
        try:
            chantier = self.gestion.chantiers.loc[heure['ID_Chantier']]
            chantier_text = f"{chantier['Numero_Commande_Client']}"
        except:
            chantier_text = "N/A"
        chantier_row = self.create_info_row("Chantier:", chantier_text)
        info_layout.addLayout(chantier_row)
        
        self.heures_details_layout.addWidget(info_frame)
        
        # === DESCRIPTION ===
        if heure['Description']:
            desc_frame = QFrame()
            desc_frame.setStyleSheet(ModernMacOSStyleHelper.get_card_stylesheet())
            desc_layout = QVBoxLayout()
            desc_layout.setContentsMargins(20, 20, 20, 20)
            desc_layout.setSpacing(12)
            desc_frame.setLayout(desc_layout)
            
            desc_title = QLabel("📝 Description")
            desc_title.setFont(QFont("SF Pro Text", 16, QFont.Weight.Bold))
            desc_title.setStyleSheet("color: #1D1D1F; margin-bottom: 10px;")
            desc_layout.addWidget(desc_title)
            
            desc_text = QLabel(heure['Description'])
            desc_text.setWordWrap(True)
            desc_text.setFont(QFont("SF Pro Text", 13))
            desc_text.setStyleSheet("color: #1D1D1F; line-height: 1.5;")
            desc_layout.addWidget(desc_text)
            
            self.heures_details_layout.addWidget(desc_frame)
        
        self.heures_details_layout.addStretch()
    
    def refresh_chantiers(self):
        """Actualiser les chantiers"""
        if not hasattr(self, 'chantiers_table'):
            return
        
        self.chantiers_table.setRowCount(0)
        
        if self.gestion.chantiers.empty:
            return
        
        search_term = self.search_entry.text().lower()
        filter_budget = None
        for button in self.filter_group.buttons():
            if button.isChecked():
                filter_budget = button.text()
                break
        
        chantiers_filtered = self.gestion.chantiers.copy()
        chantiers_filtered = chantiers_filtered[chantiers_filtered['Statut'] == 'Actif']
        
        if search_term:
            mask = (
                chantiers_filtered['Nom_Client'].str.lower().str.contains(search_term, na=False) |
                chantiers_filtered['Numero_Commande_Client'].str.lower().str.contains(search_term, na=False)
            )
            chantiers_filtered = chantiers_filtered[mask]
        
        if filter_budget and filter_budget != 'Tous':
            mask = [self.gestion.get_statut_budget(idx) == filter_budget for idx in chantiers_filtered.index]
            chantiers_filtered = chantiers_filtered[mask]
        
        colors = {
            'Excellent': '#34C759',
            'Normal': '#007AFF',
            'Attention': '#FF9500',
            'Alerte': '#FF3B30'
        }
        
        for idx, chantier in chantiers_filtered.iterrows():
            self.gestion.calculer_avancement(idx)
            statut_budget = self.gestion.get_statut_budget(idx)
            
            row = self.chantiers_table.rowCount()
            self.chantiers_table.insertRow(row)
            
            item_client = QTableWidgetItem(chantier['Nom_Client'])
            item_client.setForeground(QColor(colors.get(statut_budget, '#1D1D1F')))
            item_client.setData(Qt.ItemDataRole.UserRole, idx)
            self.chantiers_table.setItem(row, 0, item_client)
            
            self.chantiers_table.setItem(row, 1, QTableWidgetItem(chantier['Numero_Commande_Client']))
            
            adresse_courte = chantier['Adresse_Chantier'][:30] + "..." if len(chantier['Adresse_Chantier']) > 30 else chantier['Adresse_Chantier']
            self.chantiers_table.setItem(row, 2, QTableWidgetItem(adresse_courte))
            
            date_fr = self.format_date_francais(chantier['Date_Ouverture'])
            self.chantiers_table.setItem(row, 3, QTableWidgetItem(date_fr))
            
            self.chantiers_table.setItem(row, 4, QTableWidgetItem(f"{int(chantier['Duree_Prevue_Jours'])}j"))
            self.chantiers_table.setItem(row, 5, QTableWidgetItem(f"{float(chantier['Chiffrage_Global']):.0f}€"))
            self.chantiers_table.setItem(row, 6, QTableWidgetItem(f"{float(chantier['Cout_Estime_Achats']):.0f}€"))
            
            total_depenses = float(chantier['Somme_Achats_Fournisseurs']) + float(chantier['Somme_Achats_Hors_Fournisseurs'])
            self.chantiers_table.setItem(row, 7, QTableWidgetItem(f"{total_depenses:.0f}€"))
            
            self.chantiers_table.setItem(row, 8, QTableWidgetItem(f"{float(chantier['Volume_Heure_Personnel']):.1f}h"))
            
            # Colonne État avec ComboBox qui remplit toute la cellule
            etat_combo = QComboBox()
            etat_combo.addItems(["Validé", "En cours", "Terminé", "Clôturé", "Archivé"])
            etat_combo.setCursor(Qt.CursorShape.PointingHandCursor)
            
            # Définir l'état actuel
            statut_actuel = chantier['Statut']
            if statut_actuel == 'Actif':
                etat_combo.setCurrentText("En cours")
            elif statut_actuel in ["Validé", "En cours", "Terminé", "Clôturé", "Archivé"]:
                etat_combo.setCurrentText(statut_actuel)
            else:
                etat_combo.setCurrentText("En cours")
            
            # Connecter le changement d'état
            etat_combo.currentTextChanged.connect(lambda new_etat, chantier_id=idx: self.change_chantier_etat(chantier_id, new_etat))
            
            # Style pour remplir la cellule complètement sans bordure
            etat_combo.setStyleSheet("""
                QComboBox {
                    background-color: transparent;
                    border: none;
                    padding: 4px 8px;
                    font-size: 13px;
                    color: #1D1D1F;
                    font-weight: normal;
                }
                QComboBox:hover {
                    background-color: rgba(0, 122, 255, 0.08);
                }
                QComboBox:focus {
                    background-color: transparent;
                    border: none;
                    outline: none;
                }
                QComboBox::drop-down {
                    border: none;
                    background: transparent;
                    width: 0px;
                }
                QComboBox::down-arrow {
                    width: 0px;
                    height: 0px;
                    border: none;
                }
                QComboBox QAbstractItemView {
                    background-color: #FFFFFF;
                    border: 1px solid #D1D1D6;
                    border-radius: 8px;
                    padding: 6px;
                    outline: none;
                    selection-background-color: #007AFF;
                    selection-color: white;
                }
                QComboBox QAbstractItemView::item {
                    padding: 10px 16px;
                    border-radius: 4px;
                    min-height: 30px;
                    border: none;
                }
                QComboBox QAbstractItemView::item:selected {
                    background-color: #007AFF;
                    color: white;
                }
                QComboBox QAbstractItemView::item:hover {
                    background-color: rgba(0, 122, 255, 0.12);
                }
            """)
            
            # Créer un widget conteneur avec marges négatives pour couvrir les bordures de cellule
            etat_widget = QWidget()
            etat_widget.setStyleSheet("""
                QWidget {
                    background-color: transparent;
                    border: none;
                }
            """)
            
            # Layout avec marges négatives pour déborder sur les bordures de cellule
            etat_layout = QHBoxLayout(etat_widget)
            etat_layout.setContentsMargins(-1, -1, -1, -1)
            etat_layout.setSpacing(0)
            etat_layout.addWidget(etat_combo)
            
            self.chantiers_table.setCellWidget(row, 9, etat_widget)
    
    def change_chantier_etat(self, chantier_id, nouvel_etat):
        """Changer l'état d'un chantier rapidement"""
        if chantier_id not in self.gestion.chantiers.index:
            return
        
        # Mapper les états vers les statuts du système
        statut_map = {
            "Validé": "Actif",
            "En cours": "Actif",
            "Terminé": "Actif",
            "Clôturé": "Clôturé",
            "Archivé": "Archivé"
        }
        
        nouveau_statut = statut_map.get(nouvel_etat, "Actif")
        
        # Mettre à jour le statut
        self.gestion.chantiers.loc[chantier_id, 'Statut'] = nouveau_statut
        
        # Si clôturé ou archivé, ajouter la date
        if nouveau_statut in ['Clôturé', 'Archivé']:
            self.gestion.chantiers.loc[chantier_id, 'Date_Cloture'] = datetime.now().strftime('%Y-%m-%d')
        
        self.gestion.save_data()
        
        # Si le chantier devient Clôturé ou Archivé, le retirer du tableau actuel
        if nouveau_statut in ['Clôturé', 'Archivé']:
            self.refresh_chantiers()
            self.refresh_archives()

    
    def refresh_archives(self):
        """Actualiser les archives"""
        self.archives_table.setRowCount(0)
        
        archives = self.gestion.chantiers[
            (self.gestion.chantiers['Statut'] == 'Archivé') | 
            (self.gestion.chantiers['Statut'] == 'Clôturé')
        ]
        
        if archives.empty:
            return
        
        search_term = self.archives_search_entry.text().lower() if hasattr(self, 'archives_search_entry') else ""
        
        if search_term:
            mask = (
                archives['Nom_Client'].str.lower().str.contains(search_term, na=False) |
                archives['Numero_Commande_Client'].str.lower().str.contains(search_term, na=False)
            )
            archives = archives[mask]
        
        for idx, chantier in archives.iterrows():
            row = self.archives_table.rowCount()
            self.archives_table.insertRow(row)
            
            # Définir la couleur de la ligne selon le statut
            is_archived = chantier['Statut'] == 'Archivé'
            row_color = QColor("#D1D1D6") if is_archived else QColor("#FFFFFF")
            
            item_client = QTableWidgetItem(chantier['Nom_Client'])
            item_client.setData(Qt.ItemDataRole.UserRole, idx)
            if is_archived:
                item_client.setBackground(row_color)
                item_client.setForeground(QColor("#86868B"))
            self.archives_table.setItem(row, 0, item_client)
            
            item_cmd = QTableWidgetItem(chantier['Numero_Commande_Client'])
            if is_archived:
                item_cmd.setBackground(row_color)
                item_cmd.setForeground(QColor("#86868B"))
            self.archives_table.setItem(row, 1, item_cmd)
            
            adresse_courte = chantier['Adresse_Chantier'][:30] + "..." if len(chantier['Adresse_Chantier']) > 30 else chantier['Adresse_Chantier']
            item_adr = QTableWidgetItem(adresse_courte)
            if is_archived:
                item_adr.setBackground(row_color)
                item_adr.setForeground(QColor("#86868B"))
            self.archives_table.setItem(row, 2, item_adr)
            
            date_ouv = self.format_date_francais(chantier['Date_Ouverture'])
            item_ouv = QTableWidgetItem(date_ouv)
            if is_archived:
                item_ouv.setBackground(row_color)
                item_ouv.setForeground(QColor("#86868B"))
            self.archives_table.setItem(row, 3, item_ouv)
            
            date_clo = self.format_date_francais(chantier.get('Date_Cloture', '')) if pd.notna(chantier.get('Date_Cloture')) else '-'
            item_clo = QTableWidgetItem(date_clo)
            if is_archived:
                item_clo.setBackground(row_color)
                item_clo.setForeground(QColor("#86868B"))
            self.archives_table.setItem(row, 4, item_clo)
            
            statut_item = QTableWidgetItem(chantier['Statut'])
            if is_archived:
                statut_item.setBackground(row_color)
                statut_item.setForeground(QColor("#86868B"))
            else:
                statut_item.setForeground(QColor("#34C759"))
            self.archives_table.setItem(row, 5, statut_item)
            
            self.archives_table.setItem(row, 6, QTableWidgetItem(f"{int(chantier['Duree_Prevue_Jours'])}j"))
            self.archives_table.setItem(row, 7, QTableWidgetItem(f"{float(chantier['Chiffrage_Global']):.0f}€"))
            
            total_depenses = float(chantier['Somme_Achats_Fournisseurs']) + float(chantier['Somme_Achats_Hors_Fournisseurs'])
            self.archives_table.setItem(row, 8, QTableWidgetItem(f"{total_depenses:.0f}€"))
            
            self.archives_table.setItem(row, 9, QTableWidgetItem(f"{float(chantier['Volume_Heure_Personnel']):.1f}h"))
    
    def refresh_factures(self):
        """Actualiser les factures - MANUEL UNIQUEMENT"""
        self.factures_table.setRowCount(0)
        self.factures_status_label.setText("🔄 Chargement en cours...")
        self.factures_status_label.setStyleSheet("color: #FF9500;")
        
        if hasattr(self, 'btn_refresh_factures'):
            self.btn_refresh_factures.setEnabled(False)
        
        self.factures_loader = FacturesLoaderThread()
        self.factures_loader.finished.connect(self.on_factures_loaded)
        self.factures_loader.error.connect(self.on_factures_error)
        self.factures_loader.progress.connect(self.on_factures_progress)
        self.factures_loader.start()
    
    def on_factures_progress(self, message):
        self.factures_status_label.setText(f"🔄 {message}")
    
    def on_factures_loaded(self, factures):
        if hasattr(self, 'btn_refresh_factures'):
            self.btn_refresh_factures.setEnabled(True)
        
        if not factures:
            self.factures_status_label.setText("Aucune facture trouvée")
            self.factures_status_label.setStyleSheet("color: #86868B;")
            self.factures_sum_label.setText("Total: 0.00 €")
            return
        
        total_ttc = sum(facture.get('total', 0) for facture in factures)
        total_tax = sum(facture.get('tax_amount', 0) for facture in factures)
        
        self.factures_sum_label.setText(f"Total TTC: {total_ttc:,.2f} € | TVA: {total_tax:,.2f} €")
        self.factures_status_label.setText(f"✅ {len(factures)} facture(s) chargée(s)")
        self.factures_status_label.setStyleSheet("color: #34C759;")
        
        for facture in factures:
            row = self.factures_table.rowCount()
            self.factures_table.insertRow(row)
            
            numero = facture.get('number', 'N/A')
            self.factures_table.setItem(row, 0, QTableWidgetItem(numero))
            
            date_timestamp = (facture.get('date') or 
                            facture.get('sent_date') or 
                            facture.get('last_update_date') or 0)
            date_str = convert_timestamp_to_date(date_timestamp)
            self.factures_table.setItem(row, 1, QTableWidgetItem(date_str))
            
            company = facture.get('company', {})
            client_name = company.get('name', 'N/A') if company else 'N/A'
            self.factures_table.setItem(row, 2, QTableWidgetItem(client_name))
            
            total_ttc_facture = facture.get('total', 0)
            tax_amount = facture.get('tax_amount', 0)
            montant_ht = total_ttc_facture - tax_amount
            self.factures_table.setItem(row, 3, QTableWidgetItem(f"{montant_ht:.2f} €"))
            
            self.factures_table.setItem(row, 4, QTableWidgetItem(f"{tax_amount:.2f} €"))
            
            item_ttc = QTableWidgetItem(f"{total_ttc_facture:.2f} €")
            item_ttc.setFont(QFont("SF Pro Text", 11, QFont.Weight.Bold))
            self.factures_table.setItem(row, 5, item_ttc)
            
            due_date_timestamp = (facture.get('due_date') or 
                                 facture.get('delivery_date') or 0)
            due_date_str = convert_timestamp_to_date(due_date_timestamp)
            self.factures_table.setItem(row, 6, QTableWidgetItem(due_date_str))
            
            paid_date = facture.get('paid_date', 0)
            outstanding = facture.get('outstanding_amount', 0)
            
            if paid_date and paid_date != '0' and paid_date != 0:
                statut_text = "✅ Payée"
                statut_color = "#34C759"
            elif outstanding > 0:
                statut_text = f"⚠️ Impayée ({outstanding:.2f} €)"
                statut_color = "#FF9500"
            else:
                statut_text = "⏳ En attente"
                statut_color = "#007AFF"
            
            item_statut = QTableWidgetItem(statut_text)
            item_statut.setForeground(QColor(statut_color))
            self.factures_table.setItem(row, 7, item_statut)
            
            devise = facture.get('currency', 'EUR')
            self.factures_table.setItem(row, 8, QTableWidgetItem(devise))
            
            pdf_url = (facture.get('public_path') or 
                      facture.get('paid_invoice_pdf') or 
                      facture.get('customer_portal_url'))
            
            if pdf_url and str(pdf_url).strip() and str(pdf_url) not in ['None', 'null', '']:
                pdf_label = QLabel("📄")
                pdf_label.setStyleSheet("""
                    QLabel {
                        font-size: 20px;
                        padding: 4px;
                        background-color: transparent;
                        border: none;
                    }
                    QLabel:hover {
                        background-color: rgba(0, 122, 255, 0.1);
                        border-radius: 4px;
                    }
                """)
                pdf_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                pdf_label.setToolTip(f"Ouvrir le PDF de la facture {facture.get('number', 'N/A')}")
                pdf_label.setCursor(Qt.CursorShape.PointingHandCursor)
                
                pdf_widget = QWidget()
                pdf_layout = QHBoxLayout(pdf_widget)
                pdf_layout.setContentsMargins(0, 0, 0, 0)
                pdf_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
                pdf_layout.addWidget(pdf_label)
                
                pdf_label.mousePressEvent = lambda event, url=str(pdf_url): self.open_pdf(url)
                
                self.factures_table.setCellWidget(row, 9, pdf_widget)
            else:
                item_no_pdf = QTableWidgetItem("-")
                item_no_pdf.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                item_no_pdf.setForeground(QColor("#86868B"))
                self.factures_table.setItem(row, 9, item_no_pdf)
    
    def on_factures_error(self, error_message, _status_code):
        if hasattr(self, 'btn_refresh_factures'):
            self.btn_refresh_factures.setEnabled(True)
        
        self.factures_status_label.setText(f"⚠️ {error_message}")
        self.factures_status_label.setStyleSheet("color: #FF3B30;")
        
        QMessageBox.critical(self, "Erreur", f"Impossible de charger les factures:\n{error_message}")
    
    def open_pdf(self, url):
        import webbrowser
        
        if not url or str(url).strip() in ['', 'None', 'null']:
            QMessageBox.warning(self, "Erreur", "Aucun lien PDF disponible pour cette facture.")
            return
        
        url_clean = str(url).strip()
        
        if not url_clean.startswith(('http://', 'https://')):
            url_clean = 'https://' + url_clean
        
        try:
            success = webbrowser.open(url_clean)
            if not success:
                QMessageBox.warning(self, "Erreur", f"Impossible d'ouvrir le PDF.\nURL: {url_clean}")
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Impossible d'ouvrir le PDF:\n{str(e)}\n\nURL: {url_clean}")
    
    # ===============================================
    # NOUVEAU MODULE CHANTIER
    # ===============================================
    
    def create_chantier_module_page(self):
        """Page du nouveau module Chantier avec interface splitter"""
        page = QWidget()
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        page.setLayout(main_layout)
        
        # SPLITTER pour diviser en deux parties
        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setHandleWidth(2)
        splitter.setChildrenCollapsible(False)  # Empêcher les volets de se replier
        
        # === PARTIE GAUCHE: Liste des chantiers ===
        left_widget = QWidget()
        left_widget.setMinimumWidth(250)  # Largeur minimale
        left_layout = QVBoxLayout()
        left_layout.setContentsMargins(0, 0, 10, 0)
        left_layout.setSpacing(15)
        left_widget.setLayout(left_layout)
        
        # Titre
        title_label = QLabel("Liste des chantiers")
        title_label.setFont(QFont("SF Pro Text", 18, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #1D1D1F; padding: 10px 0;")
        left_layout.addWidget(title_label)
        
        # Barre de recherche
        self.chantier_module_search_entry = QLineEdit()
        self.chantier_module_search_entry.setPlaceholderText("🔍 Rechercher un chantier...")
        self.chantier_module_search_entry.textChanged.connect(self.refresh_chantier_module_list)
        left_layout.addWidget(self.chantier_module_search_entry)
        
        # Compteur
        self.chantier_module_count_label = QLabel("Total: 0 chantiers")
        self.chantier_module_count_label.setFont(QFont("SF Pro Text", 12, QFont.Weight.Bold))
        self.chantier_module_count_label.setStyleSheet("color: #86868B; padding: 5px 0;")
        left_layout.addWidget(self.chantier_module_count_label)
        
        # Liste des chantiers
        self.chantier_module_list = QTableWidget()
        self.chantier_module_list.setColumnCount(1)
        self.chantier_module_list.setHorizontalHeaderLabels(["Nom du chantier"])
        header = self.chantier_module_list.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.chantier_module_list.verticalHeader().setVisible(False)
        self.chantier_module_list.verticalHeader().setDefaultSectionSize(50)
        self.chantier_module_list.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.chantier_module_list.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.chantier_module_list.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        self.chantier_module_list.setSortingEnabled(True)
        self.chantier_module_list.itemSelectionChanged.connect(self.on_chantier_module_selection_changed)
        left_layout.addWidget(self.chantier_module_list)
        
        splitter.addWidget(left_widget)
        
        # === PARTIE DROITE: Détails du chantier ===
        right_widget = QWidget()
        right_widget.setMinimumWidth(400)  # Largeur minimale
        right_layout = QVBoxLayout()
        right_layout.setContentsMargins(10, 0, 0, 0)
        right_layout.setSpacing(20)
        right_widget.setLayout(right_layout)
        
        # Scroll area pour les détails
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setStyleSheet("QScrollArea { border: none; background-color: transparent; }")
        
        details_container = QWidget()
        self.chantier_module_details_layout = QVBoxLayout()
        self.chantier_module_details_layout.setSpacing(25)
        self.chantier_module_details_layout.setContentsMargins(0, 0, 0, 0)
        details_container.setLayout(self.chantier_module_details_layout)
        
        # Message initial
        empty_label = QLabel("Sélectionnez un chantier pour voir les détails")
        empty_label.setFont(QFont("SF Pro Text", 14))
        empty_label.setStyleSheet("color: #86868B; padding: 40px;")
        empty_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.chantier_module_details_layout.addWidget(empty_label)
        self.chantier_module_details_layout.addStretch()
        
        scroll.setWidget(details_container)
        right_layout.addWidget(scroll)
        
        splitter.addWidget(right_widget)
        
        # Définir les proportions: 30% gauche, 70% droite
        # Note: Les tailles sont en pixels, pas en pourcentage
        total_width = 1000  # Largeur approximative
        splitter.setSizes([int(total_width * 0.3), int(total_width * 0.7)])
        
        main_layout.addWidget(splitter)
        
        return page
    
    def refresh_chantier_module_list(self):
        """Rafraîchir la liste des chantiers du module"""
        self.chantier_module_list.setRowCount(0)
        
        search_term = self.chantier_module_search_entry.text().lower()
        
        # Filtrer les chantiers actifs uniquement (non archivés)
        active_chantiers = self.gestion.chantiers[
            self.gestion.chantiers['Statut'] != 'Archivé'
        ].copy()
        
        # Appliquer le filtre de recherche
        if search_term:
            active_chantiers = active_chantiers[
                active_chantiers['Nom_Client'].str.lower().str.contains(search_term, na=False) |
                active_chantiers['Numero_Commande_Client'].str.lower().str.contains(search_term, na=False)
            ]
        
        # Mettre à jour le compteur
        self.chantier_module_count_label.setText(f"Total: {len(active_chantiers)} chantiers")
        
        # Remplir la liste
        for idx, (chantier_id, row) in enumerate(active_chantiers.iterrows()):
            self.chantier_module_list.insertRow(idx)
            
            # Nom du chantier (Client)
            nom_item = QTableWidgetItem(str(row['Nom_Client']))
            nom_item.setData(Qt.ItemDataRole.UserRole, chantier_id)
            self.chantier_module_list.setItem(idx, 0, nom_item)
    
    def on_chantier_module_selection_changed(self):
        """Gérer la sélection d'un chantier dans le module"""
        selected_items = self.chantier_module_list.selectedItems()
        
        # Effacer le contenu précédent
        while self.chantier_module_details_layout.count():
            child = self.chantier_module_details_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        
        if not selected_items:
            # Aucune sélection
            empty_label = QLabel("Sélectionnez un chantier pour voir les détails")
            empty_label.setFont(QFont("SF Pro Text", 14))
            empty_label.setStyleSheet("color: #86868B; padding: 40px;")
            empty_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.chantier_module_details_layout.addWidget(empty_label)
            self.chantier_module_details_layout.addStretch()
            return
        
        # Récupérer l'ID du chantier sélectionné
        chantier_id = selected_items[0].data(Qt.ItemDataRole.UserRole)
        chantier = self.gestion.chantiers.loc[chantier_id]
        
        # === CARTE INFORMATIONS PRINCIPALES ===
        info_card = QFrame()
        info_card.setStyleSheet(ModernMacOSStyleHelper.get_card_stylesheet())
        info_layout = QVBoxLayout()
        info_layout.setContentsMargins(25, 25, 25, 25)
        info_layout.setSpacing(15)
        info_card.setLayout(info_layout)
        
        # Titre de la carte
        card_title = QLabel("Informations principales")
        card_title.setFont(QFont("SF Pro Text", 16, QFont.Weight.Bold))
        card_title.setStyleSheet("color: #1D1D1F;")
        info_layout.addWidget(card_title)
        
        # Nom du chantier
        nom_layout = QHBoxLayout()
        nom_label = QLabel("Nom du chantier:")
        nom_label.setFont(QFont("SF Pro Text", 13, QFont.Weight.Bold))
        nom_label.setFixedWidth(180)
        nom_layout.addWidget(nom_label)
        
        nom_value = QLabel(str(chantier['Nom_Client']))
        nom_value.setFont(QFont("SF Pro Text", 13))
        nom_value.setStyleSheet("color: #1D1D1F;")
        nom_layout.addWidget(nom_value)
        nom_layout.addStretch()
        info_layout.addLayout(nom_layout)
        
        # Numéro de commande
        num_layout = QHBoxLayout()
        num_label = QLabel("Numéro de commande:")
        num_label.setFont(QFont("SF Pro Text", 13, QFont.Weight.Bold))
        num_label.setFixedWidth(180)
        num_layout.addWidget(num_label)
        
        num_value = QLabel(str(chantier['Numero_Commande_Client']))
        num_value.setFont(QFont("SF Pro Text", 13))
        num_value.setStyleSheet("color: #1D1D1F;")
        num_layout.addWidget(num_value)
        num_layout.addStretch()
        info_layout.addLayout(num_layout)
        
        # Date d'ouverture
        date_layout = QHBoxLayout()
        date_label = QLabel("Date d'ouverture:")
        date_label.setFont(QFont("SF Pro Text", 13, QFont.Weight.Bold))
        date_label.setFixedWidth(180)
        date_layout.addWidget(date_label)
        
        date_value = QLabel(str(chantier['Date_Ouverture']))
        date_value.setFont(QFont("SF Pro Text", 13))
        date_value.setStyleSheet("color: #1D1D1F;")
        date_layout.addWidget(date_value)
        date_layout.addStretch()
        info_layout.addLayout(date_layout)
        
        self.chantier_module_details_layout.addWidget(info_card)
        
        # === CARTE INDICATEURS ===
        indicators_card = QFrame()
        indicators_card.setStyleSheet(ModernMacOSStyleHelper.get_card_stylesheet())
        indicators_layout = QVBoxLayout()
        indicators_layout.setContentsMargins(25, 25, 25, 25)
        indicators_layout.setSpacing(20)
        indicators_card.setLayout(indicators_layout)
        
        # Titre de la carte
        ind_title = QLabel("Indicateurs de suivi")
        ind_title.setFont(QFont("SF Pro Text", 16, QFont.Weight.Bold))
        ind_title.setStyleSheet("color: #1D1D1F;")
        indicators_layout.addWidget(ind_title)
        
        # === INDICATEUR 1: Jours ouvrés ===
        jours_frame = QFrame()
        jours_frame.setStyleSheet("""
            QFrame {
                background-color: rgba(0, 122, 255, 0.1);
                border-radius: 12px;
                border: 1px solid rgba(0, 122, 255, 0.2);
            }
        """)
        jours_layout = QVBoxLayout()
        jours_layout.setContentsMargins(20, 15, 20, 15)
        jours_layout.setSpacing(10)
        jours_frame.setLayout(jours_layout)
        
        jours_title_label = QLabel("📅  Jours ouvrés")
        jours_title_label.setFont(QFont("SF Pro Text", 14, QFont.Weight.Bold))
        jours_title_label.setStyleSheet("color: #007AFF;")
        jours_layout.addWidget(jours_title_label)
        
        # Calcul des jours réels basé sur les heures saisies
        heures_chantier = self.gestion.heures[
            self.gestion.heures['ID_Chantier'] == chantier_id
        ]
        jours_reels = len(heures_chantier['Date'].unique()) if not heures_chantier.empty else 0
        jours_estimes = int(chantier['Duree_Prevue_Jours'])
        
        jours_value_label = QLabel(f"Estimés: {jours_estimes} jours  /  Réels: {jours_reels} jours")
        jours_value_label.setFont(QFont("SF Pro Text", 13))
        jours_value_label.setStyleSheet("color: #1D1D1F;")
        jours_layout.addWidget(jours_value_label)
        
        # Barre de progression
        if jours_estimes > 0:
            progress_pct = min((jours_reels / jours_estimes) * 100, 100)
            progress_color = "#34C759" if progress_pct <= 100 else "#FF3B30"
        else:
            progress_pct = 0
            progress_color = "#86868B"
        
        progress_bar_frame = QFrame()
        progress_bar_frame.setFixedHeight(8)
        progress_bar_frame.setStyleSheet(f"""
            QFrame {{
                background-color: rgba(0, 0, 0, 0.1);
                border-radius: 4px;
            }}
        """)
        progress_bar_fill = QFrame(progress_bar_frame)
        progress_bar_fill.setFixedHeight(8)
        progress_bar_fill.setFixedWidth(int(progress_bar_frame.width() * progress_pct / 100))
        progress_bar_fill.setStyleSheet(f"""
            QFrame {{
                background-color: {progress_color};
                border-radius: 4px;
            }}
        """)
        jours_layout.addWidget(progress_bar_frame)
        
        indicators_layout.addWidget(jours_frame)
        
        # === INDICATEUR 2: Budget ===
        budget_frame = QFrame()
        budget_frame.setStyleSheet("""
            QFrame {
                background-color: rgba(52, 199, 89, 0.1);
                border-radius: 12px;
                border: 1px solid rgba(52, 199, 89, 0.2);
            }
        """)
        budget_layout = QVBoxLayout()
        budget_layout.setContentsMargins(20, 15, 20, 15)
        budget_layout.setSpacing(10)
        budget_frame.setLayout(budget_layout)
        
        budget_title_label = QLabel("💰  Budget du chantier")
        budget_title_label.setFont(QFont("SF Pro Text", 14, QFont.Weight.Bold))
        budget_title_label.setStyleSheet("color: #34C759;")
        budget_layout.addWidget(budget_title_label)
        
        # Note: Ici vous pouvez ajouter la logique pour calculer la somme des factures
        # Pour l'instant, on utilise le chiffrage
        budget_chiffre = float(chantier['Chiffrage_Global'])
        # TODO: Calculer la somme des factures associées au chantier
        budget_factures = 0.0  # À implémenter avec le module facture
        
        budget_value_label = QLabel(f"Chiffré: {budget_chiffre:,.2f} €  /  Facturé: {budget_factures:,.2f} €")
        budget_value_label.setFont(QFont("SF Pro Text", 13))
        budget_value_label.setStyleSheet("color: #1D1D1F;")
        budget_layout.addWidget(budget_value_label)
        
        # Barre de progression budget
        if budget_chiffre > 0:
            budget_progress_pct = min((budget_factures / budget_chiffre) * 100, 100)
            budget_progress_color = "#34C759" if budget_progress_pct <= 100 else "#FF3B30"
        else:
            budget_progress_pct = 0
            budget_progress_color = "#86868B"
        
        budget_progress_bar_frame = QFrame()
        budget_progress_bar_frame.setFixedHeight(8)
        budget_progress_bar_frame.setStyleSheet(f"""
            QFrame {{
                background-color: rgba(0, 0, 0, 0.1);
                border-radius: 4px;
            }}
        """)
        indicators_layout.addWidget(budget_frame)
        
        # === INDICATEUR 3: Achats ===
        achats_frame = QFrame()
        achats_frame.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 149, 0, 0.1);
                border-radius: 12px;
                border: 1px solid rgba(255, 149, 0, 0.2);
            }
        """)
        achats_layout = QVBoxLayout()
        achats_layout.setContentsMargins(20, 15, 20, 15)
        achats_layout.setSpacing(10)
        achats_frame.setLayout(achats_layout)
        
        achats_title_label = QLabel("🛒  Achats")
        achats_title_label.setFont(QFont("SF Pro Text", 14, QFont.Weight.Bold))
        achats_title_label.setStyleSheet("color: #FF9500;")
        achats_layout.addWidget(achats_title_label)
        
        # Calcul des achats réels
        achats_estimes = float(chantier['Cout_Estime_Achats'])
        achats_reels = float(chantier['Somme_Achats_Fournisseurs']) + float(chantier['Somme_Achats_Hors_Fournisseurs'])
        
        achats_value_label = QLabel(f"Estimés: {achats_estimes:,.2f} €  /  Réalisés: {achats_reels:,.2f} €")
        achats_value_label.setFont(QFont("SF Pro Text", 13))
        achats_value_label.setStyleSheet("color: #1D1D1F;")
        achats_layout.addWidget(achats_value_label)
        
        # Barre de progression achats
        if achats_estimes > 0:
            achats_progress_pct = min((achats_reels / achats_estimes) * 100, 100)
            achats_progress_color = "#34C759" if achats_progress_pct <= 100 else "#FF3B30"
        else:
            achats_progress_pct = 0
            achats_progress_color = "#86868B"
        
        achats_progress_bar_frame = QFrame()
        achats_progress_bar_frame.setFixedHeight(8)
        achats_progress_bar_frame.setStyleSheet(f"""
            QFrame {{
                background-color: rgba(0, 0, 0, 0.1);
                border-radius: 4px;
            }}
        """)
        indicators_layout.addWidget(achats_frame)
        
        self.chantier_module_details_layout.addWidget(indicators_card)
        
        # Ajouter un stretch en bas
        self.chantier_module_details_layout.addStretch()



def main():
    """Point d'entrée de l'application"""
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    # Style global pour supprimer l'encadrement gris lors de la sélection de texte
    app.setStyleSheet("""
        QTableWidget {
            outline: none;
        }
        QTableWidget::item {
            outline: none;
        }
        QTableWidget::item:selected {
            outline: none;
            border: none;
        }
        QLineEdit, QTextEdit, QComboBox {
            outline: none;
        }
    """)
    
    QLocale.setDefault(QLocale(QLocale.Language.French, QLocale.Country.France))
    
    window = GescoMainWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
