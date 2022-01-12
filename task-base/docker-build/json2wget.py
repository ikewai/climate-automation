#!/bin/python3

import sys, subprocess, json

# Currently a prototype, needs to be improved for robustness/long-term security

if sys.argv[0] == None:
    print("No arg! Exiting")
    exit(1)
elif str(sys.argv[0]) == "":
    print("Arg Empty! Exiting")
    exit(1)

# Take arg 0 as the json file to read
file_name = str(sys.argv[0])

with open(file_name) as scripts_file:
    script_urls: list = json.loads(scripts_file.read())

for script_url in script_urls:
    subprocess.run("/bin/bash", "-c", f"wget {script_url}")