import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Herramientas Agro")
st.title("Valuación de hacienda")

coltipo, colcantidad, colpeso = st.beta_columns(3)
with coltipo:
    tipo = st.text_input("Ingrese categoría de hacienda: ", format='%f')
with colcantidad:
    cantidad = st.number_input("Ingrese cantidad de cabezas: ", min_value=0.0, format='%f')
with colpeso:
    peso = st.number_input("Ingrese peso: ", min_value=0.0, format='%f')
