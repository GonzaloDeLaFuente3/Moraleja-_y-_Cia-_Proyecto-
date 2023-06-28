from django.shortcuts import render, get_object_or_404
from apps.producto.models import Producto
from apps.receta.models import Receta

# Create your views here.

def productos(request):
    productos = Producto.objects.filter(vigencia=True)
    data = {
        'productos': productos,
    }

    return render(request, 'productos/productos.html', data)

def detalle_producto(request, slug):
    producto = get_object_or_404(Producto, slug=slug)
    return render(request, 'productos/detalle_producto.html', {'producto':producto})

def beneficio_producto(request, slug):
    producto = get_object_or_404(Producto, slug=slug)
    return render(request, 'productos/beneficio_producto.html', {'producto':producto})

def receta_producto(request, slug):
    producto = get_object_or_404(Producto, slug=slug)
    recetas = Receta.objects.filter(productos__in=[producto])
    return render(request, 'receta/recetas_producto.html', {'producto': producto, 'recetas': recetas})

def detalle_receta(request, slug):
    receta = get_object_or_404(Receta, slug=slug)
    return render(request, 'receta/detalle_receta.html', {'receta':receta})

def recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'receta/recetas.html', {'recetas': recetas})