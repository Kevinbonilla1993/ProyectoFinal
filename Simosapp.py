import streamlit as st
from PIL import Image
import pandas as pd
import datetime
import streamlit as st
from streamlit_folium import folium_static
import folium
from folium.plugins import MarkerCluster

# Obtener parámetros de la URL
result = st.experimental_get_query_params()

country = result['val'][0]
latitude = result['val'][1]
longitude = result['val'][2]
depth = result['val'][3]
mag = result['val'][4]
sistype = result['val'][5]
fecha = result['val'][6]

# Set the title of the app
st.title("Earthquake App")

# Create a map centered on the earthquake location
map = folium.Map(location=[latitude, longitude], zoom_start=6)

# Add a marker to the map
folium.Marker([latitude, longitude], popup=f"Earthquake in {country}").add_to(map)

# Display the map
st.map(map)

# Add more information below the map
st.write("Date:", date)
st.write("Depth:", depth)
st.write("Magnitude:", mag)

# Create an interactive Richter scale
richter_scale = st.slider("Richter Scale", 1.0, 10.0, mag)

# Display the location in longitude and latitude
st.write("Longitude:", longitude)
st.write("Latitude:", latitude)

# Display the location in strings above the map
st.write(f"Earthquake in {country}", style={"color": "orange"})

# Add a dropdown menu with home and interactions
st.sidebar.dropdown("Menu", ["Home", "Interactions"])
