from  django.urls  import  path, include
from  rest_framework.routers  import  DefaultRouter
from app.views.event  import  AppViewSet,hello_world
from app.views.user  import  UserRegisterView,UserLoginView
from rest_framework_simplejwt import views as jwt_views
router  =  DefaultRouter()
router.register(r'event', AppViewSet)


urlpatterns  = [
  path('', include(router.urls)),
  path('hello/', hello_world, name='hello-world'),
  path('register', UserRegisterView.as_view(), name='register'),
  
  # path('login', jwt_views.TokenObtainPairView.as_view(), name='login'),
  path('login', UserLoginView.as_view(), name='login'),


]