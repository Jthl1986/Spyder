import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Herramientas Agro")
st.title("Valuación de hacienda")

coltipo, colcantidad, colpeso = st.columns(3)
with coltipo:
    tipo = st.text_input('ingrese tipo de hacienda: \n1 - Ternero\n2 - Novillito\n3 - Ternera\n4 - Vaquillona\n5 - Vaca\n')
with colcantidad:
    cantidad = st.number_input("Ingrese cantidad de cabezas: ", min_value=0.0)
with colpeso:
    peso = st.number_input("Ingrese peso: ", min_value=0.0)
