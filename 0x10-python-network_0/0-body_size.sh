#!/bin/bash
# A script that displays the size of the body of the response
curl -sI "$1" | grep "^Content-Length:\s" | cut -c17-
