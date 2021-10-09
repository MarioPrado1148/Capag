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

