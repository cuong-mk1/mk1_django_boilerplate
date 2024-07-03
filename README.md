# Django REST API Boilerplate

#### Tech Stack:

 - **Web framework:** Django
 - **Database:** PostgresSQL
 - **Containerization:** Docker
 - **Async-Task Queue:** Celery
 - **Message-Broker:** RabbitMQ
 - **WSGI Server:** Gunicorn
 - **Documentation:** Swagger-UI

# Docker run
    - docker-compose up
    - docker-compose exec rest-api python manage.py migrate
    - docker-compose exec rest-api python manage.py createsuperuser
#Manual for Django project

## Gen requirement.txt
 - pip freeze > requirements.txt
# Run django manual
 - cp .env.local .env
 - pip install -r requirements.txt
## Migrate 
 - python manage.py migrate -> Run migration
 - python manage.py makemigrations -> Tạo mới migrattion
## create super user
 - python manage.py createsuperuser
 username: cuongln
 email: cuongln.hust@gmail.com
 password: Mk1@2345
 ## start server 
  - python manage.py runserver
## 
```
├── mk1_django_base
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
├── manage.py
└── app
    ├── admin.py
    ├── serializers.py
    ├── __init__.py
    ├── models.py
    ├── urls.py
    └── views.py
```
## create app
 - python manage.py startapp app

