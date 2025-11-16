# vehicles_EDA_project

# Vehicle Market EDA

Exploração de dados de anúncios de veículos usada para entender preços, características, padrões de mercado e possíveis insights que podem ajudar compradores, vendedores e entusiastas do setor automotivo. Este projeto será futuramente disponibilizado como uma aplicação online (Streamlit) para visualização dinâmica dos resultados da análise.

## 1. Sobre o Projeto

A proposta é analisar um conjunto de dados contendo informações de veículos listados para venda, incluindo preço, quilometragem, tipo, condição, ano do modelo e outros atributos relevantes. Os principais objetivos são:

- Identificar padrões de precificação
- Detectar tendências por tipo de veículo
- Explorar impacto de variáveis como quilometragem, condição, ano, combustível
- Encontrar possíveis anomalias ou outliers
- Criar visualizações claras e intuitivas
- Preparar tudo para deploy online (Streamlit + Render)

## 2. Fonte dos Dados

Arquivo utilizado: vehicles_data.csv

O dataset contém as seguintes colunas principais:

price – Preço do veículo
model_year – Ano do modelo
model – Modelo do veículo
condition – Estado do veículo
cylinders – Nº de cilindros
fuel – Tipo de combustível
odometer – Quilometragem
transmission – Tipo de transmissão
type – Categoria (SUV, sedan, pickup etc.)
paint_color – Cor
is_4wd – Tração 4x4
date_posted – Data do anúncio
days_listed – Dias ativo antes de ser vendido

## 3. Questões a Explorar na EDA

- Como o preço varia entre diferentes tipos de veículo?
- Quilometragem influencia o preço de forma linear?
- Há marcas/modelos que depreciam mais rápido?
- Ano do modelo é um bom preditor de valor?
- Quais variáveis contribuem para outliers de preço?
- Há diferenças entre veículos 4x4 e 4x2?

## 4. Estrutura do Projeto (sugerida)

vehicles_EDA_project/
│── data/
│   └── vehicles_data.csv
│
│── notebooks/
│   └── eda.ipynb
│
│── src/
│   └── utils.py
│   └── processing.py
│
│── app/
│   └── app.py
│
│── requirements.txt
│── README.md

## 5. Tecnologias Utilizadas

Python
Pandas
NumPy
Matplotlib / Seaborn / Plotly
Streamlit
VSCode
Render (deploy)

## 6. Como Executar Localmente

Clone o repositório:

git clone https://github.com/BCaravina/vehicles_EDA_project.git
cd vehicles_EDA_project

Crie um ambiente virtual:

python3 -m venv .venv
source .venv/bin/activate

Instale os requisitos:

pip install -r requirements.txt

Rode a aplicação Streamlit:

streamlit run app/app.py

## 7. Status do Projeto

- [x] Configuração inicial
- [x] EDA preliminar
- [ ] Tratamento avançado dos dados
- [ ] Construção do dashboard Streamlit
- [ ] Deploy no Render

## 8. Licença

Projeto de uso educacional e pessoal.
