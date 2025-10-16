#This is problem 5
"""
URL: https://dog.ceo/api/breeds/image/random
Use: Get random dog image URLs.
🧩 Project Idea:
Create a Random Dog Viewer that prints a dog image URL (you can show it in browser too).
"""
import requests
import webbrowser
response = requests.get("https://dog.ceo/api/breeds/image/random")
data = response.json()
webbrowser.open(data["message"])