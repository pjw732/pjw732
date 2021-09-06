FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/pjw732/pjw732.git

WORKDIR /home/pjw732/

RUN echo "SECRET_KEY=django-insecure-gwncn-2alj%l4@0&b9o8j^tyev3l-%)zm&vbljglfvg(yb2m6-" > .env

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "practice01.wsgi", "--bind", "0.0.0.0:8000"]