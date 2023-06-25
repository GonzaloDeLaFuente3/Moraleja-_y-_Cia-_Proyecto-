from django.urls import path

from apps.producto import views

app_name = 'producto'
urlpatterns = [
    path('', views.productos, name='productos'),
    path('<slug:slug>/', views.detalle_producto, name='detalle_producto'),
    path('<slug:slug>/beneficios', views.beneficio_producto, name='beneficio_producto'),
    path('<slug:slug>/recetas_saludables', views.receta_producto, name='receta_producto'),
]