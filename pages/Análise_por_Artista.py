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


st.header('Análise por Artista')

# Filtro por Artista
selected_artist = st.selectbox('Selecione um Artista', data['track_artist'].unique())

# Exibição de Infografia do Artista
st.subheader(f'Infografia para {selected_artist}')

# Criar um gráfico de barras com a média de popularidade por música do artista selecionado
artist_data = data[data['track_artist'] == selected_artist]
fig_artist = px.bar(artist_data, x='track_name', y='track_popularity', labels={'x': 'Música', 'y': 'Popularidade'})
st.plotly_chart(fig_artist)


# Créditos
st.sidebar.text("Desenvolvido por: George Souza")