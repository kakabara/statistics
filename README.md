## Django application Сервер для просмотра прибыли по филиалам + локомотивы


1) build: docker build --no-cache -t django-stats .
2) if you use nginx or apache you can use host_name build: docker build --build-arg HOST_NAME="your host" --no-cache -t django-stats .
3) start:  docker run -d --name django -p 8000:8000 django-stats Optionally you can set HOST with arg HOST
