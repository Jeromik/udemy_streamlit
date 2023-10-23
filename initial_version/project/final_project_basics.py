import streamlit as st
import pandas as pd
from pandas_datareader import data as pdr
import plotly.express as px
import numpy as np
from PIL import Image



#######################################################
#                       MAIN
#######################################################


# Titre de la page
if __name__ == "__main__":
    st.set_page_config(
        page_title="UDEMY projet",
        page_icon="🚗",
        # layout="centered",                   # page centrée
        layout="wide",                      # toute la largeur
        initial_sidebar_state="expanded",   # sidebar de gauche
    )

    st.title("S&P500 screener & analysis")
    st.sidebar.title("Search criterion")

    image = Image.open("/Users/Jerome/Documents/GitHub/streamee/udemy_streamlit/initial_version/project/stock.jpeg")
    _,col_image_2,_ = st.columns([1,2,1])
    with col_image_2:
        st.image(image, caption="Toto")

