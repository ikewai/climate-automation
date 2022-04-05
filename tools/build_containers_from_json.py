#!/bin/python3

import sys, subprocess, json

fin = open(sys.argv[1], "rt")
container_list: dict = json.loads(fin.read())

log_dir = sys.argv[2]

for container in container_list:
    build_name: str = container["build_name"]
    build_dir: str = container["build_dir"]
    tag: str = ""
    for gh_repo in container["gh_repos"]:
        tag = f'{tag}_{gh_repo["nickname"]}.{gh_repo["repo"]}'
    
    command: str = f"./build_container.sh {build_name}:{tag} {build_dir} {log_dir}"
    subprocess.run("/bin/bash", "-c", command)

