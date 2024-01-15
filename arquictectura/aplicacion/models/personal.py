from django.db import models
from almacen import Almacen
from inventario import Inventario

class Personal(models.Model):
    nombre = models.CharField(max_length = 50)
    telefono = models.IntegerField()
    email = models.EmailField()  
    edad = models.IntegerField()
    almacen = models.ForeignObject(Almacen, on_delete = models.CASCADE, related_name = 'Almacenes')
    inventario = models.ForeignKey(Inventario, on_delete = models.CASCADE, related_name = 'Inventarios')
    class Meta:
        abstract = True