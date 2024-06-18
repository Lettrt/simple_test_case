from django.shortcuts import render
from .models import Department


def department_list(request):
    departments = Department.objects.filter(parent__isnull=True).prefetch_related('children')
    return render(request, 'department_list.html', {'departments': departments})
