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

st.title("Earthquake Alert App")
st.write(f"Country: {country}")
st.write(f"Latitude: {latitude}")
st.write(f"Length: {longitude}")
st.write(f"Depth: {depth}")
st.write(f"Magnitude: {mag}")
st.write(f"Typosis: {sistype}")
st.write(f"Date: {date}")

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

