from django.urls import path

from curso import views

app_name = 'curso'

urlpatterns = [
    path('', views.listaCurso, name="listaCurso"),
]