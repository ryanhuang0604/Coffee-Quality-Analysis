import pandas as pd
import folium
from folium.plugins import MarkerCluster

data = pd.read_csv("./arabica_data_new add variable.csv")
data.dataframeName = "arabica_data.csv"

world_map= folium.Map(tiles="cartodbpositron")
marker_cluster = MarkerCluster().add_to(world_map)

for i in range(len(data)):
        lat = data.iloc[i]['latitude']
        long = data.iloc[i]['longitude']
        radius=5
        popup_text = """Country : {}<br>
                    Total Cup Points : {}<br>"""
        popup_text = popup_text.format(data.iloc[i]['Country.of.Origin'],
                                   data.iloc[i]['Total.Cup.Points']
                                   )
        folium.CircleMarker(location = [lat, long], radius=radius, popup= popup_text, fill =True).add_to(marker_cluster)

world_map.save("coffee_map.html")