from django.shortcuts import render
# Create your views here.
from  rest_framework  import viewsets
from rest_framework.permissions import AllowAny
from app.models.event  import  Event
from rest_framework.views import APIView
from app.serializers.event  import  EventSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Class based view to Get User Details using Token Authentication
@api_view(['GET'])
def hello_world(request):
    print(request.query_params)
    return Response({'message': 'Hello, World!'})
class  AppViewSet(viewsets.ModelViewSet):
  queryset  =  Event.objects.all()
  serializer_class  =  EventSerializer