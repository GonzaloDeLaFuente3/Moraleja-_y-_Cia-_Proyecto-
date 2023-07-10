from django.contrib import admin
from solo.admin import SingletonModelAdmin
from apps.seccion.models import Nosotros, Historia, Servicios


# Register your models here.

@admin.register(Nosotros)
class NosotrosAdmin(SingletonModelAdmin):
    actions = None
    def has_add_permission(self, request):
        # Deshabilitar la opción de agregar
        return False

    def has_delete_permission(self, request, obj=None):
        # Deshabilitar la opción de eliminar
        return False

@admin.register(Historia)
class HistoriaAdmin(SingletonModelAdmin):
    actions = None
    def has_add_permission(self, request):
        # Deshabilitar la opción de agregar
        return False

    def has_delete_permission(self, request, obj=None):
        # Deshabilitar la opción de eliminar
        return False


class ServiciosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'vigencia'] #desde la lista
    fields = ['nombre', 'descripcion', 'imagen'] #desde el editor

    def get_fields(self, request, obj=None):
        if obj:
            # Si el objeto ya existe, mostrar el campo "vigencia"
            return self.fields + ['vigencia']
        else:
            # Si es un nuevo objeto, mostrar solo los campos predeterminados
            return self.fields

    # campos
    # list_display = ["id", "fechaPedido", "cliente", "estadoPedido", "comentario","envioDomicilio", "tiempoDemora", "cadete","total"]
    #  # campos que se pueden modificar
    # list_editable = ["fechaPedido", "cliente", "estadoPedido","envioDomicilio", "tiempoDemora", "cadete","total"]

admin.site.register(Servicios, ServiciosAdmin)
