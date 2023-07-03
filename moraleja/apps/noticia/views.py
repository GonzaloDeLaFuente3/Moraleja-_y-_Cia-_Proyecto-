from django.shortcuts import render, get_object_or_404
from apps.noticia.models import Noticia

# Create your views here.

def noticias(request):
    cant_noticias = Noticia.objects.count()
    return render(request, 'noticias/noticias.html', {'cant_noticias':cant_noticias})

def cargar_noticias(request, offset):
    offset = int(offset)
    noticias = Noticia.objects.all().order_by('-fecha_creacion')[offset:offset+9]  # Obtener las siguientes 3 noticias según el offset
    return render(request, 'noticias/cargar_noticias.html', {'noticias': noticias})


def detalle_noticia(request, slug):
    noticia = get_object_or_404(Noticia, slug=slug)
    return render(request, 'noticias/detalle_noticia.html', {'noticia':noticia})