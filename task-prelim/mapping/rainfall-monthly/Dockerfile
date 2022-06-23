FROM ikewai/task-pre-map

WORKDIR /docker-build
COPY txt2mkdir_rainfall.py .
COPY script_manifest.json .

# Get Directory list
RUN wget https://raw.githubusercontent.com/ikewai/hawaii_climate_products_container/main/preliminary/rainfall/docs/monthly/currentDirs.txt

# Make directories and download scripts
RUN /bin/python3 txt2mkdir_rainfall.py currentDirs.txt
RUN /bin/python3 json2wget.py script_manifest.json

WORKDIR /sync

# Get pre-staged manifest of files to upload
RUN wget https://raw.githubusercontent.com/ikewai/hawaii_climate_products_container/main/preliminary/rainfall/docs/monthly/upload_config.json

# Copy json "upload" value inserter
#COPY ./upload_list_inserter.py upload_list_inserter.py

# Copy upload config template from build context
#COPY ./upload_config.json config.json

WORKDIR /actor
COPY task.sh .