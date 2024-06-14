from django.contrib import admin
from .models import Curso, Disciplina, Turma, Docente, Estudante, Funcionario

admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Turma)
admin.site.register(Estudante)
admin.site.register(Docente)
admin.site.register(Funcionario)
