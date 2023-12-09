FROM python:3.10.1

USER root
RUN apt-get update -y && apt-get install -y build-essential
RUN pip install --upgrade pip

RUN mkdir mycode
COPY app mycode
RUN ls -l

WORKDIR /mycode

RUN pip install flask

CMD python3 server.py