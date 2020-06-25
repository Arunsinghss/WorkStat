from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    class Meta:
        model: User
        # fields = ('username','email','first_name','last_name')
        fields = "__all__"