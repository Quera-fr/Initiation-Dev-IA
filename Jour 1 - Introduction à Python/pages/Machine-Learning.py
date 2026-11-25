# Import de streamlit
import streamlit as st
import requests
import pickle

# Bouton : Start
if st.button("Start"):
    # Requette vers l'API
    r = requests.get("http://localhost:8000/train_perception")

    # Affichage du score du modèle
    st.write(r.json())

    # Téléchargement du modèle
    chemin_fichier = '/workspaces/Initiation-Dev-IA/Jour 2 - Introduction au Machine Learning/model_ever_maried.pkl'

    with open(chemin_fichier, 'rb') as f:
        st.download_button(
            label="Télécharger le modèle",
            data=f,
            file_name="model_ever_maried.pkl",
            mime="application/octet-stream"
    )

