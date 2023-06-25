from django.shortcuts import render
from apps.seccion.models import Nosotros, Historia, Servicios


# Create your views here.

def index(request):
    nosotros = Nosotros.objects.first()
    historia = Historia.objects.first()
    servicios = Servicios.objects.all()
    data = {
        'nosotros':nosotros,
        'historia': historia,
        'servicios': servicios,
    }

    return render(request, 'index/index.html', data)

