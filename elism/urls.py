# myapp/urls.py
from django.urls import path
from . import views
from .views import agregar_al_carrito, carrito, eliminar_del_carrito, proceder_al_pago

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('iniciarSesion/', views.iniciarSesion, name='iniciarSesion'),
    path('cerrarSesion/', views.cerrarSesion, name='cerrarSesion'),
    path('ropa/', views.ropa, name='ropa'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('guardar_contacto/', views.guardar_contacto, name='guardar_contacto'),
    path('crud/', views.crud, name='crud'),
    path('carrito/', views.carrito, name='carrito'),
    path('agregar_al_carrito/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar_del_carrito/<int:carrito_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('proceder_al_pago/', views.proceder_al_pago, name='proceder_al_pago'),

    path('producto/create/', views.producto_create, name='producto_create'),
    path('producto/<int:pk>/update/', views.producto_update, name='producto_update'),
    path('producto/<int:pk>/delete/', views.producto_delete, name='producto_delete'),
    path('producto/<int:pk>/', views.producto_detail, name='producto_detail'),

]










