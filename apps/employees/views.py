from django.shortcuts import render
from .models import Employee


def employee_list(request):
    employees = Employee.objects.all().select_related('department')
    return render(request, 'employee_list.html', {'employees': employees})
