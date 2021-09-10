  
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
				 'Capag - Visão detalhada',
				 'Quem somos nós']
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
	elif select_event_cidadao == 'Objetivos':
		st.markdown('Neste trabalho, utilizamos um modelo de aprendizado de máquina denominado Gradient Boosting com o objetivo de, utilizando as informações disponíveis \
		sobre os municípios brasileiros, estimar a capacidade de pagamento (Capag) dos municípios e compará-las com a Capag constante do site da Secretaria do Tesouro Nacional\
		(STN), quando disponível.')	
	elif select_event_cidadao == 'Capag - Visão detalhada':
		# st.sidebar.checkbox("Visualizar análises por município", True, key=1)
		lista_municipios = pd.Series(list(set(df['Município']))).sort_values()
		select = st.sidebar.selectbox('município', lista_municipios)
		df = df.set_index('Município')
		df['CLASS_CAPAG_real'] = df['CLASS_CAPAG_real'].astype('Int64')
		df_municipio = df[df.index==(select)]
		st.dataframe(df_municipio)
		st.text('Posicione o ponteiro do mouse sobre o dataframe para acessar a barra de rolagem.')
		st.text('Dessa forma, você conseguirá visualizar todas as variáveis')
	elif select_event_cidadao == 'Quem somos nós':
		st.markdown('Camila Maia Fátima Marques ...')
		st.markdown('Mario José Calvão Monnerat do Prado é pai, auditor-fiscal da Receita Federal, formado no MBA em Analytics e Inteligência Artificial da Fundação FIA de São Paulo')
		st.markdown('Reinaldo da Cruz Castro...')
		st.markdown('O trabalho sobre a classificação de pagamentos dos municípios brasileiros (CAPAG) foi feito, originariamente, como códigos e dissertação para o Trabalho de Conclusão de Curso de Camila em sua pós-graduação de Big Data/Data Science.')
		st.markdown('Para participar do Prêmio Tesouro Nacional, nós adaptamos os códigos para a plataforma streamlit, o que proporcionou que mais pessoas tivessem acesso a este conhecimento tão importante sobre os municípios brasileiros.')

		
	elif select_event_cidadao == 'Contextualização':
		st.markdown('A análise da capacidade de pagamento (Classificação CAPAG) apura a situação fiscal dos entes subnacionais que querem \
		contrair novos empréstimos com garantia da União. Esta classificação é um indicador de saúde econômica e fiscal dos municípios.')
		st.markdown('O intuito da CAPAG é apresentar de forma simples e transparente se um novo endividamento representa risco de crédito para o Tesouro Nacional.\
		Assim, um ente bem avaliado pelo Tesouro Nacional poderá acessar empréstimos com juros mais baixos, por contar com a União como seu garantidor.\
		Se, por algum motivo, o ente não puder honrar o pagamento da dívida, a União é quem terá que assumir o pagamento. A metodologia da CAPAG,\
		fruto de um aprimoramento da metodologia já usada anteriormente, foi elaborada pelo Tesouro Nacional, com apoio do Banco Mundial. O cálculo da CAPAG, \
		além de sintetizar essa situação fiscal em uma simples nota, possibilita a comparação entre os entes, com base em metodologia e informações conhecidas\
		e padronizadas. Corresponde a um serviço similar ao prestado pelas agências de classificação de risco de crédito. A própria STN passou a calcular e divulgar\
		as notas de modo regular, independentemente da existência de pedidos de aval ou garantia para operações de crédito. Enfim, trata-se de uma informação bastante útil\
		para os que buscam melhor compreender as finanças dos entes subnacionais.')
		st.markdown('Obter uma boa classificação da CAPAG é muito importante para os municípios, pois:')
		st.markdown('1) ao obter este reconhecimento por parte do Tesouro Nacional, o município obtém a garantia da União para contrair empréstimos; tendo a União como garantidor, o município pode obter melhores condições de financiamento.')
		st.markdown('2) licitações a preços mais vantajosos: empresas privadas podem utilizar a classificação CAPAG como um dos indicadores na tomada de decisão sobre participar ou não de um certame. O município, tendo uma boa capacidade de pagamento, pode atrair mais participantes para suas licitações e, consequentemente, propostas mais vantajosas economicamente.')
		st.markdown('3) a boa classificação de risco facilita a atração de empreendimentos e de investimentos privados para o município, pois reflete a boa saúde econômica e fiscal do ente. A classificação CAPAG pode ser um indicador a ser considerado pelos empresários e pelos investidores na tomada de decisão sobre onde abrir negócios ou investir dinheiro.')
		st.markdown('O objetivo da CAPAG é apresentar, de forma simples e transparente, os dados sobre a saúde financeira e fiscal dos municípios e é, conforme descrito acima, de grande interesse público e privado.')
		st.markdown('O valor da CAPAG varia de 1 a 4. Para fins de análise de dados, consideramos os valores 1 e 2 como sendo 0, o que mostra que o município não tem capacidade de pagamento. Também juntamos os valores 3 e 4 como sendo 1, o que indica que o município possui capacidade de pagamento')

if radio == 'Visão cientista de dados':
	lista_eventos_cientista = ['Coleta de Dados',
				   'Análise das variáveis qualitativas',
				   'Análise das variáveis quantitativas',
				   'Análise bivariada',
				   'Matriz de correlação',
				   'Dataframe completo',
				   'Aspectos técnicos']
	select_event_cientista = st.sidebar.selectbox(
		'Que informações você gostaria de visualizar?',
		lista_eventos_cientista)
	
	if select_event_cientista == 'Coleta de Dados':
		st.markdown('Foram utilizados 2 datasets neste trabalho:')
		st.markdown('1 - Capacidade de Pagamento (CAPAG) dos Municípios')
	        st.markdown('Arquivo disponível no formato csv, posteriormente convertido em excel. O dataset possui 5569 linhas e 11 colunas. Os dados foram coletados no website da Transparência do Tesouro Nacional 1, em janeiro de 2021. Link: http://www.tesourotransparente.gov.br/ckan/dataset/capag-municipios')

	elif select_event_cientista == 'Análise das variáveis qualitativas':
		st.write('Análise das variáveis qualitativas')
	elif select_event_cientista == 'Análise das variáveis quantitativas':
		st.write('Análise das variáveis quantitativas')
	elif select_event_cientista == 'Análise bivariada':
		st.write('Análise bivariada')
	elif select_event_cientista == 'Matriz de correlação':
		st.write('Matriz de correlação')
	elif select_event_cientista == 'Dataframe completo':
		st.write('Dataframe completo')
	elif select_event_cientista == 'Aspectos técnicos':
		st.write('Aspectos técnicos')
	


	

			   
#lista_eventos_projeto_capag = ['Apresentação','Contextualização','Objetivos','Coleta de Dados','Quem somos nós']
#select_event_capag = st.sidebar.selectbox('Selecione um evento.', lista_eventos_projeto_capag)

#url = ('https://raw.githubusercontent.com/MarioPrado1148/Capag/main/Images/carolina-munemasa-FYBJgygqCzM-unsplash_Ouro_Preto.jpg')
#response = requests.get(url)
#img = Image.open(BytesIO(response.content))
#st.sidebar.image(img, use_column_width = True)



