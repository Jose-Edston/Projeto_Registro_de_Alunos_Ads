from django.contrib import admin
from .models import Aluno, Nota, Turma, Frequencia

admin.site.register(Aluno)
admin.site.register(Nota)
admin.site.register(Turma)
admin.site.register(Frequencia)
