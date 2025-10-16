#This is problem 8
import requests

websites = ["https://google.com", "https://facebook.com", "https://no-site-found123.com"]

for site in websites:
    try:
        r = requests.get(site, timeout=3)
        print(site, "✅ Online" if r.status_code == 200 else "⚠️ Problem:", r.status_code)
    except:
        print(site, "❌ Not reachable")

