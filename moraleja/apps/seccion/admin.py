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


admin.site.register(Servicios)
