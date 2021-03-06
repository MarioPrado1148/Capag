# Algoritmo de classificação da capacidade de pagamento dos municípios brasileiros (Capag) com base em dados geoeconômicos.

# Contextualização
A análise da capacidade de pagamento (Classificação CAPAG) apura a situação fiscal dos entes subnacionais que querem contrair novos empréstimos com garantia da União. Esta classificação é um indicador de saúde econômica e fiscal dos municípios.  
O intuito da CAPAG é apresentar, de forma simples e transparente, se um novo endividamento representa risco de crédito para o Tesouro Nacional. Assim, um ente bem avaliado pelo Tesouro Nacional poderá acessar empréstimos com juros mais baixos, por contar com a União como seu garantidor.  
A CAPAG pode ter os valores A, B, C e D.  
O ente que possuir classificação "A" ou "B" é elegível à contratação de garantias da União em seus financiamentos. Os demais conceitos ("C” e "D”) são um sinal de que a situação fiscal e financeira do município não lhe permite realizar operações de crédito com garantia da União.  
Para o algoritmo nesse estudo, as notas C e D estão representadas por "1" e as notas A e B, por "0"; destarte, o conceito 1 indica má situação fiscal e financeira, o conceito 0, que o ente está apto à contratação de garantias.  

# Objetivos
Neste trabalho, utilizamos um modelo de aprendizado de máquina denominado XGBoost com o objetivo de, utilizando as informações geoeconômicas disponíveis sobre os municípios brasileiros, estimar a capacidade de pagamento (Capag) dos municípios e compará-las com a Capag constante do site da Secretaria do Tesouro Nacional (STN), quando disponível.  
Entende-se que é uma solução embrionária. Possuindo o órgão classificador outras variáveis úteis ao cálculo, as variáveis utilizadas na solução proposta poderiam ser utilizadas em caráter suplementar, subsidiário na estimação.

# Organização das pastas deste Repositório Github
## Dataset
Os três arquivos cujo nome inicia com 'base' são os datasets que foram importados como origem dos dados para o jupyter notebook.  
O arquivo 'base_POP2018_20210331_copia' contém dados sobre a população estimada para o ano 2018. Alguns municípios possuíam um número em evidência à direita do valor da população, o qual fazia remissão a uma tabela abaixo da tabela principal, onde constavam populações determinadas judicialmente para alguns municípios.  
Como este trabalho é didático, sem implicações econômicas, e para manter a coerência dos dados, nós utilizamos somente o valor estimado da população, sem fazer referência aos valores determinados judicialmente para alguns municípios.  
Neste mesmo arquivo, criamos a coluna IBGE7 antes de importar para o notebook do jupyter. Esta coluna é a concatenação entrea as colunas 'COD.UF.' e 'COD.MUNIC.'. Procedemos desta forma para que fosse possível, posteriormente, juntar esta tabela com as outras duas tabelas objeto do presente trabalho.  
Os outros arquivos foram criados posteriormente, em etapas diversas do projeto de ciências de dados.

## Images
Contém imagens e gráficos utilizados no aplicativo streamlit.

## Models
Contém nosso melhor modelo treinado.

## Notebooks
Os notebooks cujo nome inicia-se por algarismos foram feitos no jupyter notebook.
O notebook Capag_Inovação contém o código necessário para o funcionamento de nosso aplicativo no Streamlit, que criamos para permitir aos usuários a compreensão de todo o trabalho que fizemos para prever a Capag.  
O endereço do aplicativo streamlit é https://share.streamlit.io/marioprado1148/capag/main/Notebooks/capag_inovacao.py  
O notebook Capag contém o mesmo conteúdo que o notebook Capag_Inovação. É um notebook reserva, que poderá ser utilizado caso ocorram problemas com o notebook principal.  
Existe também um aplicativo reserva do Streamlit, disponível no endereço abaixo, que é igual ao aplicativo que inscrevemos no Prêmio Tesouro Nacional.  
https://share.streamlit.io/marioprado1148/capag/main/Notebooks/capag.py  
Os dois arquivos cujo nome inicia-se com 'df_streamlit' são utilizados como origem de dados para o aplicativo Streamlit.

# Bases de dados utilizadas
Foram utilizados 3 datasets neste trabalho:

## 1 Capacidade de Pagamento (CAPAG) dos Municípios
Os dados foram coletados no website da Transparência do Tesouro Nacional, em 16 de setembro de 2021.  
Link: http://www.tesourotransparente.gov.br/ckan/dataset/capag-municipios

## 2 PIB e outros indicadores econômicos
Os dados foram coletados na sessão de estatísticas econômicas do website do IBGE, em janeiro de 2021.  
Link: https://www.ibge.gov.br/estatisticas/economicas/contas-nacionais/9088-produto-interno-bruto-dos-municipios.html?=&t=resultados

## 3 Estimativas sobre dados de população dos municípios em 2018.
Os dados foram coletados na seção de estimativas da população do website do IBGE em 04 de outubro de 2021.  
Link: https://www.ibge.gov.br/estatisticas/sociais/populacao/9103-estimativas-de-populacao.html?edicao=17283&t=downloads
