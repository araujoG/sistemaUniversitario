from django.core.management.base import BaseCommand
from django.utils import timezone
from aluno.models import Aluno, DisciplinaCursada
import csv
from disciplina.models import Disciplina

class Command(BaseCommand):
    help = 'Popula o BD através do CSV'

    def handle(self, *args, **kwargs):
        with open('static/datasets/notas.csv', newline="") as entradaCsv:
            leitorCsv = csv.DictReader(entradaCsv)
            dicionarioDeCr = {}
            for linha in leitorCsv:
                a = Aluno(matricula=linha["MATRICULA"],curso = linha["COD_CURSO"])
                print(a)
                a.save()
            #     if dicionarioDeCr.get(linha['MATRICULA'], None) != None:
            #         dicionarioDeCr[linha['MATRICULA']] = [int(linha["NOTA"]) + int(dicionarioDeCr[linha['MATRICULA']][0]), dicionarioDeCr[linha['MATRICULA']][1] + 1]
            #     else:
            #         dicionarioDeCr[linha['MATRICULA']] = [int(linha["NOTA"]), 1]
            # print(dicionarioDeCr)


a = Aluno(matricula=100, curso=1)
d = Disciplina(codigo="tcc123", cargaHoraria="80")
disciplinaCursada = DisciplinaCursada(disciplina=d, aluno=a, nota=10, anoSemestre="20181")
a.disciplinas.add(d)