from  django.urls  import  path, include
from  rest_framework.routers  import  DefaultRouter
from .views  import  AppViewSet,hello_world
router  =  DefaultRouter()
router.register(r'app', AppViewSet)

urlpatterns  = [
  path('', include(router.urls)),
  path('hello/', hello_world, name='hello-world'),

]