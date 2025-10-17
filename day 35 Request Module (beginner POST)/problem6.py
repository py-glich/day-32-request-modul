#This is problem 6
"""
📍 Example: You log in to Instagram or Gmail.
🧠 What happens:
When you click “Login”, your email and password are sent to the server using a POST request.
The server checks if your info is correct and sends back a token or cookie to keep you logged in.
requests.post("https://example.com/login", json={"email": "you@email.com", "password": "1234"})
Real-world issue:
If data isn’t encrypted (no HTTPS), passwords can be stolen.
Wrong credentials → 401 Unauthorized error.
"""
import requests

url = "https://reqres.in/api/login"
data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}

resp = requests.post(url, json=data)
print(resp.json())  # -> {'token': 'QpwL5tke4Pnpja7X4'}
