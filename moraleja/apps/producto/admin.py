from django.contrib import admin
from django.db import models
from apps.producto.models import Producto


# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'vigencia'] #desde la lista
    fields = ['nombre', 'imagen', 'descripcion', 'beneficios'] #desde el editor

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

admin.site.register(Producto, ProductoAdmin)