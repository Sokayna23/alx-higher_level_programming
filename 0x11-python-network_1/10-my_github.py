#!/usr/bin/python3
""" module: My GitHub ID """
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/users/" + username

    data = {"Authorization": "token {}".format(password)}

    resp = requests.get(url, headers=data)
    print(resp.json().get("id"))
