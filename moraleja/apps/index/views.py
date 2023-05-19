from django.shortcuts import render

from apps.producto.models import Producto

from apps.seccion.models import Seccion


# Create your views here.

def index(request):
    productos = Producto.objects.all()
    secciones = Seccion.objects.all()
    data = {
        'productos': productos,
        'secciones':secciones
    }

    # if request.user.is_authenticated:
    #     clientes = Cliente.objects.all()
    #     clienteTemp
    #     for cliente in clientes:
    #         if cliente.usuario == User.objects.get(username=request.user.username):
    #             clienteTemp = cliente
    #
    #     if clienteTemp != None:
    #         pedidos = Pedido.objects.filter(cliente=Cliente.objects.get(cuil=clienteTemp.cuil))
    #         data = {
    #             'platos': platos,
    #             'clientes': clientes,
    #             'pedidos': pedidos
    #         }


    return render(request, 'index/index.html', data)