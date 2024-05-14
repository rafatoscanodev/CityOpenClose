import streamlit as st
import pandas as pd

# URL dos dados CSV
url = "http://dados.recife.pe.gov.br/dataset/eb9b8a72-6e51-4da2-bc2b-9d83e1f198b9/resource/87fc9349-312c-4dcb-a311-1c97365bd9f5/download/empresasativender.csv"

# Função para carregar dados
@st.cache
def load_data(url):
    df = pd.read_csv(url)
    return df

# Carregar os dados
df = load_data(url)

# Ordenar os dados pela coluna 'nome_bairro'
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
