#This is problem 1
"""
URL: https://catfact.ninja/fact
Use: Get random cat facts.
"""
import requests

response = requests.get("https://catfact.ninja/fact",params={'lenght':97})
data = response.json()
print("🐱 Cat Fact:", data["fact"])
