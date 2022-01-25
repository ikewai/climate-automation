#!/bin/python3

import sys, subprocess, json

# Currently a prototype, needs to be improved for robustness

if sys.argv[1] == None:
    print("No arg! Exiting")
    exit(1)
elif str(sys.argv[1]) == "":
    print("Arg Empty! Exiting")
    exit(1)

# Take arg 1 as the json file to read
dirs_file_name = str(sys.argv[1])
print(f"Making directories from {dirs_file_name}!")
with open(dirs_file_name) as dirs_file:
    dirs: list = json.loads(dirs_file.read())
print(f"Dirs are: {dirs}!")

for dir in dirs:
    subprocess.run(["/bin/bash", "-c", f"mkdir -p {dir}"])