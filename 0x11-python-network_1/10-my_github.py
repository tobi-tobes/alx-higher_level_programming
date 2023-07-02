#!/usr/bin/python3
"""
10-my_github.py
This module contains a script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    pwd = sys.argv[2]
    url = f"https://api.github.com/{user}"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"token {pwd}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    response = requests.get(url, headers=headers)
    resp_id = response.json().get("id")
    print(resp_id)
