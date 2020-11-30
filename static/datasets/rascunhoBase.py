
# with open('static/datasets/notas.csv', newline="") as entradaCsv:
#     leitorCsv = csv.DictReader(entradaCsv)
#     dicionarioDeCr = {}
#     for linha in leitorCsv:
#         if dicionarioDeCr.get(linha['MATRICULA'], None) != None:
#             dicionarioDeCr[linha['MATRICULA']] = [int(linha["NOTA"]) + int(dicionarioDeCr[linha['MATRICULA']][0]), dicionarioDeCr[linha['MATRICULA']][1] + 1]
#         else:
#             dicionarioDeCr[linha['MATRICULA']] = [int(linha["NOTA"]), 1]
#     print(dicionarioDeCr)
import csv
from aluno.models import Aluno, DisciplinaCursada
from django.db.models import Sum, Count, F
from feedDeDados.models import FeedDeDados
from curso.models import Curso
Curso.objects.get(codigo=31).disciplina__set.all().count()

curso = Curso.objects.get(codigo='TET00186').disciplina_set.all().count()
curso.disciplina__set.all().count()

d = DisciplinaCursada.objects.select_related('disciplina').annotate(curso=F('disciplina__cursoAssociado__codigo')).filter(curso=4)

DisciplinaCursada.objects.filter(aluno__matricula=100).select_related('disciplina')

from django.db import connection
print('conexões')
print(len(connection.queries))
feed = FeedDeDados.objects.get(nomeArquivo='notas.csv')
s = (len(connection.queries))
feed.apagaBd()
print("queries pra apagar: {}".format(s-len(connection.queries)))
s = (len(connection.queries))
feed.populaBd2()
print("queries pra popular com bulk: {}".format(s-len(connection.queries)))
s = (len(connection.queries))
feed.apagaBd()
print("queries pra apagar: {}".format(s-len(connection.queries)))
s = (len(connection.queries))
feed.populaBd()
print("queries pra popular sem bulk: {}".format(s-len(connection.queries)))

exit()


# DisciplinaCursada.objects.select_related('disciplina').annotate(curso=F('disciplina__curso')) #query com os cursos de cada disciplina

# alunos = DisciplinaCursada.objects.select_related('aluno','disciplina').values('aluno','aluno__curso').annotate(notaCarga=Sum(F('nota')*F('disciplina__cargaHoraria')), cargaHoraria= Sum(F('disciplina__cargaHoraria')))
# alunos = alunos.values('aluno','aluno__curso').annotate(cr=F('notaCarga') / F('cargaHoraria'))

# try:
#     open('static/datasets/a', newline="")
# except IOError:
#     print ("Error: File does not appear to exist.")
