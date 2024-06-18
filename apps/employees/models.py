from django.db import models

from ..departments.models import Department


class Employee(models.Model):
    '''
    Модель сотрудников
    ### Attrs:
    - full_name (str) - Полное имя сотрудника
    - job_title (str) - Должность сотрудника
    - employment_date (date) - Дата приема на работу
    - salary (decimal) - Зарплата сотрудника
    - department (FK) - Отдле в котором работает сотрудник
    '''
    full_name: models.CharField = models.CharField(
        max_length=200, verbose_name='Полное имя',
        help_text='Полное имя сотрудника. Можно указывать через пробел'
    )
    job_title: models.CharField = models.CharField(
        max_length=200, verbose_name='Должность',
        help_text='Должность сотрудника'
    )
    employment_date: models.DateField = models.DateField(
        verbose_name='Дата приема на работу',
        help_text='Укажите дату приема на работу'
    )
    salary: models.DecimalField = models.DecimalField(
        max_digits=10, decimal_places=2,
        verbose_name='Зарплата',
        help_text='Укажите размер заработной платы сотрудника'
    )
    department: models.ForeignKey = models.ForeignKey(
        Department, on_delete=models.CASCADE,
        related_name='employees', verbose_name='Отдел',
        help_text='Отдел в котором работает сотрудник'
    )

    def __str__(self):
        return f'{self.full_name} - отдел: {self.department}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['full_name']
