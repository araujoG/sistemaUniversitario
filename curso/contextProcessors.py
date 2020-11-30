from curso.models import Curso

def tabelaVazia(request):
    numLinhas = Curso.objects.all().count()
    return {
        'nCursos': numLinhas
    }
