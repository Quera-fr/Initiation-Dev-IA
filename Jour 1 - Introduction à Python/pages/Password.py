import streamlit as st

# Création d'une varible persistante
if 'n' not in st.session_state.keys():
    st.session_state['n'] = 2

# Demmandez à l'utilisateur son mot de passe
pass_word = st.text_input("Quel est le mot de passe ?")

bouton = st.button('Envoyer')

# Si le mot de passe est correcte la caméra est dispo
if pass_word == "Quera_Password" and bouton and st.session_state['n'] >= 0:
    picture = st.camera_input("Take a picture")
    st.session_state.photo_bytes = picture
    

# Si le mot de passe est incorrecte on affiche les tentatives restantes
elif bouton and st.session_state['n'] > 0:
    st.write(f'Il vous reste {st.session_state['n']} tentatives.' )
    st.session_state['n'] -=1

# S'il n'y a plus de tentatives restantes l'accès est refusé
elif st.session_state['n']<=0 and bouton:
    st.text("Accès refusé")

# Bouton reset
if st.sidebar.button('Reset'):
    st.session_state['n'] = 2