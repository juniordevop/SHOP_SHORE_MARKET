# créer une simle interface web

# import libs
import streamlit as st

# interroger l'api avec la bibs request
import requests

# import pandas
import pandas as pd
import streamlit as st

#from app import my_sc
#st.write (my_sc)
# st.title("Interface Administrateur")


st.sidebar.success("Volet de navigation")
def main():
    st.title("INTERFACE COMMERCIAL")
    st.subheader("ESPACE ACHATS")
    st.write ("OPERATIONS COMMERCIALES")

    choice = st.sidebar.selectbox("Sous Sections",["Choisir votre boutique","Chic_mode","diop_technologie","mon_electromenege"])
    
    if choice == "Chic_mode":
        st.subheader("Boutique Chic_mode")
        
        #variables
        # http://192.168.1.107:3003/api/getclients
        api_url = "http://192.168.1.107:3003"
        api_user = ""
        api_pass = ""
        api_token = "" # jeton d'authentification
        headers = {
            "Content-Type":"application/json",
            "Autorizatoin":f"Basic {api_token}"
            }

        # afficher du texte sur le navig
        # st.write ("Interface Administrateur")

        # subdiviser l'interface en troix
        col1, col2, col3 = st.columns(3)

            # champ de saisi du nom

        # colonne de gauche

        # colonne 1
        with col1:
            st.write ("Vos informations de paiement")
            moyen_paiement = st.selectbox(
                'Service de paiement',
                ["Choisir le service",'ria','orange','free',"bank_group"]
            )
            num_compte = st.text_input(label="Numero du compte")
            pass_word = st.text_input(label="Mot de passe")

            #st.write ("Afficher le contenu")

            btn_connexion = st.button("SE CONNECTER")
            btn_produits = st.button("VOIR NOS PRODUITS")
            btn_panier = st.button("VOIR VOTRE PANIER")

        # colonne 2
        with col2:
            st.write ("Faites vos achats")
            nom_produit = st.selectbox(
                'Articles disponibles',
                ["Choisir l'article",'Jeans','T-shirt','Costume',"Polo"]
            )
            Marque_produit = st.selectbox(
                'Marque produit',
                ["Choisir la marque",'Nike','adidas','Lacoste','Levis strauss']
            )   
            Quantite_produit = st.number_input(label="Quantite Souhaitee",min_value=0)
            type_action = st.selectbox(
                'ACTION SOUHAITEE',
                ["Choisir l'action",'AJOUTER AU PANIER','SOUSTRAIRE DU PANIER','ANNULER VOTRE ACHAT']
            )
            st.write ("")
            st.write ("")
            btn_valider = st.button("VALIDER")


        # colonne 3
        with col3:
            st.write ("Bilan du panier")
            st.metric(label="TOTAL ARTICLES", value="5", delta="articles")
            st.metric(label="MONTANT DU PANIER", value="18000 XOF", delta="A Payer")
            st.metric(label="Votre solde payeur", value="35000 XOF", delta="suffisant")
            st.write ("")
            st.write ("")
            btn_payer = st.button("REGLER LA FACTURE")


        # nom = st.text_input(label="saisir votre nom")
        # id_recherche = col_g.number_input(label="recherche par num_compte",min_value=0)

if __name__=='__main__':
    main()