#!/usr/bin/python3
import json
'''Save Object to a file
'''


def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
