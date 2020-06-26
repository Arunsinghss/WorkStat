from django.urls import include, path
from rest_framework import routers
from project import viewsets as restapis

router = routers.DefaultRouter()
router.register(r'getproject', restapis.ProjectViewset)

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]