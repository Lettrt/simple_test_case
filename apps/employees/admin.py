from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job_title', 'employment_date', 'salary', 'get_department')
    search_fields = ('full_name', 'job_title', 'department__name')
    ordering = ('full_name',)

    def get_department(self, obj):
        return obj.department.name if obj.department else 'Это самый главный отдел!'
    get_department.short_description = 'Вышестоящий отдел'
