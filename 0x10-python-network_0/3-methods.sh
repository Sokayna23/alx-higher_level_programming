#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server accepts.
curl -sI -X OPTIONS "$1" | awk -F ': ' '/Allow:/ { print $2 }'
