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

# Configuración de la página
st.set_page_config(page_title="App Quake", layout="wide")

# Título de la app
st.title("App Quake")

# Menú desplegable
menu_options = ["Home", "Interacciones"]
choice = st.sidebar.selectbox("Menu", menu_options)

# Mapa centrado en la ubicación del sismo
m = folium.Map(location=[latitude, longitude], zoom_start=8)

# Marcador en la ubicación del sismo
marker = folium.Marker([latitude, longitude], popup=sistype)
marker.add_to(m)

# Información del sismo
st.subheader("Información del sismo")
col1, col2 = st.beta_columns(2)
with col1:
    st.write(f"Fecha: {fecha}")
    st.write(f"Profundidad: {depth} km")
with col2:
    st.write(f"Magnitud: {mag}")

# Ubicación en longitud y latitud
st.subheader("Ubicación en coordenadas")
st.write(f"Latitud: {latitude}")
st.write(f"Longitud: {longitude}")

# Ubicación en formato de texto
st.subheader("Ubicación")
st.markdown(f"<span style='color: orange;'>{sistype}</span>", unsafe_allow_html=True)

# Mostrar el mapa
st.subheader("Mapa")
folium_static(m)
