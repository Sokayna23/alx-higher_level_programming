#!/usr/bin/python3
""" Module:  Response header value """
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    x_request_id = req.headers.get("X-Request-Id")
    print(x_request_id)
