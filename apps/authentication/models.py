from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200,null=True)
    last_name = models.CharField(max_length=200,null=True)
    cel = models.CharField(max_length=10)
    user = models.OneToOneField(User, on_delete=models.PROTECT, primary_key=True)

    def __str__(self):
        return f'{self.user}'
