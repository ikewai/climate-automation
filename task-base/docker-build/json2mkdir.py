#!/bin/python3

import sys, subprocess, json

# Currently a prototype, needs to be improved for robustness

if sys.argv[0] == None:
    print("No arg! Exiting")
    exit(1)
elif str(sys.argv[0]) == "":
    print("Arg Empty! Exiting")
    exit(1)

# Take arg 0 as the json file to read
list_of_dirs_file_name = str(sys.argv[0])

with open(list_of_dirs_file_name) as list_of_dirs_file:
    list_of_dirs = json.loads(list_of_dirs_file.read())

for dir in list_of_dirs:
    subprocess.run("/bin/bash", "-c", f"mkdir {dir}")