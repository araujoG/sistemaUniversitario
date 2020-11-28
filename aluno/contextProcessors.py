from aluno.models import Aluno


def tabelaVazia(request):
    numLinhas = Aluno.objects.all().count()
    return {
        'nAlunos': numLinhas
    }
