from django.db import models

from apps.producto.models import Producto


# Create your models here.

class Receta(models.Model):

    nombre = models.CharField(max_length=100)
    productos = models.ManyToManyField(Producto)
    ingredientes = models.TextField(max_length=2000)
    cantidad_personas = models.IntegerField()
    elaboracion = models.TextField(max_length=2000)
    imagen = models.ImageField(upload_to="admin-interface/img", blank=True)
