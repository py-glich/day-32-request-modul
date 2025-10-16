#This is problem 2
"""
URL: https://api.open-meteo.com/v1/forecast?latitude=35&longitude=139&current_weather=true
Use: Get live weather data.
🧩 Project Idea:
Ask for a city name → fetch its latitude & longitude → show temperature & wind speed.
"""
import requests
# You can change this city name later
city = "Berlin"  

# Latitude & longitude for Berlin, Germany
latitude = 52.52
longitude = 13.41 
response=requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true")
data=response.json()
print(f"🌤 Current weather in {city}: {data['current_weather']['temperature']}°C")


