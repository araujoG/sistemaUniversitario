from django.shortcuts import render
from aluno.models import Aluno, DisciplinaCursada

def listaAluno(request):
    alunos = DisciplinaCursada.objects.select_related('aluno').order_by('aluno')
    return render(request, 'aluno/index.html', {'alunos':alunos})