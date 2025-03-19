from flask import Flask, jsonify, request
from scraper import save_to_csv, url, headers  # On importe le URL, headers, et save_to_csv du scraper
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

annonces_data = []  # Liste qui va contenir les annonces extraites


@app.route('/annonces', methods=['GET'])
def get_annonces():
    """Retourne toutes les annonces collectées au format JSON"""
    return jsonify(annonces_data)


@app.route('/scrape', methods=['POST'])
def scrape():
    """Lance une nouvelle session de scraping et sauvegarde les annonces en CSV"""
    global annonces_data
    annonces_data = []

    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return jsonify({"error": f"Échec de la connexion. Code HTTP : {response.status_code}"}), 500

    soup = BeautifulSoup(response.text, "html.parser")
    annonces = soup.find_all("tr", class_="Tableau1")

    for annonce in annonces[:5]:  # Limité à 5 annonces pour tester
        cellules = annonce.find_all("td")

        if len(cellules) >= 12:
            gouvernorat = cellules[1].text.strip()
            type_bien = cellules[3].text.strip()
            titre = cellules[7].find("a").text.strip() if cellules[7].find("a") else "Titre non trouvé"
            lien = "http://www.tunisie-annonce.com/" + cellules[7].find("a")["href"] if cellules[7].find("a") else "Lien non trouvé"
            prix = cellules[9].text.strip() if cellules[9] else "Prix non disponible"
            date_publication = cellules[11].text.strip() if cellules[11] else "Date non disponible"

            annonce_data = {
                'Titre': titre,
                'Prix': prix,
                'Localisation': gouvernorat,
                'Type de bien': type_bien,
                'Date': date_publication,
                'Lien': lien
            }
            
            annonces_data.append(annonce_data)

    # Sauvegarder en CSV
    save_to_csv(annonces_data)
    return jsonify({"message": f"{len(annonces_data)} annonces ont été collectées et sauvegardées."})


if __name__ == "__main__":
    app.run(debug=True)
