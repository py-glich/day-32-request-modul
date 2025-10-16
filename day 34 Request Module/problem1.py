#This is problem 1
"""
Problem 1: Basic GET Request
Write a program that sends a GET request to https://api.github.com and prints the status code.
"""
import requests

def basic_get_request():
    url = "https://api.github.com"
    try:
        response = requests.get(url, timeout=5)  # timeout after 5 seconds

        print("✅ Request successful!")
        print("Status Code:", response.status_code)

    except Exception as e:
        print("⚠️ Something went wrong:", e)

    except requests.exceptions.Timeout:
        print("⏰ Request timed out! The server took too long to respond.")

    except requests.exceptions.ConnectionError:
        print("🌐 Connection error! Please check your internet connection.")

    except requests.exceptions.HTTPError as e:
        print("🚫 HTTP Error:", e)


# Run the function
basic_get_request()
