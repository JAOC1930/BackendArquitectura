from django.shortcuts import render
from rest_framework import viewsets, permissions
from aplicacion.models import Inventario, Almacen, RolPersona, Personal, CategoriaProducto, Producto
from aplicacion.serializers import InventarioSerializer, AlmacenSerializer, RolPersonaSerializer, PersonalSerializer, CategoriaProductoSerializer, ProductoSerializer
# Create your views here.

## Todo inventario
def index(request):
    pass


def RegistraProducto(request):
    pass

def devuelveExistenciaProducto(request):
    pass

def actualizaStock(request):
    pass

def devuelveDetallesProducto(request):
    pass

def devuelveDetallesNovedades(request):
    pass

def registrarMotivoRetiro(request):
    pass

def devuelveDetallesProductoEmpacado(request):
    pass

def devuelveDetallesLlegada(request):
    pass

########################################################

## Almacen

def notificaLlegada():
    pass


# Operador
def seleccionaProductoEmpacar():
        pass

def transportarProducto():
    pass

def registrarLlegadaProdcuto():
    pass


# Jefe

def empacaProducto():
        pass

def seleccionarProducto():
    pass

def despacharProcuto():
    pass

def asignarUbicacion():
    pass


# Gestor

def verificarDetalleProducto():
        pass

def retirarProductoMalE():
    pass

################################################
# API REST

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
    permission_classes = [permissions.IsAuthenticated]

class AlmacenViewSet(viewsets.ModelViewSet):
    queryset = Almacen.objects.all()
    serializer_class = AlmacenSerializer
    permission_classes = [permissions.IsAuthenticated]

class RolPersonaViewSet(viewsets.ModelViewSet):
    queryset = RolPersona.objects.all()
    serializer_class = RolPersonaSerializer
    permission_classes = [permissions.IsAuthenticated]

class PersonalViewSet(viewsets.ModelViewSet):
    queryset = Personal.objects.all()
    serializer_class = PersonalSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoriaProductoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]

