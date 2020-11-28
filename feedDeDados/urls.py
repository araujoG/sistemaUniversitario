from django.urls import path

from feedDeDados import views

app_name = 'feedDeDados'

urlpatterns = [
    path('cadastro/', views.cadastraFeed, name="cadastraFeed"),
    path('selecao/', views.selecionaFeed, name="selecionaFeed"),
]