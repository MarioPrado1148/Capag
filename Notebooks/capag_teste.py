# Projeto CAPAG
# Previsão da capacidade de pagamento dos municípios

# Referências:
# https://www.analyticsvidhya.com/blog/2020/10/create-interactive-dashboards-with-streamlit-and-python/

# !pip install streamlit --upgrade

# Importação das libraries
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt

# Configuração da página
st.set_page_config(layout="wide")
sns.set_style('darkgrid')
st.set_option('deprecation.showPyplotGlobalUse', False)
pd.options.display.float_format = "{:,.2f}".format

st.title('Classificação da Capacidade de Pagamento dos Municípios brasileiros com base em dados geoeconômicos')

st.markdown('Uma nova visão sobre a capacidade de pagamento de nossos municípios')

#@st.cache(persist=True)
df = pd.read_csv('https://raw.githubusercontent.com/MarioPrado1148/Capag/main/Datasets/df_streamlit_com_previsao.csv', sep = ';', index_col = 0)

# Preparação do sidebar (barra lateral)
st.sidebar.title('Seletor de Visualizações')
st.sidebar.markdown('Selecione os gráficos/dataframes que deseja visualizar')

st.sidebar.checkbox("Visualizar análises por município", True, key=1)
lista_municipios = pd.Series(list(set(df['Município']))).sort_values()
select = st.sidebar.selectbox('município', lista_municipios)

#st.table(df)

#df = df.drop(['Unnamed'],axis = 1)
df = df.set_index('Município')
df['CLASS_CAPAG_real'] = df['CLASS_CAPAG_real'].astype('Int64')
df_municipio = df[df.index==(select)]
st.write(df_municipio)

if st.sidebar.checkbox("Análise Exploratória de Dados", True, key=2):
    tipo_variaveis = ['Variáveis Categóricas', 'Variáveis Quantitativas']
    select = st.sidebar.selectbox('Tipo de Variável', tipo_variaveis)

     
if select == 'Variáveis Categóricas':
    select_status = st.sidebar.radio("Covid-19 patient's status", ('Confirmed',
                                                                   'Active', 'Recovered', 'Deceased'))
    col1, col2 = st.columns(2)
    with col1:
        st.header('Região')
        sns.countplot(data = df, x = "Região")
        st.pyplot() 
    with col2: 
        st.header('Reg_Metropolitana')
        sns.countplot(data = df, x = "Reg_Metropolitana")
        st.pyplot()

