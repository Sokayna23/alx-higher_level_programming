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
        print("Error code:", err.response.status_code)
