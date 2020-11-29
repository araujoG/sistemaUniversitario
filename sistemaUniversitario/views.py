from django.shortcuts import render
from aluno.models import Aluno
import csv


def index(request):
    frase = "esta é a frase da index candyStore"
    alunos = Aluno.objects.all()
    return render(request, 'index.html')


