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
st.set_page_config(page_title="App Quake")

# Título y menú desplegable
st.title("App Quake")
st.sidebar.title("Interacciones")
menu_options = ['Home', 'Interacciones']
selected_option = st.sidebar.selectbox("Seleccione una opción", menu_options)

# Create a map centered on the earthquake location
map = folium.Map(location=[latitude, longitude], zoom_start=8)

# Add the earthquake location to the map
folium.Marker([latitude, longitude], popup=f"Earthquake Location").add_to(map)

# Add more information below the map
st.subheader("Earthquake Details")
st.write("Date:", fecha)
st.write("Depth:", depth)
st.write("Magnitude:", mag)

# Slider de la escala de Richter
scale = st.slider("Richter Scale", 1.0, 9.9, value=float(mag))

# Add the location in longitude and latitude
st.write("Longitude:", longitude)
st.write("Latitude:", latitude)

# Add the location in strings above the map
st.write(f"Earthquake Location: {country} ({latitude}, {longitude})")

# Add an image below the dropdown menu
st.image("https://i.imgur.com/15j871F.png")

# Display the map
st.map(map)




