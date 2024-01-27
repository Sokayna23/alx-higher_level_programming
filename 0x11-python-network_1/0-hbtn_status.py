#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
   content = response.read().decode('utf-8')

print("Body response:")
print("\t- type:", type(content))
print("\t- utf8 content:", content)
