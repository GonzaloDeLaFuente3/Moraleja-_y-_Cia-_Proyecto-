from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from apps.producto.models import Producto

from apps.producto.models import BeneficioProducto


# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    search_fields = ["nombre"]

    # campos
    # list_display = ["id", "fechaPedido", "cliente", "estadoPedido", "comentario","envioDomicilio", "tiempoDemora", "cadete","total"]
    #  # campos que se pueden modificar
    # list_editable = ["fechaPedido", "cliente", "estadoPedido","envioDomicilio", "tiempoDemora", "cadete","total"]
    #
    # # filtros
    # list_filter = ["estadoPedido", "envioDomicilio"]
    #
    # list_per_page = 20

admin.site.register(Producto, ProductoAdmin)
admin.site.register(BeneficioProducto)