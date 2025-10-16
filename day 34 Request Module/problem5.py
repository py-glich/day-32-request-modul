#This is problem 5
"""
Problem 5: Send POST Request
Send a POST request to https://httpbin.org/post with the data:
{"username": "admin", "password": "1234"}
and print the JSON response.
"""
import requests

def fetch(url):
    try:
        # Step 1: Create data to send
        payload = {"username": "admin", "password": "1234"}
        
        # Step 2: Send POST request (not GET)
        response = requests.post(url, data=payload, timeout=5)
        
        # Step 3: Convert response to JSON
        data = response.json()
        
        # Step 4: Print the response
        print("✅ JSON Response:")
        print(data)

    except requests.exceptions.Timeout:
        print("⏰ Request timed out! The server took too long to respond.")

    except requests.exceptions.ConnectionError:
        print("🌐 Connection error! Please check your internet connection.")

    except requests.exceptions.HTTPError as e:
        print("🚫 HTTP Error:", e)

    except Exception as e:
        print("⚠️ Something went wrong:", e)

# Call function
fetch("https://httpbin.org/post")

