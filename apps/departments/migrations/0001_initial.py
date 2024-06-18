# Generated by Django 5.0.6 on 2024-06-18 16:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите название отдела, максимум 200 символов', max_length=200, verbose_name='Название отдела')),
                ('parent', models.ForeignKey(blank=True, help_text='Название вышестоящего отдела', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='departments.department', verbose_name='Родительский отдел')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
                'ordering': ['name'],
            },
        ),
    ]
