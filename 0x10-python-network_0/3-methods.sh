#!/bin/bash
# Bash script to display all HTTP methods the server will accept
curl -s -I -X OPTIONS $1 | grep -i "allow" | sed 's/allow: //I'
