from django.shortcuts import render
# Create your views here.
from  rest_framework  import viewsets
from .models  import  Event
from .serializers  import  EventSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, World!'})
class  EventViewSet(viewsets.ModelViewSet):
  queryset  =  Event.objects.all()
  serializer_class  =  EventSerializer