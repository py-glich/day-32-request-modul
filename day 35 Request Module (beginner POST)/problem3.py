#This is problem 3
"""
URL: https://reqres.in/api/users
Task: Send:
{"name": "Maham", "job": "developer"}
Print the user’s ID from the response.
"""
import requests

# 1️⃣ Data you want to send to the server
data = {"name": "Maham", "job": "developer"}

# 2️⃣ Send POST request to create a new user
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data).json()

# 3️⃣ Print what the server sent back
print(response)
