from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class BaseModel(models.Model):
    created_by = models.ForeignKey(User)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(User, null=True, blank=True)
    modified_on = models.DateTimeField(auto_now=True)

class Employee(BaseModel):
    user = models.ForeignKey(User, unique=True)
    designation = models.ForeignKey(EmployeeDesignation)
    emp_age = models.PositiveIntegerField(null=True, blank=True)
    emp_exp = models.PositiveIntegerField(null=True, blank=True)

class EmployeeDesignation(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)

class Project(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    assigned_to = models.ManyToManyField(Employee, null=True, blank=True)
    assigned_by = models.ForeignKey(Employee, null=True, blank=True)
    assigned_on = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    completed_on = models.DateTimeField(null=True, blank=True)
