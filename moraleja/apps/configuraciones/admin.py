from django.contrib import admin
from .models import Configuraciones

# Register your models here.

class ConfiguracionAdmin(admin.ModelAdmin):
    # list_display = ('campo1', 'campo2')
    actions = None  # Removes the default delete action.

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


@admin.register(Configuraciones)
class SiteSettingsAdmin(ConfiguracionAdmin):
    pass