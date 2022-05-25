FROM ikewai/cat-prelim-agg

WORKDIR /docker-build
COPY txt2mkdir_rainfall.py .
COPY r_script_manifest.json .
COPY sh_script_manifest.json .

# Get Directory list
RUN wget https://raw.githubusercontent.com/ikewai/hawaii_climate_products_container/main/preliminary/rainfall/docs/daily/currentDirs.txt

# Make directories and download scripts
RUN /bin/python3 txt2mkdir_rainfall.py currentDirs.txt
RUN /bin/python3 json2wget.py r_script_manifest.json
RUN /bin/python3 json2wget.py sh_script_manifest.json

WORKDIR /sync
COPY ./upload_config.json config.json