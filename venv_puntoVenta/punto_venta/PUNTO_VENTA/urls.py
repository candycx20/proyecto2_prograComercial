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

    path('nuevo_usuario/', views.nuevo_usuario, name='nuevo_usuario'),
    path('lista_usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('actualizar_usuario/<int:id>/', views.actualizar_usuario, name='actualizar_usuario'),
    path('eliminar_usuario/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),

    path('nuevo_rol/', views.nuevo_rol, name='nuevo_rol'),
    path('lista_roles/', views.lista_roles, name='lista_roles'),
    path('actualizar_rol/<int:id>/', views.actualizar_rol, name='actualizar_rol'),
    path('eliminar_rol/<int:id>/', views.eliminar_rol, name='eliminar_rol'),

    path('nuevo_pedido/', views.nuevo_pedido, name='nuevo_pedido'),
    path('lista_pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('actualizar_pedido/<int:id>/', views.actualizar_pedido, name='actualizar_pedido'),
    path('eliminar_pedido/<int:id>/', views.eliminar_pedido, name='eliminar_pedido'),

    path('nueva_compra/', views.nueva_compra, name='nueva_compra'),
    path('lista_compras/', views.lista_compras, name='lista_compras'),
    path('actualizar_compra/<int:id>/', views.actualizar_compra, name='actualizar_compra'),
    path('eliminar_compra/<int:id>/', views.eliminar_compra, name='eliminar_compra'),

    path('lista_movimientos/', views.lista_movimientos, name='lista_movimientos'),
    path('actualizar_inventario/<int:id>/', views.actualizar_inventario, name='actualizar_inventario'),
    path('eliminar_inventario/<int:id>/', views.eliminar_inventario, name='eliminar_inventario'),

    path('test/', views.test, name='test'),
    path('index/', views.index, name='index'),
    
]