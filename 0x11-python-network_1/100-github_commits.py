#!/usr/bin/python3
"""
100-github_commits.py
This module contains a script that takes 2 arguments in order to
solve this challenge.
"""

import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits?per_page=10"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    response = requests.get(url, headers=headers)
    resp = response.json()
    for commit in resp:
        sha = commit.get("sha")
        author = commit.get("commit").get("author").get("name")
        print(f"{sha}: {author}")
