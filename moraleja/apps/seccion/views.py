from django.shortcuts import render

# Create your views here.

def contacto(request):
    return render(request, 'contacto/contacto.html')

def error_404(request, exception):
    return render(request, '404/404.html', status=404)

def error_404_test(request): #pagina de prueba
    return render(request, '404/404.html')