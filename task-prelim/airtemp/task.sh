#!/bin/bash

# Run the HADS Temperature Parsing script
python3 /task/hads_temp_parse.py

# Continue the Workflow
python3 /actor/run_next.py