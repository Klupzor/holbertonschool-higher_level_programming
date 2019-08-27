#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    try:
        response = requests.get(sys.argv[1])
        print(response.headers['X-Request-Id'])
    except:
        pass
