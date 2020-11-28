from aluno.models import Aluno


def tabelaVazia(request):
    numLinhas = Aluno.objects.all().count()
    if(numLinhas == 0):
        return {
            'tabelaAlunoVazia': True, 'nAlunos': numLinhas
        }
    return {
        'tabelaAlunoVazia': False, 'nAlunos': numLinhas
    }
