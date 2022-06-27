#!/bin/bash
echo "[task.sh] Hello World! Ready to map daily Airtemp Data."

# Run the mapping workflow
cd /home/hawaii_climate_products_container/preliminary/air_temp/daily/code

/bin/bash -c /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/daily_temp_map.sh > /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/temp_map.out 2> /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/temp_map.err

# Upload the aggregated data (temporarily disabled)
cd /sync
python3 update_date_string_in_config.py upload_config.json upload_config_datestrings_loaded.json
python3 upload_list_inserter.py upload_config_datestrings_loaded.json config.json
python3 upload_auth_injector.py config.json
#python3 upload.py

echo "[task.sh] All done! Moving on to the next step if there is one."
# Continue the Workflow (temporarily removed)
#python3 /actor/run_next.py