from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    #ALUNOS
    path('alunos/', views.ViewAluno.ver_todos_alunos, name='home'),
    path('pesquisa-alunos/', views.ViewAluno.pesquisar_aluno, name='busca'),
    path('detalhes/<int:id>', views.ViewAluno.pesquisar_aluno, name='detalhes'),
    path('deletar/<int:id>', views.ViewAluno.pesquisar_aluno, name='deletar'),
    path('adicionar/', views.ViewAluno.adicionar_aluno, name='adicionar'),
    path('editar/<int:id>', views.ViewAluno.pesquisar_aluno, name='editar'),
    path('accounts/', include('accounts.urls')),
    #NOTAS
    path('notas/', views.ViewNota.ver_todas_notas, name='home_nota'),
    #FREQUENCIA
    path('frequencia/', views.ViewFrequencia.ver_todas_frequencias, name='home_frequencia'),
    
]