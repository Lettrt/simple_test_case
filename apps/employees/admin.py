from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job_title', 'employment_date', 'salary', 'department')
    search_fields = ('full_name', 'job_title', 'department')
    ordering = ('full_name',)
