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
    mapa = folium.Map(location=[latitude, longitude], zoom_start=5)
    
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
        # Profundidad mínima y máxima en tus datos
        profundidad_minima = 0
        profundidad_maxima = 300

        # Calcular la profundidad relativa en el rango de 0 a 100
        profundidad_relativa = (depth - profundidad_minima) / (profundidad_maxima - profundidad_minima) * 100

        # Asegurarse de que la profundidad relativa esté dentro del rango de 0 a 100
        profundidad_relativa = max(0, min(100, profundidad_relativa))

        # Mostrar la barra de progreso con la profundidad relativa
        st.progress(int(profundidad_relativa))
        
        st.write(f"📅 **Tipo de sismo:** {sistype}")
        st.write(f"⏰ **Fecha:** {fecha}")
    
    # Mostrar el mapa y los detalles
    col1, col2 = st.columns(2)
    with col1:
        show_details()
        
    with col2:
        show_details2()

    # Mostrar imágenes según el tipo de sismo
    if sistype == "leve":
        st.image("leve.jpeg", use_column_width=True)
    elif sistype == "medio":
        st.image("medio.jpeg", use_column_width=True)
    elif sistype == "alto":
        st.image("alto.jpeg", use_column_width=True)
    
    st.title("Círculos como Botones en Streamlit")

    # Carga de la imagen que contiene los círculos
    image_path = "alto.jpeg"
    image = Image.open(image_path)

    # Coordenadas de los círculos (cada círculo está definido por su posición x, y y radio r)
    circles = [(100, 200, 30), (300, 150, 50), (400, 300, 40)]

    # Mostrar la imagen
    st.image(image, caption="Imagen con círculos", use_column_width=True)

    # Obtener el tamaño original de la imagen
    width, height = image.size

    # Obtener el tamaño de la imagen en el visor de Streamlit
    image_width = st.image(image, caption="Imagen con círculos", use_column_width=True).beta_get_query_params()['width']

    # Calcular la escala para ajustar las coordenadas de los círculos al tamaño de la imagen en el visor
    scale = image_width / width

    # Posicionar los botones en cada círculo
    for i, circle in enumerate(circles):
        circle_x, circle_y, circle_radius = circle
        button_x = circle_x * scale
        button_y = circle_y * scale
        # Si el botón del círculo es presionado, muestra una imagen ampliada o explicación
        if st.button("", key=f"boton_{i}", help="Círculo interactivo", 
                    style=f"position:absolute;top:{button_y}px;left:{button_x}px;"):
            # Aquí puedes cargar y mostrar la imagen ampliada o la explicación para el círculo
            # Ejemplo:
            st.image("alto.jpeg")
            st.write(f"Explicación del contenido dentro del círculo en la posición (x={circle_x}, y={circle_y})")


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
    question4 = st.slider("¿En una escala del 1 al 10, qué tan fuerte percibiste el sismo?", 1, 10)
                          
    if st.button("Enviar encuesta"):
        # Guardar las respuestas de la encuesta en la lista de respuestas de encuestas
        st.session_state.survey_responses.append({
            "Pregunta 1": question1,
            "Pregunta 2": question2,
            "Pregunta 3": question3,
            "Pregunta 4": question4
        })
    
    st.subheader("Respuestas de Encuesta Guardadas")
    for response in st.session_state.survey_responses:
        st.write(response)

def ultimo_sismo():
    r = requests.get("https://www.jma.go.jp/bosai/quake/data/list.json")
    data = json.loads(r.text)
    first_5_quakes = data[:5]
    
    quake_list = []
    
    for r in first_5_quakes:
        if 'cod' in r:
            vars = r['cod'][1:]
            vars = vars.replace('+', ',')
            vars = vars.replace('-', ',')
            vars = vars.replace('/', '')
            vars = vars.split(',')

            if len(vars) >= 3:
                lat = vars[0]
                lon = vars[1]
                dept = vars[2]
                quake = {'time': r['at'], 'latitude': lat, 'longitude': lon, 'depth': dept, 'mag': r['mag'], 'localidad': r['en_anm'], 'country': 'japon'}
                quake_list.append(quake)
    
    Japon = pd.DataFrame(quake_list)
    Japon['depth'] = Japon['depth'].astype('float64')
    Japon['depth'] = (Japon['depth'] / 1000)
    Japon['time'] = pd.to_datetime(Japon['time']).dt.strftime('%Y-%m-%d %H:%M:%S')
    Japon[['latitude', 'longitude', 'depth', 'mag']] = Japon[['latitude', 'longitude', 'depth', 'mag']].round(1)

    # Ultimo dato de estados unidos
    df = pd.read_csv('https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&orderby=time')
    df = df.dropna(subset=['place'])
    df = df[['time', 'latitude', 'longitude', 'depth', 'mag', 'place']]
    estados = ['Alaska', 'California', 'Washington', 'Oregon']
    df = df[df['place'].str.contains('|'.join(estados), case=False)]
    df['localidad'] = df['place']
    df['country'] = 'ee.uu'
    df = df.drop(columns=['place'])
    eeuu = df.head(5)
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
    mexico = df_mexico.head(5)
    # Formato correcto a la columna de fechas
    mexico['time'] = pd.to_datetime(mexico['time']).dt.strftime('%Y-%m-%d %H:%M:%S')
    #Redondear las columnas 
    mexico[['latitude','longitude','depth','mag']]=mexico[['latitude','longitude','depth','mag']].round(1)

    # Concatenar los tres conjuntos de datos
    df_combinado = pd.concat([Japon, eeuu, mexico], ignore_index=True)
    
    # Mostrar el mapa con los últimos 15 sismos
    st.subheader("Mapa de los últimos 15 sismos")
    mapa = folium.Map(location=[latitude, longitude], zoom_start=1)
    for idx, sismo in df_combinado.iterrows():
        folium.Marker(location=[sismo['latitude'], sismo['longitude']], popup=f"Magnitud: {sismo['mag']}\nFecha: {sismo['time']}").add_to(mapa)
    folium_static(mapa)
   
    # Establecer un índice personalizado para la tabla para resaltar el sismo más reciente
    df_combinado.index = range(1, len(df_combinado) + 1)
    
    # Renombrar las columnas al español
    df_combinado = df_combinado.rename(columns={
    "time": "Fecha y Hora",
    "country": "País",
    "longitude": "Longitud",
    "latitude": "Latitud",
    "mag": "Magnitud",
    "depth": "Profundidad"
    })
    
    # Mostrar la tabla con los detalles de los últimos 15 sismos en español
    st.subheader("Últimos 15 sismos")
    st.dataframe(df_combinado[["Fecha y Hora", "País", "Longitud", "Latitud", "Magnitud", "Profundidad"]].reset_index(drop=True))
    
    # Convertir la columna de magnitud a valores numéricos
    df_combinado['Magnitud'] = df_combinado['Magnitud'].astype(float)
    df_combinado['Latitud'] = df_combinado['Latitud'].astype(float)
    df_combinado['Longitud'] = df_combinado['Longitud'].astype(float)
    df_combinado['Profundidad'] = df_combinado['Profundidad'].astype(float)

    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(9, 5))
    plt.plot(df_combinado['País'].astype(str), df_combinado['Magnitud'], marker='o', linestyle='-', color='b')
    plt.xlabel('País')
    plt.ylabel('Magnitud del Sismo')
    plt.title('Magnitud de los últimos 15 sismos por país')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Mostrar el gráfico en Streamlit
    st.pyplot(plt)

# Configuracion de la pagina
st.set_page_config(page_title="QuakeAlert", page_icon="🌍", layout="wide")

# Crear la disposición en 3 columnas
col1, col2, col3 = st.columns([1, 1, 2])

# Columna 1: Mostrar el GIF
gif_path = "quake_alert..gif"
col1.image(gif_path,use_column_width=True)

# Columna 3: Mostrar el nombre de la página y opciones de sismos
col3.title("QuakeAlert")
col3.subheader("¡Recibe alertas de sismos en tiempo real!")

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





