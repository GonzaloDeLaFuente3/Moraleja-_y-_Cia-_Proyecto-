from django.contrib import admin
from .models import Configuraciones
from django import forms

# Register your models here.

class ConfiguracionForm(forms.ModelForm):
    class Meta:
        model = Configuraciones
        fields = '__all__'
        widgets = {
            'telefono_1': forms.TextInput(attrs={'style': 'width: 20em;','placeholder': 'Ejemplo: 5493834999999'}),
        }
        help_texts = {
            'telefono_1': 'Escriba el número sin signos ni espacios "+,-, ", con el código de área del país y provincia correspondiente.',
        }

class ConfiguracionAdmin(admin.ModelAdmin):
    form = ConfiguracionForm
    actions = None  # Removes the default delete action.

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


@admin.register(Configuraciones)
class SiteSettingsAdmin(ConfiguracionAdmin):
    pass