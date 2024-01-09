#!/usr/bin/python3
"""
Script that adds all arguments to a Python list
and then save them to a file
"""
import sys
import os.path
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
if os.path.isfile(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])

save_to_json_file(my_list, filename)
