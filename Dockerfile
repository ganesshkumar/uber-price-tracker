FROM python:3.6-alpine

WORKDIR /
COPY requirements.txt /
run pip install -r requirements.txt
COPY src /app
WORKDIR /app
CMD python app.py
