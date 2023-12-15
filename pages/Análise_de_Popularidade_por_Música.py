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

st.header('Popularidade por Música com Filtro de Seleção')

# Filtro por Música
selected_song = st.selectbox('Selecione uma Música', data['track_name'].unique())

# Exibição da Popularidade da Música Selecionada
st.subheader(f'Popularidade para a Música: {selected_song}')

# Obtenha a popularidade da música selecionada
popularity_selected_song = data[data['track_name'] == selected_song]['track_popularity'].values[0]
st.write(f'A popularidade da música "{selected_song}" é {popularity_selected_song}')

# Créditos
st.sidebar.text("Desenvolvido por: George Souza")