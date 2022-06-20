FROM ikewai/task-pre-aq

WORKDIR /sync
COPY ./upload_config.json config.json

WORKDIR /actor
COPY ./task.sh .

CMD [ "/bin/bash", "/actor/task.sh" ]