from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import Employee
# Register your models here.
# class EmployeeAdmin(admin.ModelAdmin):
#     display=['eno','ename,'esal','eaddr']
admin.site.register(Employee)
