import streamlit as st
from get_data import load_data

def main():
    st.title("Application de qualité de l'air en France")

    # Chargement des données
    data = load_data()

    if data:
        # Titre de la section de navigation avec une taille de police plus grande
        st.sidebar.markdown("<h1 style='text-align: left;'>Navigation</h1>", unsafe_allow_html=True)

        # Sélecteur de section
        section = st.sidebar.selectbox("Sélectionnez une section :", ["Données Brutes",
                                       "Données Prétraitées", "Visualisations avant Prétraitements", "Visualisation après Prétraitements"])

        # Afficher la section sélectionnée
        if section == "Données Brutes":
            st.header("Données Brutes de Qualité de l'Air")
            st.write(data) # Afficher les données brutes
        elif section == "Données Prétraitées":
            st.header("Données Prétraitées de Qualité de l'Air")
            # Mettez votre contenu de prétraitement ici
            st.write("Contenu de la section de Données Prétraitées...")
        elif section == "Visualisations avant prétraitements":
            st.header("Visualisations avant Prétraitements")
            st.write("Contenu de la section de visualisations avant pret...")
            #st.plotly_chart(show_air_quality(data))  # Afficher la visualisation avant le prétraitement
        elif section == "Visualisation après Prétraitements":
            st.header("Visualisation après Prétraitements")
            st.write("Contenu de la section de visualisations après pret...")
            # st.plotly_chart(air_quality_map(data))  # Afficher la visualisation après le prétraitement
    else:
        st.error("Erreur lors du chargement des données. Veuillez réessayer plus tard.")

if __name__ == "__main__":
    main()
