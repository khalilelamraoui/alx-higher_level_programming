#!/bin/bash
# request to a URL that causes the server to respond with a message containing You got me!
curl -sLX PUT -H "Origin:School" -d "user_id=98" "0.0.0.0:5000/catch_me"
