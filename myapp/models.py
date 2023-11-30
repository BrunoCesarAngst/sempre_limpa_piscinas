from django.db import models
from django.contrib.auth.models import User


class Agendamento(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    piscina = models.ForeignKey('Piscina', on_delete=models.CASCADE, null=True)


class Piscina(models.Model):
    endereco = models.CharField(max_length=255)
    detalhes = models.TextField()
    localizacao = models.CharField(max_length=255)  # Você pode querer usar um campo específico para coordenadas geográficas
