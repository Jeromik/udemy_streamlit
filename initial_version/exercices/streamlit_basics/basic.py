#######################################################
#                       IMPORT
#######################################################

import streamlit as st
import pandas as pd
from PIL import Image

#######################################################
#                       DEFINITION
#######################################################

# Lecture du fichier s&p500 dans le dataframe data
def connect_data_csv():
    st.header("Titre du dataframe")

    MY_PATH = "/Users/Jerome/Documents/GitHub/streamee/udemy_streamlit/initial_version/project/s&p500.csv"

    data = pd.read_csv(MY_PATH)
    # st.dataframe(data)
    st.dataframe(data.style.highlight_max(axis=0))


def display_write():
    st.title("Title")
    st.header("Header")
    st.subheader("Subheader")
    st.write("write")
    st.caption("caption")


def display_media():
    st.header("Streamlit display media tutorial")

    st.subheader("Image")
    image = Image.open("/Users/Jerome/Documents/GitHub/streamee/udemy_streamlit/initial_version/exercices/streamlit_basics/stock.jpeg")
    st.image(image, caption="@nobody", width = 300)

    st.subheader("Audio")
    audio = Image.open("/Users/Jerome/Documents/GitHub/streamee/udemy_streamlit/initial_version/exercices/streamlit_basics/stock.jpeg")
    st.image(image, caption="@nobody", width = 300)


#######################################################
#                       START
#######################################################


# Titre de la page
if __name__ == "__main__":
    st.set_page_config(
        page_title="Ma première appli streamlit",
        # layout="centered",                   # page centrée
        layout="wide",                      # toute la largeur
        initial_sidebar_state="expanded",   # sidebar de gauche
    )


# Simuler un bandeau en haut de la page
st.markdown(
    """
    <div style="background-color: #e6e6e6; padding: 10px; border-bottom: 2px solid #d4d4d4; margin-bottom: 10px;">
        Ceci est mon bandeau en haut de la page!
    </div>
    """,
    unsafe_allow_html=True,
)

# Le reste de votre code Streamlit
st.write("Le contenu principal de votre application se trouve ici.")


# Titre dans la page
st.title("Titre dans streamlit v2")

# Affichage du Dataframe
connect_data_csv()

display_write()

display_media()