
import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos desde el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Título de la aplicación
st.header('Análisis de Vehículos Usados en EE.UU.')

# Botón para generar el histograma
hist_button = st.button('Construir histograma')

# Si se presiona el botón, se genera el histograma
if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)