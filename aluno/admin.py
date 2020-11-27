from django.contrib import admin
from .models import Aluno, DisciplinaCursada

# Register your models here.
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['matricula', 'curso', ]
    search_fields = ['matricula', 'curso']
    list_filter = ['curso']
    actions = []
    save_as = True

admin.site.register(Aluno, AlunoAdmin)

class DisciplinaCursadaAdmin(admin.ModelAdmin):
    list_display = ['aluno', 'disciplina', 'nota', 'anoSemestre']
    search_fields = ['aluno', 'disciplina']
    list_filter = ['aluno', 'disciplina', 'anoSemestre']
    actions = []
    save_as = True

admin.site.register(DisciplinaCursada, DisciplinaCursadaAdmin)