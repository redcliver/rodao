from django.db import models

# Create your models here.
class cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    celular = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=200)
    insc = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome