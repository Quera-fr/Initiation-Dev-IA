# Import de la bibliothèque streamlit
import streamlit as st

# Création d'un titre
st.title('Application Streamlit')


# Création d'une zone de texte
st.write("Ceci est du texte")

# Création d'un champ de saisi
name = st.text_input("Quel est votre nom ?")
st.write(name)

# Création d'un bouton
if st.button("Valider"):
    st.write("Bouton cliqué")

    # Affichage d'une image
    st.image('https://encrypted-tbn0.gstatic.com/licensed-image?q=tbn:ANd9GcRV0pV0Bxoj_anuhA23wL5VUNUO7oM-w0bo16Rc8zdR9uYZ-OYoANDqRcfDYucfeoAt4Aqq1MYt3ZFBw5Tytpyz7UF7n-TWL6-C59q7QueL2woOAurkbj6A9__nL9vpnmzTowpXjxcDGGs&s=19')


# Affichage d'une vidéo
st.video("https://www.youtube.com/embed/Y4s8NadbZfU?si=sIss3yAQS68ZDz-y")

# Création de colonnes 
col1, col2, col3 = st.columns(3)

with col1:
    st.write("Colonne 1")

with col2:
    st.write("Colonne 2")

with col3:
    st.write("Colonne 3")



# Configuration de la side bare
st.sidebar.image('https://quera-fablab.org/wp-content/uploads/2023/02/cropped-Logo-Quera-Fablab-1.png', width=100)


# Configuration d'une seconde page

