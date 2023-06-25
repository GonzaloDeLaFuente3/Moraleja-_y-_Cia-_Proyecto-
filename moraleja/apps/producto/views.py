from django.shortcuts import render, get_object_or_404
from apps.producto.models import Producto

# Create your views here.

def productos(request):
    productos = Producto.objects.all()
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
    return render(request, 'productos/receta_producto.html', {'producto':producto})