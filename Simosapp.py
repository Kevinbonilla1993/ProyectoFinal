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
st.set_page_config(page_title="App Quake", layout="wide")

# Título de la app
st.title("App Quake")

# Menú desplegable
menu_options = ["Home", "Interacciones"]
menu_choice = st.sidebar.selectbox("Menú", menu_options)

# Mapa centrado en la ubicación del sismo
st.header("Mapa")
map_center = [latitude, longitude]
map_zoom = 10
map_height = 600
m = folium.Map(location=map_center, zoom_start=map_zoom, height=map_height)
folium.Marker(location=map_center, popup="Ubicación del sismo").add_to(m)
folium_static = st.markdown(folium.Map(location=map_center, zoom_start=map_zoom)._repr_html_(), unsafe_allow_html=True)

# Información adicional del sismo
st.header("Información adicional")
st.subheader("Fecha")
st.write(fecha)
st.subheader("Profundidad")
st.write(depth)
st.subheader("Magnitud")
st.write(mag)

# Representación interactiva de la escala de Richter
st.subheader("Escala de Richter")
richter_scale = """
            <style>
                .richter-scale {
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                }
                .richter-scale .bar {
                    width: 100%;
                    height: 30px;
                    background-color: #CCCCCC;
                }
                .richter-scale .indicator {
                    width: 0%;
                    height: 30px;
                    background-color: #FFA500;
                }
            </style>
            <div class="richter-scale">
                <div class="bar"></div>
                <div class="indicator" style="width:{magnitude_percentage}%;"></div>
            </div>
        """
magnitude_percentage = (mag / 9) * 100  # Escala de Richter normalizada de 0 a 100
st.markdown(richter_scale.format(magnitude_percentage=magnitude_percentage), unsafe_allow_html=True)

# Ubicación en longitud y latitud
st.subheader("Ubicación (Longitud, Latitud)")
st.write(f"{longitude}, {latitude}")

# Ubicación en texto
st.subheader("Ubicación (Texto)")
st.markdown(f"<span style='color: orange;'>{country}</span>", unsafe_allow_html=True)

