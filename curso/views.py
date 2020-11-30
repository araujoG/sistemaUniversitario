from django.shortcuts import get_object_or_404, render
from django.db.models import F, Sum
from aluno.models import DisciplinaCursada
from curso.models import Curso

def listaCurso(request):
    # as queries estão retornando inteiro e não float
    cursos = DisciplinaCursada.objects.select_related('disciplina').annotate(curso=F('disciplina__cursoAssociado__codigo')).values('curso').annotate(notaCarga=Sum(F('nota')*F('disciplina__cargaHoraria')), cargaHoraria= Sum(F('disciplina__cargaHoraria')))
    cursos = cursos.values('curso').annotate(cr=F('notaCarga') / F('cargaHoraria'))
    print(cursos)
    for curso in cursos:
        curso['curso'] = get_object_or_404(Curso, codigo = curso['curso'] )
    print(cursos)
    return render(request, 'curso/index.html', {'cursos':cursos})
