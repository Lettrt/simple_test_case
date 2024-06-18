import os
import django
import random
from faker import Faker
from tqdm import tqdm

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

try:
    django.setup()
except Exception as e:
    print(f"Ошибка при настройке Django: {e}")
    raise

from apps.departments.models import Department
from apps.employees.models import Employee

fake = Faker('ru_RU')


def create_department(num_departments):
    departments = []
    for _ in tqdm(range(num_departments), desc='Создание отделов'):
        department_name = fake.company()
        parent = random.choice(departments) if departments and random.random() > 0.5 else None
        department = Department(name=department_name, parent=parent)
        department.save()
        departments.append(department)
    return departments


def create_employees(num_employees, departments):
    skip_first_lvl = [dept for dept in departments if dept.parent is not None]
    for _ in tqdm(range(num_employees), desc='Создание сотрудников'):
        full_name = fake.name()
        job_title = fake.job()
        employment_date = fake.date_this_decade()
        salary = round(random.uniform(50000, 150000), 2)
        department = random.choice(skip_first_lvl)
        employee = Employee(
            full_name=full_name,
            job_title=job_title,
            employment_date=employment_date,
            salary=salary,
            department=department
        )
        employee.save()


if __name__ == '__main__':
    departments = create_department(25)
    print('Отделы успешно созданы')
    print('Создаем работников')
    create_employees(5000, departments)
    print('База данных успешно заполнена')
