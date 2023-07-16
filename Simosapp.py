import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="Alertas Sismicas",
                   page_icon="bar_chart:",
                   layout="wide")

# Obtener parámetros de la URL
result = st.experimental_get_query_params()
print(result)

country = result['pais'][0]
latitude = result['val'][1]
longitude = result['val'][2]
depth = result['val'][3]
mag = result['val'][4]
sistype = result['val'][5]

# Crear diseño
if sistype == 'leve':
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

if country == 'usa':
    flag = ':flag-us:'
elif country == 'japon':
    flag = ':flag-jp:'
elif country == 'chile':
    flag = ':flag-cl:'
else:
    flag = ':flag-us:'

# Mostrar la página
st.markdown(f'# {flag} Intensidad: {level}') # Nivel
st.markdown('***')
d = {'lat': [float(latitude)], 'lon': [float(longitude)]}
df = pd.DataFrame(d)
col1, col2, col3 = st.columns(3)
col1.metric(label='Magnitud', value=mag, delta=delta)
col2.metric(label='Profundidad', value=depth, delta='Km')
col3.markdown('## [Ver últimos 20 :eye:](https://us-central1-alerta-sismos-386306.cloudfunctions.net/function-mongo)')

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=float(latitude),
        longitude=float(longitude),
        zoom=5,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[lon, lat]',
            get_color=rgba,
            get_radius=float(mag) * 8000,
        ),
    ],
))

# Recomendaciones
st.markdown('***')
st.markdown('## Recomendaciones')
image = Image.open('infografia.png')
image_b = Image.open(recm)
st.image(image_b)
st.image(image)
