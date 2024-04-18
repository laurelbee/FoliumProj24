#GeoJSON
m_geo = folium.Map([40.064246415012484, -75.2223008537331], zoom_start=14, tiles="cartodbpositron")

folium.Marker([40.07817, -75.2278], "Start/End").add_to(m_geo)

geojson_data = "C:/folium/wiss_trail.js"

folium.GeoJson(geojson_data, name="goejson_example").add_to(m_geo)

folium.LayerControl().add_to(m_geo)

m_geo.save("C:/folium/geojson_example3.html")