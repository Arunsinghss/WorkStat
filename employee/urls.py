from django.urls import include, path
from rest_framework import routers
from employee import views
from employee import viewsets as restapis

router = routers.DefaultRouter()
router.register(r'emp', restapis.EmployeeViewset)
router.register(r'login', restapis.UserViewset)
router.register(r'designation', restapis.EmployeeDesignationViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]