
from django.contrib import admin
from .models import Department,Role,Employee

# Register your models here.

class Employeeslist(admin.ModelAdmin):
    list_display=['fname','lname','dept']



admin.site.register(Employee,Employeeslist)
admin.site.register(Department)
admin.site.register(Role)