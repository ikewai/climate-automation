#!/bin/python3
# todo: add robustness to response handling

import sys, requests, json

repo: str = sys.argv[1] # Format: "ikewai/climate-automation"

endpoint: str = f"https://api.github.com/repos/{repo}/commits" # Get commit log

res = requests.get(endpoint)

latest_commit: str = res.json()[0]['sha'][:8] # First eight chars of sha hash of latest comm.

print(latest_commit)