#!/bin/bash
echo "[task.sh] Hello World! Ready to map daily Airtemp Data."

# Run the mapping workflow
cd /home/hawaii_climate_products_container/preliminary/air_temp/daily/code

python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/temp_map_wget.py

python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/update_predictor_table.py

python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/county_map_wrapper.py

python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/meta_data_wrapper.py

python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/state_wrapper.py

# Upload the aggregated data (temporarily disabled)
cd /sync
python3 update_date_string_in_config.py upload_config.json upload_config_datestrings_loaded.json
python3 upload_list_inserter.py upload_config_datestrings_loaded.json config.json
python3 upload_auth_injector.py config.json
#python3 upload.py

echo "[task.sh] All done! Moving on to the next step if there is one."
# Continue the Workflow (temporarily removed)
#python3 /actor/run_next.py