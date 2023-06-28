from django.contrib import admin
from apps.noticia.models import Noticia

# Register your models here.

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor_a','fecha_creacion'] #desde la lista
    #fields = ['nombre', 'imagen', 'descripcion'] #desde el editor

    # def get_fields(self, request, obj=None):
    #     if obj:
    #         # Si el objeto ya existe, mostrar el campo "vigencia"
    #         return self.fields + ['vigencia']
    #     else:
    #         # Si es un nuevo objeto, mostrar solo los campos predeterminados
    #         return self.fields

admin.site.register(Noticia, NoticiaAdmin)
