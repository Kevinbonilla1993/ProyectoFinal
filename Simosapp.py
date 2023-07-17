import streamlit as st
import folium

# Datos del sismo
country = result['val'][0]
latitude = result['val'][1]
longitude = result['val'][2]
depth = result['val'][3]
mag = result['val'][4]
sistype = result['val'][5]
fecha = result['val'][6]

# Configuración de la página
st.set_page_config(page_title='App Quake', layout='wide')

# Título de la aplicación
st.title('App Quake')

# Menú desplegable
menu_options = ['Home', 'Interacciones']
selected_menu = st.sidebar.selectbox('Menú', menu_options)

if selected_menu == 'Home':
    # Mapa centrado en el sismo
    quake_map = folium.Map(location=[latitude, longitude], zoom_start=8)
    folium.Marker([latitude, longitude], popup=country).add_to(quake_map)
    folium.TileLayer('cartodbpositron').add_to(quake_map)
    folium.TileLayer('stamentonerlabels').add_to(quake_map)
    quake_map = quake_map._repr_html_()

    # Información del sismo
    st.subheader('Información del sismo')
    st.markdown(f"**Fecha:** {fecha}")
    st.markdown(f"**Profundidad:** {depth} km")
    st.markdown(f"**Magnitud:** {mag}")
    st.markdown(f"**Tipo de sismo:** {sistype}")

    # Escala de Richter interactiva
    st.subheader('Escala de Richter')
    st.image('richter_scale.png', use_column_width=True)

else:
    # Interacciones
    st.subheader('Interacciones')
    # Agrega aquí el código para las interacciones que desees mostrar

# Estilos de la aplicación
st.markdown(
    """
    <style>
    .css-1aumxhk {
        color: orange;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Renderiza el mapa y otros elementos en la página
st.markdown(f"""
    <div style="background-color: orange; padding: 10px; border-radius: 10px; margin-top: 20px">
    <h3 style="color: white; text-align: center">{country}</h3>
    <p style="color: white; text-align: center">Latitud: {latitude}, Longitud: {longitude}</p>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(quake_map, unsafe_allow_html=True)

