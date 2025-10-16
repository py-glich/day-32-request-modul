#This is problem 2
"""
Problem 2: JSON Response Handling
Send a GET request to https://api.agify.io?name=john and print the JSON response.
"""
import requests
response=requests.get("https://api.agify.io?name=elsa")
data=response.json()
print("✅ JSON Response:")
print(data)