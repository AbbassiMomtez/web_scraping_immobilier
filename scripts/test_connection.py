import requests

# URL cible
url = "http://www.tunisie-annonce.com/AnnoncesImmobilier.asp"

# Simuler un navigateur avec un User-Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

# Envoyer la requête HTTP
response = requests.get(url, headers=headers)

# Vérifier si la requête a réussi (code 200)
if response.status_code == 200:
    print("✅ Connexion réussie ! Voici un extrait du HTML :\n")
    print(response.text[:500])  # Afficher les 500 premiers caractères du HTML
else:
    print(f"❌ Échec de la connexion. Code HTTP : {response.status_code}")
