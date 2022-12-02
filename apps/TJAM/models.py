from django.db import models

# Create your models here.
class TJAM_instancia(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return "{}".format(self.nombre)
    class Meta:
        db_table = "instancias_de_TJAM"

class TJAM_numero(models.Model):
    numero = models.CharField(max_length=100)
    instancia = models.ForeignKey(TJAM_instancia, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "{} ({})".format(self.numero, self.instancia)
    class Meta:
        db_table = "numero_de_TJAM"
       
class TJAM_tipo(models.Model):
    tipo = models.CharField(max_length=50)
    instancia = models.ForeignKey(TJAM_instancia,on_delete=models.CASCADE)


    def __str__(self) -> str:
        return "{} ({})".format(self.tipo, self.instancia)
    class Meta:
        db_table = "tipo_de_TJAM"