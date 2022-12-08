from django.db import models

# Create your models here.
class Circuito(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return "{}".format(self.nombre)

    class Meta:
        db_table = "circuitos_CJF"


class Organo_Jurisdiccional(models.Model):
    circuito = models.ForeignKey(Circuito, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return "{} ({})".format(self.nombre, self.circuito)

    class Meta:
        db_table = "OrganosJurisdiccionales_CJF"