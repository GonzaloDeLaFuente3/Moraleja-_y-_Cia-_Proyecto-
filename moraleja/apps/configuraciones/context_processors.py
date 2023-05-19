from .models import Configuraciones

def configuraciones(request):
    return {'configuraciones': Configuraciones.load()}