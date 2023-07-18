from streamlit_folium import folium_static
import streamlit as st
import folium
from datetime import datetime
import pytz
import pydeck as pdk

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

# Estilo personalizado para el título de la app
st.title("🚀 QuakeAlert 🌎")
st.markdown("Bienvenido a QuakeAlert, la aplicación que proporciona información detallada sobre sismos en tiempo real. Mantente informado sobre los últimos sismos ocurridos en todo el mundo.")

# Separadores
st.markdown("---")

# Crear un mapa 3D centrado en la ubicación del sismo
view_state = pdk.ViewState(latitude=sismo['latitude'], longitude=sismo['longitude'], zoom=10, pitch=50, bearing=-30)
layer = pdk.Layer('ScatterplotLayer', data=[sismo], get_position='[longitude, latitude]', get_color='[200, 30, 0, 160]',
                  get_radius='mag * 1000', pickable=True)
tooltip = {"html": "<b>Magnitud:</b> {mag}<br/><b>Profundidad:</b> {depth} km", "style": {"backgroundColor": "white", "color": "black", "fontSize": "12px"}}
mapa = pdk.Deck(map_style='mapbox://styles/mapbox/light-v9', initial_view_state=view_state, layers=[layer], tooltip=tooltip)

# Crear un mapa centrado en la ubicación proporcionada
mapa = folium.Map(location=[latitude, longitude], zoom_start=10)

# Añadir un marcador en la ubicación
folium.Marker(location=[latitude, longitude], popup="Mi ubicación").add_to(mapa)

# Añadir círculo en la ubicación del sismo con estilo personalizado
folium.CircleMarker(location=[latitude, longitude], radius=50, popup="Magnitud: " + str(mag),
                    fill_color='red', color='black', fill_opacity=0.7).add_to(mapa)

# Mostrar el mapa en Streamlit
folium_static(mapa)

st.subheader("Detalles del sismo")

# Función para mostrar detalles con un diseño más creativo
def show_details():
    st.subheader("Detalles Generales")
    st.markdown("---")
    st.write(f"🌍 **País:** {country}")
    st.write(f"📍 **Latitud:** {latitude}")
    st.write(f"📍 **Longitud:** {longitude}")

# Función para mostrar detalles específicos con un diseño más creativo
def show_details2():
    st.subheader("Detalles Específicos")
    st.markdown("---")
    
    st.write(f"🌋 **Magnitud:** {mag}")
    st.progress(int(mag * 10))  # Agregar una barra de progreso para visualizar la magnitud
    
    st.write(f"🌊 **Profundidad:** {depth} km")
    st.progress(int(depth))  # Agregar una barra de progreso para visualizar la profundidad
    
    st.write(f"📅 **Tipo de sismo:** {sistype}")
    st.write(f"⏰ **Fecha:** {fecha}")
    
# Mostrar el mapa y los detalles
col1, col2 = st.columns(2)
with col1:
    show_details()
    
with col2:
    show_details2()

# Dibujar la escala de Richter
st.subheader("Escala de Richter")
st.image("ritcher.jpg")





