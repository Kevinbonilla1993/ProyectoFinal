import streamlit as st
import folium

# Obtener parámetros de la URL
result = st.experimental_get_query_params()

country = result['val'][0]
latitude = float(result['val'][1])
longitude = float(result['val'][2])
depth = result['val'][3]
mag = float(result['val'][4])
sistype = result['val'][5]
date = result['val'][6]

# Crear un mapa con Folium
m = folium.Map(location=[latitude, longitude], zoom_start=6)

# Agregar un marcador al mapa con información del sismo
popup_text = f"Pais: {country}<br>Latitud: {latitude}<br>Longitud: {longitude}<br>Profundidad: {depth}<br>Magnitud: {mag}<br>Tipo: {sistype}<br>Fecha: {date}"
folium.Marker(location=[latitude, longitude], popup=popup_text, icon=folium.Icon(color='red', icon='info-sign')).add_to(m)

# Agregar un control de capas para alternar estilos de mapa
folium.TileLayer('OpenStreetMap').add_to(m)
folium.TileLayer('Stamen Terrain').add_to(m)
folium.TileLayer('Stamen Toner').add_to(m)
folium.LayerControl().add_to(m)

# Agregar algunos marcadores adicionales para mostrar lugares de interés
places = {
    "Ciudad importante 1": [latitude + 0.1, longitude + 0.1],
    "Ciudad importante 2": [latitude - 0.1, longitude - 0.1],
    "Centro turístico": [latitude, longitude + 0.2],
    "Área de interés": [latitude - 0.15, longitude + 0.15],
}

for place, coords in places.items():
    folium.Marker(location=coords, popup=place, icon=folium.Icon(color='blue', icon='star')).add_to(m)

# Convertir el mapa de Folium a HTML
map_html = m._repr_html_()

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
    .data-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        grid-gap: 20px;
    }

    .data {
        font-size: 18px;
        color: #555555;
    }

    /* Estilo para la línea separadora */
    .separator {
        height: 3px;
        background-color: #555555;
        margin: 20px 0;
    }

    /* Estilo para el contenedor del mapa */
    .map-container {
        margin-top: 20px;
    }

    /* Estilo para el mapa */
    .folium-map {
        width: 100%;
        height: 500px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Título de la aplicación
st.markdown("<h1 class='title'>QuakeAlert: Informando sobre Sismos</h1>", unsafe_allow_html=True)

# Línea separadora
st.write("", "", className="separator")

# Mostrar los datos en formato 3 columnas
st.markdown("<div class='data-container'>", unsafe_allow_html=True)

st.markdown(f"<p class='data'>Pais: {country}</p>", unsafe_allow_html=True)
st.markdown(f"<p class='data'>Latitud: {latitude}</p>", unsafe_allow_html=True)
st.markdown(f"<p class='data'>Longitud: {longitude}</p>", unsafe_allow_html=True)
st.markdown(f"<p class='data'>Profundidad: {depth}</p>", unsafe_allow_html=True)
st.markdown(f"<p class='data'>Magnitud: {mag}</p>", unsafe_allow_html=True)
st.markdown(f"<p class='data'>Tipo: {sistype}</p>", unsafe_allow_html=True)
st.markdown(f"<p class='data'>Fecha: {date}</p>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# Mostrar el mapa interactivo
st.markdown("<div class='map-container'>", unsafe_allow_html=True)
st.markdown(f"<div class='folium-map'>{map_html}</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)




