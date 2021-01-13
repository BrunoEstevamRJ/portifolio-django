from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    menssagem = models.TextField(max_length=255)

    def __str__(self):
        return self.nome
