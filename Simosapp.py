import streamlit as st

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
    </style>
    """,
    unsafe_allow_html=True
)

# Título de la aplicación
st.title("QuakeAlert: Informando sobre Sismos")

# Línea separadora
st.write("---")

# Create a map centered at the earthquake location
st.subheader("Locacion")
earthquake_map = folium.Map(location=[latitude, longitude], zoom_start=10)
folium.Marker(location=[latitude, longitude], popup="Locacion").add_to(earthquake_map)
folium_static(earthquake_map)

# Mostrar los datos
st.write(f"Pais: {country}")
st.write(f"Latitud: {latitude}")
st.write(f"Longitud: {longitude}")
st.write(f"Profundidad: {depth}")
st.write(f"Magnitud: {mag}")
st.write(f"Tipo: {sistype}")
st.write(f"Fecha: {date}")





