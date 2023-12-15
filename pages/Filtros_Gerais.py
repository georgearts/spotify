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

# Sidebar com opções
st.sidebar.title('Opções')
menu = st.sidebar.selectbox('Selecione uma opção:', ('Análise de Popularidade', 'Análise de Duração',
                                                      'Análise por Artista','Análise de Lançamentos', 
                                                      'Correlação entre Variáveis'))




# Análise de Popularidade
if menu == 'Análise de Popularidade':
    st.header('Análise de Popularidade')

    st.subheader('Distribuição de Popularidade')
    fig_popularity = px.histogram(data, x='track_popularity', nbins=20, labels={'x': 'Popularidade'})
    st.plotly_chart(fig_popularity)

    st.subheader('Top 10 Músicas Mais Populares')
    
    # Remover duplicatas com base em 'track_name'
    unique_data = data.drop_duplicates(subset='track_name')
    
    top_10_popular = unique_data.nlargest(10, 'track_popularity')[['track_name', 'track_artist', 'track_popularity']]
    st.table(top_10_popular)


# Análise de Duração
elif menu == 'Análise de Duração':
    st.header('Análise de Duração')

    st.subheader('Distribuição de Duração das Músicas')
    fig_duration = px.histogram(data, x='duration_ms', nbins=20, labels={'x': 'Duração (ms)'})
    st.plotly_chart(fig_duration)

# Análise por Artista
elif menu == 'Análise por Artista':
    st.header('Análise por Artista')

    st.subheader('Top 10 Artistas Mais Recorrentes')
    top_10_artists = data['track_artist'].value_counts().nlargest(10)
    st.bar_chart(top_10_artists)



# Análise de Lançamentos
elif menu == 'Análise de Lançamentos':
    st.header('Análise de Lançamentos')

    st.subheader('Distribuição de Lançamentos por Ano')

    # Tentar converter 'track_album_release_date' para datetime
    try:
        data['track_album_release_date'] = pd.to_datetime(data['track_album_release_date'], errors='coerce')
    except ValueError as e:
        st.warning(f"Erro ao converter datas: {e}. Certifique-se de que as datas são válidas.")

    # Filtrar células que contêm apenas o ano
    valid_date_mask = data['track_album_release_date'].notnull() & \
                      (data['track_album_release_date'].dt.month != 1) & \
                      (data['track_album_release_date'].dt.day != 1)

    # Extrair o ano de lançamento
    data['release_year'] = data.loc[valid_date_mask, 'track_album_release_date'].dt.year

    # Plotar o histograma
    fig_release_year = px.histogram(data, x='release_year', nbins=20, labels={'x': 'Ano de Lançamento'})
    st.plotly_chart(fig_release_year)

# Análise de Correlação
elif menu == 'Correlação entre Variáveis':
    st.subheader('Correlação entre Variáveis')
    
    # Selecionar apenas colunas numéricas
    numeric_columns = data.select_dtypes(include='number').columns
    
    # Substituir valores não numéricos por NaN
    data_numeric = data[numeric_columns].apply(pd.to_numeric, errors='coerce')
    
    # Calcular a matriz de correlação
    corr_matrix = data_numeric.corr()
    
    # Plotar o heatmap com Plotly Express
    fig_corr = px.imshow(corr_matrix, x=numeric_columns, y=numeric_columns,
                         labels=dict(color='Correlação'), color_continuous_scale='viridis')
    
    # Adicionar anotações
    for i in range(len(numeric_columns)):
        for j in range(len(numeric_columns)):
            fig_corr.add_annotation(x=numeric_columns[i], y=numeric_columns[j],
                                    text=f"{corr_matrix.iloc[j, i]:.2f}", showarrow=False)
    
    st.plotly_chart(fig_corr)


# Créditos
st.sidebar.text("Desenvolvido por: George Souza")
