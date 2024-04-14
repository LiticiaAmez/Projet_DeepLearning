import streamlit as st
import pandas as pd
from get_data import load_data
from pretraitements import preprocess_data
import visualisations

def main():
    st.title("Application basée sur la base des diagnostics de performance énergétique (DPE) par commune en France")

    data = load_data()

    if data:
        # Titre de la section de navigation avec une taille de police plus grande
        st.sidebar.markdown("<h1 style='text-align: left;'>Navigation</h1>", unsafe_allow_html=True)

    # Chargement des données depuis les fichiers CSV
    df_ileDeFrance = pd.read_csv("df_ileDeFrance_final.csv")
    df_HorsIleDeFrance = pd.read_csv("df_HorsIleDeFrance_final.csv")

    # Section de sélection des options générales
    section = st.sidebar.selectbox("Sélectionnez une section :", ["Données Brutes",
                                       "Données Prétraitées", "Visualisations"])

    # Afficher la section sélectionnée
    if section == "Données Brutes":
        st.subheader("Données Brutes de L'API : Diagnostics de performance énergétique (DPE) par commune en France")
        st.write(data)  # Afficher les données brutes

    elif section == "Données Prétraitées":
        # Sélection du type de données prétraitées
        preprocess_type = st.sidebar.radio("Sélectionnez une catégorie de données prétraitées :", ["Île-de-France", "Hors Île-de-France"])

        if preprocess_type == "Île-de-France":
            st.subheader("Données prétraitées - Île-de-France")
            df_ileDeFrance_preprocessed, _ = preprocess_data(df_ileDeFrance, df_HorsIleDeFrance)
            st.write(df_ileDeFrance_preprocessed)  # Afficher les données prétraitées de l'Île-de-France

        elif preprocess_type == "Hors Île-de-France":
            st.subheader("Données prétraitées - Hors Île-de-France")
            _, df_HorsIleDeFrance_preprocessed = preprocess_data(df_ileDeFrance, df_HorsIleDeFrance)
            st.write(df_HorsIleDeFrance_preprocessed)  # Afficher les données prétraitées hors Île-de-France

    elif section == "Visualisations":
        st.subheader("Visualisations")
        df_ileDeFrance_preprocessed, df_HorsIleDeFrance_preprocessed = preprocess_data(df_ileDeFrance, df_HorsIleDeFrance)
        visualisations.display_map(df_ileDeFrance_preprocessed, df_HorsIleDeFrance_preprocessed)

if __name__ == "__main__":
    main()
