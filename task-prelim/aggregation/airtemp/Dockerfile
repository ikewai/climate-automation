FROM ikewai/cat-prelim-agg

WORKDIR /docker-build
COPY dir_manifest.json .
COPY script_manifest.json .

RUN /bin/python3 json2mkdir.py dir_manifest.json
RUN /bin/python3 json2wget.py script_manifest.json

WORKDIR /sync

# Get pre-staged manifest of files to upload
RUN wget https://raw.githubusercontent.com/ikewai/hawaii_climate_products_container/main/preliminary/air_temp/daily/docs/upload_config.json

# Copy json "upload" value inserter
COPY ./upload_list_inserter.py upload_list_inserter.py

# Copy upload config template from build context
COPY ./upload_config.json config.json