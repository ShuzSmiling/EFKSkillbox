FROM python:3.10.12

COPY /requirements.txt /app/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

COPY . /app
WORKDIR /app

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]