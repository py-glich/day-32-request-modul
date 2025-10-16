#This is problem 7
"""
Goal: Show your location (country, city, region, etc.) based on your IP address.
API: https://ipinfo.io/json
No API key needed — fully free
🧠 Explanation
This API automatically detects your public IP.
It returns information like:
→ City
→ Region
→ Country
→ Location (latitude, longitude)
"""
import requests
response=requests.get("https://ipinfo.io/json")
data=response.json()
print(data['city'])
print(data['region'])
print(data['loc'])
user_input = input("Is that correct? (yes/no): ")
if user_input.lower() == "no":
    print("🗺️ Maybe you're using a VPN 😄")
else:
    print("✅ Got it!")