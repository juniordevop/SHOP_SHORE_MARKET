# créer une simle interface web

# import libs
import streamlit as st

# afficher du texte sur le navig
st.write ("bonjour, bv à la form dama")

# créer des colonnes
col_g, col_d = st.columns(2)

# faire une interface pour récupérer le nom et le salaire

    # champ de saisi du nom
# nom = st.text_input(label="saisir votre nom")
nom = col_g.text_input(label="saisir votre nom")

    # champ de saisi du salaire
# compte = st.number_input(label="saisir le numéro de compte")
compte = col_g.number_input(label="saisir le numéro de compte")

    # champ de saisi du salaire
# salaire = st.number_input(label="saisir votre salaire")
salaire = col_g.number_input(label="saisir votre salaire")

    # champ slider
# age = st.slider(label="Age de recherche", min_value=0,max_value=150,step = 1)
age = col_d.slider(label="Age de recherche", min_value=0,max_value=150,step = 1)

    # sélection (liste de choix)
# type_compte = st.selectbox(
type_compte = col_d.selectbox(
    'Type de compte',
    ['courant','épargne']
)

    # radio button
# gender = st.radio("genre", ("H","F"))
gender = col_d.radio("genre", ("H","F"))


# Ajout bouton
# btn = st.button("submit")
btn = col_d.button("submit")

# ecouteur de clic
if btn:
    st.write(f"Le nom est : {nom}")
    st.write(f"Le numéro de compte est : {compte}")
    st.write(f"Le salaire est : {salaire}")
    st.write(f"L'âge est : {age}  ans")
    st.write(f"Le type de compte est : {type_compte}")
    st.write(f"Le genre est : {gender}")

# Faire appel à l'API avec les informations saisies

# streamlit .\first_stream.py --