# créer une simle interface web

# import libs
import streamlit as st

# interroger l'api avec la bibs request
import requests

# import pandas
import pandas as pd

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
st.write ("Interface Administrateur")

# subdiviser l'interface en deux
col_g, col_d = st.columns(2)

    # champ de saisi du nom

# colonne de gauche

# colonne de droite
# -- data = {"nom":"NDIAYE", "prenom":"alou", "num_compte" :26, "Type_compte":"particulier","solde" : 2000000,"mdp":1818}
nom_client = col_g.text_input(label="nom client")
prenom_client = col_g.text_input(label="prenom client")
num_compte = col_g.number_input(label="num compte",min_value=0)
#Type_compte = col_d.text_input(label="Type_compte")
Type_compte = col_d.selectbox(
     'Type compte',
     ['Choisir le type','professionnel','particulier']
)
solde_compte = col_d.number_input(label="solde compte",min_value=0.0)
mdp_compte = col_d.number_input(label="mdp compte",min_value=0)

#statut_compte = col_d.selectbox(
#     'statut compte',
#     ['Actif','Inactif']
#)
type_action = col_d.selectbox(
     'ACTION SOUHAITEE',
     ["Choisir l'action",'AJOUTER','MODIFIER','SUPPRIMER']
)

btn_nouveau = col_d.button("ENREGISTRER")


# nom = st.text_input(label="saisir votre nom")
id_recherche = col_g.number_input(label="recherche par num_compte",min_value=0)

# Ajout bouton
# btn = st.button("recherche")
btn_recherche = col_g.button("rechercher le compte client")


# ecouteur click
if btn_recherche:
   # 0 test de la zone de recherche
   if id_recherche == 0:
        # 1 faire appel à l'api
        reponse = requests.get(
             api_url+"/api/cmdclientsbg",
             headers = headers # si header obligatoire
             ) # ,auth=(api_user,api_pass)
   else:
        # 1 faire appel à l'api
        reponse = requests.get(
             api_url+f"/api/cmdtrouveidclient?idclient={id_recherche}"
             ) # ,auth=(api_user,api_pass)

   if reponse.status_code == 200:
        # 2 recupérer le resultat
        resultat = reponse.json()
        # 3 afficher le resultat
        # transformer  resultat en liste
        liste_resultat = list(resultat["resultats"])
        # transformer liste en dataframe
        pd_result = pd.DataFrame(liste_resultat,columns=["nume_compte", "Type_compte", "prenom", "nom", "mdp", "solde"])
        # afficher dataframe
        st.dataframe(pd_result)
        #st.write(resultat["resultats"])
   else:
        st.write(f"Error code: {reponse.status_code}")

# ecouteur click       
if btn_nouveau:
   # 0 test de la zone de recherche
   if type_action == "AJOUTER":
          # ajout de nouveau client avec post
          # 1 déclarer les variables et les paramètres
               # ---data = {"nom":"NDIAYE", "prenom":"alou", "num_compte" :26, "Type_compte":"particulier","solde" : 2000000,"mdp":1818}
          data = {
               "nom":nom_client,
               "prenom":prenom_client,
               "num_compte" :num_compte,
               "Type_compte": Type_compte,
               "solde" : solde_compte,
               "mdp":mdp_compte
               #"statut": 1 if statut_compte == 'Actif' else 0
               }
               # 2 appel de l'api avec post et les paramètres
          reponse = requests.post(
                    api_url+"/api/cmdajoutclientbg",
                    headers = headers, # si header obligatoire
                    json = data
                    ) # ,auth=(api_user,api_pass)
               # 3 recuperer le resultat
          if reponse.status_code == 200:
          # 2 recupérer le resultat
               resultat = reponse.json()
               # 4 afficher le resultat 
               st.write(resultat)
          else:
               st.write(f"Error code: {reponse.status_code}")

   if type_action == "MODIFIER":
           # Modifier client avec post
          # 1 déclarer les variables et les paramètres
               # ---data = {"nom":"NDIAYE", "prenom":"alou", "num_compte" :26, "Type_compte":"particulier","solde" : 2000000,"mdp":1818}
          data = {
               "nom":nom_client,
               "prenom":prenom_client,
               "num_compte" :num_compte,
               "Type_compte": Type_compte,
               "solde" : solde_compte,
               "mdp":mdp_compte
               #"statut": 1 if statut_compte == 'Actif' else 0
               }
               # 2 appel de l'api avec post et les paramètres
          reponse = requests.post(
                    api_url+"/api/cmdupdateclientbg",
                    headers = headers, # si header obligatoire
                    json = data
                    ) # ,auth=(api_user,api_pass)
               # 3 recuperer le resultat
          if reponse.status_code == 200:
          # 2 recupérer le resultat
               resultat = reponse.json()
               # 4 afficher le resultat 
               st.write(resultat)
          else:
               st.write(f"Error code: {reponse.status_code}") 

   if type_action == "SUPPRIMER":
          
          reponse = requests.delete(
             api_url+f"/api/cmddeleteidclient?idclient={num_compte}"
             ) # ,auth=(api_user,api_pass)
        
               # 3 recuperer le resultat
          if reponse.status_code == 200:
          # 2 recupérer le resultat
               resultat = reponse.json()
               # 4 afficher le resultat 
               st.write(resultat)
          else:
               st.write(f"Error code: {reponse.status_code}") 

   # streamlit run .\st_api.py
   # streamlit run .\st_api.py -- server.port=80
   # D:\REPRISES COURS DIT 082023\streamlit_cours