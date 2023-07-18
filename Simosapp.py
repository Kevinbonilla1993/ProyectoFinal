import streamlit as st
import folium

# Obtener parámetros de la URL
result = st.experimental_get_query_params()

# Verificar si las variables están presentes en la URL
if 'val' in result:
    val_list = result['val']

    if len(val_list) == 7:
        country = val_list[0]
        latitude = float(val_list[1])  # Convertir a número
        longitude = float(val_list[2])  # Convertir a número
        depth = val_list[3]
        mag = val_list[4]
        sistype = val_list[5]
        date = val_list[6]

        # Crear el mapa con las coordenadas dadas
        mapa = folium.Map(location=[latitude, longitude], zoom_start=10)

        # Agregar marcador para la ubicación dada
        folium.Marker([latitude, longitude], popup=f'{country}, {date}').add_to(mapa)

        # Mostrar el mapa en Streamlit
        st.write(mapa)
    else:
        st.write("URL mal formada. Asegúrate de proporcionar todos los valores necesarios.")
else:
    st.write("No se encontraron valores en la URL. Asegúrate de proporcionar los parámetros 'val' en la URL.")



