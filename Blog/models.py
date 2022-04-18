from email.policy import default
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class Materia(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome_materia = models.CharField(max_length=200)
    resumo = models.CharField(max_length=400)
    materia = models.TextField()
    categoria = models.CharField(max_length=100)
    data_materia = models.DateTimeField(default=datetime.now, blank=True)
    foto = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    publicada = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_materia
