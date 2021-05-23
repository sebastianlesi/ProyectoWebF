FROM python:latest
ENV PYTHONUNBUFFERED=1
RUN mkdir /era
WORKDIR /era
ADD requirements.txt /era/
RUN pip install -r requirements.txt
ADD . /era/


