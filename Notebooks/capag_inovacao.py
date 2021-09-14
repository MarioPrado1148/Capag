  
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
				 'Quem somos']
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
		texto1 = 'Neste trabalho, utilizamos um modelo de aprendizado de máquina denominado Gradient Boosting com o objetivo de, utilizando as informações disponíveis \
		sobre os municípios brasileiros, estimar a capacidade de pagamento (Capag) dos municípios e compará-las com a Capag constante do site da Secretaria do Tesouro Nacional\
		(STN), quando disponível.'
		st.markdown(texto1)
		#st.markdown(f"<h2 style='text-align: justify;'><b>{texto}</b></h2>", unsafe_allow_html=True)
		#st.markdown(f"<h5 style='text-align: justify;'>{texto1}</h5>", unsafe_allow_html=True)
		#st.markdown(f"<p style='text-align: justify;'>{texto1}</p>", unsafe_allow_html=True)
		
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
	elif select_event_cidadao == 'Quem somos':
		st.markdown('Camila Fátima Maia Marques é esposa do Breno, mãe da Malu e da Bebela, médica, analista-tributário da Receita Federal, especialista em Ciência de Dados e Big Data pela Puc Minas.')
		st.markdown('Mario José Calvão Monnerat do Prado é esposo de Roxana, pai da Nicole, auditor-fiscal da Receita Federal, formado pela FIA/USP nos cursos de Data Mining e MBA em Analytics e Inteligência Artificial, estudante na pós-graduação em Direito Tributário e Compliance pela Universidade Católica de Brasília. Atualmente é supervisor do Laboratório de Inovação da SRRF08 da Receita Federal do Brasil')
		st.markdown('Reinaldo da Cruz Castro é esposo de Elízia; pai de João Pedro e Luís Felipe; auditor-fiscal da Receita Federal, especialista em Direito Tributário pelo IBET, formado em Data Mining pela FIA/USP, especialista em Big Data e Ciência de Dados pela Puc Minas e estudante de Teologia pela Uninter. Atualmente é supervisor do Laboratório de Inovação da SRRF08 da Receita Federal do Brasil.')
    

		
	elif select_event_cidadao == 'Contextualização':
		st.markdown('A análise da capacidade de pagamento (Classificação CAPAG) apura a situação fiscal dos entes subnacionais que querem \
		contrair novos empréstimos com garantia da União. Esta classificação é um indicador de saúde econômica e fiscal dos municípios.')
		st.markdown('O intuito da CAPAG é apresentar, de forma simples e transparente, se um novo endividamento representa risco de crédito para o Tesouro Nacional.\
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
		st.markdown('A CAPAG pode ter os valores A, B, C e D.')
		st.markdown('O ente que possuir classificação "A" ou "B" é elegível à contratação de garantias da União em seus financiamentos. Os demais conceitos ("C” e "D”) são um sinal de que a situação fiscal e financeira do município não lhe permite realizar operações de crédito..')
		st.markdown('Para o algoritmo nesse estudo, as notas C e D estão representadas por "1" e as notas A e B, por "0"; destarte, o conceito 1 indica má situação fiscal e financeira, o conceito 0, que o ente está apto à contratação de garantias.')
		st.markdown('O trabalho sobre a classificação de pagamentos dos municípios brasileiros (CAPAG) foi feito, originariamente, como códigos e dissertação para o Trabalho de Conclusão de Curso de Camila em sua pós-graduação de Big Data/Data Science.')
		st.markdown('Para participar do Prêmio Tesouro Nacional, nós adaptamos os códigos para a plataforma streamlit, o que proporcionou que mais pessoas tivessem acesso a este conhecimento tão importante sobre os municípios brasileiros.')

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
		st.text('Arquivo com 5569 linhas e 11 colunas, disponível no formato csv.')
		st.text('Os dados foram coletados no website da Transparência do Tesouro Nacional 1, em janeiro de 2021.')
		st.text('Link: http://www.tesourotransparente.gov.br/ckan/dataset/capag-municipios')
		
		st.markdown('2.	PIB e outros indicadores econômicos')
		st.text('Arquivo com 50115 linhas e 43 colunas, disponível no formato xls.')
		st.text('Os dados foram coletados na sessão de estatísticas econômicas do website do IBGE, em janeiro de 2021.')
		st.text('Link: https://www.ibge.gov.br/estatisticas/economicas/contas-nacionais/9088-produto-interno-bruto-dos-municipios.html?=&t=resultados')

	elif select_event_cientista == 'Análise das variáveis qualitativas':	
		select_radio_quali = st.sidebar.radio('Selecione a variável',['Região','Região Metropolitana', 'Mun_Reg_Geog_Imediata'])
		if select_radio_quali == 'Região':
			col1, col2 = st.columns(2)

			with col1:
			    st.markdown("<h1 style='text-align: center; color: blue;'>Variável 'Região'</h1>", unsafe_allow_html=True)
			    sns.countplot(x = "Região", data = df).set_ylabel('Quantidade')
			    st.pyplot()

			with col2: 
			    st.markdown("<h1 style='text-align: center; color: blue;'>Análise</h1>", unsafe_allow_html=True)
			    st.markdown('Verifica-se que há maior quantidade de municípios na Região Nordeste, a qual é seguida de perto pela Região Sudeste')
		
		elif select_radio_quali == 'Região Metropolitana':
			col1, col2 = st.columns(2)

			with col1:
			    st.markdown("<h1 style='text-align: center; color: blue;'>Variável 'Região Metropolitana'</h1>", unsafe_allow_html=True)
			    sns.countplot(data = df, x = "Reg_Metropolitana")
			    st.pyplot()

			with col2: 
			    st.markdown("<h1 style='text-align: center; color: blue;'>Análise</h1>", unsafe_allow_html=True)
			    st.markdown('Verifica-se que há maior parte dos municípios brasileiros não integra Regiões Metropolitanas.')
				
		elif select_radio_quali == 'Mun_Reg_Geog_Imediata':
			col1, col2 = st.columns(2)

			with col1:
			    st.markdown("<h1 style='text-align: center; color: blue;'>Variável 'Mun_Reg_Geog_Imediata'</h1>", unsafe_allow_html=True)
			    sns.countplot(data = df, x = "Mun_Reg_Geog_Imediata")
			    st.pyplot()

			with col2: 
			    st.markdown("<h1 style='text-align: center; color: blue;'>Análise</h1>", unsafe_allow_html=True)
			    st.markdown('Verifica-se que apenas uma pequena parte dos municípios brasileiros constitui Polos. A grande maioria está no entorno dos polos.')
				
					    
	elif select_event_cientista == 'Análise das variáveis quantitativas':
		select_radio_quanti = st.sidebar.radio('Selecione a variável',['PIB percentual', 'VAB_Agricultura/Total','VAB_Indústria/Total','VAB_Serviço/Total','VAB_Adm/Total'])
		if select_radio_quanti == 'PIB percentual':
			#st.write('teste')
			col1, col2 = st.columns(2)
			with col1:
				st.markdown("<h1 style='text-align: center; color: blue;'>Variável 'Pib Percentual'</h1>", unsafe_allow_html=True)
				fig = px.box(df, y = 'PIB_PERC')
				fig.update_layout(height=400, width = 400)
				st.plotly_chart(fig,height=400) 
		
		if select_radio_quanti == 'VAB_Agricultura/Total':
			#st.write('teste')
			col1, col2 = st.columns(2)
			with col1:
				st.markdown("<h1 style='text-align: center; color: blue;'>Variável 'VAB_Agricultura/Total'</h1>", unsafe_allow_html=True)
				fig = px.box(df, y = 'VAB_Agricultura/Total')
				fig.update_layout(height=400, width = 400)
				st.plotly_chart(fig,height=400)
				
		
		if select_radio_quanti == 'VAB_Indústria/Total':
			#st.write('teste')
			col1, col2 = st.columns(2)
			with col1:
				st.markdown("<h1 style='text-align: center; color: blue;'>Variável 'VAB_Indústria/Total'</h1>", unsafe_allow_html=True)
				fig = px.box(df, y = 'VAB_Indústria/Total')
				fig.update_layout(height=400, width = 400)
				st.plotly_chart(fig,height=400)
				
		
		if select_radio_quanti == 'VAB_Serviço/Total':
			#st.write('teste')
			col1, col2 = st.columns(2)
			with col1:
				st.markdown("<h1 style='text-align: center; color: blue;'>Variável 'VAB_Serviço/Total'</h1>", unsafe_allow_html=True)
				fig = px.box(df, y = 'VAB_Serviço/Total')
				fig.update_layout(height=400, width = 400)
				st.plotly_chart(fig,height=400)
				
		
		if select_radio_quanti == 'VAB_Adm/Total':
			#st.write('teste')
			col1, col2 = st.columns(2)
			with col1:
				st.markdown("<h1 style='text-align: center; color: blue;'>Variável 'VAB_Adm/Total'</h1>", unsafe_allow_html=True)
				fig = px.box(df, y = 'VAB_Adm/Total')
				fig.update_layout(height=400, width = 400)
				st.plotly_chart(fig,height=400)
		
		
	elif select_event_cientista == 'Análise bivariada':
		st.write('Análise bivariada')
	elif select_event_cientista == 'Matriz de correlação':
		st.write('Matriz de correlação')
	elif select_event_cientista == 'Dataframe completo':
		st.dataframe(df)
	elif select_event_cientista == 'Aspectos técnicos':
		st.markdown('Este trabalho teve por objetivo prever a capacidade de pagamento dos municípios brasileiros (Capag), utilizando variáveis disponíveis sob a forma de dados abertos.')
	


	

			   
#lista_eventos_projeto_capag = ['Apresentação','Contextualização','Objetivos','Coleta de Dados','Quem somos nós']
#select_event_capag = st.sidebar.selectbox('Selecione um evento.', lista_eventos_projeto_capag)

#url = ('https://raw.githubusercontent.com/MarioPrado1148/Capag/main/Images/carolina-munemasa-FYBJgygqCzM-unsplash_Ouro_Preto.jpg')
#response = requests.get(url)
#img = Image.open(BytesIO(response.content))
#st.sidebar.image(img, use_column_width = True)



