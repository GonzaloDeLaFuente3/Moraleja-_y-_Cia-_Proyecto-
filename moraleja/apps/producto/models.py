from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField

# Create your models here.

class Producto(models.Model):

    nombre = models.CharField(max_length=51)
    imagen = models.ImageField(upload_to="productos", blank=True)
    descripcion = RichTextField()
    beneficios = RichTextField()
    slug = AutoSlugField(populate_from='nombre', unique=True, null=True, default=None)
    vigencia = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

