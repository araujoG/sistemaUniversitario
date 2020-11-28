from django.contrib import admin
from .models import FeedDeDados

class FeedDeDadosAdmin(admin.ModelAdmin):
    list_display = ['nomeArquivo', 'dataCarregamento']
    search_fields = ['nomeArquivo', 'dataCarregamento']
    list_filter = ['nomeArquivo', 'dataCarregamento']
    actions = []
    save_as = True

admin.site.register(FeedDeDados, FeedDeDadosAdmin)


