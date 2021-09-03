FROM python:3.9.0

WORKDIR /home/

RUN git clone -b 8/11_3ban_class_commit_1 https://github.com/MrRyuwon/gis_3ban_1.git

WORKDIR /home/gis_3ban_1/

RUN echo "SECRET_KEY=django-insecure-y*7(@vu)z_q$qmc5tee=dbuo$5f(!$rf@n)vsgfkipumfu(jp+" > .env

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]