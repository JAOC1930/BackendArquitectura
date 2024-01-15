from django.db import models
from almacen import Almacen

class Orden(models.Model):
    ordenEnvio = models.CharField(max_length = 60)
    fechaGeneracion = models.DateTimeField()
    
    