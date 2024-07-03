from  rest_framework  import  serializers
from  app.models.event  import  Event
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class  EventSerializer(serializers.ModelSerializer):
  class  Meta:
    model  =  Event
    fields  =  '__all__'


