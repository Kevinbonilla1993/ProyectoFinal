import streamlit as st
import folium
from streamlit_folium import folium_static

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

    /* Estilo para el título */
    .title {
        font-size: 36px;
        color: #333333;
        margin-bottom: 20px;
    }

    /* Estilo para los datos */
    .data {
        font-size: 18px;
        color: #555555;
        margin-bottom: 10px;
    }

    /* Estilo para la línea separadora */
    .separator {
        height: 3px;
        background-color: #555555;
        margin: 20px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título de la aplicación
st.markdown("<h1 class='title'>QuakeAlert: Informando sobre Sismos</h1>", unsafe_allow_html=True)

# Línea separadora
st.write("", "", className="separator")

# Mostrar los datos
st.markdown(f"<p class='data'>Pais: {country}</p>", unsafe_allow_html=True)
st.markdown(f"<p class='data'>Latitud: {latitude}</p>", unsafe_allow_html=True)
st.markdown(f"<p class='data'>Longitud: {longitude}</p>", unsafe_allow_html=True)
st.markdown(f"<p class='data'>Profundidad: {depth}</p>", unsafe_allow_html=True)
st.markdown(f"<p class='data'>Magnitud: {mag}</p>", unsafe_allow_html=True)
st.markdown(f"<p class='data'>Tipo: {sistype}</p>", unsafe_allow_html=True)
st.markdown(f"<p class='data'>Fecha: {date}</p>", unsafe_allow_html=True)

# Display the images
st.subheader("Escala de richter")
image1 = st.image("ritcher.jpg")

# Create a map centered at the earthquake location
st.subheader("Locacion")
earthquake_map = folium.Map(location=[latitude, longitude], zoom_start=10)
folium.Marker(location=[latitude, longitude], popup="Locacion").add_to(earthquake_map)
folium_static(earthquake_map)

# Display recommendations
st.subheader("Recommendations")
recommendation = st.text_area("Enter your recommendations here.")

image2 = st.image("recomendaciones.jpg")

