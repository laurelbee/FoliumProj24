#import folium
import folium as f

# initialize map
#map = f.Map(location = [40.054671, -75.221652], zoom_start = 13)

##############################################################################

## stylize the map ##
# change scale and zoom levels

# change basemap tiles example
f.Map(location=[40.054671, -75.221652], tiles="Cartodb dark_matter", zoom_start= 13)

##############################################################################
## add data to map ##
# geoJSON file example
trails_file = ("C:/Users/tus97759/Desktop/GIS_Programming_ClassNotes/FoliumPractice/Wissahickon_Yellow_Trail_Loop.js")
f.GeoJson(trails_file).add_to(map)

##############################################################################
## add markers and popups ##
# adding markers 
f.Marker([40.07817, -75.2278]).add_to(map)

# adding popups
f.Marker([40.07817, -75.2278], "Start/End").add_to(map)

#save map as html file so we can view it
map.save('C:/Users/tus97759/Desktop/GIS_Programming_ClassNotes/FoliumPractice/mappractice.html')
