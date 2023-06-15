from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    #ALUNOS
    path('accounts/', include('accounts.urls')),
    path('alunos/', views.ViewAluno.ver_todos_alunos, name='home'),
    path('pesquisa-alunos/', views.ViewAluno.pesquisar_aluno, name='busca'),
    path('deletar/<int:id>', views.ViewAluno.pesquisar_aluno, name='deletar'),
    path('adicionar/', views.ViewAluno.adicionar_aluno, name='adicionar'),
    path('editar/<int:numero_matricula>', views.ViewAluno.editar_aluno, name='editar_aluno'),

    #NOTAS
    path('cadastrar_nota/<int:numero_matricula>', views.ViewNota.cadastrar_nota, name='cadastro_nota'),

    #FREQUENCIA
    path('frequencia/<int:numero_matricula>', views.ViewFrequencia.cadastrar_frequencia, name='cadastrar_frequencia'),
    
]