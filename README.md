# Web Scraping Immobilier en Tunisie

Ce projet a pour but de collecter des annonces immobilières en Tunisie et de les exposer via une API REST. Les annonces sont extraites de sites web comme **Tunisie Annonce**. Les données collectées comprennent des informations telles que le titre de l'annonce, le prix, le type de bien, la localisation, la date de publication, et plus encore.

## Fonctionnalités

- **Scraping des annonces immobilières** : Extraction des données depuis **Tunisie Annonce** et d'autres sites immobiliers en Tunisie.
- **API REST** : Exposition des données collectées via une API REST simple.
- **Enregistrement des données** : Les annonces sont enregistrées dans un fichier CSV ou JSON, et peuvent aussi être stockées dans une base de données (SQLite, PostgreSQL, ou MongoDB).

## Prérequis

Avant de commencer, assurez-vous que les éléments suivants sont installés :

- **Python 3.x**  
- **Git** pour le versionnement du code
- **Les bibliothèques Python suivantes** :
    - `requests` : pour envoyer des requêtes HTTP.
    - `beautifulsoup4` : pour l’analyse des pages HTML.
    - `flask` ou `fastapi` : pour la création de l'API REST.
    - `pandas` : pour la gestion des données et leur conversion en CSV/JSON.
    
Vous pouvez installer ces dépendances en exécutant la commande suivante :

```bash
pip install -r requirements.txt
