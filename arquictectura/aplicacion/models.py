from django.db import models

# Create your models here.


class Almacen(models.Model):
    nombre = models.CharField(max_length = 50)
    telefono = models.IntegerField()
    email = models.EmailField()
    ubicacion = models.CharField(max_length = 50)

    def notificaLlegada():
        pass


class Inventario(models.Model):
    cantidad = models.IntegerField()

    def devuelveExistenciaProducto():
        pass

    def registraProducto():
        pass

    def actualizaStock():
        pass

    def devuelveDetallesProducto():
        pass

    def devuelveDetallesNovedades():
        pass

    def registrarMotivoRetiro():
        pass

    def devuelveDetallesProductoEmpacado():
        pass

    def devuelveDetallesLlegada():
        pass

    
class Personal(models.Model):
    nombre = models.CharField(max_length = 50)
    telefono = models.IntegerField()
    email = models.EmailField()  
    edad = models.IntegerField()
    almacen = almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE, related_name='Almacenes')
    inventario = models.ForeignKey(Inventario, on_delete = models.CASCADE, related_name = 'Inventarios')
    class Meta:
        abstract = True

class Gestor(Personal):
    id_gestor = models.CharField(max_length = 30)

    def verificarDetalleProducto():
        pass

    def retirarProductoMalE():
        pass


class Jefe(Personal):
    id_jefe = models.CharField(max_length = 30)

    def empacaProducto():
        pass

    def seleccionarProducto():
        pass

    def despacharProcuto():
        pass

    def asignarUbicacion():
        pass

class Operador(Personal):
    id_operador = models.CharField(max_length = 30)

    def seleccionaProductoEmpacar():
        pass

    def transportarProducto():
        pass

    def registrarLlegadaProdcuto():
        pass

class Orden(models.Model):
    ordenEnvio = models.CharField(max_length = 60)
    fechaGeneracion = models.DateTimeField()

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