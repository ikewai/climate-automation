#!/bin/bash
echo "[task.sh] Hello World! Ready to aggregate daily Airtemp Data."

# Run the aggregation workflow
cd /home/hawaii_climate_products_container/preliminary/air_temp/daily/code
# the following will eventually be programmatic based on daily_temp_agg.sh
python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/temp_agg_wget.py

python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/hads_temp_parse.py

python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/madis_temp_parse.py

python3 -W ignore /home/hawaii_climate_products_container/preliminary/air_temp/daily/code/air_temp_aggregate_wrapper.py

# Upload the aggregated data TEMPORARILY DISABLED
cd /sync
python3 update_date_string_in_config.py upload_config.json upload_config_datestrings_loaded.json
python3 upload_list_inserter.py upload_config_datestrings_loaded.json config.json
python3 upload_auth_injector.py config.json
#python3 upload.py

echo "[task.sh] All done! Moving on to the next step if there is one."
# Continue the Workflow (temporarily removed)
#python3 /actor/run_next.py