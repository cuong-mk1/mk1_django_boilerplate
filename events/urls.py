from  django.urls  import  path, include
from  rest_framework.routers  import  DefaultRouter
from .views  import  EventViewSet,hello_world
router  =  DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns  = [
  path('', include(router.urls)),
  path('hello/', hello_world, name='hello-world'),
]