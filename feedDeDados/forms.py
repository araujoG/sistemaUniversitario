from feedDeDados.models import FeedDeDados
from django.core.validators import RegexValidator


class FeedDeDadosFormForm(forms.ModelForm):

    class Meta:
        model = FeedDeDados
        fields = ("nomeArquivo", "dataCarregamento")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nomeArquivo'].validators=[
            RegexValidator(regex='^[a-z]+\.(csv)$', message='Nome do arquivo de dados é inválido.')]