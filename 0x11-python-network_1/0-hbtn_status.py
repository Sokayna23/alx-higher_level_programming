#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
from urllib import request


url = "https://alx-intranet.hbtn.io/status"

with request.urlopen(url) as response:
    html = response.read()
    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
    print("\t- utf8 content:", html.decode('utf-8'))
