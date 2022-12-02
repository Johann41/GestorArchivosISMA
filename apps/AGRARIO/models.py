from django.db import models
# Create your models here.

class Tribunales_AGRARIOS(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self) -> str:
        return "{}".format(self.nombre)

    class Meta:
        db_table = "tribunales_AGRARIOS"
