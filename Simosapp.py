from streamlit_folium import folium_static
import streamlit as st
import folium
from datetime import datetime
import pytz
import pydeck as pdk
import time

# Obtener parámetros de la URL
result = st.experimental_get_query_params()

country = result['val'][0]
latitude = float(result['val'][1])
longitude = float(result['val'][2])
depth = float(result['val'][3])
mag = float(result['val'][4])
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

# Crear un mapa centrado en la ubicación proporcionada
mapa = folium.Map(location=[latitude, longitude], zoom_start=10)

# Añadir círculo en la ubicación del sismo con estilo personalizado
folium.CircleMarker(location=[latitude, longitude], radius=50, popup="Magnitud: " + str(mag),
                    fill_color='red', color='black', fill_opacity=0.7).add_to(mapa)

folium_static(mapa)

st.subheader("Detalles del sismo")

# Función para mostrar detalles con un diseño más creativo
def show_details():
    st.subheader("Detalles Generales")
    st.markdown("---")
    st.write(f"🌍 **País:** {country}")
    st.write(f"📍 **Latitud:** {latitude}")
    st.write(f"📍 **Longitud:** {longitude}")

    st.subheader("Tiempo desde el sismo")
    timezone = pytz.timezone('America/Bogota')  # Cambia 'NombreDeTuZonaHoraria' por la zona horaria correspondiente
    sismo_time = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')
    sismo_time = timezone.localize(sismo_time)
    now = datetime.now(timezone)
    time_diff = now - sismo_time
    st.write(f"Ha pasado {time_diff.days} días, {time_diff.seconds // 3600} horas y {time_diff.seconds // 60} minutos desde el sismo.")

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

      # Gráfico interactivo de profundidad
    st.subheader("Gráfico de Profundidad")
    depth_chart_data = pd.DataFrame(depth)
    depth_chart = pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=latitude,
            longitude=longitude,
            zoom=10,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
                'ColumnLayer',
                data=depth_chart_data,
                get_position='[0, 0]',
                get_elevation='Profundidad * 100',  # Escala la profundidad para mejor visualización
                elevation_scale=1000,
                radius=20000,
                get_fill_color='[255, 0, 0]',
                auto_highlight=True,
                pickable=True,
            ),
        ],
    )
    st.pydeck_chart(depth_chart)
# Mostrar el mapa y los detalles
col1, col2 = st.columns(2)
with col1:
    show_details()
    
with col2:
    show_details2()

# Dibujar la escala de Richter
st.subheader("Escala de Richter")
st.image("ritcher.jpg")





