#!/usr/bin/python3
"""
7-error_code.py
This module contains a script that takes in a URL,
sends a request to the URL and displays the body of
the response.
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    resp = requests.get(url)
    if resp.status_code >= 400:
        print("Error code:", resp.status_code)
    else:
        print(resp.text)
