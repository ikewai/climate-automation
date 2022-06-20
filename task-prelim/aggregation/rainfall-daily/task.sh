#!/bin/bash
echo "[task.sh] Hello World! Ready to aggregate daily Rainfall Data."

# Run the aggregation workflow
cd /home/hawaii_climate_products_container/preliminary/rainfall/code/daily
Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/daily/rcode/hads_daily_rf_FINAL.R
Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/daily/rcode/nws_rr5_daily_rf_FINAL.R
Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/daily/rcode/madis_daily_rf_FINAL.R
Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/daily/rcode/all_data_daily_merge_table_rf_FINAL.R
Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/daily/rcode/qaqc_randfor_bad_data_flag_remove_rf_FINAL.R
Rscript /home/hawaii_climate_products_container/preliminary/rainfall/code/daily/rcode/daily_gap_fill_NR_only_rf_FINAL.R

# Upload the aggregated data TEMPORARILY DISABLED
cd /sync
python3 update_date_string_in_config.py upload_config.json upload_config_datestrings_loaded.json
python3 upload_list_inserter.py upload_config_datestrings_loaded.json config.json
python3 upload_auth_injector.py config.json
#python3 upload.py

echo "[task.sh] All done! Moving on to the next step if there is one."
# Continue the Workflow (temporarily removed)
#python3 /actor/run_next.py