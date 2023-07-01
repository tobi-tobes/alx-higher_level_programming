#!/usr/bin/python3
"""
3-error_code.py
This module contains a script that takes in a URL,
sends a request to the URL and displays the body of
the response (decoded in utf-8).
"""

import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as resp:
            response = resp.read().decode("UTF-8")
            print(response)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
