import streamlit as st
import folium
import tkinter as tk

# Obtener parámetros de la URL
result = st.experimental_get_query_params()

country = result['val'][0]
latitude = float(result['val'][1])
longitude = float(result['val'][2])
depth = result['val'][3]
mag = float(result['val'][4])
sistype = result['val'][5]
date = result['val'][6]

# Crear la ventana de la aplicación
app = tk.Tk()
app.title("Quake Alert")
app.geometry("400x300")
app.configure(bg="orange")

# Crear el título de la aplicación
title_label = tk.Label(app, text="Quake Alert", font=("Helvetica", 20, "bold"), bg="orange")
title_label.pack(pady=10)

# Crear el separador
separator = tk.Frame(app, height=2, bd=1, relief="sunken", bg="black")
separator.pack(fill="x", padx=10)

# Crear el mapa o la información del sismo
earthquake_info_label = tk.Label(app, text=f"Latest Earthquake in {country}\nMagnitude: {mag}\nDepth: {depth}\nType: {sistype}\nDate: {date}", font=("Helvetica", 12), bg="orange")
earthquake_info_label.pack(pady=10)

# Puedes agregar aquí el código para mostrar un mapa con la ubicación del sismo utilizando librerías adicionales.

app.mainloop()




