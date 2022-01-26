#!/bin/python3

import os, sys, subprocess, json
# Currently a prototype, needs to be improved for robustness

if sys.argv[1] == None:
    print("No arg! Exiting")
    exit(1)
elif str(sys.argv[1]) == "":
    print("Arg Empty! Exiting")
    exit(1)

# Take arg 1 as the upload config file
config_file_name = str(sys.argv[1])
print(f"Adding auth variables to {config_file_name}!")
with open(config_file_name, "rw") as config_file:
    upload_config: dict = json.loads(config_file.read())

# Inject auth variables from directly named environment variables if local,
# or from the Abaco msg if on Abaco.
if os.environ['NOT_ABACO'] == "TRUE":
    upload_config['agave_options']['username'] = os.environ['IW_USERNAME']
    upload_config['agave_options']['password'] = os.environ['IW_PASSWORD']
    upload_config['agave_options']['api_key'] = os.environ['IW_API_KEY']
    upload_config['agave_options']['api_secret'] = os.environ['IW_API_SECRET']
else:
    msg: dict = json.loads(os.environ["MSG"])
    upload_config['agave_options']['username'] = os.environ['MSG']['iw_credentials']['username']
    upload_config['agave_options']['password'] = os.environ['MSG']['iw_credentials']['password']
    upload_config['agave_options']['api_key'] = os.environ['MSG']['iw_credentials']['client_name']
    upload_config['agave_options']['api_secret'] = os.environ['MSG']['iw_credentials']['api_secret']

# then, write the changes to file
config_to_write = json.dumps(upload_config)

config_file.write(config_to_write)