from django.db import models

# Create your models here.

class Producto(models.Model):

    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to="admin-interface/img", blank=True)
    descripcion = models.TextField(max_length=1200)

class BeneficioProducto(models.Model):

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='beneficio_producto')
    descripcion = models.TextField(max_length=2000)

