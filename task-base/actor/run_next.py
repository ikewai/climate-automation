#!/bin/python3

import json, os
from tapipy import Tapis

msg: dict = json.loads(os.environ['MSG'])

# If this is the last actor in the series, just exit
if (msg['index']+ 1) == len(msg['tasks']):
    exit

# Increment Index
msg['index'] += 1

# Construct new Tapis object capable of sending a message to an actor
t = Tapis(
    base_url = os.environ['_abaco_api_server'],
    client_id = msg['tacc_credentials']['client_name'],
    access_token = os.environ['_abaco_access_token']
)

# Send the message
t.actors.sendMessage(
    actor_id=msg['tasks'][msg['index']]['actor_id'],
    request_body={
        'message': msg
    }    
)

