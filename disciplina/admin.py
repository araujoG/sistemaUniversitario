from django.contrib import admin
from .models import Disciplina

# Register your models here.
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'cargaHoraria']
    search_fields = ['codigo', 'cargaHoraria']
    list_filter = ['codigo', 'cargaHoraria']
    actions = []
    save_as = True

admin.site.register(Disciplina, DisciplinaAdmin)