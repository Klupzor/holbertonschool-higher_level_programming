#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        data = {'q': ""}
    else:
        data = {'q': sys.argv[1]}
    response = requests.post("http://0.0.0.0:5000/search_user", data)
    try:
        jsn = response.json()
    except BaseException:
        print("Not a valid JSON")
    else:
        if jsn:
            print("[{}] {}".format(jsn.get('id'), jsn.get('name')))
        else:
            print("No result")
