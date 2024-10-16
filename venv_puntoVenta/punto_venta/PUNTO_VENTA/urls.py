from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),

    path('lista_categorias/', views.lista_categorias, name='lista_categorias'),
    path('actualizar_categoria/<int:id>/', views.actualizar_categoria, name='actualizar_categoria'),
    path('eliminar_categoria/<int:id>/', views.eliminar_categoria, name='eliminar_categoria'),
    path('nueva_categoria/', views.nueva_categoria, name='nueva_categoria'),

    path('nuevo_proveedor/', views.nuevo_proveedor, name='nuevo_proveedor'),
    path('lista_proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('actualizar_proveedor/<int:id>/', views.actualizar_proveedor, name='actualizar_proveedor'),
    path('eliminar_proveedor/<int:id>/', views.eliminar_proveedor, name='eliminar_proveedor'),

    path('nuevo_producto/', views.nuevo_producto, name='nuevo_producto'),
    path('lista_productos/', views.lista_productos, name='lista_productos'),
    path('actualizar_producto/<int:id>/', views.actualizar_producto, name='actualizar_producto'),
    path('eliminar_producto/<int:id>/', views.eliminar_producto, name='eliminar_producto'),

    path('nuevo_cliente/', views.nuevo_cliente, name='nuevo_cliente'),
    path('lista_clientes/', views.lista_clientes, name='lista_clientes'),
    path('actualizar_cliente/<int:id>/', views.actualizar_cliente, name='actualizar_cliente'),
    path('eliminar_cliente/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),

    path('nuevo_pedido/', views.nuevo_pedido, name='nuevo_pedido'),
    path('lista_pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('actualizar_pedido/<int:id>/', views.actualizar_pedido, name='actualizar_pedido'),
    path('eliminar_pedido/<int:id>/', views.eliminar_pedido, name='eliminar_pedido'),


    path('test/', views.test, name='test'),
    path('index/', views.index, name='index'),
    
]