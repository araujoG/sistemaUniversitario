from django.db import models
from disciplina.models import Disciplina
import csv


class Aluno(models.Model):
    matricula = models.CharField(max_length=8, db_index=True, unique=True, primary_key=True)
    curso = models.CharField(max_length=5)
    disciplinas = models.ManyToManyField(Disciplina, through='DisciplinaCursada')

    class Meta:
        db_table = 'aluno'

    def __str__(self):
        return self.matricula

    

# Create your models here.
class DisciplinaCursada(models.Model):
    disciplina = models.ForeignKey(Disciplina, db_index=True, on_delete=models.PROTECT, null=False, to_field='codigo')
    aluno = models.ForeignKey(Aluno, db_index=True, on_delete=models.PROTECT, null=False, to_field='matricula')
    nota = models.IntegerField(default=0) ##Validar: 0->100 , max_value = 100, min_values = 0
    anoSemestre = models.CharField(max_length=5, default="")


    class Meta:
        db_table = 'disciplinaCursada'
        unique_together = ['disciplina', 'aluno','anoSemestre']

    def __str__(self):
        return str(self.disciplina)