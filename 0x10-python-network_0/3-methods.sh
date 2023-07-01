#!/bin/bash
# A script that takes in a URL and displays all HTTP
# methods the server will accept.

curl -sIX OPTIONS "$1" | grep "^Allowed:\s" | cut -c8-
