FROM ikewai/cat-prelim-base

WORKDIR /actor

COPY ./task.sh .

WORKDIR /docker-build

COPY dir_manifest.json .
COPY script_manifest.json .

# temporary, this copy will be back in cat-base soon :)
COPY json2mkdir.py .
COPY json2wget.py .

RUN /bin/python3 json2mkdir.py dir_manifest.json
RUN /bin/python3 json2wget.py script_manifest.json


CMD [ "/bin/bash", "/actor/task.sh" ]