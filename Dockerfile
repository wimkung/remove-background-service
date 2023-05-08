FROM python:3.9.6-alpine

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/requirements.txt
COPY . .
RUN pip3 install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]