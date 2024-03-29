import requests

def load_data():
    # Définir l'URL de l'API
    url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/qualite-de-lair-france/records?limit=20&timezone=Europe%2FParis"

    try:
        # Envoyer une requête GET à l'API
        response = requests.get(url)

        # Vérifier si la requête a réussi (statut 200)
        if response.status_code == 200:
            # Récupérer les données JSON
            data = response.json()
            
            # Afficher le contenu de data pour le débogage
            print("Contenu de data:", data)
            
            return data
        else:
            # Afficher un message d'erreur si la requête a échoué
            print("Erreur lors de la récupération des données:", response.status_code)
            return None
    except Exception as e:
        # Afficher un message d'erreur en cas d'exception
        print("Erreur lors du chargement des données:", e)
        return None

load_data()
