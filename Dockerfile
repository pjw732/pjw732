
FROM python:3.9.0

WORKDIR /home/

RUN echo "admkl"

RUN git clone https://github.com/pjw732/pjw732.git

WORKDIR /home/pjw732/

#RUN echo "SECRET_KEY=django-insecure-gwncn-2alj%l4@0&b9o8j^tyev3l-%)zm&vbljglfvg(yb2m6-" > .env

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=practice01.settings.deploy && python manage.py migrate --settings=practice01.settings.deploy && gunicorn --env DJANGO_SETTINGS_MODULE=practice01.settings.deploy practice01.wsgi --bind 0.0.0.0:8000"]