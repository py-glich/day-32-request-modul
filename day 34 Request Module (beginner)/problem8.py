#This is problem 8
"""
Goal: Convert money between currencies (like USD → PKR, EUR → INR).
API: https://api.exchangerate.host/convert
🧠 Explanation
You pass two parameters:
from → base currency (e.g., USD)
to → target currency (e.g., PKR)
API gives you the conversion rate and result.
"""
import requests
input_value=int(input("enter any number:"))
convert=(input("enter any country currency:"))
url = "https://open.er-api.com/v6/latest/USD"
data = requests.get(url).json()
conversion=data["rates"][f"{convert}"]
print(conversion*input_value)
