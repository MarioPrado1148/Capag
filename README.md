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
Contém os datasets importados para o notebook 01.

## Images
Contém imagens utilizadas no aplicativo streamlit.

## Models
Contém nosso melhor modelo treinado.

## Notebooks
Os notebooks cujo nome inicia-se por algarismos foram feitos no jupyter notebook.
O notebook Capag_Inovação contém o código necessário para o funcionamento de nosso aplicativo no Streamlit, que criamos para permitir aos usuários a compreensão de todo o trabalho que fizemos para prever a Capag.
O endereço do aplicativo streamlit é https://share.streamlit.io/marioprado1148/capag/main/Notebooks/capag_inovacao.py
O notebook Capag contém o mesmo conteúdo que o notebook Capag_Inovação. É um notebook reserva, que poderá ser utilizado caso ocorram problemas com o notebook principal.
Existe também um aplicativo reserva do Streamlit, disponível no endereço abaixo, que é igual ao aplicativo que inscrevemos no Prêmio Tesouro Nacional.

