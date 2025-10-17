#This is problem 7
"""
URL: https://httpbin.org/post
Task:
Send your name and role in JSON format, with a custom header like {"App-Name": "MyFirstApp"}.
Then print what the server received in the headers and JSON.
"""
import requests
url = "https://httpbin.org/post"

# Data to send
data = {"name": "Maham", "role": "student"}

# Custom header
headers = {"App-Name": "MyFirstApp"}

# Send POST request with headers
response = requests.post(url, json=data, headers=headers)

# Convert response to JSON
result = response.json()

# Print what the server received
print("🧠 Server got this JSON:", result["json"])
print("📬 Server got this Header:", result["headers"])