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
    audio_file = open("/Users/Jerome/Documents/GitHub/streamee/udemy_streamlit/initial_version/exercices/streamlit_basics/audio.ogg", "rb")
    audio = audio_file.read()
    st.audio(audio, format="audio/ogg")


    st.subheader("Video")
    # video_url = "/Users/Jerome/Documents/GitHub/streamee/udemy_streamlit/initial_version/exercices/streamlit_basics/video.mp4"
    # html_code = f'<iframe src="{video_url}" width="480" height="320"></iframe>'
    # st.markdown(html_code, unsafe_allow_html=True)

    # video_file = open("/Users/Jerome/Documents/GitHub/streamee/udemy_streamlit/initial_version/exercices/streamlit_basics/video.mp4", "rb")
    # video = video_file.read()
    # st.video(video)

    DEFAULT_WIDTH = 80
    VIDEO_DATA = "https://www.youtube.com/watch?v=89LPVXrm_Ic"

    # st.set_page_config(layout="wide")

    width = st.sidebar.slider(label="Width", min_value=0, max_value=100, value=DEFAULT_WIDTH, format="%d%%")
    # width = st.slider(label="Width", min_value=0, max_value=100, value=DEFAULT_WIDTH, format="%d%%")

    width = max(width, 0.01)
    side = max((100 - width) / 2, 0.01)

    _, container, _ = st.columns([side, width, side])
    container.video(data=VIDEO_DATA)

def layout():
    st.header("Tutoriel sur le layout")

    #Sidebar
    st.sidebar.title("Titre de barre navigation")  
    st.sidebar.write("projet des accidents")
    st.sidebar.metric(label="Temperature", value="70 °F", delta="1.2 °F")

    #Columns
    col1, col2 = st.columns(2)

    with col1:
        st.write("colonne 1")
        st.write("colonne 1")
        st.write("colonne 1")

    with col2:
        st.write("colonne 2")
        st.write("colonne 2")

    #Containers
    with st.container():
        st.header("Container 1")
        st.write("J'adore ...")
    with st.container():
        st.header("Container 2")
        st.write("...les sushis")

#######################################################
#                       MAIN
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

layout()