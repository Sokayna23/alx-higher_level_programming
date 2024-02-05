#!/usr/bin/python3
""" Interview: list commits """
import requests
import sys


if __name__ == "__main__":
    REPO = sys.argv[1]
    OWNER = sys.argv[2]
    count = 10
    url = f"https://api.github.com/repos/{OWNER}/{REPO}\
            /commits?per_page={count}"
    params = {"author": OWNER, "per_page": count}

    response = requests.get(url, params=params)
    commits = response.json()
    for commit in commits:
        name = commit.get("commit").get("author").get("name")
        print(f'{commit.get("sha")}: {name}')
