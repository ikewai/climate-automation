FROM ikewai/cat-prelim-base

WORKDIR /actor

COPY ./task.sh .

WORKDIR /task
RUN wget "https://raw.githubusercontent.com/ikewai/hawaii_climate_products_container/main/preliminary/air_temp/code/hads_temp_parse.py"

CMD [ "/bin/bash", "/actor/task.sh" ]