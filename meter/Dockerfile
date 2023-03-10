FROM python:3.11-slim-bullseye

WORKDIR /src

## Install pipenv as we'll use it to install dependencies
RUN pip install pipenv

COPY ./src/ ./

RUN pipenv sync --system

CMD python main.py
