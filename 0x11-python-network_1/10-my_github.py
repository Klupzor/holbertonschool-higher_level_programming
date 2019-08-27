#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    prm = requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=prm)
    j = response.json()
    print(j.get('id'))
