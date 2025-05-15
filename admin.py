from django.contrib import admin
from .models import Employee, Role, Department

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'location')
    ordering = ['id']  # Order departments by ID in ascending order

class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ['id']  # Order roles by ID in ascending order

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'dept', 'role', 'salary', 'phone', 'hire_date')
    ordering = ['id']  # Order employees by emp_id (ID) in ascending order

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Role, RoleAdmin)
