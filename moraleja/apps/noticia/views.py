from django.shortcuts import render

# Create your views here.

def noticias(request):
    return render(request, 'noticias/noticias.html')

def detalle_noticia(request):
    return render(request, 'noticias/detalle_noticia.html')