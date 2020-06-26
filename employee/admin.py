from django.contrib import admin
from employee.models import *
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'designation', 'emp_exp', 'emp_age')

class EmployeeDesignationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(EmployeeDesignation, EmployeeDesignationAdmin)