from django.db import models

# Create your models here.
class Cadastro(models.Model):
    nome = models.CharField(max_length=255)
    imagem = models.ImageField()
    cpf = models.CharField(max_length=14)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    telefone_emergencia = models.CharField(max_length=20)
    altura = models.DecimalField(max_digits=3, decimal_places=2)
    historico_familiar = models.TextField(null=True, blank=True)
    data_nascimento = models.DateField()
    ativo = models.BooleanField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Cadastro'
    

