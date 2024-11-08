from rest_framework import generics
from .models import *
from .serializers import *
import uuid
from .permissions import Admin, Vendedor, SuperAdmin
from django_filters import rest_framework as filters

# ____________ CATEGORIA ____________
class CategoriaListCreate(generics.ListCreateAPIView):  # GET (list) | POST (create)
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [ Admin | SuperAdmin]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['nombre'] 

class CategoriaDetail(generics.RetrieveUpdateDestroyAPIView):  # GET | PUT | DELETE
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [ Admin | SuperAdmin]

# ____________ PROVEEDOR ____________
class ProveedorListCreate(generics.ListCreateAPIView):  # GET | POST
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [ Admin | SuperAdmin]

class ProveedorDetail(generics.RetrieveUpdateDestroyAPIView):  # GET | PUT | DELETE
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer
    permission_classes = [ Admin | SuperAdmin]

# ____________ PRODUCTO ____________
class ProductoListCreate(generics.ListCreateAPIView):  # GET | POST
    serializer_class = ProductoSerializer
    permission_classes = [ Admin | SuperAdmin]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['categoria', 'proveedor']

    def get_queryset(self):
        return Producto.objects.all()

    def perform_create(self, serializer):
        categoria_id = self.kwargs['categoria_id']
        proveedor_id = self.kwargs['proveedor_id']
        categoria = Categoria.objects.get(id=categoria_id)
        proveedor = Proveedor.objects.get(id=proveedor_id)
        serializer.save(categoria=categoria, proveedor=proveedor)

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):  # GET | PUT | DELETE
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [ Admin | SuperAdmin]

# ____________ CLIENTE ____________
class ClienteListCreate(generics.ListCreateAPIView):  # GET | POST
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):  # GET | PUT | DELETE
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

# ____________ ROL ____________
class RolListCreate(generics.ListCreateAPIView):  # GET | POST
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

class RolDetail(generics.RetrieveUpdateDestroyAPIView):  # GET | PUT | DELETE
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

# ____________ USUARIO ____________
class UsuarioListCreate(generics.ListCreateAPIView):  # GET | POST
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        return Usuario.objects.all()

    def perform_create(self, serializer):
        rol_id = self.kwargs['rol_id']
        rol = Rol.objects.get(id=rol_id)
        serializer.save(rol=rol)

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):  # GET | PUT | DELETE
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# ____________ PEDIDO ____________
class PedidoListCreate(generics.ListCreateAPIView):  # GET | POST
    serializer_class = PedidoSerializer
    permission_classes = [Vendedor | SuperAdmin]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['fecha', 'cliente']

    def get_queryset(self):
        return Pedido.objects.all()

    def perform_create(self, serializer):
        cliente_id = self.kwargs['cliente_id']
        cliente = Cliente.objects.get(id=cliente_id)
        pedido = serializer.save(cliente=cliente, numero_pedido=f"PED-{uuid.uuid4()}", estado='pendiente')
        pedido.calcular_total()

class PedidoDetail(generics.RetrieveUpdateDestroyAPIView):  # GET | PUT | DELETE
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [Vendedor | SuperAdmin]

# ____________ COMPRA ____________
class CompraListCreate(generics.ListCreateAPIView):  # GET | POST
    serializer_class = CompraSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['fecha', 'proveedor']

    def get_queryset(self):
        return Compra.objects.all()

    def perform_create(self, serializer):
        proveedor_id = self.kwargs['proveedor_id']
        proveedor = Proveedor.objects.get(id=proveedor_id)
        compra = serializer.save(proveedor=proveedor, numero_compra=f"COMP-{uuid.uuid4()}", estado='pendiente')
        compra.calcular_total()

class CompraDetail(generics.RetrieveUpdateDestroyAPIView):  # GET | PUT | DELETE
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

# ____________ INVENTARIO ____________
class InventarioListCreate(generics.ListCreateAPIView):  # GET | POST
    serializer_class = InventarioSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['producto', 'referencia_pedido', 'referencia_compra']

    def get_queryset(self):
        return Inventario.objects.all()

    def perform_create(self, serializer):
        producto_id = self.kwargs['producto_id']
        referencia_pedido_id = self.kwargs.get('referencia_pedido_id')
        referencia_compra_id = self.kwargs.get('referencia_compra_id')

        producto = Producto.objects.get(id=producto_id)
        referencia_pedido = Pedido.objects.get(id=referencia_pedido_id) if referencia_pedido_id else None
        referencia_compra = Compra.objects.get(id=referencia_compra_id) if referencia_compra_id else None

        serializer.save(
            producto=producto,
            referencia_pedido=referencia_pedido,
            referencia_compra=referencia_compra
        )

class InventarioDetail(generics.RetrieveUpdateDestroyAPIView):  # GET | PUT | DELETE
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer
