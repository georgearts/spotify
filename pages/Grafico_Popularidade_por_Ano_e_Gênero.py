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

# Gráfico de Popularidade por Ano e Gênero
st.header('Gráfico de Popularidade por Ano e Gênero')

# Extrair o ano da coluna track_album_release_date
data['release_year'] = pd.to_datetime(data['track_album_release_date'], errors='coerce').dt.year.astype('Int64')

# Filtros
selected_year = st.selectbox('Selecione o Ano:', data['release_year'].unique())

# Filtrar dados com base no ano selecionado
filtered_data_year = data[data['release_year'] == selected_year]

# Criar o gráfico de barras
fig_popularity_by_genre = px.bar(filtered_data_year, x='playlist_genre', y='track_popularity', 
                                     labels={'x': 'Gênero', 'y': 'Popularidade Média'},
                                     title=f'Popularidade Média por Gênero ({selected_year})',
                                     category_orders={'playlist_genre': filtered_data_year.groupby('playlist_genre')['track_popularity'].mean().sort_values(ascending=False).index})

st.plotly_chart(fig_popularity_by_genre)

# Créditos
st.sidebar.text("Desenvolvido por: George Souza")