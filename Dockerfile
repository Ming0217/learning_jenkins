FROM jfloff/alpine-python:2.7-slim

ENV APP_HOME /usr/src/app
WORKDIR /$APP_HOME

COPY learn_decorator.py /usr/src/app

CMD [ "python", "/usr/src/app/learn_decorator.py" ]
