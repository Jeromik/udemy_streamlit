import streamlit as st
import pandas as pd
from pandas_datareader import data as pdr
import plotly.express as px
import numpy as np
from PIL import Image

#######################################################
#                     FUNCTIONS
#######################################################


def read_data():
    my_path = "/Users/Jerome/Documents/GitHub/streamee/udemy_streamlit/initial_version/project/s&p500.csv"
    df = pd.read_csv(my_path)
    return df

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

    df = read_data()

    st.subheader("Part 1 - S&P500 screener")
    with st.expander("Part 1 - Explications", expanded = False):
        st.write("""
            In the table below, you will find most of the companies in the S&P500 (stock market index of the 500 largest American companies) with certain criteria such as :
                
                - The name of the company
                - The sector of activity
                - Market capitalization
                - Dividend payout percentage (dividend/stock price)
                - The company's profit margin in percentage
            
            ⚠️ This data is scrapped in real time from the yahoo finance API. ⚠️

            ℹ️ You can filter / search for a company with the filters on the left. ℹ️
        """)
    st.write("Nombre d'entreprises:", len(df))
    st.dataframe(df.iloc[:,1:])

