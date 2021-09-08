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
# https://github.com/MarioPrado1148/Capag/blob/main/Datasets/df_streamlit_com_previsao.csv',error_bad_lines=False
df = pd.read_excel('D:/PremioTesouroNacional/df_streamlit_com_previsao.xlsx')

st.dataframe(df)
