#import folium
import folium as f

# initialize map
map = f.Map(location = [40.054671, -75.221652], zoom_start = 13)

#add geoJSON data to map
trails_file = ("C:/Users/tus97759/Desktop/GIS_Programming_ClassNotes/FoliumPractice/Wissahickon_Yellow_Trail_Loop.js")
f.GeoJson(trails_file).add_to(map)

#save map as html file so we can view it
map.save('C:/Users/tus97759/Desktop/GIS_Programming_ClassNotes/FoliumPractice/mappractice.html')
