import phonenumbers
import opencage
import folium

from phone import number

from phonenumbers import geocoder
pepnumber=phonenumbers.parse(number)
location=geocoder.description_for_number(pepnumber,"en")
print(location)

from phonenumbers import carrier
service_pro=phonenumbers.parse(number)
print(carrier.name_for_number(service_pro,"en"))

from opencage.geocoder import OpenCageGeocode
key='3836c003753140ac82b5e021635e26a0'

geocoder=OpenCageGeocode(key)
query=str(location)
result=geocoder.geocode(query)

print(result)
lat=result[0]['geometry']['lat']
lng=result[0]['geometry']['lng']
print(lat,lng)

my_map=folium.Map(location=[lat,lng],zoom_start= 9)
folium.Marker([lat,lng],popup=location).add_to(my_map)

my_map.save("mylocation.html")