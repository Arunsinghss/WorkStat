from django.contrib.auth.models import User, Group
from project.serializers import ProjectSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from project.models import Project
from employee.models import Employee
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from datetime import datetime
import json

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

    def update(self, request, pk=None, *args, **kwargs):
        try:
            params = request.data.dict() if request.data else request.POST
            kw = {}
            assigned_to = json.loads(params.get('assigned_to','[]'))
            project = Project.objects.filter(pk=pk)
            
            for key,val in params.items():
                if key in ['name', 'description']:
                    if val.strip():
                        kw[key]= val
                    else :
                        return JsonResponse({'message': 'Project {} is not valid'.format(key)}, status=400)
                
                if key in ['start_date', 'end_date', 'assigned_on', 'completed_on']:
                    if val.strip():
                        kw[key] = datetime.strptime(val, '%d-%m-%Y')
                    else:
                        return JsonResponse({'message': 'Project {} is not valid'.format(key)}, status=400)
                
                kw['is_completed'] = True if params.get('is_completed','') == 'true' else False
            
            kw['modified_by'] = request.user
            project.update(**kw)
            project = project.first()
            
            if assigned_to:
                for x in assigned_to:
                    project.assigned_to.add(Employee.objects.get(id=x))
                project.save()

            return JsonResponse({"Message": 'Data Updated Successfully....', "data": ProjectSerializer(project).data}, status=200)
        
        except Exception as e:
            return JsonResponse({"Message": str(e)}, status=400)
