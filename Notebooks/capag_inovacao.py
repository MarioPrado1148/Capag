  
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

########################################################################################
# Carregamento dos dados
#df_streamlit_com_previsao
data_url =('https://raw.githubusercontent.com/MarioPrado1148/Capag/main/Dataset/df_streamlit_com_previsao.csv')
@st.cache(persist=True)

def load_data():
    data=pd.read_csv(data_url, sep = ';', index_col = 0)
    return data

df =load_data()

########################################################################################
# Carregamento dos dados
#df_streamlit_com_previsao_resumido
data_url_resumido =('https://raw.githubusercontent.com/MarioPrado1148/Capag/main/Dataset/df_streamlit_com_previsao_resumido.csv')
@st.cache(persist=True)

def load_data_resumido():
    data_resumido=pd.read_csv(data_url_resumido, sep = ',', index_col = 0)
    return data_resumido

df_resumido =load_data_resumido()


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
	# Imagem
	url2 = ('https://raw.githubusercontent.com/MarioPrado1148/Capag/main/Images/digitalmarketing.jpg')
	response = requests.get(url2)
	img2 = Image.open(BytesIO(response.content))
	st.sidebar.image(img2)
	
	
	if select_event_cidadao == 'Apresentação':
		url = ('https://raw.githubusercontent.com/MarioPrado1148/Capag/main/Images/carolina-munemasa-FYBJgygqCzM-unsplash_Ouro_Preto.jpg')
		response = requests.get(url)
		img = Image.open(BytesIO(response.content))
		st.image(img)
		st.text('Fotografia de Ouro Preto (MG). Autoria de Carolina Munemasa.')
		st.text('Fonte: https://unsplash.com/s/photos/ouro-preto. Consultado em 09/09/2021')
	elif select_event_cidadao == 'Objetivos':
		texto1 = 'Neste trabalho, utilizamos um modelo de aprendizado de máquina denominado XGBoost com o objetivo de, utilizando as informações disponíveis \
		sobre os municípios brasileiros, estimar a capacidade de pagamento (Capag) dos municípios e compará-las com a Capag constante do site da Secretaria do Tesouro Nacional\
		(STN), quando disponível.'
		st.markdown(texto1)
		st.markdown('Esse modelo utilizou apenas as variáveis geoeconômicas para estimar a Capag dos municípios para os quais esta não foi calculada pelo órgão classificador.')
		st.markdown('Entende-se que é uma solução embrionária. Possuindo o órgão classificador outras variáveis úteis ao cálculo, as features utilizadas na solução proposta poderiam ser utilizadas em caráter suplementar, subsidiário na estimação.')
		
	elif select_event_cidadao == 'Capag - Visão detalhada':
		# st.sidebar.checkbox("Visualizar análises por município", True, key=1)
		lista_municipios = pd.Series(list(set(df['Município']))).sort_values()
		select = st.sidebar.selectbox('município', lista_municipios)
		df = df.set_index('Município')
		df['Capag_real'] = df['Capag_real'].astype('Int64')
		df_municipio = df[df.index==(select)]
		st.dataframe(df_municipio)
		st.text('Posicione o ponteiro do mouse sobre o dataframe para acessar a barra de rolagem.')
		st.text('Dessa forma, você conseguirá visualizar todas as variáveis')
	elif select_event_cidadao == 'Quem somos':
		st.markdown('Camila Fátima Maia Marques é esposa do Breno, mãe da Malu e da Bebela, médica, analista-tributário da Receita Federal, especialista em Ciência de Dados e Big Data pela Puc Minas.')
		st.markdown('Mario José Calvão Monnerat do Prado é esposo de Roxana, pai da Nicole, auditor-fiscal da Receita Federal, formado pela FIA/USP nos cursos de Data Mining e MBA em Analytics e Inteligência Artificial, estudante na pós-graduação em Direito Tributário e Compliance pela Universidade Católica de Brasília. Atualmente é supervisor do Laboratório de Inovação da SRRF08 da Receita Federal do Brasil.')
		st.markdown('Reinaldo da Cruz Castro é esposo de Elízia; pai de João Pedro e Luís Felipe; auditor-fiscal da Receita Federal, especialista em Direito Tributário pelo IBET, formado em Data Mining pela FIA/USP, especialista em Big Data e Ciência de Dados pela Puc Minas e estudante de Teologia pela Uninter. Atualmente é supervisor do Laboratório de Inovação da SRRF08 da Receita Federal do Brasil.')
    		
	elif select_event_cidadao == 'Contextualização':
		st.markdown('A análise da capacidade de pagamento (Classificação CAPAG) apura a situação fiscal dos entes subnacionais que querem \
		contrair novos empréstimos com garantia da União. Esta classificação é um indicador de saúde econômica e fiscal dos municípios.')
		st.markdown('O intuito da CAPAG é apresentar, de forma simples e transparente, se um novo endividamento representa risco de crédito para o Tesouro Nacional.\
		Assim, um ente bem avaliado pelo Tesouro Nacional poderá acessar empréstimos com juros mais baixos, por contar com a União como seu garantidor.')
		st.markdown('A metodologia da CAPAG foi elaborada pelo Tesouro Nacional, com apoio do Banco Mundial e possibilita a comparação entre os entes federados, \
		com base em metodologia e informações conhecidas e padronizadas. Corresponde a um serviço similar ao prestado pelas agências de classificação de risco de crédito.\
		A própria STN passou a calcular e divulgar as notas de modo regular, independentemente da existência de pedidos de aval ou garantia para operações de crédito. Enfim, trata-se de uma informação bastante útil para os que buscam melhor compreender as finanças dos entes subnacionais.')
		st.markdown('Uma boa classificação da CAPAG é muito importante para os municípios, pois:')
		st.markdown('1) ao obter este reconhecimento por parte do Tesouro Nacional, o município obtém a garantia da União para contrair empréstimos; tendo a União como garantidor, o município pode obter melhores condições de financiamento.')
		st.markdown('2) licitações a preços mais vantajosos: empresas privadas podem utilizar a classificação CAPAG como um dos indicadores na tomada de decisão sobre\
		participar ou não de um certame. O município, tendo uma boa capacidade de pagamento, pode atrair mais participantes para suas licitações e, consequentemente,\
		propostas mais vantajosas economicamente para a coletividade.')
		st.markdown('3) a boa classificação de risco facilita a atração de empreendimentos e de investimentos privados para o município, pois reflete a boa saúde econômica e\
		fiscal do ente. A classificação CAPAG pode ser um indicador a ser considerado pelos empresários e pelos investidores na tomada de decisão sobre onde abrir negócios ou \
		investir dinheiro.')
		st.markdown('A CAPAG pode ter os valores A, B, C e D.')
		st.markdown('O ente que possuir classificação "A" ou "B" é elegível à contratação de garantias da União em seus financiamentos. Os demais conceitos ("C” e "D”)\
		são um sinal de que a situação fiscal e financeira do município não lhe permite realizar operações de crédito com garantia da União.')
		st.markdown('Para o algoritmo nesse estudo, as notas C e D estão representadas por "1" e as notas A e B, por "0"; destarte, o conceito 1 indica má situação fiscal\
		e financeira, o conceito 0, que o ente está apto à contratação de garantias.')
		st.markdown('O trabalho sobre a classificação de pagamentos dos municípios brasileiros (CAPAG) foi feito, originariamente, como códigos e dissertação para o \
		Trabalho de Conclusão de Curso de Camila, da equipe de autores desta proposta de solução, em sua pós-graduação em Ciência de Dados e Big Data.')
		st.markdown('Para participar do Prêmio Tesouro Nacional, evoluímos o modelo e adaptamos os códigos para a plataforma streamlit, com o intuito de mais pessoas tivessem acesso \
			    a este conhecimento tão importante sobre os municípios brasileiros.')

if radio == 'Visão cientista de dados':
	lista_eventos_cientista = ['Coleta de Dados',
				   'Análise das variáveis qualitativas',
				   'Análise das variáveis quantitativas',
				   'Variável Capag (alvo)',
				   'Análise bivariada',
				   'Matriz de correlação',
				   'Dataframe completo'
				   ]
	select_event_cientista = st.sidebar.selectbox(
		'Que informações você gostaria de visualizar?',
		lista_eventos_cientista)
	
	
	if select_event_cientista == 'Coleta de Dados':
		st.markdown('Foram utilizados 2 datasets neste trabalho:')
		st.markdown('1 - Capacidade de Pagamento (CAPAG) dos Municípios')
		st.text('Arquivo com 5569 linhas e 19 colunas, disponível no formato csv.')
		st.text('Os dados foram coletados no website da Transparência do Tesouro Nacional, em 16 de setembro de 2021.')
		st.text('Link: http://www.tesourotransparente.gov.br/ckan/dataset/capag-municipios')
		st.markdown('2.	PIB e outros indicadores econômicos')
		st.text('Arquivo com 50115 linhas e 43 colunas, disponível no formato xls.')
		st.text('Os dados foram coletados na sessão de estatísticas econômicas do website do IBGE, em janeiro de 2021.')
		st.text('Link: https://www.ibge.gov.br/estatisticas/economicas/contas-nacionais/9088-produto-interno-bruto-dos-municipios.html?=&t=resultados')
		
		# Imagem
		url2 = ('https://raw.githubusercontent.com/MarioPrado1148/Capag/main/Images/programa.jpg')
		response = requests.get(url2)
		img2 = Image.open(BytesIO(response.content))
		st.sidebar.image(img2)

	elif select_event_cientista == 'Análise das variáveis qualitativas':	
		select_radio_quali = st.sidebar.radio('Selecione a variável',['Região','Região Metropolitana', 'Mun_Reg_Geog_Imediata'])
		if select_radio_quali == 'Região':
			col1, col2 = st.columns(2)
			with col1:
				st.header('Variável Região')
				sns.countplot(x = "Região", data = df).set_ylabel('Quantidade')
				st.pyplot()
			with col2: 
				st.header('Análise') 			
				st.markdown('Verifica-se que há mais municípios na Região Nordeste, seguida de perto pela Região Sudeste.')
					
		elif select_radio_quali == 'Região Metropolitana':
			col1, col2 = st.columns(2)
			with col1:
				st.header('Variável Região Metropolitana')			
				sns.countplot(data = df, x = "Reg_Metropolitana").set_ylabel('Quantidade')
				st.pyplot()
			with col2:
				st.header('Análise') 
				st.markdown('Verifica-se que a maior parte dos municípios brasileiros não integra Regiões Metropolitanas.')
				
		elif select_radio_quali == 'Mun_Reg_Geog_Imediata':
			col1, col2 = st.columns(2)
			with col1:
				st.header('Variável Mun_Reg_Geog_Imediata')
				sns.countplot(data = df, x = "Mun_Reg_Geog_Imediata").set_ylabel('Quantidade')
				st.pyplot()
			with col2: 
				st.header('Análise') 

				st.markdown('Verifica-se que apenas uma pequena parte dos municípios brasileiros constitui polos. A grande maioria está no entorno dos polos.')
				
					    
	elif select_event_cientista == 'Análise das variáveis quantitativas':
		select_radio_quanti = st.sidebar.radio('Selecione a variável',['PIB_per_capita', 'VAB_Agricultura/Total','VAB_Indústria/Total','VAB_Serviço/Total','VAB_Adm/Total'])
		if select_radio_quanti == 'PIB_per_capita':
			
			col1, col2 = st.columns(2)
			with col1:
				st.header('Variável PIB_per_capita')
				url = ('https://raw.githubusercontent.com/MarioPrado1148/Capag/main/Images/boxplot_PIB_per_capita.jpg')
				response = requests.get(url)
				img1 = Image.open(BytesIO(response.content))
				st.image(img1)
				
			with col2: 
				st.header('Análise') 
				st.markdown('A variável PIB_per_capita expressa o valor médio do PIB, em reais.')
				st.markdown('Verifica-se que quase todos os municípios possuem PIB per capita inferior a R$ 50.000,00.')
				st.markdown('Há presença de outliers superiores, caracterizados pelos pontos acima do traço vertical superior.')
				
		
		if select_radio_quanti == 'VAB_Agricultura/Total':
			
			col1, col2 = st.columns(2)
			with col1:
				st.header("Variável VAB_Agricultura/Total")
				url = ('https://raw.githubusercontent.com/MarioPrado1148/Capag/main/Images/boxplot_VAB_Agricultura_Total.jpg')
				response = requests.get(url)
				img2 = Image.open(BytesIO(response.content))
				st.image(img2)

			with col2: 
				st.header('Análise') 
				st.markdown('Esta variável expressa a razão entre o Valor Agregado pela Agricultura e o total dos Valores Agregados pela Economia.')
				st.markdown('Até 50 % dos municípios possuem VAB_Agricultura/Total inferior a 20 %.')
				st.markdown('Constata-se a presença de outliers, que são valores disprepantes em relação aos demais, representados pelos pontos que estão acima do traço horizontal superior.')
				
		
		if select_radio_quanti == 'VAB_Indústria/Total':
			
			col1, col2 = st.columns(2)
			with col1:
				st.header("Variável VAB_Indústria/Total")
				url = ('https://raw.githubusercontent.com/MarioPrado1148/Capag/main/Images/boxplot_VAB_Indústria_Total.jpg')
				response = requests.get(url)
				img3 = Image.open(BytesIO(response.content))
				st.image(img3)
			with col2: 
				st.header('Análise') 
				st.markdown('Esta variável expressa a razão entre o Valor Agregado pela Indústria e o total dos Valores Agregados pela Economia.')
				st.markdown('Até 50 % dos municípios possuem VAB_Indústria/Total inferior a 10 %.')
				st.markdown('Constata-se a presença de outliers, que são valores disprepantes em relação aos demais, representados pelos pontos que estão acima do traço horizontal superior.')
				
		
		if select_radio_quanti == 'VAB_Serviço/Total':
			col1, col2 = st.columns(2)
			with col1:
				st.header('Variável VAB_Serviço/Total')
				url = ('https://raw.githubusercontent.com/MarioPrado1148/Capag/main/Images/boxplot_VAB_Serviço_Total.jpg')
				response = requests.get(url)
				img4 = Image.open(BytesIO(response.content))
				st.image(img4)
			with col2: 
				st.header('Análise') 
				st.markdown('Esta variável expressa a razão entre o Valor Agregado pelo setor de Serviços e o total dos Valores Agregados pela Economia.')
				st.markdown('Até 50 % dos municípios possuem VAB_Serviço/Total inferior a 30 %.')
				st.markdown('Constata-se a presença de outliers, que são valores disprepantes em relação aos demais, representados pelos pontos que estão acima do traço horizontal superior.')
					
		if select_radio_quanti == 'VAB_Adm/Total':
			
			col1, col2 = st.columns(2)
			with col1:
				st.header('Variável VAB_Adm/Total')
				url = ('https://raw.githubusercontent.com/MarioPrado1148/Capag/main/Images/boxplot_VAB_Adm_Total.jpg')
				response = requests.get(url)
				img5 = Image.open(BytesIO(response.content))
				st.image(img5)
			with col2: 
				st.header('Análise') 
				st.markdown('Esta variável expressa a razão entre o Valor Agregado pelo setor de Administração, Defesa, Educação e Saúde Públicas e Seguridade Social (VAB_Adm) e o total dos Valores Agregados pela Economia.')
				st.markdown('Até 50 % dos municípios possuem VAB_Adm/Total inferior a 30 %.')
				st.markdown('Não se verifica a presença de outliers (valores discrepantes).')
	elif select_event_cientista == 'Variável Capag (alvo)':
		col1, col2 = st.columns(2)
		with col1:
			st.header('Variável Capag')
			url = ('https://raw.githubusercontent.com/MarioPrado1148/Capag/main/Images/graf_barros_capag.jpg')
			response = requests.get(url)
			img7 = Image.open(BytesIO(response.content))
			st.image(img7)

		with col2: 
			st.header('Análise')
			st.markdown('O valor 0 indica que o município possui Capag A ou B segundo o cálculo oficial da Secretaria do Tesouro Nacional (STN); o valor 1 indica Capag C ou D.')	
			st.markdown('Verifica-se que o quantitativo de municípios com Capag A ou B é ligeiramente menor do que o número de municípios que possuem Capag C ou D.')
			st.markdown('Destaque-se que há 1.152 municípios para os quais não há Capag calculado pela STN, os quais não estão representados no gráfico.')
		
	elif select_event_cientista == 'Análise bivariada':
		select_radio_bivariada = st.sidebar.radio('Selecione as variáveis',['Capag x PIB_per_capita','Capag x VAB_Agricultura/Total',
										   'Capag x VAB_Indústria/Total','Capag x VAB_Serviço/Total',
										   'Capag x VAB_Adm/Total'])
		
			
		if select_radio_bivariada == 'Capag x PIB_per_capita':
			col1, col2 = st.columns(2)
			with col1:
				st.header('Variáveis Capag x PIB_per_capita')
				url = ('https://raw.githubusercontent.com/MarioPrado1148/Capag/main/Images/boxplot_Capag_X_PIB__per_capita.jpg')
				response = requests.get(url)
				img6 = Image.open(BytesIO(response.content))
				st.image(img6)
			with col2: 
				st.header('Análise') 			
				st.markdown('Verifica-se que a mediana do PIB dos municípios com Capag classes A e B (representadas pelo valor 0) é superior à mediana dos municípios com Capag  nas classe C e D.');
				st.markdown('Há mais outliers superiores (valores muito grandes, que se destacam dos demais),para os municípios das classes A e B (representadas pelo valor 0).')
		if select_radio_bivariada == 'Capag x VAB_Agricultura/Total':
			col1, col2 = st.columns(2)
			with col1:
				st.header('Variáveis Capag x VAB_Agricultura/Total')
				url = ('https://raw.githubusercontent.com/MarioPrado1148/Capag/main/Images/boxplot_Capag_X_VAB_Agricultura_Total.jpg')
				response = requests.get(url)
				img6 = Image.open(BytesIO(response.content))
				st.image(img6)
			with col2: 
				st.header('Análise') 			
				st.markdown('Observa-se que a mediana do VAB_Agricultura/Total com Capag classes A e B (representadas pelo valor 0) é superior à mediana dos municípios com Capag  nas classe C e D.')
				st.markdown('Há mais outliers superiores (valores muito grandes, que se destacam dos demais), para os municípios das classes C e D (representadas pelo valor 1).')
		if select_radio_bivariada == 'Capag x VAB_Indústria/Total':
			col1, col2 = st.columns(2)
			with col1:
				st.header('Variáveis Capag x VAB_Indústria/Total')
				url = ('https://raw.githubusercontent.com/MarioPrado1148/Capag/main/Images/boxplot_Capag_X_VAB_Indústria_Total.jpg')
				response = requests.get(url)
				img6 = Image.open(BytesIO(response.content))
				st.image(img6)
			with col2: 
				st.header('Análise') 			
				st.markdown('Observa-se que a mediana do VAB_Indústria/Total dos municípios com Capag classes A e B (representadas pelo valor 0) é superior à mediana dos municípios com Capag  nas classe C e D.')
				st.markdown('Há mais outliers superiores (valores muito grandes, que se destacam dos demais), para os municípios das classes C e D (representadas pelo valor 1).')
		if select_radio_bivariada == 'Capag x VAB_Serviço/Total':
			col1, col2 = st.columns(2)
			with col1:
				st.header('Variáveis Capag x VAB_Serviço/Total')
				url = ('https://raw.githubusercontent.com/MarioPrado1148/Capag/main/Images/boxplot_Capag_X_VAB_Serviço_Total.jpg')
				response = requests.get(url)
				img6 = Image.open(BytesIO(response.content))
				st.image(img6)
			with col2: 
				st.header('Análise') 			
				st.markdown('Observa-se que a mediana do VAB_Serviço/Total dos municípios com Capag classes A e B (representadas pelo valor 0) é superior à mediana dos municípios com Capag  nas classe C e D.')
				st.markdown('Há mais outliers superiores (valores muito grandes, que se destacam dos demais), para os municípios das classes C e D (representadas pelo valor 1).')
		if select_radio_bivariada == 'Capag x VAB_Adm/Total':
			col1, col2 = st.columns(2)
			with col1:
				st.header('Variáveis Capag x VAB_Adm/Total')
				url = ('https://raw.githubusercontent.com/MarioPrado1148/Capag/main/Images/boxplot_Capag_X_VAB_Adm_Total.jpg')
				response = requests.get(url)
				img6 = Image.open(BytesIO(response.content))
				st.image(img6)
			with col2: 
				st.header('Análise') 			
				st.markdown('Observa-se que a mediana do VAB_Adm/Total dos municípios com Capag classes C e D (representadas pelo valor 1) é superior à mediana dos municípios com Capag  nas classe A e B.')
				st.markdown('Há mais outliers superiores (valores muito grandes, que se destacam dos demais), para os municípios das classes C e D (representadas pelo valor 1).')

		
	elif select_event_cientista == 'Matriz de correlação':
		url = ('https://raw.githubusercontent.com/MarioPrado1148/Capag/main/Images/corr_matrix4.jpg')
		response = requests.get(url)
		img = Image.open(BytesIO(response.content))
		st.markdown('A matriz de correlação expressa a relação entre as variáveis quantitativas.')
		st.markdown('O valor mais alto de correlação, em módulo, refere-se à correlação entre as variáveis VAB_Adm/Total e Pib_per_capita. O sinal negativo indica que quando uma aumenta, a outra diminui.')
		st.markdown('Destaque-se também a forte correlação positiva entre VAB_Indústria/Total e o Pib_per_capita, o que indica que quanto maior a participação da indústria na economia do município, maior o Pib per capita.')	    			    
		st.image(img)
		
		
		
	elif select_event_cientista == 'Dataframe completo':
		st.dataframe(df)
		
		#Imagem
		url2 = ('https://raw.githubusercontent.com/MarioPrado1148/Capag/main/Images/programa.jpg')
		response = requests.get(url2)
		img2 = Image.open(BytesIO(response.content))
		st.sidebar.image(img2)
	elif select_event_cientista == 'Aspectos técnicos':
		st.markdown('Este trabalho teve por objetivo prever a capacidade de pagamento dos municípios brasileiros (Capag), utilizando variáveis disponíveis sob a forma de dados abertos.')
	 



