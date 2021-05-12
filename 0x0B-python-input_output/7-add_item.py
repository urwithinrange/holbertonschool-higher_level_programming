#!/usr/bin/python3
"""script adds all arguments to a python list and then save them to a file"""
import json
import sys
import os
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

f = "add_item.json"
a_list = []

for i in range(len(sys.argv)):
    if i > 0:
        a_list.append(sys.argv[i])

if os.path.exists(f):
    b_list = load_from_json_file(f)
    for i in a_list:
        b_list.append(i)
    save_to_json_file(b_list, f)
else:
    save_to_json_file(a_list, f)
