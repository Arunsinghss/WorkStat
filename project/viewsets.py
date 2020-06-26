from django.contrib.auth.models import User, Group
from project.serializers import ProjectSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from project.models import Project
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        return JsonResponse({"message": "New Project Added Successfully...", "data": {}}, status=200)
