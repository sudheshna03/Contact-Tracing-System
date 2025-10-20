import folium
from folium.plugins import HeatMapWithTime

def create_heatmap(df):
    lat_long_list = []
    for i in range(1, 25):
        temp = []
        for _, instance in df[df['hour'] == i].iterrows():
            temp.append([instance['latitude'], instance['longitude']])
        lat_long_list.append(temp)
    
    m = folium.Map(location=[16.5062, 80.6480], zoom_start=11)
    HeatMapWithTime(lat_long_list, radius=15, auto_play=True).add_to(m)
    return m
