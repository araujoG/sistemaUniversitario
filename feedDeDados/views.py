from django.shortcuts import get_object_or_404, redirect, render
from feedDeDados.models import FeedDeDados
from feedDeDados.forms import FeedDeDadosForm, SelecaoFeedDeDadosForm

def cadastraFeed(request):
    if request.POST:
        form = FeedDeDadosForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)
            feed.save()
            return redirect('feedDeDados:selecionaFeed')
    else:
        form = FeedDeDadosForm()
    return render(request, 'feedDeDados/cadastro.html', {'form':form})

def selecionaFeed(request):
    if request.GET:
        form = SelecaoFeedDeDadosForm(request.GET)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            feedSelecionado = get_object_or_404(FeedDeDados, nomeArquivo=nome)
            feedSelecionado.substituiBd()
            return redirect('aluno:listaAluno')
    else:
        form = SelecaoFeedDeDadosForm()
    return render(request, 'feedDeDados/selecao.html', {'form':form})
    

