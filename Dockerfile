FROM python:3.6.3

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP app.py

CMD flask run --host=0.0.0.0
