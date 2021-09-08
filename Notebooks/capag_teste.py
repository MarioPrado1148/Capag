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


st.title('Classificação da Capacidade de Pagamento dos Municípios brasileiros com base em dados geoeconômicos')

st.subtitle('Uma nova visão sobre a capacidade de pagamento de nossos municípios')
