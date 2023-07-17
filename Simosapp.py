import streamlit as st
import folium

# Obtener parámetros de la URL
result = st.experimental_get_query_params()

country = result['val'][0]
latitude = float(result['val'][1])
longitude = float(result['val'][2])
depth = result['val'][3]
mag = float(result['val'][4])
sistype = result['val'][5]
date = result['val'][6]

# Crear un mapa con Folium
m = folium.Map(location=[latitude, longitude], zoom_start=6)

# Agregar un marcador al mapa con información del sismo
popup_text = f"Pais: {country}<br>Latitud: {latitude}<br>Longitud: {longitude}<br>Profundidad: {depth}<br>Magnitud: {mag}<br>Tipo: {sistype}<br>Fecha: {date}"
folium.Marker(location=[latitude, longitude], popup=popup_text, icon=folium.Icon(color='red', icon='info-sign')).add_to(m)

# Agregar un control de capas para alternar estilos de mapa
folium.TileLayer('OpenStreetMap').add_to(m)
folium.TileLayer('Stamen Terrain').add_to(m)
folium.TileLayer('Stamen Toner').add_to(m)
folium.LayerControl().add_to(m)

# Agregar algunos marcadores adicionales para mostrar lugares de interés
places = {
    "Ciudad importante 1": [latitude + 0.1, longitude + 0.1],
    "Ciudad importante 2": [latitude - 0.1, longitude - 0.1],
    "Centro turístico": [latitude, longitude + 0.2],
    "Área de interés": [latitude - 0.15, longitude + 0.15],
}

for place, coords in places.items():
    folium.Marker(location=coords, popup=place, icon=folium.Icon(color='blue', icon='star')).add_to(m)

# Convertir el mapa de Folium a HTML
map_html = m._repr_html_()




