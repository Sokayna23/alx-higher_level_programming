#!/usr/bin/python3
""" Module Error code """
from urllib import request, error
import sys


if __name__== "__main__":
    url = sys.argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            pass
    except error.HTTPError as e:
        print("Error code:", e.code)
   
