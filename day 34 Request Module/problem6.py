#This is problem 6
"""
Problem 6: Custom Headers
Send a GET request to https://httpbin.org/headers with a custom header:
User-Agent: "MyPythonApp/1.0"
Print the response JSON to confirm the header was received.
"""
import requests
def Custom_Headers(url):
    try:
        # Step 1: Create a header dictionary
        headers = {"User-Agent": "MyPythonApp/1.0"}
        
        # Step 2: Send GET request with custom headers
        response = requests.get(url, headers=headers, timeout=5)
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
Custom_Headers("https://httpbin.org/headers")      

