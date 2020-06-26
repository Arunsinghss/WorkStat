from django.contrib import admin
from project.models import *
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name' ,'description' ,'start_date' ,'end_date' ,'get_assigned_emp' ,'assigned_by' ,'assigned_on' ,'is_completed' ,'completed_on')

admin.site.register(Project, ProjectAdmin)