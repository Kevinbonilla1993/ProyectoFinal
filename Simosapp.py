import streamlit as st
import folium

# Obtener parámetros de la URL
result = st.experimental_get_query_params()

country = result[0]
latitude = float(result[1])  # Convertir a número
longitude = float(result[2])  # Convertir a número
depth = result[3]
mag = result[4]
sistype = result[5]
date = result[6]

# Crear el mapa con las coordenadas dadas
mapa = folium.Map(location=[latitude, longitude], zoom_start=10)

# Agregar marcador para la ubicación dada
folium.Marker([latitude, longitude], popup=f'{country}, {date}').add_to(mapa)

# Mostrar el mapa en Streamlit
st.write(mapa)
