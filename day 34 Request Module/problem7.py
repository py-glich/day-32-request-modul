#This is problem 7
import requests

# You can change this city name later
city = "Berlin"  

# Latitude & longitude for Berlin, Germany
latitude = 52.52
longitude = 13.41  

# Open-Meteo API endpoint
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

# Send request
response = requests.get(url)
data = response.json()

# Display result
print(f"🌤 Current weather in {city}: {data['current_weather']['temperature']}°C")



