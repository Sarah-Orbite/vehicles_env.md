import streamlit as st
import pandas as pd
import plotly.express as px

# Ler os dados
data = pd.read_csvpd.read_csv("vehicles.csv")

# Cabeçalho do aplicativo
st.header("Dashboard de Análise de Veículos")

# Botão para criar o histograma
if st.button("Criar Histograma de Preços"):
    st.write("Histograma mostrando a distribuição de preços dos veículos:")
    fig = px.histogram(data, x="price", nbins=50, title="Distribuição de Preços")
    st.plotly_chart(fig, use_container_width=True)

# Botão para criar o gráfico de dispersão
if st.button("Criar Gráfico de Dispersão: Preço vs Hodômetro"):
    st.write("Gráfico de dispersão mostrando a relação entre preço e hodômetro:")
    fig = px.scatter(data, x="odometer", y="price", color="condition",
                     title="Preço vs. Hodômetro por Condição")
    st.plotly_chart(fig, use_container_width=True)

# Caixa de seleção para o histograma
if st.checkbox("Exibir Histograma de Preços"):
    st.write("Histograma mostrando a distribuição de preços dos veículos:")
    fig = px.histogram(data, x="price", nbins=50, title="Distribuição de Preços")
    st.plotly_chart(fig, use_container_width=True)

# Caixa de seleção para o gráfico de dispersão
if st.checkbox("Exibir Gráfico de Dispersão: Preço vs Hodômetro"):
    st.write("Gráfico de dispersão mostrando a relação entre preço e hodômetro:")
    fig = px.scatter(data, x="odometer", y="price", color="condition",
                     title="Preço vs. Hodômetro por Condição")
    st.plotly_chart(fig, use_container_width=True)
