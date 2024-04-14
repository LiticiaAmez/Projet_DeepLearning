import folium
from streamlit_folium import folium_static

def display_map(df_ileDeFrance_preprocessed, df_HorsIleDeFrance_preprocessed):
    map = folium.Map(location=[48.8566, 2.3522], zoom_start=6)
    # Ajout des marqueurs pour Île-de-France
    for index, row in df_ileDeFrance_preprocessed.iterrows():
        folium.Marker(location=[row['Latitude'], row['Longitude']], popup=row['ville']).add_to(map)
    # Ajout des marqueurs pour Hors Île-de-France
    for index, row in df_HorsIleDeFrance_preprocessed.iterrows():
        folium.Marker(location=[row['Latitude'], row['Longitude']], popup=row['ville'], icon=folium.Icon(color='red')).add_to(map)
    # Afficher la carte
    folium_static(map)
