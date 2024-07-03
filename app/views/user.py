from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from app.serializers.user  import  UserSerializer,UserLoginSerializer
from django.conf import settings
#import make_password
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
#import JsonResponse
from django.http import JsonResponse
#create error code status 
from rest_framework import status
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action
from drf_yasg import openapi
from app.views.swagger import RegisterSwaggerParams,RegisterSwaggerResponse,LoginSwaggerParams
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserRegisterView(APIView):
    #define register api swagger
    @swagger_auto_schema(tags=["Auth"], method='POST', request_body=RegisterSwaggerParams,responses=RegisterSwaggerResponse)
    @action(detail=False, methods=['post'])
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            user = serializer.save()
            
            return JsonResponse({
                'message': 'Register successful!'
            }, status=status.HTTP_201_CREATED)

        else:
            return JsonResponse({
                'error_message': 'This email has already exist!',
                'errors_code': 400,
            }, status=status.HTTP_400_BAD_REQUEST)
class UserLoginView(APIView):
    @swagger_auto_schema(tags=["Auth"], method='POST', request_body=LoginSwaggerParams)
    @action(detail=False, methods=['post'])
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            # check user is exist or not
            user = User.objects.filter(email=serializer.validated_data['email']).first()
            # user = authenticate(
            #     request,
            #     username=serializer.validated_data['email'],
            #     password=serializer.validated_data['password']
            # )
            if user:
                refresh = TokenObtainPairSerializer.get_token(user)
                data = {
                    'refresh_token': str(refresh),
                    'access_token': str(refresh.access_token),
                    'access_expires': int(settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'].total_seconds()),
                    'refresh_expires': int(settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'].total_seconds())
                }
                return Response(data, status=status.HTTP_200_OK)
                
            return Response({
                'error_message': 'Email or password is incorrect!',
                'error_code': 400
            }, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({
            'error_messages': serializer.errors,
            'error_code': 400
        }, status=status.HTTP_400_BAD_REQUEST)
