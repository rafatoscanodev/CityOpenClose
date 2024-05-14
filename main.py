import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt

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

# Verificar colunas do DataFrame
st.write("Colunas do DataFrame:")
st.write(df.columns)

# Exibir DataFrame
st.write(df)

# Visualização 1: Contagem de registros por categoria (substituir 'categoria' pela coluna correta)
if 'categoria' in df.columns:
    st.subheader("Contagem de Registros por Categoria")
    fig1, ax1 = plt.subplots()
    df['categoria'].value_counts().plot(kind='bar', ax=ax1)
    ax1.set_title("Contagem de Registros por Categoria")
    ax1.set_xlabel("Categoria")
    ax1.set_ylabel("Contagem")
    st.pyplot(fig1)
else:
    st.write("Coluna 'categoria' não encontrada nos dados.")

# Visualização 2: Distribuição de Idades (substituir 'idade' pela coluna correta)
if 'idade' in df.columns:
    st.subheader("Distribuição de Idades")
    fig2, ax2 = plt.subplots()
    df['idade'].plot(kind='hist', bins=20, ax=ax2)
    ax2.set_title("Distribuição de Idades")
    ax2.set_xlabel("Idade")
    ax2.set_ylabel("Frequência")
    st.pyplot(fig2)
else:
    st.write("Coluna 'idade' não encontrada nos dados.")

# Visualização 3: Latitudes e Longitudes
if 'latitude' in df.columns and 'longitude' in df.columns:
    st.subheader("Latitudes e Longitudes")
    fig3, ax3 = plt.subplots()
    ax3.scatter(df['longitude'], df['latitude'])
    ax3.set_title("Latitudes e Longitudes")
    ax3.set_xlabel("Longitude")
    ax3.set_ylabel("Latitude")
    st.pyplot(fig3)
else:
    st.write("Colunas 'latitude' e/ou 'longitude' não encontradas nos dados.")

# Visualização 4: Contagem de Registros por Sexo (substituir 'sexo' pela coluna correta)
if 'sexo' in df.columns:
    st.subheader("Contagem de Registros por Sexo")
    fig4, ax4 = plt.subplots()
    df['sexo'].value_counts().plot(kind='bar', ax=ax4)
    ax4.set_title("Contagem de Registros por Sexo")
    ax4.set_xlabel("Sexo")
    ax4.set_ylabel("Contagem")
    st.pyplot(fig4)
else:
    st.write("Coluna 'sexo' não encontrada nos dados.")



