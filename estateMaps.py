import json
import folium
import urllib

def getGeoForAddress(addr):
    addressUrl = "http://maps.googleapis.com/maps/api/geocode/json?address=" + addr
    addressUrlQuote = urllib.parse.quote(addressUrl, ':?=/')  
    response = urllib.request.urlopen(addressUrlQuote).read().decode('utf-8')  
    responseJson = json.loads(response)
    #print(responseJson)
    if (responseJson["status"] == "OK") :
        lat = responseJson.get('results')[0]['geometry']['location']['lat']  
        lng = responseJson.get('results')[0]['geometry']['location']['lng']
        return [lat, lng]
    else:
        return

with open('houses.json', 'r', encoding='utf-8') as file:
    house_list = json.load(file)

map = folium.Map(location=[25.0666907,121.5531035], zoom_start=12)
taipeiEstate = folium.FeatureGroup(name='house')
for item in house_list:
    print(item['address'])
    coordinate = getGeoForAddress(item['address'])
    print(coordinate)
    taipeiEstate.add_child(folium.CircleMarker(location=[coordinate[0],coordinate[1]], 
    popup=item['houseName'] + ' ' + item['averPrice'] + ' ' + item['address'], fill_color='red', 
    color='grey',fill_opacity=0.7, radius=10))

map.add_child(taipeiEstate)
map.save('TaipeiEstate.html')