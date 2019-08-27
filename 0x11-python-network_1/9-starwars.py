#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    data = {'search': sys.argv[1]}
    response = requests.get("https://swapi.co/api/people", params=data)
    j = response.json()
    print("Number of results: {}".format(j.get('count')))
    for item in j.get('results'):
        print(item.get('name'))
