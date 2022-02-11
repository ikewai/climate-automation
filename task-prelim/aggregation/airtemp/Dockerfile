FROM ikewai/cat-prelim-agg

WORKDIR /docker-build
COPY dir_manifest.json .
COPY script_manifest .
RUN /bin/python3 json2mkdir.py dir_manifest.json
RUN /bin/python3 json2wget.py script_manifest.json

WORKDIR /sync
COPY ./upload_config.json config.json