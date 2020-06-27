from django.contrib.auth.models import User, Group
from rest_framework import serializers
from employee.models import Employee, EmployeeDesignation
from project.serializers import ProjectSerializer
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from project.models import Project

class UserSerializer(serializers.ModelSerializer):
    groups = SerializerMethodField()
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'groups')

    def get_groups(self, obj):
        return list(obj.groups.all().values_list('name',flat=True))

class EmployeeDesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDesignation
        fields = ('id','name','description')

class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    assigned_projects = SerializerMethodField()
    designation = EmployeeDesignationSerializer()

    class Meta:
        model = Employee
        fields = "__all__"

    def get_assigned_projects(self, obj):
        return ProjectSerializer(Project.objects.filter(assigned_to__in=[obj]), many=True).data



