from django.shortcuts import render
from apps.seccion.models import Nosotros, Historia, Servicios
from apps.noticia.models import Noticia


# Create your views here.

def index(request):
    nosotros = Nosotros.objects.first()
    historia = Historia.objects.first()
    servicios = Servicios.objects.all()
    noticias = Noticia.objects.all().order_by('-fecha_creacion')[:3]  # Obtener los últimos 3 objetos Noticia
    cant_noticias = Noticia.objects.count()
    data = {
        'nosotros': nosotros,
        'historia': historia,
        'servicios': servicios,
        'noticias': noticias,  # Agregar el queryset de noticias al contexto de renderizado
        'cant_noticias':cant_noticias,
    }

    return render(request, 'index/index.html', data)

