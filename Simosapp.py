import streamlit as st
import folium

# Obtener parámetros de la URL
result = st.experimental_get_query_params()

country = result['val'][0]
latitude = result['val'][1]
longitude = result['val'][2]
depth = result['val'][3]
mag = result['val'][4]
sistype = result['val'][5]
date = result['val'][6]

# Create the app
app = st.empty()

# Add the title
app.title('Earthquake App')

# Add the country
app.write('Country:', country)

# Add the latitude and longitude
app.write('Latitude:', latitude)
app.write('Longitude:', length)

# Add the depth
app.write('Depth:', depth)

# Add the magnitude
mag_level = random.randint(1, 9)
if mag_level <= 4:
    color = 'green'
elif mag_level <= 6:
    color = 'orange'
else:
    color = 'red'
app.write('Magnitude:', mag, f' ({color})')

# Add the type
app.write('Type:', typosis)

# Add the date
app.write('Date:', date)

# Add the Richter scale images
st.image('ritcher.jpg', color=color)
st.image('ritcher.jpg', color=color)

# Add the recommendations
st.write('Recommendations:')
st.write('* Stay away from buildings or structures that could collapse.')
st.write('* Stay indoors if you are in a building.')
st.write('* If you are outdoors, find a low-lying area and lie down.')

# Add a map of the epicenter
app.map(latitude, length)

# Add a news feed
st.write('Latest Earthquakes:')
for earthquake in earthquakes:
    mag_level = random.randint(1, 9)
    if mag_level <= 4:
        color = 'green'
    elif mag_level <= 6:
        color = 'orange'
    else:
        color = 'red'
    st.write(earthquake['country'], f' ({mag}, {color})')

# Show the app
app.show()



