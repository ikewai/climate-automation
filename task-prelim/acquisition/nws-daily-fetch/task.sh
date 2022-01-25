#!/bin/bash
echo "task.sh reporting! Ready to get today's hourly NWS data."

# Execute Collection of NWS Hourly Data
cd /home/hawaii_climate_products_container/preliminary/data_aqs/code/nws_rr5
Rscript nws_rr5_hrly_24hr_webscape.R

echo "[task.sh] All done! Moving on to the next step if there is one."
# Continue the Workflow (momentarily removed)
#python3 /actor/run_next.py