FROM python:3.8-stretch

WORKDIR /home/

RUN echo "bbqqweb1011223344"

RUN git clone https://github.com/hale-in/bbqqweb

WORKDIR /home/bbqqweb/

#RUN echo "SECRET_KEY=django-insecure-y*7(@vu)z_q$qmc5tee=bbqqqutation6699" > .env

RUN pip install --upgrade pip

RUN pip install requests==2.20.0

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient


EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=djangoProject2.settings.deploy && python manage.py migrate --settings=djangoProject2.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=bbqqweb.settings.deploy bbqqweb.wsgi --bind 0.0.0.0:8000"]