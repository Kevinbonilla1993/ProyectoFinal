import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Alertas Sismicas",
                   page_icon="bar_chart:",
                   layout="wide")

# Obtener parámetros de la URL
result = st.experimental_get_query_params()




st.image('bajo.jpg', caption='Imagen de Japón')

