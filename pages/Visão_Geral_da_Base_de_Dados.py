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

#Visão Geral dos Dados
st.header('Visão Geral das Músicas do Spotify')
st.write(data.head())

st.subheader('Informações Gerais')

# Renomear os rótulos das estatísticas descritivas para português
descricao_estatisticas = data.describe().rename(index={
        'count': 'Contagem',
        'mean': 'Média',
        'std': 'Desvio Padrão',
        'min': 'Mínimo',
        '25%': '25º Percentil',
        '50%': 'Mediana',
        '75%': '75º Percentil',
        'max': 'Máximo'
    })

st.write("A tabela abaixo apresenta estatísticas descritivas sobre as músicas do Spotify.")
st.write(descricao_estatisticas)

# Créditos
st.sidebar.text("Desenvolvido por: George Souza")