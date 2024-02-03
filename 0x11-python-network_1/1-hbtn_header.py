#!/usr/bin/python3
""" module """
from urllib import request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as response:
        headers = response.info()["X-Request-Id"]
        print(headers)
