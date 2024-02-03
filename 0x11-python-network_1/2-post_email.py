#!/usr/bin/python3
""" Module that POST an email """
from urllib import request, parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = parse.urlencode({'email': email}).encode('utf-8')
    req = request.Request(url, data=data, method='POST')
    with request.urlopen(url) as response:
        print(response.read().decode('utf-8'))
