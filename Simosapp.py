from streamlit_folium import folium_static
import streamlit as st
import folium
from datetime import datetime
import time
import requests
import json 
import pytz
import pandas as pd
# Obtener parámetros de la URL
result = st.experimental_get_query_params()

country = result['val'][0]
latitude = float(result['val'][1])
longitude = float(result['val'][2])
depth = float(result['val'][3])
mag = float(result['val'][4])
sistype = result['val'][5]
fecha = result['val'][6]

# funciones
def mostrar_inicio():
    # Crear el mapa
    mapa = folium.Map(location=[latitude, longitude], zoom_start=10)
    
    # Agregar un marcador para mostrar la ubicación del sismo
    folium.Marker(location=[latitude, longitude], popup=f"Sismo en {country}\nMagnitud: {mag}\nFecha: {fecha}").add_to(mapa)
    
    # Mostrar el mapa interactivo
    folium_static(mapa)
    
    st.subheader("Detalles del sismo")
    
    # Función para mostrar detalles con un diseño más creativo
    def show_details():
        st.subheader("Detalles Generales")
        st.markdown("---")
        st.write(f"🌍 **País:** {country}")
        st.write(f"📍 **Latitud:** {latitude}")
        st.write(f"📍 **Longitud:** {longitude}")
    
        st.subheader("Tiempo desde el sismo")
        timezone = pytz.timezone('America/Bogota')  # Cambia 'NombreDeTuZonaHoraria' por la zona horaria correspondiente
        sismo_time = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')
        sismo_time = timezone.localize(sismo_time)
        now = datetime.now(timezone)
        time_diff = now - sismo_time
        st.write(f"Ha pasado {time_diff.days} días, {time_diff.seconds // 3600} horas y {time_diff.seconds // 60} minutos desde el sismo.")
    
    # Función para mostrar detalles específicos con un diseño más creativo
    def show_details2():
        st.subheader("Detalles Específicos")
        st.markdown("---")
        
        st.write(f"🌋 **Magnitud:** {mag}")
        st.progress(int(mag * 10))  # Agregar una barra de progreso para visualizar la magnitud
        
        st.write(f"🌊 **Profundidad:** {depth} km")
        st.progress(int(depth))  # Agregar una barra de progreso para visualizar la profundidad
        
        st.write(f"📅 **Tipo de sismo:** {sistype}")
        st.write(f"⏰ **Fecha:** {fecha}")
    
    # Mostrar el mapa y los detalles
    col1, col2 = st.columns(2)
    with col1:
        show_details()
        
    with col2:
        show_details2()
    
    # Inicializar la sesión
    if 'comments' not in st.session_state:
        st.session_state.comments = []
    
    if 'survey_responses' not in st.session_state:
        st.session_state.survey_responses = []
    
    # Agregar una encuesta rápida sobre seguridad
    st.subheader("Encuesta de Seguridad")
    question1 = st.radio("¿Tienes un plan de evacuación en caso de sismo?", ("Sí", "No"))
    question2 = st.radio("¿Tienes un kit de emergencia preparado?", ("Sí", "No"))
    question3 = st.radio("¿Conoces los lugares seguros en tu hogar?", ("Sí", "No"))
    
    if st.button("Enviar encuesta"):
        # Guardar las respuestas de la encuesta en la lista de respuestas de encuestas
        st.session_state.survey_responses.append({
            "Pregunta 1": question1,
            "Pregunta 2": question2,
            "Pregunta 3": question3
        })
    
    st.subheader("Respuestas de Encuesta Guardadas")
    for response in st.session_state.survey_responses:
        st.write(response)

def ultimo_sismo():
    # Ultimo dato de japon
    r = requests.get("https://www.jma.go.jp/bosai/quake/data/list.json")
    r = r.text
    r = json.loads(r)
    r = r[0]
    vars = r['cod'][1:]
    vars = vars.replace('+', ',')
    vars = vars.replace('-', ',')
    vars = vars.replace('/', '')
    vars = vars.split(',')
    lat = vars[0]
    lon = vars[1]
    dept = vars[2]
    quake = {'time': r['at'], 'latitude': lat, 'longitude': lon, 'depth': dept, 'mag': r['mag'], 'localidad': r['en_anm'], 'country': 'japon'}
    Japon = pd.DataFrame([quake])
    #convertimos a float la columna "depth"
    Japon['depth'] = Japon['depth'].astype('float64')
    #dividimos por mil para llevar la unidad de medida a KM para mantener la misma en todos los datasets
    Japon['depth'] = (Japon['depth'] / 1000)
    # Formato correcto a la columna de fechas
    Japon['time'] = pd.to_datetime(Japon['time']).dt.strftime('%Y-%m-%d %H:%M:%S')
    #Redondear las columnas 
    Japon[['latitude','longitude','depth','mag']]=Japon[['latitude','longitude','depth','mag']].round(1)

    # Ultimo dato de estados unidos
    df = pd.read_csv('https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&orderby=time')
    df = df.dropna(subset=['place'])
    df = df[['time', 'latitude', 'longitude', 'depth', 'mag', 'place']]
    estados = ['Alaska', 'California', 'Washington', 'Oregon']
    df = df[df['place'].str.contains('|'.join(estados), case=False)]
    df['localidad'] = df['place']
    df['country'] = 'ee.uu'
    df = df.drop(columns=['place'])
    eeuu = df.head(1)
    # Formato correcto a la columna de fechas
    eeuu['time'] = pd.to_datetime(eeuu['time']).dt.strftime('%Y-%m-%d %H:%M:%S')
    #Redondear las columnas 
    eeuu[['latitude','longitude','depth','mag']]=eeuu[['latitude','longitude','depth','mag']].round(1)
    

    # Ultimo dato de mexico
    df = pd.read_csv('https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&orderby=time')
    # Eliminar filas con valores nulos en la columna 'place'
    df = df.dropna(subset=['place'])
    # Filtrar los registros de México
    df_mexico = df[df['place'].str.contains('Mexico')]
    # Seleccionar las columnas deseadas
    df_mexico = df_mexico[['time', 'latitude', 'longitude', 'depth', 'mag', 'place']]
    df_mexico['localidad'] = df_mexico['place']
    df_mexico['country'] = 'mexico'
    df_mexico = df_mexico.drop(columns=['place'])
    mexico = df_mexico.head(1)
    # Formato correcto a la columna de fechas
    mexico['time'] = pd.to_datetime(mexico['time']).dt.strftime('%Y-%m-%d %H:%M:%S')
    #Redondear las columnas 
    mexico[['latitude','longitude','depth','mag']]=mexico[['latitude','longitude','depth','mag']].round(1)

    # Concatenar los tres conjuntos de datos
    df_combinado = pd.concat([Japon, eeuu, mexico], ignore_index=True)
    
    # Mostrar el mapa con los últimos 10 sismos
    st.subheader("Mapa de los últimos 10 sismos")
    mapa = folium.Map(location=[latitude, longitude], zoom_start=6)
    for idx, sismo in df_combinado.iterrows():
        folium.Marker(location=[sismo['latitude'], sismo['longitude']], popup=f"Magnitud: {sismo['mag']}\nFecha: {sismo['time']}").add_to(mapa)
    folium_static(mapa)

    # Mostrar la tabla con los detalles de los últimos 10 sismos
    st.subheader("Últimos 10 sismos")
    st.table(df_combinado[["time", "mag", "depth", "place"]].reset_index(drop=True))

# Configuracion de la pagina
st.set_page_config(page_title="QuakeAlert", page_icon="🌍", layout="wide")

# Crear la disposición en 3 columnas
col1, col2, col3 = st.columns([1, 2, 1])

# Columna 1: Mostrar el GIF
gif_path = "quake_alert..gif"
col1.image(gif_path,use_column_width=True)

# Columna 2: Mostrar el nombre de la página y opciones de sismos
col2.subheader("QuakeAlert")

# Columna 3: Mostrar el menú desplegable
st.sidebar.title("Menú desplegable")

# Opciones del menú desplegable
paginas = ["Inicio", "Últimos sismos"]
pagina_seleccionada = st.sidebar.radio("Selecciona una opción:", paginas)

# Contenido de la página seleccionada
if pagina_seleccionada == "Inicio":
    mostrar_inicio()
elif pagina_seleccionada == "Últimos sismos":
    ultimo_sismo()

# Separadores
st.markdown("---")




