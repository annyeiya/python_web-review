FROM python:3.10.1

USER root
RUN apt-get update -y && apt-get install -y build-essential
RUN pip install --upgrade pip

RUN mkdir mycode
COPY scraper mycode
COPY config.py mycode
COPY /base/run_num.txt mycode
RUN ls -l

WORKDIR /mycode

RUN pip install -r requirements.txt

CMD bash run_scripts.sh
