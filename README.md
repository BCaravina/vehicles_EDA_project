Vehicle Dashboard (Streamlit)

Este projeto não tem como foco realizar uma análise exploratória profunda.
O objetivo principal foi praticar a construção de dashboards interativos e aprender a hospedar uma aplicação web acessível remotamente, utilizando Streamlit e Render.

A página inclui visualizações simples e intuitivas baseadas no arquivo vehicles_us.csv, permitindo ao usuário explorar os dados de forma dinâmica.

⸻

1. Sobre o Projeto

A aplicação contém:
	•	Uma tabela interativa exibindo todo o conteúdo do arquivo vehicles_us.csv
	•	Um menu de seleção com 4 opções para gerar histogramas:
	•	Ano de fabricação (model_year)
	•	Cor do veículo (paint_color)
	•	Tipo de veículo (type)
	•	Marca (brand)
	•	Dois botões que permitem escolher gráficos de dispersão:
	•	Quilometragem vs Preço (odometer vs price)
	•	Ano de fabricação vs Preço (model_year vs price)

O foco foi exercitar:
	•	manipulação dinâmica de dados com pandas,
	•	construção de visualizações com Plotly,
	•	interação via Streamlit,
	•	organização do código em componentes reutilizáveis,
	•	e deploy da aplicação em ambiente online.

2. Fonte dos Dados

Arquivo utilizado: vehicles_us.csv

Principais colunas contidas no dataset:
	•	price – Preço do veículo
	•	model_year – Ano de fabricação
	•	model – Modelo
	•	condition – Estado do veículo
	•	cylinders – Número de cilindros
	•	fuel – Tipo de combustível
	•	odometer – Quilometragem
	•	transmission – Tipo de transmissão
	•	type – Categoria (SUV, sedan, pickup, etc.)
	•	paint_color – Cor
	•	is_4wd – Tração 4x4
	•	date_posted – Data do anúncio
	•	days_listed – Quantidade de dias listado

⸻

3. Objetivo da Aplicação

O objetivo não é interpretar esses dados profundamente, mas sim:
	•	demonstrar visualizações básicas de forma interativa,
	•	permitir que qualquer usuário explore o dataset rapidamente,
	•	e aprender a publicar essa aplicação online para acesso de qualquer lugar.

4. Estrutura do Projeto

vehicles_EDA_project/
│── .streamlit/
│   └── config.toml
|
│── notebooks/
│   └── EDA.ipynb
│
│── vehicles-eda-venv
| 
│── app.py
│── README.md
│── requirements.txt
│── vehicles_data.csv

Obs.: Como o foco do projeto era desenvolver a aplicação em Streamlit e fazer deploy a estrutura foi mantida enxuta propositalmente.

5. Tecnologias Utilizadas
•	Python
•	Pandas – carregamento e manipulação de dados
•	Plotly – gráficos interativos
•	Streamlit – interface e interação com o usuário
•	VSCode – ambiente de desenvolvimento
•	Render – hospedagem da aplicação online

6. Como Executar Localmente

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

A aplicação abrirá automaticamente no seu navegador.

7. Status do Projeto

•	Estrutura inicial do projeto
•	Construção dos dashboards interativos
•	Implementação de histogramas
•	Implementação de gráficos de dispersão
•	Deploy online via Render

8. Licença

Projeto desenvolvido para fins educacionais e pessoais.
