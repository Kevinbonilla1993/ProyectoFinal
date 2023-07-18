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

# Título de la app
st.title("QuakeAlert")

# Agregar una descripción breve
st.markdown('**Esta aplicación proporciona información detallada sobre sismos.**')

# Filtros interactivos
st.sidebar.title("Filtros")
filtro_mag = st.sidebar.slider("Magnitud", 4.0, 9.0, 6.0, 0.1)
filtro_depth = st.sidebar.slider("Profundidad (km)", 0.0, 100.0, 50.0, 1.0)

# Filtrar sismos
sismos_filtrados = [sismo for sismo in sismos if sismo['mag'] >= filtro_mag and sismo['depth'] <= filtro_depth]

# Crear un mapa centrado en la ubicación del primer sismo
if sismos_filtrados:
    mapa = folium.Map(location=[sismos_filtrados[0]['latitude'], sismos_filtrados[0]['longitude']], zoom_start=5)
else:
    mapa = folium.Map(location=[0, 0], zoom_start=2)

# Añadir marcadores de los sismos filtrados
for sismo in sismos_filtrados:
    folium.Marker(location=[sismo['latitude'], sismo['longitude']], popup=sismo['country'], icon=folium.Icon(color='red')).add_to(mapa)

# Capa de mapa de calor para visualizar la densidad de sismos
heat_data = [[sismo['latitude'], sismo['longitude']] for sismo in sismos_filtrados]
folium.plugins.HeatMap(heat_data, radius=15).add_to(mapa)

# Estilo personalizado para los círculos de los sismos
def style_function(feature):
    return {
        'fillColor': 'red',
        'color': 'black',
        'weight': 2,
        'fillOpacity': 0.7,
    }
folium.GeoJson(geojson='https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_boundaries.json', style_function=style_function).add_to(mapa)

# Mostrar el mapa en Streamlit
folium_static(mapa)

st.subheader("Detalles de los sismos filtrados")

# Mostrar los detalles de los sismos filtrados
for sismo in sismos_filtrados:
    st.write(f"País: {sismo['country']}")
    st.write(f"Latitud: {sismo['latitude']}")
    st.write(f"Longitud: {sismo['longitude']}")
    st.write(f"Magnitud: {sismo['mag']}")
    st.write(f"Profundidad: {sismo['depth']} km")
    st.write(f"Tipo de sismo: {sismo['sistype']}")
    st.write(f"Fecha: {sismo['fecha']}")
    st.markdown("---")

# Gráfico de barras para visualizar la distribución de sismos por país
pais_count = {}
for sismo in sismos_filtrados:
    if sismo['country'] in pais_count:
        pais_count[sismo['country']] += 1
    else:
        pais_count[sismo['country']] = 1

st.subheader("Distribución de sismos por país")
st.bar_chart(pais_count)

# Línea de tiempo interactiva para visualizar la frecuencia de sismos a lo largo del tiempo
fechas = [datetime.strptime(sismo['fecha'], '%Y-%m-%d %H:%M:%S').astimezone(pytz.timezone('America/Mexico_City')) for sismo in sismos_filtrados]
st.subheader("Frecuencia de sismos a lo largo del tiempo")
st.line_chart(fechas)

# Función para mostrar notificación en caso de sismos significativos
def notify_significant_earthquake(mag_threshold):
    for sismo in sismos_filtrados:
        if sismo['mag'] >= mag_threshold:
            st.error(f"¡ALERTA! Sismo significativo detectado en {sismo['country']} de magnitud {sismo['mag']}.")

# Notificar en tiempo real si hay sismos significativos (magnitud mayor o igual a 7.0)
notify_significant_earthquake(7.0)
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





