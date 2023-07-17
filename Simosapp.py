import streamlit as st
import folium

# Datos del sismo

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
st.set_page_config(page_title="App Quake", page_icon=":earth_americas:")

# Título y menú desplegable
st.title("App Quake")
st.sidebar.title("Interacciones")
menu_options = ['Home', 'Interacciones']
selected_option = st.sidebar.selectbox("Seleccione una opción", menu_options)

# Mostrar el mapa centrado en la ubicación del sismo
m = folium.Map(location=[latitude, longitude], zoom_start=8)
folium.Marker([latitude, longitude], popup=f"{country}: {mag}").add_to(m)
folium_static = folium.Figure(width=800, height=600)
folium_static.add_child(m)
st.markdown(folium_static._repr_html_(), unsafe_allow_html=True)

# Información adicional del sismo
st.subheader("Información del sismo")
st.write(f"Fecha: {fecha}")
st.write(f"Profundidad: {depth} km")
st.write(f"Magnitud: {mag}")

# Dibujo interactivo de la escala de Richter
st.subheader("Escala de Richter")
st.image("ritcher.jpg", use_column_width=True)

# Ubicación en longitud y latitud
st.subheader("Ubicación en coordenadas")
st.write(f"Latitud: {latitude}")
st.write(f"Longitud: {longitude}")

# Ubicación en formato de texto encima del mapa
st.markdown(f"<span style='color: orange;'>Ubicación: {country}</span>", unsafe_allow_html=True)

# Imagen de recomendaciones
st.subheader("Recomendaciones")
st.image("recomendaciones.jpg", use_column_width=True)







