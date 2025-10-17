#This is problem 1
"""
URL: https://httpbin.org/post
Task: Send your name in JSON and print what the server received.
"""
import requests

# Step 1: Website (API) link
url = "https://httpbin.org/post"

# Step 2: Data to send
data = {"name": "Maham"}

# Step 3: Send POST request
response = requests.post(url, json=data)

# Step 4: Convert response to JSON
result = response.json()

# Step 5: Print what the server received
print("Server received this JSON data:")
print(result["json"])

