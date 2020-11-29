from django.urls import path

from aluno import views

app_name = 'aluno'

urlpatterns = [
    path('', views.listaAluno, name="listaAluno"),
    path('historico/<int:matricula>', views.exibeHistorico, name="exibeHistorico")
]