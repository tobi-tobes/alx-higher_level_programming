#!/usr/bin/python3
"""
4-hbtn_status.py
This module contains a script that fetches
https://alx-intranet.hbtn.io/status
"""

import requests


if __name__ == "__main__":
    resp = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(resp.text))
    print("\t- content:", resp.text)
