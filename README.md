## Django application Сервер для просмотра прибыли по филиалам + локомотивы


1) build: docker build --no-cache -t django-stats .
2) if you use nginx or apache you can use host_name build: docker build --build-arg HOST_NAME="your host" --no-cache -t django-stats .
3) start:  docker run -d --name django -p 80:8000 django-stats
4) From webBrowser you can access by http://127.0.0.1 or http://your-host-name
