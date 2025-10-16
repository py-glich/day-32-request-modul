#This is problem 4
"""
URL: https://api.adviceslip.com/advice
Use: Get random life advice.
🧩 Project Idea:
Make a “Life Advice Generator” that prints one piece of advice each time you run it.
"""
import requests
response=requests.get("https://api.adviceslip.com/advice/66")
data=response.json()
slip={'id':66}
print("💡 Advice:", data["slip"]["advice"])
