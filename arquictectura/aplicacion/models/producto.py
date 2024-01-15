from django.db import models
from almacen import Almacen
from inventario import Inventario

class Producto(models.Model):
    cantidad = models.IntegerField()
    categoria = models.CharField(max_length = 30)
    nombre = models.CharField(max_length = 30)
    estado = models.CharField(max_length = 30)
    fechaCaducidad = models.DateField()
    fechaEntrada = models.DateField()
    novedad = models.CharField(max_length = 50)
    inventario = models.ForeignKey(Inventario, on_delete = models.CASCADE, related_name = 'Inventarios')
    almacen = models.ManyToManyField(Almacen)
    
    class Meta:
        abstract = True  # Hace que esta clase sea abstracta, no se crea en la base de datos

class Medicamento(Producto):
    id_medicamento = models.IntegerField()

class InsumoMedico(Producto):
    id_insu_medi = models.IntegerField()

class DipositivoMedico(Producto):
    id_disp_medi = models.IntegerField()