#!/usr/bin/python3
""" module: My GitHub! """
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/users/" + username
    data = {"Authorization": password}
    response = requests.get(url, headers=data)
    json = response.json()
    if (response.status_code >= 400):
        print("None")
        exit()
    print(json.get("id"))
