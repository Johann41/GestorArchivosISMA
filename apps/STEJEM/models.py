from django.db import models

# Create your models here.
class areas_Salas(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return "{}".format(self.nombre)
    
    class Meta: 
        db_table = "areas_Salas"

class distrito_Juzgado(models.Model):
    nombre = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return "{}".format(self.nombre)
    
    class Meta: 
        db_table = "distrito_Juzgados"

class areas_Juzgado(models.Model):
    nombre = models.CharField(max_length=100, null=True)
    distrito = models.ForeignKey(distrito_Juzgado, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "{} ({})".format(self.nombre, self.distrito)
    
    class Meta: 
        db_table = "areas_Juzgados"