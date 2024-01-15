from django.db import models
from personal import Personal

class Operador(Personal):
    id_operador = models.CharField(max_length = 30)

    def seleccionaProductoEmpacar():
        pass

    def transportarProducto():
        pass

    def registrarLlegadaProdcuto():
        pass

    