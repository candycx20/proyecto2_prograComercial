from django.urls import path
from . import views
from rest_framework_simplejwt.views import *
from .views import *


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', CurrentUserView.as_view(), name='current-user'),
    
    path('categorias/', CategoriaListCreate.as_view(), name='categoria-list-create'),
    path('categorias/<int:pk>/', CategoriaDetail.as_view(), name='categoria-detail'),

    path('proveedores/', ProveedorListCreate.as_view(), name='proveedor-list-create'),
    path('proveedores/<int:pk>/', ProveedorDetail.as_view(), name='proveedor-detail'),

    path('productos/', ProductoListCreate.as_view(), name='producto-list'),
    path('productos/<int:categoria_id>/<int:proveedor_id>/', ProductoListCreate.as_view(), name='producto-list-create'),
    path('productos/<int:pk>/', ProductoDetail.as_view(), name='producto-detail'),

    path('clientes/', ClienteListCreate.as_view(), name='cliente-list-create'),
    path('clientes/<int:pk>/', ClienteDetail.as_view(), name='cliente-detail'),

    path('roles/', RolListCreate.as_view(), name='rol-list-create'),
    path('roles/<int:pk>/', RolDetail.as_view(), name='rol-detail'),

    path('usuarios/', UsuarioListCreate.as_view(), name='usuario-list'),
    path('usuarios/<int:rol_id>/', UsuarioListCreate.as_view(), name='usuario-list-create'),
    path('usuarios/<int:pk>/', UsuarioDetail.as_view(), name='usuario-detail'),

    path('pedidos/', PedidoListCreate.as_view(), name='pedido-list'),
    path('pedidos/<int:cliente_id>/', PedidoListCreate.as_view(), name='pedido-list-create'),
    path('pedidos/<int:pk>/', PedidoDetail.as_view(), name='pedido-detail'),

    path('compras/', CompraListCreate.as_view(), name='compra-list'),
    path('compras/<int:proveedor_id>/', CompraListCreate.as_view(), name='compra-list-create'),
    path('compras/<int:pk>/', CompraDetail.as_view(), name='compra-detail'),

    path('inventarios/', InventarioListCreate.as_view(), name='inventario-list'),
    path('inventarios/<int:producto_id>/<int:referencia_pedido_id>/<int:referencia_compra_id>/', InventarioListCreate.as_view(), name='inventario-list-create'),
    path('inventarios/<int:pk>/', InventarioDetail.as_view(), name='inventario-detail'),
]
    
