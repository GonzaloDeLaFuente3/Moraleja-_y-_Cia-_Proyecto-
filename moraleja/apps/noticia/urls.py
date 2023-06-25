from django.urls import path

from apps.noticia import views
app_name = 'noticia'
urlpatterns = [
    path('', views.noticias, name='noticias'),
    path('detalle_noticia/', views.detalle_noticia, name='detalle_noticia'),
]