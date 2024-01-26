#!/bin/bash
# cURL only methods
curl -sI -X OPTIONS "$1" | awk '{ print $2 }'
