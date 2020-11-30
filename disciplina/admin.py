from django.contrib import admin
from .models import Disciplina

# Register your models here.
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'cargaHoraria', 'cursoAssociado']
    search_fields = ['codigo', 'cargaHoraria', 'cursoAssociado']
    list_filter = ['cargaHoraria', 'cursoAssociado']
    actions = []
    save_as = True

admin.site.register(Disciplina, DisciplinaAdmin)