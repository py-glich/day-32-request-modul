#This is problem 4
"""
Problem 4: Handle Request Errors
Write a function fetch_url(url) that makes a GET request and handles exceptions like:
ConnectionError
Timeout
HTTPError
Use a try-except block.
"""

import requests

def fetch_url(url):
    try:
        response = requests.get(url, timeout=5)

        repos = response.json()      # get JSON data

        print("\n✅ py-glich's Public Repositories:")
        if not repos:
            print("No public repositories found.")
        else:
            for repo in repos:
                print("-", repo["name"])


    except requests.exceptions.Timeout:
        print("⏰ Request timed out! The server took too long to respond.")

    except requests.exceptions.ConnectionError:
        print("🌐 Connection error! Please check your internet connection.")

    except requests.exceptions.HTTPError as e:
        print("🚫 HTTP Error:", e)

    except Exception as e:
        print("⚠️ Something went wrong:", e)


# ✅ Use GitHub API URL, not the normal GitHub link
fetch_url("https://api.github.com/users/py-glich/repos")
