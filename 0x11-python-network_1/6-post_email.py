#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    try:
        response = requests.post(sys.argv[1], data={'email': sys.argv[2]})
        print(response.text)
    except:
        pass
