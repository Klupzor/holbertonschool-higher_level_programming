#!/usr/bin/python3
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
'''Load, add, save
'''

if __name__ == '__main':
    filename = "add_item.json"
    my_list = sys.argv[1:]

    try:
        my_set = load_from_json_file(filename)

    except Exception as e:
        my_set = []

    my_set.extend(my_list)
    save_to_json_file(my_set, filename)
