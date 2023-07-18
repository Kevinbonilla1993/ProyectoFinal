from streamlit_folium import folium_static
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
fecha = result['val'][6]
# Configuración de la página
st.set_page_config(page_title="QuakeAlert", layout="wide")

# Agregar CSS personalizado para el fondo de pantalla
st.markdown(
    """
    <style>
    body {
        background-color: orange;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título de la app
st.title("QuakeAlert")

# Separadores
st.markdown("---")

# Mapa centrado en la ubicación del sismo
m = folium.Map(location=[latitude, longitude], zoom_start=8)

# Marcador en la ubicación del sismo
marker = folium.Marker([latitude, longitude], popup=sistype)
marker.add_to(m)

# Mostrar el mapa
st.subheader("Mapa")
folium_static(m)

# Ubicación en longitud y latitud
st.subheader("Ubicación en coordenadas")
st.write(f"Latitud: {latitude}")
st.write(f"Longitud: {longitude}")

# Ubicación en formato de texto
st.subheader("Ubicación")
st.markdown(f"<span style='color: orange;'>{country}</span>", unsafe_allow_html=True)

# Menú desplegable
menu_options = ["Inicio", "Detalles Sismo"]
choice = st.sidebar.selectbox("Menu", menu_options)


# Dibujar la escala de Richter
st.subheader("Escala de Richter")
st.image("ritcher.jpg")

# Información del sismo
st.subheader("Información del sismo")
col1, col2 = st.columns(2)
with col1:
    st.write(f"Fecha: {fecha}")
    st.write(f"Profundidad: {depth} km")
with col2:
    st.write(f"Magnitud: {mag}")



