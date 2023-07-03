from django.urls import path

from apps.seccion import views
app_name = 'seccion'
urlpatterns = [
    path('contacto', views.contacto, name='contacto'),
    path('error_404_test', views.error_404_test, name='error_404_test'), #esto es solo para probar el diseño de la pag 404
    path('enviar_formulario/', views.enviar_formulario, name='enviar_formulario'),
]