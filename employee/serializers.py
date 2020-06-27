from django.contrib.auth.models import User, Group
from rest_framework import serializers
from employee.models import Employee, EmployeeDesignation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class EmployeeDesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDesignation
        fields = "__all__"