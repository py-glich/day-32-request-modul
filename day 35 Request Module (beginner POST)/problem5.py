#This is problem 5
"""
URL: https://httpbin.org/post
Task: Send name, email, and message.
Print only the "form" part from the JSON response.
"""
import requests
data = {
    "name": "Maham",
    "email": "maham@example.com",
    "message": "Hello, this is my contact form!"
}
# 2️⃣ Send POST request to create a new user
response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data).json()
print(response)