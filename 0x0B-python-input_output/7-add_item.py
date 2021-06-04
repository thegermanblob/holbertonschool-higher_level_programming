#!/usr/bin/python3
""" Script that add arguments into a list to make a json file """
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    temp_list = load_from_json_file("add_item.json")
except:
    temp_list = []
temp_list.extend(sys.argv[1:])
save_to_json_file(temp_list, "add_item.json")
