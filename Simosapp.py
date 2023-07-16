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
    level = 'Leve :large_green_circle:'
    delta = 'ML'
    rgba = '[0,204,0,160]'
    recm = 'bajo.jpeg'
elif sistype == 'medio':
    level = 'Medio :large_yellow_circle:'
    delta = 'ML'
    rgba = '[255,255,0,160]'
    recm = 'medio.jpeg'
elif sistype == 'alto':
    level = 'Alto :red_circle:'
    delta = '-ML'
    rgba = '[255,0,0,160]'
    recm = 'alto.jpeg'
else:
    level = ':white_circle: Desconocido'
    delta = 'ML'
    rgba = '[255,255,0,160]'
    recm = 'bajo.jpeg'
