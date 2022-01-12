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
dirs_file_name = str(sys.argv[0])

with open(dirs_file_name) as dirs_file:
    dirs: list = json.loads(dirs_file.read())

for dir in dirs:
    subprocess.run("/bin/bash", "-c", f"mkdir {dir}")