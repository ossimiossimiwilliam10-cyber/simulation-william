@echo off
rem Ouvre le téléphone de William (page de la simulation) dans le navigateur, SANS Claude.
rem Laisser cette fenêtre ouverte. Sur le téléphone du joueur (même Wi-Fi) : l'adresse du réseau s'affiche ci-dessous.
chcp 65001 >nul
cd /d "%~dp0"
python outils\telephone_serveur.py --ouvrir
pause
