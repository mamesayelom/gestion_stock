# Gestion de Stock – Python & MySQL

## Description
Ce projet est une application de gestion de stock développée en Python avec une base de données MySQL.
Il permet de gérer des catégories, des produits et les mouvements de stock (entrées et sorties).

Ce projet a été réalisé dans le cadre d’un apprentissage du développement backend avec Python et MySQL.

---

## Fonctionnalités
- Ajouter et lister des catégories (Informatique, Papeterie, Mobilier)
- Ajouter des produits associés à une catégorie existante
- Gérer les mouvements de stock (entrée / sortie)
- Historique des mouvements de stock
- Afficher les produits avec leur catégorie
- Alerte pour les produits dont le stock est inférieur à 5 unités

---

## Technologies utilisées
- Python 3
- MySQL
- MySQL Connector
- Git & GitHub
- Environnement virtuel Python (env)

---

## Installation

1. Cloner le projet :
```bash
git clone https://github.com/mamesayelom/gestion_stock.git

```

## Création environement virtuel et activation

- python3 -m venv .env

- source venv .env/bin/activate

## Installer les dépendances
- pip install mysql-connector-python

## Configurer la base de données

- Créer la base MySQL

- Importer le script SQL (tables + contraintes)

- Mettre à jour les paramètres de connexion dans database/db_connection.py

## Lancement
- python main.py