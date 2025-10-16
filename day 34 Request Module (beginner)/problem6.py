#This is problem 6
"""
URL: https://restcountries.com/v3.1/name/{country}
Use: Get info about a country.
🧩 Project Idea:
Enter a country → show its capital, region, population, and currency.
"""
import requests

country = "pakistan"  # you can replace with any country name
url = f"https://restcountries.com/v3.1/name/{country}"

response = requests.get(url, timeout=5)
data = response.json()[0]
capital=data["capital"][0]
region=data["region"]
currency=list(data["currencies"].keys())[0]
print(capital)
print(region)
print(currency)