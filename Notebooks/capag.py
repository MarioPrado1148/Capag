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
import math

# Configuração da página
st.set_page_config(layout="wide")
sns.set_style('darkgrid')
st.set_option('deprecation.showPyplotGlobalUse', False)
pd.options.display.float_format = "{:,.2f}".format

# Carregamento dos dados
data_url =('https://github.com/MarioPrado1148/Capag/blob/main/Datasets/df_streamlit_com_previsao.xlsx')
@st.cache(persist=True)

def load_data():
    data=pd.read_excel(data_url)
    return data

df =load_data()

# Página Principal
st.title('Classificação da Capacidade de Pagamento dos Municípios brasileiros com base em dados geoeconômicos')

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
    
    
    



    
