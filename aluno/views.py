from django.shortcuts import get_object_or_404, render
from aluno.models import Aluno, DisciplinaCursada
from django.db.models import Sum, Count, F

def listaAluno(request):
    # as queries estão retornando inteiro e não float
    alunos = DisciplinaCursada.objects.select_related('aluno','disciplina').values('aluno').annotate(notaCarga=Sum(F('nota')*F('disciplina__cargaHoraria')), cargaHoraria= Sum(F('disciplina__cargaHoraria')))
    alunos = alunos.values('aluno').annotate(cr=F('notaCarga') / F('cargaHoraria'))
    for aluno in alunos:
        aluno['aluno'] = get_object_or_404(Aluno, matricula = aluno['aluno'] )
        aluno['aluno'] = aluno.pop('aluno', None)
    print(alunos)
    return render(request, 'aluno/index.html', {'alunos':alunos})