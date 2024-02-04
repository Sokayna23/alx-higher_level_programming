#!/usr/bin/python3
""" module: Error code """
import requests
import sys


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        if err.response.status_code >= 400:
            print("Error code:", err.response.status_code)
        elif err.response.status_code == 200:
            print(response.text)
