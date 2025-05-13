import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos desde el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Título de la aplicación
st.header('Análisis de Vehículos Usados en EE.UU.')

# Casilla de verificación para mostrar el histograma
if st.checkbox('Mostrar histograma del odómetro'):
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Casilla de verificación para mostrar el gráfico de dispersión
if st.checkbox('Mostrar gráfico de dispersión de odómetro vs precio'):
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Relación entre Kilometraje y Precio")
    st.plotly_chart(fig_scatter, use_container_width=True)