# Projeto CAPAG
# Previsão da capacidade de pagamento dos municípios

# Referências:
# https://www.analyticsvidhya.com/blog/2020/10/create-interactive-dashboards-with-streamlit-and-python/
# https://towardsdatascience.com/build-your-first-data-visualization-web-app-in-python-using-streamlit-37e4c83a85db
# https://www.analyticsvidhya.com/blog/2020/12/deploying-machine-learning-models-using-streamlit-an-introductory-guide-to-model-deployment/
# https://towardsdatascience.com/interactive-machine-learning-and-data-visualization-with-streamlit-7108c5032144
# https://www.coursera.org/projects/interactive-dashboards-streamlit-python
#### https://www.analyticsvidhya.com/blog/2021/05/a-brief-introduction-to-building-interactive-ml-webapps-with-streamlit/ ####

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
st.title('Classificação da Capacidade de Pagamento dos Municípios brasileiros com base em dados geoeconômicos')

# Preparação do sidebar (barra lateral)
st.sidebar.title('Seletor de Análises e Gráficos')
#st.sidebar.markdown('Que informações você gostaria de visualizar?')

lista_eventos = ['Apresentação','Contextualização','Análise das Variáveis Categóricas','Análise das Variáveis Quantitativas', 'Dataframe completo', 'Visão por Município','Quem somos nós']
select_event = st.sidebar.selectbox('Que informações você gostaria de visualizar?', lista_eventos)

if select_event == 'Apresentação':
	st.header('Conheça a saúde financeira de seu município')
	st.subheader('Acesse o menu ao lado e analise os dados como um cientista de dados!')
	url = ('https://raw.githubusercontent.com/MarioPrado1148/Capag/main/Images/carolina-munemasa-FYBJgygqCzM-unsplash_Ouro_Preto.jpg')
	response = requests.get(url)
	img = Image.open(BytesIO(response.content))
	st.image(img)
	st.text('Fotografia de Ouro Preto (MG). Autoria de Carolina Munemasa.')
	st.text('Fonte: https://unsplash.com/s/photos/ouro-preto. Consultado em 09/09/2021')
	
	
		
elif select_event == 'Contextualização':
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

    
# Análise Exploratória de dados das Variáveis Categóricas
elif select_event == 'Análise das Variáveis Categóricas':
    select_radio = st.sidebar.radio('Selecione a variável',['Região',
							    'Região Metropolitana',
							    #'Unidade da Federação',
							    'Mun_Reg_Geog_Imediata'
							    #'Hierarquia Urbana',
							 #   'Região Rural'
							   ])
    if select_radio == 'Região':
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h1 style='text-align: center; color: blue;'>Variável 'Região'</h1>", unsafe_allow_html=True)
            sns.countplot(data = df, x = "Região")
            st.pyplot()
            
        with col2: 
            st.markdown("<h1 style='text-align: center; color: blue;'>Análise</h1>", unsafe_allow_html=True)
            st.markdown('Verifica-se que a região Nordeste possui a maior quantidade de municípios do Brasil, seguida de perto pela Região Sudeste')
    elif select_radio == 'Região Metropolitana':
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h1 style='text-align: center; color: blue;'>Variável 'Região Metropolitana'</h1>", unsafe_allow_html=True)
            sns.countplot(data = df, x = "Reg_Metropolitana")
            st.pyplot()
            
        with col2: 
            st.markdown("<h1 style='text-align: center; color: blue;'>Análise</h1>", unsafe_allow_html=True)
            st.markdown('Verifica-se que a maior parte dos municípios não está localizada em Regiões Metropolitanas.')
    elif select_radio == 'Unidade da Federação':
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h1 style='text-align: center; color: blue;'>Variável 'Unidade da Federação'</h1>", unsafe_allow_html=True)
            sns.countplot(data = df, x = "UF")
            st.pyplot()
            
        with col2: 
            st.markdown("<h1 style='text-align: center; color: blue;'>Análise</h1>", unsafe_allow_html=True)
            st.markdown('Verifica-se que há maior parte dos municípios não faz parte de Regiões Metropolitanas.')
    
    elif select_radio == 'Mun_Reg_Geog_Imediata':
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<h1 style='text-align: center; color: blue;'>Variável 'Mun_Reg_Geog_Imediata'</h1>", unsafe_allow_html=True)
            sns.countplot(data = df, x = "Mun_Reg_Geog_Imediata")
            st.pyplot()
        with col2: 
            st.markdown("<h1 style='text-align: center; color: blue;'>Análise</h1>", unsafe_allow_html=True)
            st.markdown('Verifica-se que há maior parte dos municípios não faz parte de Regiões Metropolitanas.')

		#elif select_radio == 'Hierarquia Urbana':
       # col1, col2 = st.columns(2)
      #  with col1:
     #       st.markdown("<h1 style='text-align: center; color: blue;'>Variável 'Hierarquia Urbana'</h1>", unsafe_allow_html=True)
    #        sns.countplot(data = df, x = "Hierarquia_Urbana")
   #         st.pyplot()
  #      with col2: 
 #           st.markdown("<h1 style='text-align: center; color: blue;'>Análise</h1>", unsafe_allow_html=True)
#            st.markdown('Verifica-se que a maior parte dos municípios não faz parte de Regiões Metropolitanas.')
# Análise Exploratória de dados das Variáveis Quantitativas       
                  
          
elif select_event == 'Análise das Variáveis Quantitativas':
    select_radio = st.sidebar.radio('Selecione a variável',['PIB percentual', 'VAB_Agricultura/Total','VAB_Indústria/Total','VAB_Serviço/Total','VAB_Adm/Total'])
    if select_radio == 'PIB percentual':
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<h1 style='text-align: center; color: blue;'>Variável 'Pib Percentual'</h1>", unsafe_allow_html=True)
            fig = px.box(df, y = 'PIB_PERC')
            fig.update_layout(height=400, width = 400)
            st.plotly_chart(fig,height=400)        
        with col2: 
            st.markdown("<h1 style='text-align: center; color: blue;'>Análise</h1>", unsafe_allow_html=True)
            st.markdown('Verifica-se que há maior quantidade de municípios na Região Nordeste, a qual é seguida de perto pela Região Sudeste')
    
    elif select_radio == 'VAB_Agricultura/Total':
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<h1 style='text-align: center; color: blue;'>Variável 'VAB_Agricultura/Total'</h1>", unsafe_allow_html=True)
            fig = px.box(df, y = 'VAB_Agricultura/Total')
            st.plotly_chart(fig)        
        with col2: 
            st.markdown("<h1 style='text-align: center; color: blue;'>Análise</h1>", unsafe_allow_html=True)
            st.markdown('Verifica-se que há maior quantidade de municípios na Região Nordeste, a qual é seguida de perto pela Região Sudeste')
   
    elif select_radio == 'VAB_Indústria/Total':
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<h1 style='text-align: center; color: blue;'>Variável 'VAB_Indústria/Total'</h1>", unsafe_allow_html=True)
            fig = px.box(df, y = 'VAB_Indústria/Total')
            st.plotly_chart(fig)        
        with col2: 
            st.markdown("<h1 style='text-align: center; color: blue;'>Análise</h1>", unsafe_allow_html=True)
            st.markdown('Verifica-se que há maior quantidade de municípios na Região Nordeste, a qual é seguida de perto pela Região Sudeste')
    
    elif select_radio == 'VAB_Serviço/Total':
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<h1 style='text-align: center; color: blue;'>Variável 'VAB_Serviço/Total'</h1>", unsafe_allow_html=True)
            fig = px.box(df, y = 'VAB_Serviço/Total')
            st.plotly_chart(fig)        
        with col2: 
            st.markdown("<h1 style='text-align: center; color: blue;'>Análise</h1>", unsafe_allow_html=True)
            st.markdown('Verifica-se que há maior quantidade de municípios na Região Nordeste, a qual é seguida de perto pela Região Sudeste')
    
    elif select_radio == 'VAB_Adm/Total':
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<h1 style='text-align: center; color: blue;'>Variável 'VAB_Adm/Total'</h1>", unsafe_allow_html=True)
            fig = px.box(df, y = 'VAB_Adm/Total')
            st.plotly_chart(fig)        
        with col2: 
            st.markdown("<h1 style='text-align: center; color: blue;'>Análise</h1>", unsafe_allow_html=True)
            st.markdown('Verifica-se que há maior quantidade de municípios na Região Nordeste, a qual é seguida de perto pela Região Sudeste')

# Apresentação do Dataframe completo
elif select_event == 'Dataframe completo':
    st.table(df)
elif:
  # st.sidebar.checkbox("Visualizar análises por município", True, key=1)
    lista_municipios = pd.Series(list(set(df['Município']))).sort_values()
    select = st.sidebar.selectbox('município', lista_municipios)
    df = df.set_index('Município')
    df['CLASS_CAPAG_real'] = df['CLASS_CAPAG_real'].astype('Int64')
    df_municipio = df[df.index==(select)]
    st.write(df_municipio)
elif select_event == 'Quem somos nós':
	st.markdown('Camila Maia Fátima Marques ...'
		    'Mario José Calvão Monnerat do Prado é pai, auditor-fiscal da Receita Federal, formado no MBA em Analytics e Inteligência Artificial da Fundação FIA de São Paulo'
		   'Reinaldo da Cruz Castro...')
