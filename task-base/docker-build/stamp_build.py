#!/bin/python3

import json, sys, subprocess, os

if sys.argv[1] == None:
    print("No arg! Exiting")
    exit(1)
elif str(sys.argv[1]) == "":
    print("Arg Empty! Exiting")
    exit(1)

# All args are interpreted as libraries to clone.

for repo in sys.argv[1::1]: # skips the first arg, which would be "stamp_build.py"
    subprocess.run(["/bin/bash", "-c", f"git clone {repo}"])

for repo in os.listdir(): # list all things 
    subprocess.run("/bin/bash", "-c", f"cat {repo}/FETCH_HEAD") # need to figure out this parsing logic

