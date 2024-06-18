from django.db import models
from django.core.exceptions import ValidationError


class Department(models.Model):
    '''
    Модель отделов
    ### Attrs:
    - name (str) - Название отдела
    - parent(FK) - Поле связи с этой моделью, для создания иерархической структуры
    '''
    name: models.CharField = models.CharField(
        max_length=200, verbose_name='Название отдела',
        help_text='Укажите название отдела, максимум 200 символов')
    parent: models.ForeignKey = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        null=True, blank=True, related_name='children',
        verbose_name='Родительский отдел', help_text='Название вышестоящего отдела'
    )

    def __str__(self):
        return f'{self.name}, вышестоящий отдел - {self.parent}'

    def clean(self):
        '''
        Функция для валидации уровня вложенности
        '''
        current_level = 0
        parent = self.parent
        while parent is not None:
            current_level += 1
            if current_level >= 5:
                raise ValidationError(
                    'Нельзя создавать больше 5 вложенностей отделов'
                )
            parent = parent.parent

    def save(self, *args, **kwargs):
        self.clean()
        super(Department, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'
        ordering = ['name']
