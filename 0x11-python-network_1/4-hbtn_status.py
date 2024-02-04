#!/usr/bin/python3
""" Module: Fetche Url """
import requests


if __name__ == "__main__":
    req = requests.get("https://alx-intranet.hbtn.io/status")
    html = req.text
    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
