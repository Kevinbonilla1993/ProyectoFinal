import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Alertas Sismicas",
                   page_icon="bar_chart:",
                   layout="wide")

# Obtener parámetros de la URL
result = st.experimental_get_query_params()

country = result['val'][0]
latitude = result['val'][1]
longitude=result['val'][2]
depth = result['val'][3]
mag = result['val'][4]
sistype = result['val'][5]

# Crear diseño
if country == 'japon':
    st.image('bajo.jpg', caption='Imagen de Japón')

