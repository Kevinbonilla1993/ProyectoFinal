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

# Crear el mapa con las coordenadas dadas
mapa = folium.Map(location=[latitude, longitude], zoom_start=10)

# Agregar marcador para la ubicación dada
folium.Marker([latitude, longitude], popup=f'{country}, {date}').add_to(mapa)

# Mostrar el mapa en Streamlit
st.write(mapa)



