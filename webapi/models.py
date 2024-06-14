from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Custom user
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('student', 'Estudante'),
        ('employee', 'Funcionario'),
        ('teacher', 'Docente'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


class Curso(models.Model):
    idCurso = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    duracao_em_anos = models.IntegerField()
    semestre = models.IntegerField(default=1)

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    idDisciplina = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField(help_text="Carga horária em horas")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='disciplinas')

    def __str__(self):
        return self.nome


class Turma(models.Model):
    idTurma = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='turmas')
    disciplinas = models.ManyToManyField(Disciplina, related_name='turmas')
    ano = models.IntegerField()

    def __str__(self):
        return f"{self.nome} ({self.ano})"


class Funcionario(models.Model):
    idFuncionario = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.nome


class Estudante(models.Model):
    idEstudante = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    nome_do_pai = models.CharField(max_length=350)
    nome_da_mae = models.CharField(max_length=350)
    apelido = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    numero_bi = models.IntegerField()
    nuit = models.IntegerField()
    data_emissao = models.DateField()
    data_expira = models.DateField()
    endereco = models.CharField(max_length=225)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    matricula = models.CharField(max_length=20, unique=True)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='estudantes')
    user = models.ForeignKey(CustomUser, on_delete=models.SET_DEFAULT, default=1)
    # avaliacoes
    teste1 = models.IntegerField()
    teste2 = models.IntegerField()
    teste3 = models.IntegerField()
    trabalho1 = models.IntegerField()
    exame_normal = models.IntegerField()
    exame_recorrencia = models.IntegerField()
    situacao = models.CharField(max_length=200)
    # extras
    escola_anterior = models.CharField(max_length=800)
    ano_conclusao = models.DateField()

    def __str__(self):
        return self.nome


class Docente(models.Model):
    idDocente = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    numero_bi = models.IntegerField()
    nuit = models.IntegerField()
    data_emissao = models.DateField()
    data_expira = models.DateField()
    endereco = models.CharField(max_length=225)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    disciplinas = models.ManyToManyField(Disciplina, related_name='docentes')
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE, related_name='docentes')
    user = models.ForeignKey(CustomUser, on_delete=models.SET_DEFAULT, default=1)

    def __str__(self):
        return self.nome


"""
from django.db import models

# Create your models here.
from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    duracao_em_anos = models.IntegerField()

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField(help_text="Carga horária em horas")
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='disciplinas')

    def __str__(self):
        return self.nome

class Turma(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='turmas')
    disciplinas = models.ManyToManyField(Disciplina, related_name='turmas')
    ano = models.IntegerField()

    def __str__(self):
        return f"{self.nome} ({self.ano})"
"""