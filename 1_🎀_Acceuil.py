import streamlit as st

from app import my_sc

st.sidebar.success("Select a page above")
def main():
    st.title("BIENVENU A SHOP SHORE")
    st.subheader("Voir nos adresses")
    st.write (my_sc)

    choice = st.sidebar.selectbox("SubMenu",["pandas","tensforflow"])
    if choice == "pandas":
        st.subheader("pandas")


if __name__=='__main__':
    main()


# streamlit run .\Acceuil.py