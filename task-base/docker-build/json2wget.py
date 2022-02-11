#!/bin/python3

import sys, subprocess, json

# Currently a prototype, needs to be improved for robustness/long-term security

# Check for arguments
if (sys.argv[1] == None) or (str(sys.argv[1]) == ""):
    print("This script needs args! Pass it a json manifest.")
    exit(1)

# Take arg 1 as the json file to read
fname = str(sys.argv[1])

with open(fname) as scripts_file:
    script_json: dict = json.loads(scripts_file.read())

# var names and structure here are ugly, will fix later 🤞
script_base_url: str = script_json["base_url"]
script_placement_dir = script_json["placement_url"]
script_list: list = script_json["scripts"]
script_urls: list = script_list.copy()
for i in range(len(script_urls)):
    script_url = script_urls[i]
    script_urls[i] = f"{script_base_url}{script_url}"


for i in range(len(script_urls)):
    command: str = f"wget {script_urls[i]} -O {script_placement_dir}/{script_list[i]}"
    subprocess.run(["/bin/bash", "-c", command])