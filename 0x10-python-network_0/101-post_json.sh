#!/bin/bash
# A script that sends a JSON POST request and displays the body of the response.
curl -sH 'Content-Type: Application/json' -d@"$2" "$1"
