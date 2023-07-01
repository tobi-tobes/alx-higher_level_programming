#!/bin/bash
# A script that takes in a URL and displays the methods the server will accept.
curl -sIX OPTIONS "$1" | grep "^Allow:\s" | cut -c8-
