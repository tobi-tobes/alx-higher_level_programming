#!/usr/bin/python3
"""
2-post_email.py
This module contains a script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {"email": email}
    data = urllib.parse.urlencode(values)
    data = data.encode()
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as resp:
        response = resp.read().decode("UTF-8")
        print(response)
