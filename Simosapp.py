from streamlit_folium import folium_static
import streamlit as st
import folium
from datetime import datetime
import pytz

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
st.set_page_config(page_title="QuakeAlert", page_icon="🌍", layout="wide")

# Agregar CSS personalizado para el área de la aplicación
st.markdown(
    """
    <style>
    .stApp {
        background-color: orange;
        max-width: 800px; /* Ajusta el ancho máximo según tus preferencias */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título de la app
st.title("QuakeAlert")

# Agregar una descripción breve
st.markdown('**Esta aplicación proporciona información detallada sobre sismos.**')

# Separadores
st.markdown("---")

# Crear un mapa centrado en la ubicación proporcionada
mapa = folium.Map(location=[latitude, longitude], zoom_start=10)

# Añadir un marcador en la ubicación
folium.Marker(location=[latitude, longitude], popup="Mi ubicación").add_to(mapa)

# Añadir círculo en la ubicación del sismo con estilo personalizado
folium.CircleMarker(location=[latitude, longitude], radius=10, popup="Magnitud: " + str(mag),
                    fill_color='red', color='black', fill_opacity=0.7).add_to(mapa)

# Mostrar el mapa en Streamlit
folium_static(mapa)

st.subheader("Detalles del sismo")

# Función para mostrar los detalles del último sismo
def show_details():
   
    st.write(f"País: {country}")
    st.write(f"Latitud: {latitude}")
    st.write(f"Longitud: {longitude}")

def show_details2():
    st.write(f"Magnitud: {mag}")
    st.write(f"Profundidad: {depth} km")
    st.write(f"Tipo de sismo: {sistype}")
    st.write(f"Fecha: {fecha}")

    
# Mostrar el mapa y los detalles
col1, col2 = st.columns(2)
with col1:
    show_details()
    
with col2:
    show_details2()

# Dibujar la escala de Richter
st.subheader("Escala de Richter")
st.image("ritcher.jpg")





