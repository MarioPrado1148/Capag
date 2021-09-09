# Projeto CAPAG
# Previsão da capacidade de pagamento dos municípios

# Referências:
# https://www.analyticsvidhya.com/blog/2020/10/create-interactive-dashboards-with-streamlit-and-python/
# https://towardsdatascience.com/build-your-first-data-visualization-web-app-in-python-using-streamlit-37e4c83a85db

# !pip install streamlit --upgrade

# Importação das libraries
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
import plotly.express as px
import math

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

lista_eventos = ['Contextualização','Análise das Variáveis Categóricas','Análise das Variáveis Quantitativas', 'Dataframe completo', 'Visão por Município']
select_event = st.sidebar.selectbox('Que informações você gostaria de visualizar?', lista_eventos)

if select_event == 'Contextualização':
    st.markdown('Colocar explicação sobre o projeto aqui')
    
# Análise Exploratória de dados das Variáveis Categóricas
elif select_event == 'Análise das Variáveis Categóricas':
    select_radio = st.sidebar.radio('Selecione a variável',['Região','Região Metropolitana','Unidade da Federação', 'Mun_Reg_Geof_Imediata','Hierarquia Urbana','Região Rural'])
    if select_radio == 'Região':
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h1 style='text-align: center; color: blue;'>Variável 'Região'</h1>", unsafe_allow_html=True)
            sns.countplot(data = df, x = "Região")
            st.pyplot()
            
        with col2: 
            st.markdown("<h1 style='text-align: center; color: blue;'>Análise</h1>", unsafe_allow_html=True)
            st.markdown('Verifica-se que há maior quantidade de municípios na Região Nordeste, a qual é seguida de perto pela Região Sudeste')
    elif select_radio == 'Região Metropolitana':
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h1 style='text-align: center; color: blue;'>Variável 'Região Metropolitana'</h1>", unsafe_allow_html=True)
            sns.countplot(data = df, x = "Reg_Metropolitana")
            st.pyplot()
            
        with col2: 
            st.markdown("<h1 style='text-align: center; color: blue;'>Análise</h1>", unsafe_allow_html=True)
            st.markdown('Verifica-se que há maior parte dos municípios não faz parte de Regiões Metropolitanas.')
    elif select_radio == 'Unidade da Federação':
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("<h1 style='text-align: center; color: blue;'>Variável 'Unidade da Federação'</h1>", unsafe_allow_html=True)
            sns.countplot(data = df, x = "UF")
            st.pyplot()
            
        with col2: 
            st.markdown("<h1 style='text-align: center; color: blue;'>Análise</h1>", unsafe_allow_html=True)
            st.markdown('Verifica-se que há maior parte dos municípios não faz parte de Regiões Metropolitanas.')
    
    elif select_radio == 'Mun_Reg_Geof_Imediata':
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<h1 style='text-align: center; color: blue;'>Variável 'Mun_Reg_Geof_Imediata'</h1>", unsafe_allow_html=True)
            sns.countplot(data = df, x = "Mun_Reg_Geof_Imediata")
            st.pyplot()
        with col2: 
            st.markdown("<h1 style='text-align: center; color: blue;'>Análise</h1>", unsafe_allow_html=True)
            st.markdown('Verifica-se que há maior parte dos municípios não faz parte de Regiões Metropolitanas.')
    elif select_radio == 'Hierarquia Urbana':
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<h1 style='text-align: center; color: blue;'>Variável 'Hierarquia Urbana'</h1>", unsafe_allow_html=True)
            sns.countplot(data = df, x = "Hierarquia_Urbana")
            st.pyplot()
        with col2: 
            st.markdown("<h1 style='text-align: center; color: blue;'>Análise</h1>", unsafe_allow_html=True)
            st.markdown('Verifica-se que há maior parte dos municípios não faz parte de Regiões Metropolitanas.')
    
    elif select_radio == 'Região Rural':
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<h1 style='text-align: center; color: blue;'>Variável 'Região Rural'</h1>", unsafe_allow_html=True)
            sns.countplot(data = df, x = "Região_rural")
            st.pyplot()
        with col2: 
            st.markdown("<h1 style='text-align: center; color: blue;'>Análise</h1>", unsafe_allow_html=True)
            st.markdown('Verifica-se que há maior parte dos municípios não faz parte de Regiões Metropolitanas.')
                  
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
    elif select_radio == 'VAB_Indústria/Total':
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("<h1 style='text-align: center; color: blue;'>Variável 'VAB_Indústria/Total'</h1>", unsafe_allow_html=True)
            fig = px.box(df, y = 'VAB_Indústria/Total')
            st.plotly_chart(fig)        
        with col2: 
            st.markdown("<h1 style='text-align: center; color: blue;'>Análise</h1>", unsafe_allow_html=True)
            st.markdown('Verifica-se que há maior quantidade de municípios na Região Nordeste, a qual é seguida de perto pela Região Sudeste')
    
    
    
elif select_event == 'Dataframe completo':
    st.table(df)
else:
  # st.sidebar.checkbox("Visualizar análises por município", True, key=1)
    lista_municipios = pd.Series(list(set(df['Município']))).sort_values()
    select = st.sidebar.selectbox('município', lista_municipios)
    df = df.set_index('Município')
    df['CLASS_CAPAG_real'] = df['CLASS_CAPAG_real'].astype('Int64')
    df_municipio = df[df.index==(select)]
    st.write(df_municipio)
