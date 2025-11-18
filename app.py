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

# EXIBINDO A TABELA DE DADOS OU NÃO E DEFININDO A QUANTIDADE DE LINHAS
st.subheader("Base de dados")

mostrar_tabela = st.checkbox("Mostrar tabela?", value=False)

if mostrar_tabela:
    num_linhas = st.slider(
        "Quantidade de linhas a exibir:",
        min_value=10,
        max_value=len(car_data),
        value=50,
        step=10,
    )

    st.dataframe(car_data.head(num_linhas))
else:
    st.info("Marque a caixa acima para visualizar a tabela.")

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
def gerar_dispersao(df, x_col, y_col, max_points=10000):
    """Função que cria um scatterplot (com amostragem para melhorar o desempenho) baseado no clique do usuário em um botão e o adiciona à tela.
    Opções de gráfico:
    - quilometragem vs preço;
    - ano de fabricação vs preço.
    """
    df_plot = df[[x_col, y_col]].dropna()

    # amostragem se há muitos pontos
    if len(df_plot) > max_points:
        df_plot = df_plot.sample(max_points, random_state=42)

    fig = px.scatter(
        df_plot,
        x=x_col,
        y=y_col,
        opacity=0.7,
        title=f"{x_col} vs {y_col}",
        render_mode="webgl",
    )

    if x_col == "odometer":
        fig.update_xaxes(
            tickformat=",d",
            separatethousands=True,
        )

    st.plotly_chart(fig, use_container_width=True)


# inicializando o session state
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
    gerar_dispersao(car_data, x_col, y_col, max_points=10000)
