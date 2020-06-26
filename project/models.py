from django.db import models
from datetime import datetime
from employee.models import BaseModel, Employee
# Create your models here.


class Project(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    assigned_to = models.ManyToManyField(Employee, related_name='assigned_to', blank=True)
    assigned_by = models.ForeignKey(Employee, null=True, blank=True, related_name='assigned_by', on_delete=models.SET_NULL)
    assigned_on = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    completed_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_assigned_emp(self):
        
        return ", ".join([emp.user.first_name for emp in self.assigned_to.all()])
