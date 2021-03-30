FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /code1
WORKDIR /code1
ADD requirements.txt /code1/
RUN pip install -r requirements.txt
ADD . /code1/
