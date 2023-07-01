#!/usr/bin/python3
"""
6-post_email.py
This module contains a script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {"email": email}
    resp = requests.post(url, data=values)
    print(resp.text)
