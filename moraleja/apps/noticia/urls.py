from django.urls import path

from apps.noticia import views
app_name = 'noticia'
urlpatterns = [
    path('', views.noticias, name='noticias'),
    path('/<slug:slug>', views.detalle_noticia, name='detalle_noticia'),
    path('/cargar/<int:offset>/', views.cargar_noticias, name='cargar_noticias'),
]