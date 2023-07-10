from django.urls import path

from apps.seccion import views
app_name = 'seccion'
urlpatterns = [
    path('contacto', views.contacto, name='contacto'),
    path('servicios', views.servicios, name='servicios'),
    path('enviar_formulario/', views.enviar_formulario, name='enviar_formulario'),
]