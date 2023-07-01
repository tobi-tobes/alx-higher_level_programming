#!/bin/bash
# A script that sends a request and displays only the status code of the response.
curl -o /dev/null -s -w "%{http_code}" "$1"
