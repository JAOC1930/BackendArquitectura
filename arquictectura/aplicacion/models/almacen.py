from django.db import models

# Create your models here.
class Almacen(models.Model):
    nombre = models.CharField(max_length = 50)
    telefono = models.IntegerField()
    email = models.EmailField()
    ubicacion = models.CharField(max_length = 50)

    def notificaLlegada():
        pass