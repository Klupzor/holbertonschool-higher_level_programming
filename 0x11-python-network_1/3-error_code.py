#!/usr/bin/python3
import urllib.request
from sys import argv

if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            page = response.read()
            print(page.decode("utf-8"))
    except urllib.error.URLError as e:
        print('Error code: {}'.format(e.code))
