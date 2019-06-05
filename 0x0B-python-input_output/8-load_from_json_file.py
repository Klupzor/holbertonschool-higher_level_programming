#!/usr/bin/python3
import json
'''Create object from a JSON file
'''


def load_from_json_file(filename):
    with open(filename, 'r', encoding="UTF8") as f:
        return json.load(f)
