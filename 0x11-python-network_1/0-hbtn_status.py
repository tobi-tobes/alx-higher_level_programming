#!/usr/bin/python3
"""
0-hbtn_status.py
This module contains a script that fetches
https://alx-intranet.hbtn.io/status
"""

import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
    html = resp.read()
    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
    print("\t- utf8 content:", html.decode("UTF-8"))
