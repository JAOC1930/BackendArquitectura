from django.db import models
from personal import Personal

class Gestor(Personal):
    id_gestor = models.CharField(max_length = 30)

    def verificarDetalleProducto():
        pass

    def retirarProductoMalE():
        pass
