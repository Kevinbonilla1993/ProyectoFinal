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

# Establecer el estilo de la barra superior
st.markdown(
    """
    <style>
    .stApp {
        background-color: #964b00; /* Código de color café */
        padding: 30px; /* Añade un espacio alrededor de la barra */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título de la aplicación
st.title("QuakeAlert: Informando sobre Sismos")

# Línea separadora
st.write("---")

# Crear un mapa con Folium
m = folium.Map(location=[latitude, longitude], zoom_start=8)

# Agregar un marcador al mapa con información del sismo
popup_text = f"Pais: {country}<br>Latitud: {latitude}<br>Longitud: {longitude}<br>Profundidad: {depth}<br>Magnitud: {mag}<br>Tipo: {sistype}<br>Fecha: {date}"
folium.Marker(location=[latitude, longitude], popup=popup_text).add_to(m)

# Convertir el mapa de Folium a HTML
map_html = m._repr_html_()

# Mostrar los datos
st.write(f"Pais: {country}")
st.write(f"Latitud: {latitude}")
st.write(f"Longitud: {longitude}")
st.write(f"Profundidad: {depth}")
st.write(f"Magnitud: {mag}")
st.write(f"Tipo: {sistype}")
st.write(f"Fecha: {date}")





