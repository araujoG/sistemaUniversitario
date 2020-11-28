from feedDeDados.models import FeedDeDados
from django.core.validators import RegexValidator
from feedDeDados.validators import validaArquivo


class FeedDeDadosFormForm(forms.ModelForm):

    class Meta:
        model = FeedDeDados
        fields = ("nomeArquivo", "dataCarregamento")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['nomeArquivo'].validators=[
        #     RegexValidator(regex='^[a-z]+\.(csv)$', message='O arquivo de dados deve ter o formato CSV'), validaArquivo]
        self.fields['nomeArquivo'].widget.attrs.update({'class': 'form-control','id':'inputNomeArquivo','placeholder':'Nome do Arquivo de Dados'})

    