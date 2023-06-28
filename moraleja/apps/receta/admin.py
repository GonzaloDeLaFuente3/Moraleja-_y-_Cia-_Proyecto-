from django.contrib import admin
from apps.receta.models import Receta
# Register your models here.

# filtros
# list_filter = ["producto"]

admin.site.register(Receta)
