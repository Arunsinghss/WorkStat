from django.contrib.auth.models import User, Group
from project.models import Project
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class ProjectSerializer(serializers.ModelSerializer):

    created_by = SerializerMethodField()
    assigned_by = SerializerMethodField()
    assigned_to = SerializerMethodField()

    class Meta:
        model = Project
        fields = "__all__"

    def get_created_by(self, obj):
        return {'id':obj.created_by.employee.id, 'name':obj.created_by.employee.get_full_name}
    
    def get_assigned_by(self, obj):
        if obj.assigned_by:
            return {'id':obj.assigned_by.employee.id, 'name':obj.assigned_by.employee.get_full_name}
        else:
            return {}

    def get_assigned_to(self, obj):
        data = []
        for x in obj.assigned_to.all():
            data.append({'id':x.id, 'name':x.get_full_name})
        return data