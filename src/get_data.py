import pandas as pd
import matplotlib.pyplot as plt
import requests

def load_data():
    # Définir l'URL de l'API
    url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/base-des-diagnostics-de-performance-energetique-dpe/records?limit=-1"

    try:
        # Envoyer une requête GET à l'API
        response = requests.get(url)

        # Vérifier si la requête a réussi (statut 200)
        if response.status_code == 200:
            # Récupérer les données JSON
            data = response.json()
            return data
        else:
            # Afficher un message d'erreur si la requête a échoué
            print("Erreur lors de la récupération des données:", response.status_code)
            return None
    except Exception as e:
        # Afficher un message d'erreur en cas d'exception
        print("Erreur lors du chargement des données:", e)
        return None

# Appeler la fonction load_data pour obtenir les données
data = load_data()

# Afficher les données récupérées
print(data)

#--------

# Charger les données à partir du fichier CSV
df = pd.read_csv("base_dpe.csv", delimiter=";", nrows=None)

# Afficher les premières lignes pour vérification
print(df.head())
