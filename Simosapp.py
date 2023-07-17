import streamlit as st
from PIL import Image
import pandas as pd
import datetime
import streamlit as st
from streamlit_folium import folium_static
import folium
from folium.plugins import MarkerCluster

# Obtener parámetros de la URL
result = st.experimental_get_query_params()

country = result['val'][0]
latitude = result['val'][1]
longitude = result['val'][2]
depth = result['val'][3]
mag = result['val'][4]
sistype = result['val'][5]
fecha = result['val'][6]

# Configurar el estilo de la página
st.set_page_config(
    page_title="App Quake",
    page_icon="🌍",
    layout="wide"
)

# Título de la app
st.title("App Quake")

# Crear un mapa centrado en las coordenadas del sismo
mapa = folium.Map(location=[latitude, longitude], zoom_start=8)

# Marcador del sismo en el mapa
folium.Marker(
    location=[latitude, longitude],
    popup=f"Sismo: {country}",
    icon=folium.Icon(color="orange")
).add_to(mapa)

# Mostrar el mapa en Streamlit
st.markdown("## Mapa del sismo")
folium_static(mapa)

# Menú desplegable
menu_opciones = ["Home", "Interacciones"]
opcion = st.sidebar.selectbox("Menú", menu_opciones)
st.sidebar.markdown("## Opciones")
st.sidebar.info(f"Seleccionaste: {opcion}")

# Información adicional del sismo
st.markdown("## Información del sismo")
st.write(f"- Fecha: {fecha}")
st.write(f"- Profundidad: {depth} km")
st.write(f"- Magnitud: {mag}")

# Dibujo interactivo de la escala de Richter
st.markdown("## Escala de Richter")
# Aquí puedes agregar el código necesario para mostrar la escala de Richter

# Ubicación en coordenadas
st.markdown("## Ubicación en coordenadas")
st.write(f"- Latitud: {latitude}")
st.write(f"- Longitud: {longitude}")

# Ubicación en formato de texto
st.markdown("## Ubicación en texto")
st.info(f"Ubicación: {country}")
