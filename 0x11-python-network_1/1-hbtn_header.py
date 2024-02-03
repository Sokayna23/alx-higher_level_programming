#!/usr/bin/python3
"""Response header value #0"""
import sys
from urllib import request


url = sys.argv[1]
if __name__ == "__main__":
    with request.urlopen(url) as response:
        headers = response.info()["X-Request-Id"]
        print(headers)
