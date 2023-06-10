from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    #ALUNOS
    path('alunos/', views.ViewAluno.ver_todos_alunos, name='home'),
    path('pesquisa-alunos/', views.ViewAluno.pesquisar_aluno, name='busca'),
    path('detalhes/<int:id>', views.ViewAluno.pesquisar_aluno, name='detalhes'),
    path('deletar/<int:id>', views.ViewAluno.pesquisar_aluno, name='deletar'),
    path('adicionar/', views.ViewAluno.pesquisar_aluno, name='adicionar'),
    path('editar/<int:id>', views.ViewAluno.pesquisar_aluno, name='editar'),
]