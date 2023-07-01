#!/usr/bin/python3
"""
0-hbtn_status.py
This module contains a script that fetches
https://alx-intranet.hbtn.io/status
"""

import urllib.request
import sys


url = sys.argv[1]
with urllib.request.urlopen(url) as resp:
    header_id = resp.getheader('X-Request-Id')
    print(header_id)
