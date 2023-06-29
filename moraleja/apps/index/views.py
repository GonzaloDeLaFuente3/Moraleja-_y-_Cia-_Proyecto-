from django.shortcuts import render
from apps.seccion.models import Nosotros, Historia, Servicios
from apps.noticia.models import Noticia


# Create your views here.

def index(request):
    nosotros = Nosotros.objects.first()
    historia = Historia.objects.first()
    servicios = Servicios.objects.all()
    cant_noticias = Noticia.objects.count()
    data = {
        'nosotros': nosotros,
        'historia': historia,
        'servicios': servicios,
        'cant_noticias':cant_noticias,
    }

    return render(request, 'index/index.html', data)

