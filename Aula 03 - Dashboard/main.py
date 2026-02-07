import streamlit as st
import pandas as pd

dados = pd.read_excel("Database/lista.xlsx")

print(dados)

st.title("Dashboard Eletronicos")
st.subheader("Análise das principais empresas")
st.write("Quantidade de empresas analisadas: ", dados["FABRICANTE"].nunique())

st.sidebar.title("FILTRO")
fabricantes = st.sidebar.multiselect("Selecione uma empresa", dados['FABRICANTE'].unique())

if fabricantes:
    dados = dados[dados['FABRICANTE'].isin(fabricantes)]
    st.metric(f"TOTAL DE  {dados['FABRICANTE'].unique()}", f"R${dados['RECEITA BRUTA'].sum():,.2f}") 
    st.metric(f"Média da quantidade de itens de {dados['FABRICANTE'].unique()}: ", f"{dados['QUANTIDADE'].mean():,.2f}")
else:
    st.metric("TOTAL GERAL", f"R${dados['RECEITA BRUTA'].sum():,.2f}")
    st.metric("Média da quantidade de itens GERAL: ", f"{dados['QUANTIDADE'].mean():,.2f}")

st.write("Grafico de barras de Fabricante e Receita bruta")
st.bar_chart(dados.groupby("FABRICANTE")["RECEITA BRUTA"].sum())

st.write("Grafico de Linhas de Fabricantes e Quantidade")
st.line_chart(dados.groupby("FABRICANTE")["QUANTIDADE"].sum())

st.dataframe(dados)

