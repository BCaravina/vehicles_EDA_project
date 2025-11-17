import streamlit as st
import pandas as pd
import plotly.express as px

# TÍTULO E CABEÇALHO
st.title("Exploração de dados de veículos")
st.text(
    "Interaja com a base de dados e os dashboards abaixo para visualizar diversas características sobre veículos à venda nos Estados Unidos no ano de 2019."
)
st.divider()


# LENDO, EDITANDO E CARREGANDO OS DADOS NA PÁGINA
@st.cache_data
def load_data():
    """Função para editar o df e remover colunas desnecessárias apenas ao carregar a página para evitar lentidão no site."""
    df = pd.read_csv("vehicles_us.csv")
    df = df.drop(columns=["days_listed", "date_posted"])
    df[["brand", "model_name"]] = df["model"].str.split(pat=" ", n=1, expand=True)

    return df


car_data = load_data()

# TABELA DE DADOS
st.subheader("Base de dados")
st.write(car_data)
st.divider()

# CAIXA DE SELEÇÃO PARA GERAR HISTOGRAMA (3 opções)
st.subheader("Histogramas")
st.write("Selecione uma das opções abaixo para gerar um histograma.")
st.divider()

# GRÁFICOS DE DISPERSÃO (criar 2 ou 3 e usar um botão para gerar um deles aleatoriamente)
st.subheader("Gráficos de dispersão")
st.button("Gerar gráfico")
st.divider()

# SLIDER BAR COM OS PREÇOS DOS VEÍCULOS
st.subheader("Barra rolante")
st.write("Deslize a barra para ver ")
st.slider()
