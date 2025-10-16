#This is problem 3
"""
Problem 3: Extract Specific Data

From the response of https://api.agify.io?name=john, print only the predicted age value.
"""
import requests
response=requests.get("https://api.agify.io?name=elsa")
data=response.json()
age=data["age"]
print("✅ JSON Response:")
print("Predicted Age:", age)
