from django.shortcuts import redirect, render
from feedDeDados.models import FeedDeDados
from feedDeDados.forms import FeedDeDadosForm, SelecaoFeedDeDadosForm

def cadastraFeed(request):
    form = FeedDeDadosForm()
    return render(request, 'feedDeDados/cadastro.html', {'form':form})

def selecionaFeed(request):
    form = SelecaoFeedDeDadosForm(request.GET)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        return redirect('aluno:listaAluno')
    else:
        return render(request, 'feedDeDados/selecao.html', {'form':form})
    

