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

# Consulta por Filtros

st.header('Consulta por Filtros')

    # Filtros
selected_genre = st.selectbox('Selecione o Gênero:', data['playlist_genre'].unique())
    
    # Filtrar artistas com base no gênero selecionado
artists_by_genre = data[data['playlist_genre'] == selected_genre]['track_artist'].unique()
artists_by_genre.sort()  # Ordenar os artistas

selected_artist = st.selectbox('Selecione o Artista:', artists_by_genre)

    # Converter a coluna para o formato de data
data['track_album_release_date'] = pd.to_datetime(data['track_album_release_date'], errors='coerce')
    
    # Extrair o ano e eliminar valores nulos
release_years = data['track_album_release_date'].dt.year.dropna().astype(int).unique()
release_years.sort()  # Ordenar os anos
    
selected_release_year = st.selectbox('Selecione o Ano de Lançamento:', release_years)

    # Aplicar filtros
filtro_genre = (data['playlist_genre'] == selected_genre)
filtro_artist = (data['track_artist'] == selected_artist)
    
    # Considerar apenas registros válidos (não NaN) para evitar o erro
filtro_release_year = (data['track_album_release_date'].notna()) & (data['track_album_release_date'].dt.year == selected_release_year)

filtered_data = data[filtro_genre & filtro_artist & filtro_release_year]

st.subheader('Resultados da Consulta')
st.write(filtered_data)

# Créditos
st.sidebar.text("Desenvolvido por: George Souza")