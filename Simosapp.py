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
st.set_page_config(page_title="QuakeAlert", page_icon="🌍", layout="wide")

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

# Agregar una descripción breve
st.markdown('Esta aplicación proporciona información detallada sobre sismos.')

# Separadores
st.markdown("---")

# Función para mostrar el mapa con los últimos sismos
def show_map():
    st.subheader("Mapa de los últimos sismos")
    m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=3)
    for i in range(len(df)):
        folium.Marker([df['Latitude'][i], df['Longitude'][i]], popup=f"Magnitud: {df['Magnitude'][i]} | Profundidad: {df['Depth'][i]} km").add_to(m)
    return m

# Función para mostrar los detalles del último sismo
def show_details():
    st.subheader("Detalles del último sismo")
    st.write(f"Fecha: {df['Date'][0]}")
    st.write(f"País: {df['Country'][0]}")
    st.write(f"Magnitud: {df['Magnitude'][0]}")
    st.write(f"Profundidad: {df['Depth'][0]} km")
# Mostrar el mapa y los detalles
col1, col2 = st.columns(2)
with col1:
    show_map()

with col2:
    show_details()

# Información del sismo
st.subheader("Información del sismo")
col1, col2, col3 = st.columns(3)
with col1:
    st.write(f"Fecha: {fecha}")
    
with col2:
    st.write(f"Magnitud: {mag}")
    st.write(f"Profundidad: {depth} km")
with col3:
    st.write(f"Latitud: {latitude}")
    st.write(f"Longitud: {longitude}")
# Ubicación en formato de texto
st.subheader("Ubicación")
st.markdown(f"<span style='color: orange;'>{country}</span>", unsafe_allow_html=True)


# Dibujar la escala de Richter
st.subheader("Escala de Richter")
st.image("ritcher.jpg")





