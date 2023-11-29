FROM python:3.10.1

USER root
RUN apt-get update -y && apt-get install -y build-essential
RUN pip install --upgrade pip

RUN mkdir mycode
COPY scraper mycode
RUN ls -l

WORKDIR /mycode

RUN pip install bs4
RUN pip install lxml
RUN pip install requests

CMD bash run_scripts.sh
