#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    try:
        response = requests.get(sys.argv[1])
        response.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.response.status_code))
    else:
        print(response.text)
