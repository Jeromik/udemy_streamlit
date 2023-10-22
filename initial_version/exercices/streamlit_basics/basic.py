import streamlit as st
import pandas as pd
from PIL import Image


# Pour augmenter la largeur de l'affichage au max
def set_page_full():
    st.markdown(
        """<style>
            .reportview-container .main .block-container {
                max-width: 100%;
            }
        </style>""",
        unsafe_allow_html=True,
    )

# Pour augmenter la largeur de l'affichage du nombre de pixels précisés
def set_page_width(width):
    st.markdown(
        f"""<style>
            .reportview-container .main .block-container {{
                max-width: {width}px;
            }}
        </style>""",
        unsafe_allow_html=True,
    )

# set_page_full()
# set_page_width(YOUR_WIDTH_IN_PIXELS)


def connect_data_csv():
    st.header("Streamlit data connect tutorial")

    MY_PATH = "C:\Users\Jerome\Documents\GitHub\streamee\udemy_streamlit\initial_version\project\s&p500.csv"

    data = pd.read_csv(MY_PATH)
    st.dataframe(data)


if __name__ == "__main__":
    st.set_page_config(
        page_title="Ma première appli streamlit",
        layout="centered"
    )

st.title("Titre dans streamlit v2")