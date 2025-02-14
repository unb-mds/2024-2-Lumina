import streamlit as st
import plotly.express as px
import pandas as pd
import altair as alt

# Gerando dados fictícios
data = {
    'Mês': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Vendas': [200, 220, 250, 230, 270, 300, 280, 320, 310, 350, 370, 400]
}
df = pd.DataFrame(data)

# Título da aplicação Streamlit
# st.title("Exemplo de Gráficos com Plotly e Altair")

# Gráfico de Barras Interativo com Plotly
# st.subheader("Gráfico Interativo de Barras (Plotly)")
fig_bar = px.bar(df, x='Mês', y='Vendas', title="Vendas por Mês (Plotly)", labels={'Mês': 'Mês', 'Vendas': 'Vendas'})
st.plotly_chart(fig_bar)

# Gráfico de Linhas Interativo com Plotly
# st.subheader("Gráfico de Linhas Interativo (Plotly)")
fig_line = px.line(df, x='Mês', y='Vendas', title="Vendas por Mês (Interativo)", markers=True)
st.plotly_chart(fig_line)

# Gráfico de Linhas com Altair
# st.subheader("Gráfico de Linhas (Altair)")
chart = alt.Chart(df).mark_line(point=True).encode(
    x='Mês',
    y='Vendas',
    tooltip=['Mês', 'Vendas']
).properties(title="Vendas por Mês (Altair)")
st.altair_chart(chart, use_container_width=True)
