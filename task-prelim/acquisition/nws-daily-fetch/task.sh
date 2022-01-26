#!/bin/bash
echo "[task.sh] Hello World! Ready to get today's hourly NWS data."

# Execute Collection of NWS Hourly Data
cd /home/hawaii_climate_products_container/preliminary/data_aqs/code/nws_rr5
Rscript nws_rr5_hrly_24hr_webscape.R

# Upload the collected data
python3 /sync/upload_auth_injector.py /sync/upload_config.json
python3 /sync/upload.py

echo "[task.sh] All done! Moving on to the next step if there is one."
# Continue the Workflow (temporarily removed)
#python3 /actor/run_next.py