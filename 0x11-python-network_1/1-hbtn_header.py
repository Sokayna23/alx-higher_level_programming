#!/usr/bin/python3
""" module """
from urllib import request
import sys


url = sys.argv[1]
if __name__ == "__main__":
    with request.urlopen(url) as response:
        headers = response.info()["X-Request-Id"]
        print(headers)
