from django.shortcuts import render, get_object_or_404
from apps.noticia.models import Noticia

# Create your views here.

def noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias/noticias.html', {'noticias':noticias})

def detalle_noticia(request, slug):
    noticia = get_object_or_404(Noticia, slug=slug)
    return render(request, 'noticias/detalle_noticia.html', {'noticia':noticia})