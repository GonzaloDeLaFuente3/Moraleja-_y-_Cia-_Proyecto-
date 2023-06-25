from django.db import models
from autoslug import AutoSlugField

# Create your models here.

class Producto(models.Model):

    nombre = models.CharField(max_length=51)
    imagen = models.ImageField(upload_to="media/productos", blank=True)
    descripcion = models.TextField(max_length=1200)
    slug = AutoSlugField(populate_from='nombre', unique=True, null=True, default=None)

    def __str__(self):
        return self.nombre

class BeneficioProducto(models.Model):

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='beneficio_producto',default=None)
    descripcion = models.TextField(max_length=2000)

