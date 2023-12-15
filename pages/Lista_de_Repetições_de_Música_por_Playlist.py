import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px

# Carregar os dados
@st.cache_data
def load_data():
    data = pd.read_csv('spotfy.csv', sep=';')
    return data

# Lê os dados
data = load_data()

# Inserir a logo do Spotify
st.image('Spotify-logo.png',  use_column_width=True)

# Nova Análise: Repetições por Playlist

st.header('Repetições por Playlist')

# Filtro por Playlist
selected_playlist = st.selectbox('Selecione uma Playlist', data['playlist_name'].unique())

# Exibição da quantidade de repetições por música na playlist selecionada
playlist_data = data[data['playlist_name'] == selected_playlist]
repetitions_by_song = playlist_data['track_name'].value_counts()
st.bar_chart(repetitions_by_song)

# Créditos
st.sidebar.text("Desenvolvido por: George Souza")