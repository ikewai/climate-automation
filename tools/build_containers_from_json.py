#!/bin/python3
# This script builds docker containers from local files, as defined by a JSON file.
# Arg 1: Path to the JSON file to read from.
# Arg 2: Directory to log results to.


import sys, subprocess, json

fin = open(sys.argv[1], "rt")
container_list: dict = json.loads(fin.read())

log_dir = sys.argv[2]

for container in container_list:
    build_name: str = container["build_name"]
    build_dir: str = container["build_dir"]
    tag: str = ""
    for gh_repo in container["gh_repos"]:
        tag = f'{tag}_{gh_repo["nickname"]}.{gh_repo["repo"]}' # Tag naming scheme
    
    command: str = f"./build_container.sh {build_name}:{tag} {build_dir} {log_dir}" # Pass arguments to build_container.sh
    subprocess.run("/bin/bash", "-c", command)

