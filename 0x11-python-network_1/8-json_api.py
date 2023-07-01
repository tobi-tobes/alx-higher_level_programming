#!/usr/bin/python3
"""
8-json_api.py
This module contains a script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        if len(sys.argv) > 1:
            print("No result")
            sys.exit(1)
        q = sys.argv[1]
    values = {"q": q}
    resp = requests.post("http://0.0.0.0:5000/search_user", data=values)
    try:
        resp_dict = resp.json()
        if len(resp_dict) == 0 or resp.status_code >= 400:
            print("No result")
        else:
            resp_id = resp_dict.get("id")
            resp_name = resp_dict.get("name")
            print(f"[{resp_id}] {resp_name}")
    except requests.exceptions.JSONDecodeError as e:
        print("Not a valid JSON")
