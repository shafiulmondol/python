import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium

def trace_phone_number(number):
    # Parse the phone number
    parsed_number = phonenumbers.parse(number)
    
    # Get location (country/city) information
    location = geocoder.description_for_number(parsed_number, "en")
    print("Location:", location)
    
    # Get carrier information
    service_provider = carrier.name_for_number(parsed_number, "en")
    print("Carrier:", service_provider)
    
    # Geocode the location to get latitude and longitude
    key = 'YOUR_OPENCAGE_API_KEY'
    open_cage_geocoder = OpenCageGeocode(key)
    query = str(location)
    results = open_cage_geocoder.geocode(query)
    
    if results and len(results) > 0:
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        print("Latitude:", lat, "Longitude:", lng)
        
        # Create a map with a marker
        mymap = folium.Map(location=[lat, lng], zoom_start=9)
        folium.Marker([lat, lng], popup=location).add_to(mymap)
        
        # Save the map as an HTML file
        map_file = "phone_location.html"
        mymap.save(map_file)
        print(f"Map saved to {map_file}")
    else:
        print("Could not geocode the location.")

# Example usage
trace_phone_number("+8801978308414")  # Replace with the actual phone number
