# forms.py
from django import forms
from .models import *

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        # fields = ['nombre', 'edad', 'fecha_nacimiento']


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'