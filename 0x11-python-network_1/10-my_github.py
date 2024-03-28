#!/usr/bin/python3
"""
script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/user'
    user = argv[1]
    passwd = argv[2]
    r = requests.get(url, auth=HTTPBasicAuth(user, passwd))
    print(r.json().get('id'))
