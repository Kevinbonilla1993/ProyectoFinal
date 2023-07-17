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

import streamlit as st
import folium
import requests

def get_map(country, latitude, longitude, depth, mag):
    """Gets a map of the earthquake location."""
    map = folium.Map(location=[latitude, longitude], zoom_start=6)
    folium.CircleMarker([latitude, longitude], radius=mag*10, color='red', fill=True, fill_color='red').add_to(map)
    return map

def get_scale(mag):
    """Gets an interactive drawing of the Richter scale."""
    scale = requests.get('https://raw.githubusercontent.com/streamlit/streamlit/master/examples/widgets/richter_scale.html')
    return scale

def main():
    """Main function."""
    st.title('App Quake')
    map = get_map(country, latitude, longitude, depth, mag)
    st.write(map)
    st.write('Date:', date)
    st.write('Depth:', depth)
    st.write('Magnitude:', mag, '(Richter scale)')
    st.write(get_scale(mag))
    st.write('Location:', latitude, ',', longitude)

if __name__ == '__main__':
    main()

