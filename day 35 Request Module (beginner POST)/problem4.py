#This is problem 4
"""
URL: https://jsonplaceholder.typicode.com/posts
Task: Send:
{"player": "Maham", "score": 98}
Print the returned post ID.
"""
import requests
data={"player": "Maham", "score": 98}
# 2️⃣ Send POST request to create a new user
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data).json()
print(response)