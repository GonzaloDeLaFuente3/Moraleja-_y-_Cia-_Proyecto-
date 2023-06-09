from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.

class Noticia(models.Model):

    titulo = models.CharField(max_length=200)   #noticias
    slug = AutoSlugField(populate_from='titulo', unique=True, null=True, default=None)
    autor_a = models.CharField(max_length=200)  #noticias
    cuerpo = RichTextField()
    imagen = models.ImageField(upload_to="noticias", blank=True)  #noticias
    epigrafe = models.CharField(max_length=200, blank=True) #acompaña a la imagen
    fecha_creacion = models.DateTimeField(auto_now_add=True)    #noticias

    def __str__(self):
        return self.titulo