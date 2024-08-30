FROM python:3.10.12

COPY /requirements.txt /tmp/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt

ADD app.py /var/server/app.py
COPY . /app
WORKDIR /app
RUN chmod 777 /app

