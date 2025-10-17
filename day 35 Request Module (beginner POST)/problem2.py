#This is problem 2
"""
URL: https://reqres.in/api/login
Task: Send:
{"email": "eve.holt@reqres.in", "password": "cityslicka"}
Print the token you get from the response.
"""
import requests

url = "https://httpbin.org/post"
data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}

response = requests.post(url, json=data).json()
print(response["json"]["email"])
print(response["json"]["password"])