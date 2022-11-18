from django.db import models
from django.dispatch import receiver
# Create your models here.

class Perfil(models.Model): 
    usuario = models.CharField( max_length=30)
    cel = models.IntegerField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.usuario

