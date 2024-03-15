import pandas as pd
import plotly.express as px
import streamlit as st

# Lee el archivo CSV del conjunto de datos
car_data = pd.read_csv('vehicles_us.csv')

# Configuración de la página
st.title('Cuadro de Mandos de Anuncios de Venta de Coches')

# Encabezado
st.header('Visualizaciones')

# Botón para construir histograma
hist_button = st.button('Construir histograma')

# Botón para construir gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

# Verificar si se hizo clic en el botón de histograma
if hist_button:
    # Crear un histograma
    fig_hist = px.histogram(car_data, x="odometer")
    # Mostrar el histograma
    st.plotly_chart(fig_hist, use_container_width=True)

# Verificar si se hizo clic en el botón de gráfico de dispersión
if scatter_button:
    # Crear un gráfico de dispersión
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    # Mostrar el gráfico de dispersión
    st.plotly_chart(fig_scatter, use_container_width=True)
