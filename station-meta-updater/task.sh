#!/bin/bash

# Use async transfer to import file from github into the gateway
curl -sk -H "Authorization: Bearer $IKEWAI_TOKEN" \
 -X POST -d "urlToIngest=https://raw.githubusercontent.com/ikewai/hawaii_wx_station_mgmt_container/main/Hawaii_Master_Station_Meta.csv" \
 -d "fileName=Hawaii_Master_Station_Meta.csv" https://ikewai.its.hawaii.edu/files/v2/media/mdodge/test_dir