import csv
import os
import requests
from bs4 import BeautifulSoup

def save_to_csv(data, filename='data/annonces.csv'):
    # Crée le dossier /data s'il n'existe pas déjà
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    # Détermine si le fichier existe déjà
    file_exists = os.path.isfile(filename)

    # Définit les en-têtes des colonnes
    fieldnames = ['Titre', 'Prix', 'Localisation', 'Type de bien', 'Date', 'Lien']
    
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Écrit les en-têtes si le fichier est créé pour la première fois
        if not file_exists:
            writer.writeheader()
        
        # Écrit les données ligne par ligne
        for annonce in data:
            writer.writerow(annonce)

# URL des annonces immobilières
url = "http://www.tunisie-annonce.com/AnnoncesImmobilier.asp"

# Simuler un navigateur avec un User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

# Envoyer la requête HTTP
response = requests.get(url, headers=headers)

# Liste pour stocker les annonces extraites
annonces_data = []

# Vérifier si la requête est réussie
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Trouver toutes les annonces (balise <tr class="Tableau1">)
    annonces = soup.find_all("tr", class_="Tableau1")

    for annonce in annonces[:5]:  # Limité à 5 annonces pour tester
        cellules = annonce.find_all("td")  # Récupérer toutes les colonnes

        if len(cellules) >= 12:  # Vérifier qu'on a assez de colonnes
            gouvernorat = cellules[1].text.strip()
            type_bien = cellules[3].text.strip()
            titre = cellules[7].find("a").text.strip() if cellules[7].find("a") else "Titre non trouvé"
            lien = "http://www.tunisie-annonce.com/" + cellules[7].find("a")["href"] if cellules[7].find("a") else "Lien non trouvé"
            prix = cellules[9].text.strip() if cellules[9] else "Prix non disponible"
            date_publication = cellules[11].text.strip() if cellules[11] else "Date non disponible"
            
            # Ajouter les données extraites à la liste
            annonces_data.append({
                'Titre': titre,
                'Prix': prix,
                'Localisation': gouvernorat,
                'Type de bien': type_bien,
                'Date': date_publication,
                'Lien': lien
            })

            # Affichage console pour vérifier
            print(f"🏡 Titre : {titre}")
            print(f"📍 Localisation : {gouvernorat}")
            print(f"🏠 Type de bien : {type_bien}")
            print(f"💰 Prix : {prix}")
            print(f"🗓️ Date : {date_publication}")
            print(f"🔗 Lien : {lien}")
            print("-" * 50)

    # Appeler la fonction d'enregistrement en CSV
    save_to_csv(annonces_data)
    print(f"✅ {len(annonces_data)} annonces ont été sauvegardées dans le fichier CSV.")
else:
    print(f"❌ Échec de la connexion. Code HTTP : {response.status_code}")
