#!/usr/bin/python3
"""Response header value #0"""
import sys
from urllib import request


url = sys.argv[1]
if __name__ == "__main__" and len(sys.argv) == 2:
    with request.urlopen(url) as response:
        headers = response.info()
        id = headers.get('X-Request-Id')
        print(id)
