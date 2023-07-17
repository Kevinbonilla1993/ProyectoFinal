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

# Título de la app
st.title("App Quake")

# Menú desplegable
menu_options = ['Home', 'Interacciones']
selected_option = st.sidebar.selectbox("Menú", menu_options)

# Mostrar el mapa centrado en el lugar del sismo
st.map((latitude, longitude), zoom=8)

# Información adicional
st.header("Información adicional")
st.subheader("Fecha: " + fecha)
st.subheader("Profundidad: " + str(depth))
st.subheader("Magnitud: " + str(mag))

# Dibujo interactivo de la escala de Richter
st.subheader("Escala de Richter")
st.image("richter.jpg", use_column_width=True)

# Ubicación en longitud y latitud
st.subheader("Ubicación")
st.write("Latitud:", latitude)
st.write("Longitud:", longitude)

# Ubicación en formato de cadena
st.subheader("Ubicación (string)")
st.write(country)

# Recomendaciones
st.image("recomendaciones.jpg", use_column_width=True)

