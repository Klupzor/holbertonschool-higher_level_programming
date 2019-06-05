#!/usr/bin/python3
import json
'''Save Object to a file
'''


def save_to_json_file(my_obj, filename):
    text = json.dumps(my_obj)
    with open(filename, 'w', encoding="UTF8") as f:
        f.write(text)
