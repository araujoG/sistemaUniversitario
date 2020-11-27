from feedDeDados.models import FeedDeDados


class FeedDeDadosFormForm(forms.ModelForm):

    class Meta:
        model = FeedDeDados
        fields = ("nomeArquivo", "dataCarregamento")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
