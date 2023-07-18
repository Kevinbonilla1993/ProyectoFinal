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

# Carga del GIF desde el directorio local
gif_path = "quake_alert.gif"
st.image(gif_path,use_column_width=True)

# Estilo personalizado para el título de la app
# st.title("🚀 QuakeAlert 🌎")
# st.markdown("Bienvenido a QuakeAlert, la aplicación que proporciona información detallada sobre sismos en tiempo real. Mantente informado sobre los últimos sismos ocurridos en todo el mundo.")

# Separadores
st.markdown("---")

# Crear un mapa centrado en la ubicación proporcionada
mapa = folium.Map(location=[latitude, longitude], zoom_start=10)

folium.Marker([latitude, longitude], popup="Epicentro del Sismo").add_to(folium_map)
    st.write(folium_map._repr_html_(), unsafe_allow_html=True)

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

# Mostrar el mapa y los detalles
col1, col2 = st.columns(2)
with col1:
    show_details()
    
with col2:
    show_details2()

# Inicializar la sesión
if 'comments' not in st.session_state:
    st.session_state.comments = []

if 'survey_responses' not in st.session_state:
    st.session_state.survey_responses = []

# Agregar una encuesta rápida sobre seguridad
st.subheader("Encuesta de Seguridad")
question1 = st.radio("¿Tienes un plan de evacuación en caso de sismo?", ("Sí", "No"))
question2 = st.radio("¿Tienes un kit de emergencia preparado?", ("Sí", "No"))
question3 = st.radio("¿Conoces los lugares seguros en tu hogar?", ("Sí", "No"))

if st.button("Enviar encuesta"):
    # Guardar las respuestas de la encuesta en la lista de respuestas de encuestas
    st.session_state.survey_responses.append({
        "Pregunta 1": question1,
        "Pregunta 2": question2,
        "Pregunta 3": question3
    })

st.subheader("Respuestas de Encuesta Guardadas")
for response in st.session_state.survey_responses:
    st.write(response)




