from django.urls import path

from apps.producto import views

app_name = 'producto'
urlpatterns = [
    path('', views.productos, name='productos'),
    path('/<slug:slug>', views.detalle_producto, name='detalle_producto'),
    path('/<slug:slug>/beneficios', views.beneficio_producto, name='beneficio_producto'),
    path('/<slug:slug>/recetas-saludables', views.receta_producto, name='receta_producto'),
    path('/recetas-saludables/', views.recetas, name='recetas'),
    path('/recetas-saludables/<slug:slug>', views.detalle_receta, name='detalle_receta'),

]