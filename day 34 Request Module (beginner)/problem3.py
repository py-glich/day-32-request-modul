#This is problem 3
"""
URL: "https://zenquotes.io/api/random"
Use: Get random motivational quotes.
🧩 Project Idea:
Build a “Daily Motivation” program that prints a new quote every morning.
"""
import requests

response = requests.get("https://zenquotes.io/api/random")
data = response.json()
print("💬 Quote:", data[0]['q'])
print("—", data[0]['a'])


