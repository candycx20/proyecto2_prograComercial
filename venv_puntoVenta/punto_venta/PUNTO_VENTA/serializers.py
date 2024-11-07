# serializers.py
from rest_framework import serializers
from .models import *

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion']

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = ['id', 'empresa', 'contacto', 'direccion', 'telefono']

class ProductoSerializer(serializers.ModelSerializer):
    categoria = serializers.StringRelatedField()
    proveedor = serializers.StringRelatedField()

    class Meta:
        model = Producto
        fields = ['id', 'codigo', 'nombre', 'descripcion', 'precio', 'costo', 'cantidad', 'categoria', 'proveedor']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre', 'apellido', 'direccion', 'telefono', 'email']

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id', 'nombre', 'descripcion']

class UsuarioSerializer(serializers.ModelSerializer):
    rol = serializers.StringRelatedField()

    class Meta:
        model = Usuario
        fields = ['id', 'nombre', 'contrasenia', 'rol']
        extra_kwargs = {
            'contrasenia': {'write_only': True}  # Para que la contraseña no sea devuelta en la respuesta JSON
        }

class PedidoSerializer(serializers.ModelSerializer):
    cliente = serializers.StringRelatedField()
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)  # Solo lectura para evitar edición

    class Meta:
        model = Pedido
        fields = ['id', 'numero_pedido', 'fecha', 'total', 'estado', 'cliente']

class DetallePedidoSerializer(serializers.ModelSerializer):
    pedido = serializers.StringRelatedField()
    producto = serializers.StringRelatedField()

    class Meta:
        model = DetallePedido
        fields = ['id', 'pedido', 'producto', 'cantidad']

class CompraSerializer(serializers.ModelSerializer):
    proveedor = serializers.StringRelatedField()
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)  # Solo lectura

    class Meta:
        model = Compra
        fields = ['id', 'numero_compra', 'fecha', 'proveedor', 'total', 'estado']

class DetalleCompraSerializer(serializers.ModelSerializer):
    compra = serializers.StringRelatedField()
    producto = serializers.StringRelatedField()

    class Meta:
        model = DetalleCompra
        fields = ['id', 'compra', 'producto', 'cantidad']

class InventarioSerializer(serializers.ModelSerializer):
    producto = serializers.StringRelatedField()
    referencia_pedido = serializers.StringRelatedField()
    referencia_compra = serializers.StringRelatedField()

    class Meta:
        model = Inventario
        fields = [
            'id', 'fecha_movimiento', 'tipo_movimiento', 'cantidad', 'tipo_actividad',
            'producto', 'referencia_pedido', 'referencia_compra'
        ]
