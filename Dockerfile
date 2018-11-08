FROM python:3.4-jessie

ARG HOST_NAME='127.0.0.1:8000'

#RUN apt-get upgrade
#RUN apt-get update
#RUN apt-get install -y libssl-dev openssl gunicorn nano

RUN mkdir -p /var/www/stat_app
WORKDIR /var/www/stat_app
COPY server /var/www/stat_app
RUN echo "host_name=$HOST_NAME" > env.py
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

EXPOSE 8000
CMD exec gunicorn app.wsgi:application --bind 0.0.0.0:8000 --workers 3