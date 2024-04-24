#import folium
import folium as f

# initialize map
#Wissahickon Trail Lat Long: [40.054671, -75.221652]
map = f.Map(location = [40.054671, -75.221652], zoom_start = 13)

##############################################################################

## stylize the map ##
# change scale and zoom levels

# change basemap tiles

##############################################################################
## add data to map ##
# geoJSON file example
trails_file = ('your file path')
f.GeoJson(trails_file).add_to(map)


##############################################################################
## add markers and popups ##
# adding markers 
f.Marker([40.07817, -75.2278]).add_to(map)
#add a popup to your marker

# adding marker with a custom icon
# create a variable for your icon file path
icon_image = ('your file path')
# create a variable for your icon
icon = f.CustomIcon(icon_image,icon_size=(38, 40))
# creating the custom icon marker
f.Marker(location=[40.07817, -75.2278], icon=icon, popup="This is the trail start and end.").add_to(map)

#############################################################################


#save map as html file so we can view it
map.save('your file path / yourmapname.html')