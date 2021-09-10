  
# Projeto CAPAG
# Previsão da capacidade de pagamento dos municípios

# Referências:
# https://www.analyticsvidhya.com/blog/2021/05/a-brief-introduction-to-building-interactive-ml-webapps-with-streamlit/ 

# !pip install streamlit --upgrade

# Importação das libraries
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
import plotly.express as px
import math
from PIL import Image
import requests
from io import BytesIO

# Configuração da página
st.set_page_config(layout="wide")
sns.set_style('darkgrid')
st.set_option('deprecation.showPyplotGlobalUse', False)
pd.options.display.float_format = "{:,.2f}".format

# Carregamento dos dados
data_url =('https://raw.githubusercontent.com/MarioPrado1148/Capag/main/Datasets/df_streamlit_com_previsao.csv')
@st.cache(persist=True)

def load_data():
    data=pd.read_csv(data_url, sep = ';', index_col = 0)
    return data

df =load_data()

# Página Principal
st.title('Classificação da capacidade de pagamento dos municípios brasileiros com base em dados geoeconômicos')

st.sidebar.title('Estimação da Capag com Ciências de Dados')

lista_eventos_radio = ['Visão cidadão', 'Visão cientista de dados']
radio = st.sidebar.radio('Escolha sua Visão',lista_eventos_radio)

if radio == 'Visão cidadão':
	lista_eventos_cidadao = ['Apresentação',
				 'Contextualização',
				 'Objetivos',
				 'Capag - Visão resumida',
				 'Capag - Visão detalhada']
	select_event_cidadao = st.sidebar.selectbox(
		'Que informações você gostaria de visualizar?',
		lista_eventos_cidadao)
	
	if select_event_cidadao == 'Apresentação':
		url = ('https://raw.githubusercontent.com/MarioPrado1148/Capag/main/Images/carolina-munemasa-FYBJgygqCzM-unsplash_Ouro_Preto.jpg')
		response = requests.get(url)
		img = Image.open(BytesIO(response.content))
		st.image(img)
		st.text('Fotografia de Ouro Preto (MG). Autoria de Carolina Munemasa.')
		st.text('Fonte: https://unsplash.com/s/photos/ouro-preto. Consultado em 09/09/2021')
	
if radio == 'Visão cientista de dados':
	lista_eventos_cientista = ['Coleta de Dados',
				   'Análise das variáveis qualitativas',
				   'Análise das variáveis quantitativas',
				   'Análise bivariada',
				   'Matriz de correlação'
				   'Dataframe completo',
				   'Aspectos técnicos',
				   'Quem somos nós']
	select_event_cientista = st.sidebar.selectbox(
		'Que informações você gostaria de visualizar?',
		lista_eventos_cientista)


	

			   
#lista_eventos_projeto_capag = ['Apresentação','Contextualização','Objetivos','Coleta de Dados','Quem somos nós']
#select_event_capag = st.sidebar.selectbox('Selecione um evento.', lista_eventos_projeto_capag)

#url = ('https://raw.githubusercontent.com/MarioPrado1148/Capag/main/Images/carolina-munemasa-FYBJgygqCzM-unsplash_Ouro_Preto.jpg')
#response = requests.get(url)
#img = Image.open(BytesIO(response.content))
#st.sidebar.image(img, use_column_width = True)



