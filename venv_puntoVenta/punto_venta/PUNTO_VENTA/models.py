from django.db import models
from django.contrib.auth.hashers import make_password
from django.db.models import Sum
from django.db.models import F, Sum


# Modelo Categoria
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

# Modelo Proveedor
class Proveedor(models.Model):
    empresa = models.CharField(max_length=200)
    contacto = models.CharField(max_length=15)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.empresa

# Modelo Producto
class Producto(models.Model):
    codigo = models.CharField(max_length=200, unique=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

# Modelo Cliente
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo Rol
class Rol(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

# Modelo Usuario
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    contrasenia = models.CharField(max_length=50)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Hashea la contraseña antes de guardarla
        if not self.pk:  # Solo si es un usuario nuevo
            self.contrasenia = make_password(self.contrasenia)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre

# Modelo Pedido
class Pedido(models.Model):
    numero_pedido = models.CharField(max_length=100, unique=True)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    estado = models.CharField(
        max_length=50,
        choices=[('pendiente', 'Pendiente'), ('completado', 'Completado'), ('cancelado', 'Cancelado')]
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def calcular_total(self):
        # Calcula el total sumando los precios de los productos multiplicados por sus cantidades
        total = self.detallepedido_set.aggregate(
            total=Sum(F('producto__precio') * F('cantidad'))
        )['total']
        self.total = total or 0
        self.save()

    def __str__(self):
        return f"Pedido {self.numero_pedido} - {self.cliente}"


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Detalle del Pedido {self.pedido.numero_pedido} - {self.producto.nombre}"

# Modelo Compra
class Compra(models.Model):
    numero_compra = models.CharField(max_length=100, unique=True)
    fecha = models.DateTimeField(auto_now_add=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    estado = models.CharField(
        max_length=50,
        choices=[('pendiente', 'Pendiente'), ('recibida', 'Recibida'), ('cancelada', 'Cancelada')]
    )

    def calcular_total(self):
        # Calcula el total sumando los costos de los productos en el detalle de la compra
        total = self.detallecompra_set.aggregate(
            total=Sum(F('producto__costo') * F('cantidad'))
        )['total']
        self.total = total or 0
        self.save()

    def __str__(self):
        return f"Compra {self.numero_compra} - {self.proveedor.empresa}"


class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f"Detalle de la Compra {self.compra.numero_compra} - Producto: {self.producto.nombre}"

        
# Modelo Inventario
class Inventario(models.Model):
    fecha_movimiento = models.DateTimeField(auto_now_add=True)
    tipo_movimiento = models.CharField(
        max_length=50,
        choices=[('entrada', 'Entrada'), ('salida', 'Salida')]
    )
    cantidad = models.IntegerField()
    tipo_actividad = models.CharField(max_length=50)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tipo_movimiento} de {self.producto.nombre}"
