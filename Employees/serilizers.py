from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    class Meta:
        model: User
        fileds = ['username','email','first_name','last_name']