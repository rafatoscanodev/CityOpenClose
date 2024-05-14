import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

# URL dos dados CSV
url = "http://dados.recife.pe.gov.br/dataset/eb9b8a72-6e51-4da2-bc2b-9d83e1f198b9/resource/87fc9349-312c-4dcb-a311-1c97365bd9f5/download/empresasativender.csv"

# Função para carregar dados
@st.cache
def load_data(url):
    try:
        # Tentativa 1: Leitura padrão
        df = pd.read_csv(url)
        return df
    except pd.errors.ParserError:
        try:
            # Tentativa 2: Especificar delimitador como ponto e vírgula
            df = pd.read_csv(url, delimiter=';')
            return df
        except pd.errors.ParserError as e:
            st.error(f"Erro ao carregar os dados: {e}")
            return None

# Carregar os dados
df = load_data(url)

if df is not None:
    # Ordenar os dados pela coluna 'nome_bairro'
    if 'nome_bairro' in df.columns:
        df_sorted = df.sort_values(by='nome_bairro')

        # Exibir título e descrição do aplicativo
        st.title("Empresas Ativas em Recife")
        st.write("Dados carregados da URL fornecida e ordenados por 'nome_bairro'.")

        # Exibir colunas do DataFrame
        st.write("Colunas do DataFrame:")
        st.write(df.columns)

        # Exibir DataFrame ordenado
        st.write("Primeiros registros do DataFrame ordenado:")
        st.write(df_sorted.head(20))  # Exibe as primeiras 20 linhas do DataFrame ordenado

        # Verificar se as colunas de latitude e longitude existem
        if 'latitude' in df.columns and 'longitude' in df.columns:
            # Visualização: Latitudes e Longitudes por nome_bairro
            st.subheader("Latitudes e Longitudes por Nome Bairro")
            fig, ax = plt.subplots(figsize=(10, 6))
            for bairro in df['nome_bairro'].unique():
                bairro_data = df[df['nome_bairro'] == bairro]
                ax.scatter(bairro_data['longitude'], bairro_data['latitude'], label=bairro, alpha=0.6)
            
            ax.set_title("Latitudes e Longitudes por Nome Bairro")
            ax.set_xlabel("Longitude")
            ax.set_ylabel("Latitude")
            ax.legend(title="Bairro")
            st.pyplot(fig)
        else:
            st.error("As colunas 'latitude' e/ou 'longitude' não foram encontradas nos dados.")
    else:
        st.error("A coluna 'nome_bairro' não foi encontrada nos dados.")
else:
    st.error("Os dados não puderam ser carregados.")
