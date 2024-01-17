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
from .models import Medicamento
from .models import InsumoMedico
from .models import DipositivoMedico

class AlmacenAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'email', 'ubicacion', 'inventario')
    search_fields = ('id', 'nombre', 'telefono', 'email', 'ubicacion', 'inventario__cantidad')

admin.site.register(Almacen, AlmacenAdmin)


class PersonalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'email',
                    'edad', 'almacen', 'inventario')
    search_fields = ('nombre', 'telefono', 'email',
                     'edad', 'almacen', 'inventario')


admin.site.register(Personal, PersonalAdmin)

class InventarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'cantidad')
    search_fields = ('id', 'cantidad')


admin.site.register(Inventario, InventarioAdmin)

class GestorAdmin(admin.ModelAdmin):
    search_fields = ('id_gestor',)

admin.site.register(Gestor, GestorAdmin)

class JefeAdmin(admin.ModelAdmin):
    search_fields = ('id_jefe',)

admin.site.register(Jefe, JefeAdmin)

class OperadorAdmin(admin.ModelAdmin):
    search_fields = ('id_operador',)

admin.site.register(Operador, OperadorAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('cantidad', 'categoria', 'nombre', 'estado', 'fechaCaducidad', 'fechaEntrada', 'novedad', 'inventario')
    search_fields = ('nombre',)  # Agregado 'nombre' para la búsqueda

admin.site.register(Producto, ProductoAdmin)


class OrdenAdmin(admin.ModelAdmin):
    list_display = ('ordenEnvio', 'fechaGeneracion')
    search_fields = ('ordenEnvio', 'fechaGeneracion')


admin.site.register(Orden, OrdenAdmin)

class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('id_medicamento', 'producto')
    search_fields = ('id_medicamento', 'producto')



admin.site.register(Medicamento, MedicamentoAdmin)


class InsumoMedicoAdmin(admin.ModelAdmin):
    list_display = ('id_insu_medi', 'producto')
    search_fields = ('id_insu_medi', 'producto__nombre')

admin.site.register(InsumoMedico, InsumoMedicoAdmin)

class DipositivoMedicoAdmin(admin.ModelAdmin):
    list_display = ('id_disp_medi', 'producto')
    search_fields = ('id_disp_medi', 'producto__nombre')

admin.site.register(DipositivoMedico, DipositivoMedicoAdmin)

