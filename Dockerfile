FROM python:3.16.0a1-alpine3.23

RUN mkdir \/app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src /app/src/

CMD python3 /app/src/app.py