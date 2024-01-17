from django.db import models

# Create your models here.


class Inventario(models.Model):
    cantidad = models.IntegerField()

class Almacen(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.EmailField()
    ubicacion = models.CharField(max_length=50)
    inventario = models.OneToOneField(Inventario, on_delete=models.CASCADE, related_name='almacen')

class Personal(models.Model):
    nombre = models.CharField(max_length = 50)
    telefono = models.IntegerField()
    email = models.EmailField()  
    edad = models.IntegerField()
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE, related_name='Almacenes')
    inventario = models.ForeignKey(Inventario, on_delete = models.CASCADE, related_name = 'Inventarios')

class Gestor(models.Model):
    id_gestor = models.CharField(max_length = 30)
    personal = models.ForeignKey(Personal, on_delete = models.CASCADE, related_name = 'Personales_gestor')



class Jefe(models.Model):
    id_jefe = models.CharField(max_length = 30)
    personal = models.ForeignKey(Personal, on_delete = models.CASCADE, related_name = 'Personales_jefe')



class Operador(models.Model):
    id_operador = models.CharField(max_length = 30)
    personal = models.ForeignKey(Personal, on_delete = models.CASCADE, related_name = 'Personales_operador')



class Orden(models.Model):
    ordenEnvio = models.CharField(max_length = 60)
    fechaGeneracion = models.DateTimeField()

class Producto(models.Model):
    cantidad = models.IntegerField()
    categoria = models.CharField(max_length=30)
    nombre = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    fechaCaducidad = models.DateField()
    fechaEntrada = models.DateField()
    novedad = models.CharField(max_length=50)
    inventario = models.OneToOneField(Inventario, on_delete=models.CASCADE, related_name='producto')
    # Elimina la relación 'almacen'

class Medicamento(models.Model):
    id_medicamento = models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='medicamentos')

class InsumoMedico(models.Model):
    id_insu_medi = models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='insumos_medicos')

class DipositivoMedico(models.Model):
    id_disp_medi = models.IntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='dispositivos_medicos')