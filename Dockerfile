FROM python:3.6

COPY requirements.txt requirements.txt
RUN apt-get update && pip install -r requirements.txt
COPY app/ app/
COPY templates templates
