import streamlit as st
import pandas as pd
from pandas.api.types import is_numeric_dtype
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

# EXIBINDO A TABELA DE DADOS
st.subheader("Base de dados")
st.write(car_data)
st.divider()

# CAIXA DE SELEÇÃO PARA GERAR HISTOGRAMA (4 opções)
st.subheader("Histogramas")

feature_map = {
    "Ano de Fabricação": "model_year",
    "Tipo de Carro": "type",
    "Cor do Carro": "paint_color",
    "Marcas": "brand",
}

feature_label = st.selectbox(
    "Escolha uma variável para visualizar:",
    list(feature_map.keys()),
)

column_name = feature_map[feature_label]
series = car_data[column_name].dropna()

if is_numeric_dtype(series):
    fig = px.histogram(
        car_data,
        x=column_name,
        nbins=30,
        title=f"Histograma de {feature_label}",
    )
    fig.update_layout(xaxis_title=None)
else:
    fig = px.histogram(
        car_data,
        x=column_name,
        color=column_name,
        title=f"Distribuição de {feature_label}",
    )
    fig.update_layout(xaxis_title=None)

st.plotly_chart(fig, use_container_width=True)
st.caption("Os valores nulos foram removidos para geração dos gráficos acima.")
st.divider()


# GRÁFICOS DE DISPERSÃO COM BOTÕES
def gerar_dispersao(df, x_col, y_col):
    """Função que cria e exibe um scatterplot baseado no clique do usuário em um botão.
    Opções de gráfico:
    - quilometragem vs preço;
    - ano de fabricação vs preço.
    """
    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        opacity=0.7,
        # trendline="ols",
        title=f"{x_col} vs {y_col}",
    )

    # atualizando o eixo x da quilometragem de milhões para milhares
    if x_col == "odometer":
        fig.update_xaxes(tickformat=",d", separatethousands=True)

    # exibindo no Streamlit:
    st.plotly_chart(fig, use_container_width=True)


st.subheader("Gráficos de dispersão")
st.caption("Selecione um dos botões abaixo para visualizar o gráfico correspondente.")

if "grafico_atual" not in st.session_state:
    st.session_state["grafico_atual"] = None

# adicionando e mantendo os botões lado a lado
button_1, button_2 = st.columns(2)

with button_1:
    if st.button("Quilometragem vs Preço"):
        st.session_state["grafico_atual"] = ("odometer", "price")
with button_2:
    if st.button("Ano de Fabricação vs Preço"):
        st.session_state["grafico_atual"] = ("model_year", "price")

# atualizando o session state para mostrar o gráfico na tela
if st.session_state["grafico_atual"] is not None:
    x_col, y_col = st.session_state["grafico_atual"]
    gerar_dispersao(car_data, x_col, y_col)
