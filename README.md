# Web Scraping Immobilier - API Flask

## Description
Ce projet permet de récupérer les annonces immobilières publiées en Tunisie sur le site **Tunisie Annonce**. Les informations extraites incluent des détails sur les propriétés disponibles à la vente ou en location, comme le titre, le prix, la localisation, le type de bien, etc. Les données collectées sont exposées via une API REST que l'on peut interroger pour obtenir les annonces sous différents formats (JSON).

## Fonctionnalités
- Scraping des annonces immobilières (titre, prix, type de bien, localisation, description, date de publication).
- Stockage des annonces dans un fichier CSV.
- API REST pour interagir avec les données :
  - `GET /annonces` : Récupère toutes les annonces collectées.
  - `POST /scrape` : Lance une nouvelle session de scraping pour collecter les dernières annonces.

## Prérequis
Avant de pouvoir utiliser ce projet, assure-toi que tu as installé Python et les dépendances nécessaires.

### Installer les dépendances
1. Clone ce dépôt sur ton ordinateur :
   ```bash
   git clone https://github.com/<ton_nom_utilisateur>/web_scraping_immobilier.git
   ```
2. Crée un environnement virtuel et active-le :
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```
3. Installe les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Lancer le projet
1. Lance l'application Flask pour démarrer l'API :
   ```bash
   python scripts/api.py
   ```

2. Une fois l'application lancée, tu peux accéder à l'API :
   - `GET http://127.0.0.1:5000/annonces` : Pour récupérer les annonces collectées.
   - `POST http://127.0.0.1:5000/scrape` : Pour lancer une nouvelle session de scraping.

## Structure du projet
```
/web_scraping_immobilier/
│── /data/                 # Dossier pour stocker les fichiers CSV
│── /scripts/              # Dossier contenant les scripts Python
│   ├── scraper.py         # Script pour extraire les données des annonces
│   ├── api.py             # Script pour lancer l'API Flask
│── /notebooks/            # Dossier pour les tests en Jupyter Notebook
│   ├── test_scraping.ipynb  # Notebook pour tester le scraping
│── requirements.txt        # Liste des bibliothèques à installer
│── README.md              # Ce fichier
│── .gitignore             # Exclure fichiers inutiles (cache, venv, etc.)
```

## Contributions
Si tu veux contribuer à ce projet, tu peux :
1. Fork ce dépôt.
2. Créer une branche pour ta fonctionnalité (`git checkout -b feature-nouvelle-fonction`).
3. Commit tes modifications (`git commit -am 'Ajout d\'une nouvelle fonctionnalité'`).
4. Pousser la branche (`git push origin feature-nouvelle-fonction`).
5. Ouvrir une **Pull Request**.

## Licence
Ce projet est sous licence **MIT** - consulte le fichier [LICENSE](LICENSE) pour plus de détails.
```

---