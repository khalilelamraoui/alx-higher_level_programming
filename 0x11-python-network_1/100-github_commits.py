#!/usr/bin/python3
"""
script that takes 2 arguments in order to solve this challenge.
"""
import requests
import sys

if __name__ == '__main__':
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1])
    r = requests.get(url)
    for i in r.json()[:10]:
        sha = i.get('sha')
        commit = i.get('commit')
        author = commit.get('author')
        print("{}: {}".format(sha, author.get('name')))
