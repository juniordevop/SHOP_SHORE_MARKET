#import streamlit as st

#st.set_page_config(
    #page_title="SHOP SHORE",
    #page_icon="✨"
#)
# titre sur la page principale
#st.title("BIENVENU A SHOP SHORE")
# instruction sur le volet
#st.sidebar.success("Select a page above")

# créer une simle interface web

# import libs
import streamlit as st

# interroger l'api avec la bibs request
import requests

# import pandas
import pandas as pd

st.sidebar.success("Volet de navigation")
def main():
    st.title("INTERFACE COMMERCIAL")
    st.subheader("ESPACE ACHATS")
    st.write ("OPERATIONS COMMERCIALES")

    choice = st.sidebar.selectbox("Sous Sections",["Choisir votre boutique","Chic_mode","diop_technologie","mon_electromenege"])
    if choice == "Chic_mode":
        st.subheader("Boutique Chic_mode")


if __name__=='__main__':
    main()

   # streamlit run .\st_api.py
   # streamlit run .\st_api.py -- server.port=80
   # D:\REPRISES COURS DIT 082023\streamlit_cours