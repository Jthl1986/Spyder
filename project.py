import streamlit as st
import pandas as pd

st.set_page_config(page_title="Herramientas Agro")
st.title("Valuación de hacienda")

coltipo, colcantidad, colpeso = st.columns(3)
with coltipo:
    tipo = st.selectbox('ingrese tipo de hacienda: ', [" Ternero", "Novillito", "Ternera", "Vaquillona", "Vaca"])
with colcantidad:
    cantidad = st.number_input("Ingrese cantidad de cabezas: ", min_value=0.0)
with colpeso:
    peso = st.number_input("Ingrese peso: ", min_value=0.0)
df=pd.read_html('https://www.monasterio-tattersall.com/precios-hacienda') #leo la tabla de la página
df[0]
hacienda = df[0] #asigno una variable a la tabla
categoria = hacienda.Categoría #creo las series
promedio = hacienda.Promedio
tabla = pd.DataFrame({'categoria':categoria,'promedio':promedio}) #creo un dataframe con categoria y promedio
ternero = tabla[0:4]
novillito = tabla[4:7]
ternera = tabla[7:11]
vaquillona = tabla[11:14]
vaca = tabla[19:20]
fecha = (tabla[25:26].values)[0][0]
ternero160 = int(ternero.promedio[0][2:5])
ternero180 = int(ternero.promedio[1][2:5])
ternero200 = int(ternero.promedio[2][2:5])
ternero230 = int(ternero.promedio[3][2:5])
novillo260 = int(novillito.promedio[4][2:5])
novillo300 = int(novillito.promedio[5][2:5])
novillo301 = int(novillito.promedio[6][2:5])
ternera150 = int(ternera.promedio[7][2:5])
ternera170 = int(ternera.promedio[8][2:5])
ternera190 = int(ternera.promedio[9][2:5])
ternera210 = int(ternera.promedio[10][2:5])
vaquillona250 = int(vaquillona.promedio[11][2:5])
vaquillona290 = int(vaquillona.promedio[12][2:5])
vaquillona291 = int(vaquillona.promedio[13][2:5])
vacas = int(vaca.promedio[19][2:8])
