FROM python:3.4-jessie

RUN apt-get upgrade
RUN apt-get update
RUN apt-get install -y libssl-dev openssl gunicorn nano

RUN mkdir -p /var/www/stat_app
WORKDIR /var/www/stat_app
ADD . /var/www/stat_app
RUN pip install -r requirements.txt

EXPOSE 8000
CMD exec gunicorn app.wsgi:application --bind 0.0.0.0:8000 --workers 3