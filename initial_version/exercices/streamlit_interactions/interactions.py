import streamlit as st
import numpy as np
import pandas as pd
import datetime 


#######################################################
#                       FUNCTIONS
#######################################################

def button():
    button = st.button("Click me")
    st.write(f"Click status: {button}")


def checkbox():
    st.header("Check box")
    checkbox = st.checkbox("I am OK")
    st.write(f"Click status: {checkbox}")


def radio():
    st.header("Radio button")
    color = st.radio(
        "Quelle couleur préférez-vous ?",
        ("rouge", "vert", "bleu"),
        index = 0
    )

    st.write(f"Statut du clic: {color}")


def select_box():
    st.header("Select box")
    color = st.selectbox(
        "Quelle couleur préférez-vous ?",
        ("rouge", "vert", "bleu"),
        index = 0
    )
    st.write(f"Statut du clic: {color}")

def multi_select():
    st.header("Multi select")
    color = st.multiselect(
        "Quelle couleur préférez-vous ?",
        ("rouge", "vert", "bleu")
    )
    st.write(f"Statut du clic: {color}")


def slider():
    st.header("Slider")
    slider = st.slider("Entrez un nombre", min_value = 5, max_value = 25, step = 5)
    st.write(f"Le nombre est : {slider}")

def number_input():
    st.header("Nombre")
    number = st.number_input("Entrez un nombre", min_value = 5, max_value = 25, step = 5)
    st.write(f"Le nombre est : {number}")

def date_input():
    st.header("Date")
    date = st.date_input("Entrez une date", datetime.date(2023,8,31))
    st.write(f"La date est : {date}")   

def camera():
    st.header("Camera")
    photo = st.camera_input("Prenez une photo")
    if photo:
        st.image(photo)


#######################################################
#                       MAIN
#######################################################


# Titre de la page
if __name__ == "__main__":
    st.set_page_config(
        page_title="Streamlit interactive",
        page_icon="🚗",
        # layout="centered",                   # page centrée
        layout="wide",                      # toute la largeur
        initial_sidebar_state="expanded",   # sidebar de gauche
    )

    st.title("Widget toturial")
    st.sidebar.title("Search criterion")


    button()

    checkbox()

    radio()

    select_box()

    multi_select()

    slider()

    number_input()

    date_input()

    camera()