import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

# Configuração da página do Streamlit
st.set_page_config(page_title="Gráficos com Plotly e Altair", layout="wide")

# Dados fictícios
data = {
    "Ano": [2021, 2022, 2023, 2024, 2025],
    "Vendas": [100, 150, 200, 250, 300],
    "Lucro": [20, 30, 50, 70, 90],
    "Custo": [80, 120, 150, 180, 210]
}
df = pd.DataFrame(data)

# Título
st.title("Gráficos Interativos com Plotly e Altair")

# Gráfico de linha (Altair)
st.subheader("Gráfico de Linha - Altair")
line_chart = alt.Chart(df).mark_line(point=True).encode(
    x="Ano:O",
    y="Vendas:Q",
    tooltip=["Ano", "Vendas"]
).properties(
    width=700, height=400
)
st.altair_chart(line_chart, use_container_width=True)

# Gráfico de barras (Plotly)
st.subheader("Gráfico de Barras - Plotly")
bar_chart = px.bar(
    df, x="Ano", y="Lucro", color="Ano",
    labels={"Ano": "Ano", "Lucro": "Lucro (em mil)"},
    title="Lucro por Ano"
)
st.plotly_chart(bar_chart, use_container_width=True)

# Gráfico de dispersão (Altair)
st.subheader("Gráfico de Dispersão - Altair")
scatter_chart = alt.Chart(df).mark_circle(size=100).encode(
    x="Custo:Q",
    y="Lucro:Q",
    color="Ano:N",
    tooltip=["Ano", "Custo", "Lucro"]
).properties(
    width=700, height=400
)
st.altair_chart(scatter_chart, use_container_width=True)

st.write("### Observações:")
st.write("Esses gráficos são apenas exemplos. Você pode ajustar os dados para atender às suas necessidades.")