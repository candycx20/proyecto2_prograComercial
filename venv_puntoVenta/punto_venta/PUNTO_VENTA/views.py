from django.shortcuts import render
from datetime import datetime
import uuid


# Create your views here.
from .models import *
from django.http import HttpResponse

def inicio(request):
    return render(request, 'form_select.html') 


from .forms import *
from django.shortcuts import redirect, get_object_or_404



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



# ___________________CLIENTES_____________________________

def nuevo_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('lista_clientes') 
    else:
        form = ClienteForm()
        return render(request, 'form_create.html', {
            'form': form, 
            'modelo':'Cliente'})


def lista_clientes(request):
    queryset = Cliente.objects.all()
    clientes_data = [
        {field.name: getattr(item, field.name) for field in Cliente._meta.fields}
        for item in queryset
    ]
    return render(request, 'form_select.html', {
        'queryset': clientes_data,
        'modelo': 'Cliente'
    })


def actualizar_cliente(request, id):
    queryset = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=queryset)
    return render(request, 'form_update.html', {
        'form': form,
        'modelo': 'Cliente'
    })


def eliminar_cliente(request, id):
    queryset = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        queryset.delete()
        return redirect('lista_clientes')
    else:
        return HttpResponse("Metodo no permitido")



# ___________________ROLES_____________________________

def nuevo_rol(request):
    if request.method == 'POST':
        form = RolForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('lista_roles') 
    else:
        form = RolForm()
        return render(request, 'form_create.html', {
            'form': form, 
            'modelo':'Rol'})


def lista_roles(request):
    queryset = Rol.objects.all()
    roles_data = [
        {field.name: getattr(item, field.name) for field in Rol._meta.fields}
        for item in queryset
    ]
    return render(request, 'form_select.html', {
        'queryset': roles_data,
        'modelo': 'Rol'
    })


def actualizar_rol(request, id):
    queryset = get_object_or_404(Rol, id=id)
    if request.method == 'POST':
        form = RolForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('lista_roles')
    else:
        form = RolForm(instance=queryset)
    return render(request, 'form_update.html', {
        'form': form,
        'modelo': 'Rol'
    })


def eliminar_rol(request, id):
    queryset = get_object_or_404(Rol, id=id)
    if request.method == 'POST':
        queryset.delete()
        return redirect('lista_roles')
    else:
        return HttpResponse("Metodo no permitido")



# ___________________Usuarios_____________________________

def nuevo_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('lista_usuarios') 
    else:
        form = UsuarioForm()
        return render(request, 'form_create.html', {
            'form': form, 
            'modelo':'Usuario'})


def lista_usuarios(request):
    return render(request, 'select_form.html')


def actualizar_usuario(request, id):
    queryset = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('lista_usuarios')
    else:
        form = UsuarioForm(instance=queryset)
    return render(request, 'form_update.html', {
        'form': form,
        'modelo': 'Usuario'
    })


def eliminar_usuario(request, id):
    queryset = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        queryset.delete()
        return redirect('lista_usuarios')
    else:
        return HttpResponse("Metodo no permitido")



# ___________________PEDIDOS_____________________________

def nuevo_pedido(request):
    if request.method == 'POST':
        pedido_form = PedidoCreateForm(request.POST)
        if pedido_form.is_valid():
            pedido = pedido_form.save(commit=False)
            pedido.numero_pedido = f"PED-{uuid.uuid4()}"
            pedido.estado = 'pendiente'
            pedido.save()

            productos = request.POST.getlist('productos')
            cantidades = request.POST.getlist('cantidades')

            for producto_id, cantidad in zip(productos, cantidades):
                producto = get_object_or_404(Producto, id=producto_id)
                DetallePedido.objects.create(pedido=pedido, producto=producto, cantidad=cantidad)

                producto.cantidad -= int(cantidad)
                producto.save()

                Inventario.objects.create(
                    tipo_movimiento='salida',
                    tipo_actividad='Venta',
                    producto=producto,
                    cantidad=int(cantidad),
                    referencia_pedido=pedido
                )

            pedido.calcular_total()

            return redirect('lista_pedidos')
    else:
        pedido_form = PedidoCreateForm()

    productos = Producto.objects.all()
    return render(request, 'form_create_pedido.html', {
        'pedido_form': pedido_form,
        'productos': productos,
    })




def lista_pedidos(request):
    queryset = Pedido.objects.all()
    pedidos_data = [
        {field.name: getattr(item, field.name) for field in Pedido._meta.fields}
        for item in queryset
    ]
    return render(request, 'form_select.html', {
        'queryset': pedidos_data,
        'modelo': 'Pedido'
    })


def detalle_pedido(request, id):
    queryset = DetallePedido.objects.all()
    detallePedidos_data = [
        {field.name: getattr(item, field.name) for field in DetallePedido._meta.fields}
        for item in queryset
    ]
    return render(request, 'form_select.html', {
        'queryset': detallePedidos_data,
        'modelo': 'DetallePedido'
    })




def actualizar_pedido(request, id):
    queryset = get_object_or_404(Pedido, id=id)
    if request.method == 'POST':
        form = PedidoUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('lista_pedidos')
    else:
        form = PedidoUpdateForm(instance=queryset)
    return render(request, 'form_update.html', {
        'form': form,
        'modelo': 'Pedido'
    })


def eliminar_pedido(request, id):
    queryset = get_object_or_404(Pedido, id=id)
    
    if request.method == 'POST':
        detalles_pedido = queryset.detallepedido_set.all()
        
        for detalle in detalles_pedido:
            producto = detalle.producto
            producto.cantidad += detalle.cantidad
            producto.save()

            Inventario.objects.create(
                tipo_movimiento='entrada',
                tipo_actividad='Devolución por eliminación de pedido',
                producto=producto,
                cantidad=detalle.cantidad,
                referencia_pedido=queryset
            )
        queryset.delete()
        
        return redirect('lista_pedidos')
    else:
        return HttpResponse("Metodo no permitido")




# ___________________COMPRAS_____________________________

def nueva_compra(request):
    if request.method == 'POST':
        compra_form = CompraCreateForm(request.POST)
        if compra_form.is_valid():
            compra = compra_form.save(commit=False)
            compra.numero_compra = f"COMP-{uuid.uuid4()}"
            compra.estado = 'pendiente'
            compra.save()

            productos = request.POST.getlist('productos')
            cantidades = request.POST.getlist('cantidades')

            for producto_id, cantidad in zip(productos, cantidades):
                producto = get_object_or_404(Producto, id=producto_id)
                DetalleCompra.objects.create(compra=compra, producto=producto, cantidad=cantidad)

                producto.cantidad += int(cantidad)
                producto.save()

                Inventario.objects.create(
                    tipo_movimiento='entrada',
                    tipo_actividad='Compra',
                    producto=producto,
                    cantidad=int(cantidad),
                    referencia_compra=compra
                )

            compra.calcular_total()

            return redirect('lista_compras')
    else:
        compra_form = CompraCreateForm()

    productos = Producto.objects.all()
    return render(request, 'form_create_compra.html', {
        'compra_form': compra_form,
        'productos': productos,
    })



def lista_compras(request):
    queryset = Compra.objects.all()
    compras_data = [
        {field.name: getattr(item, field.name) for field in Compra._meta.fields}
        for item in queryset
    ]
    return render(request, 'form_select.html', {
        'queryset': compras_data,
        'modelo': 'Compra'
    })

def detalle_compra(request, id):
    queryset = DetalleCompra.objects.all()
    detalleCompras_data = [
        {field.name: getattr(item, field.name) for field in DetalleCompra._meta.fields}
        for item in queryset
    ]
    return render(request, 'form_select3.html', {
        'queryset': detalleCompras_data,
        'modelo': 'DetalleCompra'
    })


def actualizar_compra(request, id):
    queryset = get_object_or_404(Compra, id=id)
    if request.method == 'POST':
        form = CompraUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('lista_compras')
    else:
        form = CompraUpdateForm(instance=queryset)
    return render(request, 'form_update.html', {
        'form': form,
        'modelo': 'Compra'
    })


def eliminar_compra(request, id):
    queryset = get_object_or_404(Compra, id=id)
    
    if request.method == 'POST':
        detalles_compra = queryset.detallecompra_set.all()

        for detalle in detalles_compra:
            producto = detalle.producto
            producto.cantidad -= detalle.cantidad  
            producto.save()

            Inventario.objects.create(
                tipo_movimiento='salida',
                tipo_actividad='Retiro por eliminación de compra',
                producto=producto,
                cantidad=detalle.cantidad,
                referencia_compra=queryset
            )

        queryset.delete()
        
        return redirect('lista_compras')
    else:
        return HttpResponse("Metodo no permitido")



def calcular_total(self):
    total = self.detallecompra_set.aggregate(
        total=Sum(F('producto__costo') * F('cantidad'), output_field=DecimalField())
    )['total'] or 0
    self.total = total
    self.save()


# ___________________MOVIMIENTOS INVENTARIO_____________________________

def lista_movimientos(request):
    queryset = Inventario.objects.all()
    movimientos_data = [
        {field.name: getattr(item, field.name) for field in Inventario._meta.fields}
        for item in queryset
    ]
    return render(request, 'form_select3.html', {
        'queryset': movimientos_data,
        'modelo': 'Inventario'
    })

def actualizar_inventario(request, id):
    queryset = get_object_or_404(Inventario, id=id)
    if request.method == 'POST':
        form = InventarioForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            return redirect('lista_movimientos')
    else:
        form = InventarioForm(instance=queryset)
    return render(request, 'form_update.html', {
        'form': form,
        'modelo': 'Inveantario'
    })

def eliminar_inventario(request, id):
    queryset = get_object_or_404(Inventario, id=id)
    if request.method == 'POST':
        queryset.delete()
        return redirect('lista_movimientos')
    else:
        return HttpResponse("Metodo no permitido")


def test(request):
    return render(request, 'autenticated_test.html')

def index(request):
    return render(request, 'index.html')