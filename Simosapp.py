import streamlit as st
import folium

# Obtener parámetros de la URL
result = st.experimental_get_query_params()

country = result['val'][0]
latitude = result['val'][1]
longitude = result['val'][2]
depth = result['val'][3]
mag = result['val'][4]
sistype = result['val'][5]
date = result['val'][6]

# Crea un mapa centrado en las coordenadas proporcionadas
mapa = folium.Map(location=[latitude, longitude], zoom_start=15)

# Agrega un marcador en las coordenadas proporcionadas
folium.Marker([latitude, longitude], popup="country").add_to(mapa)

# Guarda el mapa en un archivo HTML
mapa.save("mi_mapa.html")




