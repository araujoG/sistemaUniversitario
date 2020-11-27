from django.shortcuts import render
from aluno.models import Aluno
import csv


def index(request):
    frase = "esta é a frase da index candyStore"
    alunos = Aluno.objects.all()
    return render(request, 'index.html')

def index2(request):
    print("entrou")
    populaAlunoFromCsv()
    print("populou")
    frase = "esta é a frase da index candyStore"
    alunos = Aluno.objects.all()
    return render(request, 'index2.html')

def populaAlunoFromCsv():
    with open('static/datasets/notas.csv', newline="") as entradaCsv:
        leitorCsv = csv.DictReader(entradaCsv)
        dicionarioDeCr = {}
        for linha in leitorCsv:
            a = Aluno(matricula=linha["MATRICULA"],curso = linha["COD_CURSO"])
            print(a)
            a.save()