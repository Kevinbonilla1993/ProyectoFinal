import streamlit as st
import folium

# Obtener parámetros de la URL
result = st.experimental_get_query_params()

country = result['val'][0]
latitude = float(result['val'][1])
longitude = float(result['val'][2])
depth = result['val'][3]
mag = float(result['val'][4])
sistype = result['val'][5]
date = result['val'][6]

import streamlit as st
import folium

# Crear una función para generar el mapa con Folium
def generate_map(latitude, longitude, country, depth, mag, sistype, date):
    # Crear un mapa con Folium
    m = folium.Map(location=[latitude, longitude], zoom_start=8)

    # Agregar un marcador al mapa con información del sismo
    popup_text = f"Pais: {country}<br>Latitud: {latitude}<br>Longitud: {longitude}<br>Profundidad: {depth}<br>Magnitud: {mag}<br>Tipo: {sistype}<br>Fecha: {date}"
    folium.Marker(location=[latitude, longitude], popup=popup_text).add_to(m)

    # Convertir el mapa de Folium a HTML
    map_html = m._repr_html_()
    return map_html

# Página principal de la aplicación
def main():
    st.title("QuakeAlert: Informando sobre Sismos")
    st.write("Ingrese los datos del sismo:")
    country = st.text_input("Pais")
    latitude = st.number_input("Latitud", value=0.0)
    longitude = st.number_input("Longitud", value=0.0)
    depth = st.text_input("Profundidad")
    mag = st.number_input("Magnitud", value=0.0)
    sistype = st.text_input("Tipo")
    date = st.text_input("Fecha")

    if st.button("Mostrar Mapa"):
        map_html = generate_map(latitude, longitude, country, depth, mag, sistype, date)
        st.markdown(f"<div>{map_html}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()




