from django.contrib import admin
from .models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_parent')
    search_fields = ('name', 'parent__name')
    ordering = ('name',)

    def get_parent(self, obj):
        return obj.parent.name if obj.parent else 'Это самый главный отдел!'
    get_parent.short_description = 'Вышестоящий отдел'
