from django.db import models
from solo.models import SingletonModel
from ckeditor.fields import RichTextField
# Create your models here.

class Seccion(models.Model):
    titulo = models.CharField(max_length=50)

class Nosotros(SingletonModel):

    descripcion = RichTextField()
    imagen = models.ImageField(upload_to="img", blank=True)

    class Meta:
        verbose_name_plural = "Nosotros"

    def __str__(self):
        return "Nosotros"

class Historia(SingletonModel):

    descripcion = RichTextField()
    imagen = models.ImageField(upload_to="img", blank=True)

    class Meta:
        verbose_name_plural = "Historia"

    def __str__(self):
        return "Historia"

class Servicios(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = RichTextField()
    imagen = models.ImageField(upload_to="servicios", blank=True)
    vigencia = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Servicios"