FROM ikewai/cat-prelim

RUN apt update
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /docker-build

COPY dir_manifest.json .
COPY script_manifest.json .

RUN /bin/python3 json2mkdir.py dir_manifest.json
RUN /bin/python3 json2wget.py script_manifest.json

WORKDIR /sync
COPY ./upload_config.json config.json

WORKDIR /actor
COPY ./task.sh .

CMD ["/bin/bash", "/actor/task.sh"]