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

# Agregar CSS personalizado para el área de la aplicación
st.markdown(
    """
    <style>
    .stApp {
        background-color: orange;
        max-width: 800px; /* Ajusta el ancho máximo según tus preferencias */
        padding: 20px; /* Añade un relleno para que el contenido no quede pegado al borde */
        margin: 0 auto; /* Centra el contenedor horizontalmente */
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

# Información del sismo
st.subheader("Información del sismo")
col1, col2, col3 = st.columns(3)
with col1:
    st.write(f"Fecha: {fecha}")
    st.write(f"Profundidad: {depth} km")
with col2:
    st.write(f"Magnitud: {mag}")
with col3:
    st.write(f"Latitud: {latitude}")
st.write(f"Longitud: {longitude}")
# Ubicación en formato de texto
st.subheader("Ubicación")
st.markdown(f"<span style='color: orange;'>{country}</span>", unsafe_allow_html=True)


# Dibujar la escala de Richter
st.subheader("Escala de Richter")
st.image("ritcher.jpg")





