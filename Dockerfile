FROM python:3.9.0

WORKDIR /home/

RUN echo "bbqqweb"

RUN git clone https://github.com/hale-in/bbqqweb

WORKDIR /home/bbqqweb/

#RUN echo "SECRET_KEY=django-insecure-y*7(@vu)z_q$qmc5tee=bbqqqutation6699" > .env

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=djangoProject2.settings.deploy && python manage.py migrate --settings=djangoProject2.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=bbqqweb.settings.deploy bbqqweb.wsgi --bind 0.0.0.0:8000"]