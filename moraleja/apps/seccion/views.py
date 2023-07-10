from django.shortcuts import render, redirect
from django.contrib import messages
from apps.seccion.models import Servicios
from django.urls import reverse

# Create your views here.

def contacto(request):
    return render(request, 'contacto/contacto.html')

def servicios(request):
    servicios = Servicios.objects.filter(vigencia=True)
    return render(request, 'servicios/servicios.html', {'servicios':servicios})

def error_404(request, exception):
    return render(request, '404/404.html', status=404)

def error_404_test(request): #pagina de prueba
    return render(request, '404/404.html')


def enviar_formulario(request):
    if request.method == 'POST':
        # Procesa el formulario y envía el correo electrónico

        # Agrega un mensaje de éxito
        messages.success(request, 'El formulario se envió correctamente.')

        return redirect(reverse("seccion:contacto"))

    return render(request, 'contacto/contacto.html')