import streamlit as st


# Inserir a logo do Spotify
st.image('Spotify-logo.png',  use_column_width=True)

# Centralizar o título do dashboard
st.markdown("<h1 style='text-align: center;'>Análises de Músicas Spotify</h1>", unsafe_allow_html=True)

# Apresentação do estudo
st.title("Estudo analítico de Dados do Spotify")

st.write("""
Este estudo analisa dados obtidos do API da plataforma Spotify, com dados obtidos de um recorte da 4ª semana do mês de Janeiro do ano de 2020, num pacote de cerca de 5000 músicas e 30000 execuções no aplicativo 
""")

st.subheader("Dicionário de Dados")

tabela_markdown = """
| Variável                   | Classe     | Descrição                                      |
|----------------------------|------------|------------------------------------------------|
| track_id                   | character  | Id único da Canção                              |
| track_name                 | character  | Nome da Canção                                  |
| track_artist               | character  | Nome do Artista                                 |
| track_popularity          | double     | Popularidade da Canção de 0 a 100               |
| track_album_id             | character  | Id único do Álbum Musical                       |
| track_album_name           | character  | Nome do Álbum Musical                           |
| track_album_release_date   | character  | Data de lançamento do Álbum                     |
| playlist_name              | character  | Nome da lista de música                         |
| playlist_id                | character  | Id da lista de música                           |
| playlist_genre             | character  | Gênero musical da lista                         |
| playlist_subgenre          | character  | Subgênero musical da lista                      |
| duration_ms                | double     | Duração da música em Milisegundos              |
"""

# Usando st.write para exibir a tabela Markdown
st.write(tabela_markdown)


# Apresentação das principais análises realizadas
st.subheader("Principais Análises Realizadas:")
st.markdown("""
- **Análise de Popularidade:** Exploração da distribuição da popularidade das músicas no conjunto de dados, identificando padrões e outliers.
- **Análise de Duração:** Investigação da duração média das músicas, identificando se existe alguma tendência ao longo do tempo.
- **Análise por Artista:** Segmentação dos dados por artista para avaliar a popularidade média, duração média e outras métricas relevantes.
- **Distribuição de Popularidade por Gênero:** Visualização da distribuição da popularidade das músicas agrupadas por gênero musical.
- **Análise de Lançamentos:** Estudo da distribuição temporal dos lançamentos de músicas, identificando períodos de maior atividade.
- **Correlação entre Variáveis:** Análise da relação entre diferentes variáveis, como popularidade, duração e outras métricas relevantes.
- **Gráfico de Popularidade por Ano e Gênero Musical:** Criação de gráficos para visualizar a evolução da popularidade ao longo dos anos, segmentada por gênero musical.
- **Visão Geral dos Dados:** Apresentação de estatísticas descritivas e insights gerais sobre o conjunto de dados do Spotify.
- **Informações Gerais:** Inclusão de detalhes sobre o tamanho do conjunto de dados, fonte dos dados e quaisquer observações importantes.
""")


# Créditos
st.sidebar.text("Desenvolvido por: George Souza")