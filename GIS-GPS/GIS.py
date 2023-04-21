import numpy as np
import folium
import geopandas as gpd
import json
from shapely.geometry import Point
import math


def haversine(lat_self, lon_self, lat_round,lon_round):
    lon_self,lat_self , lon_round,lat_round = map(math.radians, [lon_self,lat_self , lon_round,lat_round])
    dlon = lon_round - lon_self
    dlat = lat_round - lat_self
    a = math.sin(dlat/2)**2 + math.cos(lat_self) * math.cos(lat_round) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371
    x = c * r *1000 #公尺
    return x

def create_store_point(lats,lons):
    lats_vect = np.array(lats)
    lons_vect = np.array(lons)
    lons_lats_vect = np.column_stack((lats_vect,  lons_vect))
    return lons_lats_vect

def create_self_point(lat,lon):
    new_point = Point(zip(lat,lon))
    new_geojson = json.loads(new_point.to_json())
    return new_geojson

def create_map(lat_self,lon_self,news_stores_points):
    # lat 緯度 lng/lon 經度
    m = folium.Map(
        location=[lat_self,lon_self],
        max_zoom=20,
        zoom_start=18,
        tiles="OpenStreetMap"
    )

    sums = 0
    no_sums = 0
    for station_point in news_stores_points:
        x = haversine(lat_self,lon_self,station_point[0],station_point[1])
        print( f'離第{sums+no_sums+1}圓心{x:.2f}公尺' )
        if x < 35:
            sums+=1
        else:
            no_sums+=1
        folium.Circle(
        radius=35,
        location=[station_point[0],station_point[1]],
        popup='店家',
        fill_color='red',
        fill_opacity=0.5,
        color="#555",
        weight=1
        ).add_to(m)
    print(f'踩到{sums}個點,還有{no_sums}個點沒踩!')
    

    folium.Marker(
        radius=1,
        location=[lat_self,lon_self],
        popup='自己',
        fill_color='blue',
        fill_opacity=0.5,
        color="#555",
        weight=1
        ).add_to(m)
    m.save('try-2.html')


new_store_point = create_store_point(
    [25.00171,25.01084,25.02602,25.02512,24.99032], 
    [121.45497,121.45823,121.47228,121.46318,121.43123]  
    )
create_map(25.001766093224507,121.45485940085867,new_store_point)
# create_map(25.079221282618455,121.48338856186713,new_store_point)