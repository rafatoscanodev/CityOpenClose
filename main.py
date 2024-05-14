import streamlit as st
import pandas as pd
import requests

# URL dos dados JSON
url = "http://dados.recife.pe.gov.br/dataset/eb9b8a72-6e51-4da2-bc2b-9d83e1f198b9/resource/b4c77553-4d25-4e3a-adb2-b225813a02f1/download/metadados_empativas.json"

# Função para carregar dados
@st.cache
def load_data(url):
    response = requests.get(url)
    data = response.json()
    return data

# Carregar os dados
data = load_data(url)

# Converter para DataFrame
df = pd.DataFrame(data)

# Exibir título e descrição do aplicativo
st.title("Visualizações de Empatias em Recife")
st.write("Dados carregados da URL fornecida.")

# Exibir DataFrame
st.write("Primeiros registros do DataFrame:")
st.write(df.head())

# Exibir colunas do DataFrame
st.write("Colunas do DataFrame:")
st.write(df.columns)




