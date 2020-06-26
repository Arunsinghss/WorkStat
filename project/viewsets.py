from django.contrib.auth.models import User, Group
from project.serializers import ProjectSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from project.models import Project
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from datetime import datetime

class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        params = request.data if request.data else request.POST
        kwargs = {
            'name':  params.get('name', ''),
            'description':  params.get('description', ''),
            'start_date':  params.get('start_date', ''),
            'end_date':  params.get('end_date', '')
        }

        for key, val in kwargs.items():
            if val == '':
                return JsonResponse({"message": "Please Provide all the fields ..."}, status=400)

        if Project.objects.filter(name=kwargs.get('name')).exists():
            return JsonResponse({"message": "Project with Same Name Already exists..."}, status=400)

        try:
            kw = {
                'name': kwargs.get('name'),
                'description': kwargs.get('description'),
                'start_date': datetime.strptime(kwargs.get('start_date'), '%d-%m-%Y'),
                'end_date': datetime.strptime(kwargs.get('end_date'), '%d-%m-%Y')
            }
            newobj = Project.objects.create(**kw)
            data = self.serializer_class(newobj).data
            return JsonResponse({"message": "New Project Added Successfully...", "data": data}, status=200)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=400)
