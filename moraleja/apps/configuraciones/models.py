from django.db import models
from django.core.cache import cache
# Create your models here.

from django.db import models

class SingletonConfiguracion(models.Model):

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        pass

    def set_cache(self):
        cache.set(self.__class__.__name__, self)

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonConfiguracion, self).save(*args, **kwargs)

        self.set_cache()

    @classmethod
    def load(cls):
        if cache.get(cls.__name__) is None:
            obj, created = cls.objects.get_or_create(pk=1)
            if not created:
                obj.set_cache()
        return cache.get(cls.__name__)


class Configuraciones(SingletonConfiguracion):

    telefono1 = models.CharField(max_length=250)
    telefono2 = models.CharField(max_length=250, blank=True)
    linklinkedin = models.URLField(max_length=200)
    linkinstagram = models.URLField(max_length=200)

    class Meta:
        verbose_name_plural = "Configuraciones"

    def __str__(self):
        return "Configuraciones"