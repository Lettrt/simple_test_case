from django.shortcuts import render
from .models import Department


def department_list(request):
    '''
    Используется prefetch_related для предварительной загрузки дочерних отделов
    '''
    departments = Department.objects.filter(parent__isnull=True).prefetch_related('children', 'employees')
    return render(request, 'department_list.html', {'departments': departments})
