from django.db import models

class Aluno(models.Model):
    numero_matricula = models.IntegerField(unique=True)
    nome = models.CharField(max_length=255)
    imagem = models.ImageField()
    cpf = models.CharField(max_length=14)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    telefone_emergencia = models.CharField(max_length=20)
    historico_familiar = models.TextField(null=True, blank=True)
    data_nascimento = models.DateField()
    aprovado = models.BooleanField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Aluno'

class Turma(models.Model):
    matricula_aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    porcentagem_aprovacao = models.IntegerField()
    media_frequencia = models.FloatField()
    media_notas = models.FloatField



class Nota(models.Model):
   matricula_aluno = models.ForeignKey(Aluno, on_delete=models.DO_NOTHING)
   disciplina = models.CharField(max_length=20)
   peso = models.IntegerField()
   nota_1 = models.FloatField()
   nota_2 = models.FloatField()
   nota_3 = models.FloatField()
   nota_4 = models.FloatField()
   nota_final = models.FloatField()

class Frequencia(models.Model):
    matricula_aluno = models.ForeignKey(Aluno, on_delete=models.DO_NOTHING)
    disciplina = models.CharField(max_length=20)
    data = models.DateField()
    presenca = models.BooleanField()
    falta = models.IntegerField()
    

