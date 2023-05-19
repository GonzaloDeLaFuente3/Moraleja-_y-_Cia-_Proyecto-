from django.db import models

# Create your models here.

class Seccion(models.Model):

    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=1200)
    imagen = models.ImageField(upload_to="admin-interface/img", blank=True)