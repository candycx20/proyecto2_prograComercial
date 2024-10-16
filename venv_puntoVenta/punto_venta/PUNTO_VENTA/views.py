from django.shortcuts import render

# Create your views here.
from .models import *
from django.http import HttpResponse

def inicio(request):
    return render(request, 'form_select.html') 


from .forms import *
from django.shortcuts import redirect, get_object_or_404

# ___________________PRODUCTOS_____________________________

def nuevo_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('lista_productos') 
    else:
        form = ProductoForm()
        return render(request, 'form_create.html', {
            'form': form, 
            'modelo':'Producto'})

def lista_productos(request):
    queryset = Producto.objects.all()
    productos_data = [
        {field.name: getattr(item, field.name) for field in Producto._meta.fields}
        for item in queryset
    ]
    return render(request, 'form_select.html', {
        'queryset': productos_data,
        'modelo': 'Producto'
    })


def actualizar_producto(request, id):
    queryset = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=queryset)
    return render(request, 'form_update.html', {
        'form': form,
        'modelo': 'Producto'
    })

def eliminar_producto(request, id):
    queryset = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        queryset.delete()
        return redirect('lista_productos')
    else:
        return HttpResponse("Metodo no permitido")
   


# ___________________CATEGORIAS_____________________________

def nueva_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('lista_categorias') 
    else:
        form = CategoriaForm()
        return render(request, 'form_create.html', {
            'form': form, 
            'modelo':'Categoria'})


def lista_categorias(request):
    queryset = Categoria.objects.all()
    categorias_data = [
        {field.name: getattr(item, field.name) for field in Categoria._meta.fields}
        for item in queryset
    ]
    return render(request, 'form_select.html', {
        'queryset': categorias_data,
        'modelo': 'Categoria'
    })


def actualizar_categoria(request, id):
    queryset = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('lista_categorias')
    else:
        form = CategoriaForm(instance=queryset)
    return render(request, 'form_update.html', {
        'form': form,
        'modelo': 'Categoria'
    })

def eliminar_categoria(request, id):
    queryset = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        queryset.delete()
        return redirect('lista_categorias')
    else:
        return HttpResponse("Metodo no permitido")



# ___________________PROVEEDORES_____________________________

def nuevo_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('lista_proveedores') 
    else:
        form = ProveedorForm()
        return render(request, 'form_create.html', {
            'form': form, 
            'modelo':'Proveedor'})


def lista_proveedores(request):
    queryset = Proveedor.objects.all()
    proveedores_data = [
        {field.name: getattr(item, field.name) for field in Proveedor._meta.fields}
        for item in queryset
    ]
    return render(request, 'form_select.html', {
        'queryset': proveedores_data,
        'modelo': 'Proveedor'
    })


def actualizar_proveedor(request, id):
    queryset = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        form = ProveedorForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('lista_proveedores')
    else:
        form = ProveedorForm(instance=queryset)
    return render(request, 'form_update.html', {
        'form': form,
        'modelo': 'Proveedor'
    })

def eliminar_proveedor(request, id):
    queryset = get_object_or_404(Proveedor, id=id)
    if request.method == 'POST':
        queryset.delete()
        return redirect('lista_proveedores')
    else:
        return HttpResponse("Metodo no permitido")












def test(request):
    return render(request, 'autenticated_test.html')

def index(request):
    return render(request, 'index.html')