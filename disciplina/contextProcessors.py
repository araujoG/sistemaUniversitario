from disciplina.models import Disciplina

def tabelaVazia(request):
    numLinhas = Disciplina.objects.all().count()
    return {
        'nDisciplinas': numLinhas
    }
