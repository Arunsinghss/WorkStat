from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class BaseModel(models.Model):
    created_by = models.ForeignKey(User, null=True, blank=True, related_name='created_by', on_delete=models.SET_NULL)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, null=True, blank=True, related_name='modified_by', on_delete=models.SET_NULL)
    modified_on = models.DateTimeField(auto_now=True)


class EmployeeDesignation(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name


class Employee(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    designation = models.ForeignKey(EmployeeDesignation, null=True, blank=True, on_delete=models.SET_NULL)
    emp_age = models.PositiveIntegerField(null=True, blank=True)
    emp_exp = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
