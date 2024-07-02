FROM python:3.11-alpine

EXPOSE 8000

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
#RUN apt-get update && apt-get install -y libpq-dev gcc python3-dev musl-dev
# copy project

WORKDIR /usr/src/app
RUN pip install --upgrade pip
COPY . /usr/src/app/
COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

# CMD  python init.py && python manage.py runserver 0.0.0.0:8000
CMD python manage.py runserver 0.0.0.0:8000 && python manage.py migrate

#CMD python entrypoint.py
