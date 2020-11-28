from django import forms
from feedDeDados.models import FeedDeDados
from django.core.validators import RegexValidator
from feedDeDados.validators import validaArquivo


class SelecaoFeedDeDadosForm(forms.Form):
    
    nome = forms.ModelChoiceField(queryset=FeedDeDados.objects.all(), required=True,empty_label='Selecione um Arquivo')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'custom-select my-1 mr-sm-2'})
        self.fields['nome'].validators=[]

class FeedDeDadosForm(forms.ModelForm):

    class Meta:
        model = FeedDeDados
        fields = ('nomeArquivo',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['nomeArquivo'].validators=[
        #     RegexValidator(regex='^[a-z]+\.(csv)$', message='O arquivo de dados deve ter o formato CSV'), validaArquivo]
        self.fields['nomeArquivo'].widget.attrs.update({'class': 'form-control','id':'inputNomeArquivo','placeholder':'Nome do Arquivo de Dados'})

    