# forms.py
from django import forms
from .models import *


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        exclude = '__all__'


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class RolForm(forms.ModelForm):
    class Meta:
        model = Rol
        fields = '__all__'


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = '__all__'


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'estado'] 

class PedidoCreateForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente'] 

class PedidoUpdateForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['estado'] 


class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['proveedor', 'estado']

class CompraCreateForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['proveedor']      

class CompraUpdateForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['estado']     


class DetalleCompraForm(forms.ModelForm):
    class Meta:
        model = DetalleCompra
        fields = '__all__'


class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = '__all__'

