# Copy of the JupyterLab code

# import pandas to read excel
import pandas as pd

#read CSV file data
officeLocations = pd.read_csv("CAOfficesComplete.csv")

#import Folium to create map 
import folium

#Sets the center of the map
loc_center = [officeLocations['Latitude'].mean(), officeLocations['Longitude'].mean()]

#Clear the previous version of map
mainMap = folium.Map()

#Create the Map
mainMap = folium.Map(
    location = loc_center,
    tiles = 'Openstreetmap',
    zoom_start = 6,
    min_zoom = 6,
    max_zoom = 19,
    control_scale=True
)

#Display the blank map
mainMap

#Loop to add data to map, 3 mile radius
for index, loc in officeLocations.iterrows():
    folium.Circle(
        [loc['Latitude'], loc['Longitude']],
        radius=4828,
        weight=2,
        color='#003f5c',
        fill=True,
        fill_color='#FFFF00'
    ).add_to(mainMap)

#Display the map with the data
mainMap

#Loop to add data to map, 2 mile radius
for index, loc in officeLocations.iterrows():
    folium.Circle(
        [loc['Latitude'], loc['Longitude']],
        radius=3219,
        weight=2,
        color='#003f5c',
        fill=True,
        fill_color='#FF0000'
    ).add_to(mainMap)

#Display the map with the data
mainMap

#Loop to add data to map, 1 mile radius
for index, loc in officeLocations.iterrows():
    folium.Circle(
        [loc['Latitude'], loc['Longitude']],
        radius=1609,
        weight=2,
        color='#003f5c',
        fill=True,
        fill_color='#00FF00',
        popup=loc['CSO']
    ).add_to(mainMap)

#Display the map with the data
mainMap

#Loop to add data to map, location marker
for index, loc in officeLocations.iterrows():
    folium.Circle(
        [loc['Latitude'], loc['Longitude']],
        radius=2,
        weight=2,
        color='#003f5c',
        fill=True,
        fill_color='#003f5c',
        popup=loc['CSO']
    ).add_to(mainMap)

#Display the map with the data
mainMap

#Export the map as an HTML file
mainMap.save('OfficeLocationsMap.html');









