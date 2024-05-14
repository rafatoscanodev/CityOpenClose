import streamlit as st
import pandas as pd
import requests
import folium
from streamlit_folium import folium_static

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

# Extrair dados de latitude e longitude
df = pd.DataFrame(data)
df = df[['latitude', 'longitude']].dropna()

# Converter para tipo numérico
df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')

# Remover linhas com valores inválidos
df = df.dropna(subset=['latitude', 'longitude'])

# Configurar o Streamlit
st.title("Mapa Interativo de Empatias em Recife")

# Criar o mapa
mapa = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=12)

# Adicionar pontos ao mapa
for index, row in df.iterrows():
    folium.Marker([row['latitude'], row['longitude']]).add_to(mapa)

# Exibir o mapa no Streamlit
folium_static(mapa)

