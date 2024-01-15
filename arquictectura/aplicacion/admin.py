from django.contrib import admin

# Register your models here.
from .models import Almacen
from .models import Gestor
from .models import Inventario
from .models import Jefe
from .models import Operador
from .models import Orden
from .models import Personal
from .models import Producto

class AlmacenAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'telefono', 'email', 'ubicacion')
    search_fields = ('id', 'nombre', 'telefono', 'email', 'ubicacion')

admin.site.register(Almacen, AlmacenAdmin)

class PersonalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'email', 'edad', 'almacen', 'inventario')
    search_fields = ('nombre', 'telefono', 'email', 'edad', 'almacen', 'inventario')

admin.site.register(Personal, PersonalAdmin)
class GestorAdmin(admin.ModelAdmin):
    list_display = ('id_gestor')
    search_fields = ('id_gestor')

admin.site.register(Gestor, PersonalAdmin)

class InventarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'cantidad')
    search_fields = ('id', 'cantidad')

admin.site.register(Inventario, InventarioAdmin)

class JefeAdmin(admin.ModelAdmin):
    list_display = ('id_jefe')
    search_fields = ('id_jefe')

admin.site.register(Jefe, PersonalAdmin)

class OperadorAdmin(admin.ModelAdmin):
    list_display = ('id_operador')
    search_fields = ('id_operador')

admin.site.register(Operador, PersonalAdmin)



class ProductoAdmin(admin.ModelAdmin):
    list_display = ('cantidad', 'categoria', 'nombre', 'estado', 'fechaCaducidad', 'fechaEntrada', 'novedad', 'inventario', 'almacen')
    search_fields = ('cantidad', 'categoria', 'nombre', 'estado', 'fechaCaducidad', 'fechaEntrada', 'novedad', 'inventario', 'almacen')

admin.site.register(Producto, ProductoAdmin)