#!/usr/bin/python3
"""
taking a URL, sending a request to the URL
and displaying the value of the X-Request-Id
in the header of the response.
"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.info().get('X-Request-Id'))
