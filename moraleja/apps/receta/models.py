from django.db import models
from autoslug import AutoSlugField

from apps.producto.models import Producto


# Create your models here.

class Receta(models.Model):

    nombre = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='nombre', unique=True, null=True, default=None)
    productos = models.ManyToManyField(Producto)
    ingredientes = models.TextField(max_length=2000)
    cantidad_personas = models.IntegerField()
    elaboracion = models.TextField(max_length=2000)
    imagen = models.ImageField(upload_to="media/recetas", blank=True)

    def __str__(self):
        return self.nombre
