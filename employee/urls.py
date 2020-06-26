from django.urls import include, path
from rest_framework import routers
from employee import views
from employee import viewsets as restapis

router = routers.DefaultRouter()
router.register(r'getemp', restapis.UserViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]