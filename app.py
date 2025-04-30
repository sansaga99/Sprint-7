import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Análisis de Anuncios de Autos Usados')

car_data = pd.read_csv('vehicles_us.csv')


hist_button = st.button('Construir histograma')


if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button('Construir gráfico de dispersión')


if scatter_button:
    st.write('Creación de un gráfico de dispersión para el conjunto de datos')
    fig = px.scatter(car_data, x="odometer", y="price", color="condition", 
                     title="Gráfico de dispersión: Precio vs. Odometer")
    st.plotly_chart(fig, use_container_width=True)

    
