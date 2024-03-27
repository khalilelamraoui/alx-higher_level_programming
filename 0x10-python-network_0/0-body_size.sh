#!/bin/bash
# request to a URL and display the size of the body's response
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}'
