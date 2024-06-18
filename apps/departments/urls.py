from django.urls import path
from .views import department_list

urlpatterns = [
    path('', department_list, name='department_list')
]