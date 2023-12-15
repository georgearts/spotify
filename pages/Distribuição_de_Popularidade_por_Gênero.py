import streamlit as st
import pandas as pd

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

# Distribuição de Popularidade por Gênero
st.header('Distribuição de Popularidade por Gênero')

fig_genre_popularity = px.box(data, x='playlist_genre', y='track_popularity', labels={'x': 'Gênero', 'y': 'Popularidade'})
st.plotly_chart(fig_genre_popularity)

# Créditos
st.sidebar.text("Desenvolvido por: George Souza")