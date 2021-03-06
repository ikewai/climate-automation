#!/bin/bash
echo "[task.sh] Hello World! Ready to get today's MADIS data."

# Execute Collection of MADIS Data
cd /home/hawaii_climate_products_container/preliminary/data_aqs/code/madis
python3 mesonet_24hr_fetch_dev.py
python3 hfmetar_24hr_fetch_dev.py

# Upload the collected data
cd /sync
python3 upload_auth_injector.py config.json
python3 upload.py

echo "[task.sh] All done! Moving on to the next step if there is one."
# Continue the Workflow (temporarily removed)
#python3 /actor/run_next.py