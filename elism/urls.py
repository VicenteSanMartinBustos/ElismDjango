# myapp/urls.py
from django.urls import path
from . import views
from .views import (
    ProductoListView,
    ProductoDetailView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
    
)

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('iniciarSesion/', views.iniciarSesion, name='iniciarSesion'),
    path('ropa/', views.ropa, name='ropa'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('carrito/', views.carrito, name='carrito'),
    path('products/', ProductoListView.as_view(), name='producto_list'),
    path('products/<int:pk>/', ProductoDetailView.as_view(), name='producto_detail'),
    path('products/new/', ProductoCreateView.as_view(), name='producto_create'),
    path('products/<int:pk>/edit/', ProductoUpdateView.as_view(), name='producto_edit'),
    path('products/<int:pk>/delete/', ProductoDeleteView.as_view(), name='producto_delete'),
    
]

