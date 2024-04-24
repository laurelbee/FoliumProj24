#import folium
import folium as f

# initialize map
#map = f.Map(location = [40.054671, -75.221652], zoom_start = 13)

##############################################################################

## stylize the map ##
# change scale and zoom levels

# change basemap tiles example
map = f.Map(location=[40.054671, -75.221652], tiles="OpenStreetMap", zoom_start= 13)

##############################################################################
## add data to map ##
# geoJSON file example
trails_file = ("C:/Users/tus97759/Desktop/GIS_Programming_ClassNotes/FoliumPractice/Wissahickon_Yellow_Trail_Loop.js")
f.GeoJson(trails_file).add_to(map)


##############################################################################
## add markers and popups ##
# adding markers 
#f.Marker([40.07817, -75.2278]).add_to(map)
#add popup
f.Marker([40.07817, -75.2278], "This is the trail Start/End").add_to(map) 

#custom icon

icon_image = ("C:/Users/tus97759/Desktop/Web_Mapping_GIS/Week12/pin.png")

icon = f.CustomIcon(icon_image,icon_size=(38, 40))

f.Marker(location=[40.07817, -75.2278], icon=icon, popup="Custom Icon").add_to(map)

#############################################################################


#save map as html file so we can view it
map.save('C:/Users/tus97759/Desktop/GIS_Programming_ClassNotes/FoliumPractice/mappractice.html')
