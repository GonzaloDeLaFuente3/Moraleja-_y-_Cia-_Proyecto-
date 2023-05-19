from django.db import models

# Create your models here.

class Noticia(models.Model):

    volanta = models.CharField(max_length=200)
    titular = models.CharField(max_length=200)
    autor_a = models.CharField(max_length=200)
    cuerpo = models.TextField(max_length=2000)
    imagen = models.ImageField(upload_to="admin-interface/img", blank=True)
    epigrafe = models.CharField(max_length=200)