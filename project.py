import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Herramientas Agro")
st.title("Valuación de hacienda")

coltipo, colcantidad, colpeso = st.columns(3)
with coltipo:
    tipo = st.selectbox('ingrese tipo de hacienda: ', [" Ternero", "Novillito", "Ternera", "Vaquillona", "Vaca"])
with colcantidad:
    cantidad = st.number_input("Ingrese cantidad de cabezas: ", min_value=0.0)
with colpeso:
    peso = st.number_input("Ingrese peso: ", min_value=0.0)
from tabulate import tabulate
    return print(f'\n\n{tabulate(metalista, headers=["Categoría", "Cantidad", "Peso", "Valuación"])}
