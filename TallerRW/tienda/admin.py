from django.contrib import admin
from .models import *
from django.utils.html import mark_safe

# Register your models here.


@admin.register(Categoria)
class Categoria(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'descripcion_categoria']
    search_fields = ['nombre']


@admin.register(Cotizaciones)
class Cotizaciones(admin.ModelAdmin):
    list_display = ['id', 'modelo', 'placa', 'kilometraje',
                    'linea', 'servicio', 'cliente', 'empleado']
    search_fields = ['empleado']


@admin.register(Productos)
class Producto(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'Precio', 'descripcion_producto',
                    'cantidad', 'fecha_Creacion', 'foto', 'ver_foto']
    search_fields = ['nombre']

    def ver_foto(self, obj):
        return mark_safe(f"<a href='{obj.foto.url}'><img src='{obj.foto.url}' width='25%'></a>")


@admin.register(Servicios)
class Servicio(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'descripcion_servicio',
                    'foto', 'precio', 'ver_foto']
    search_fields = ['nombre']

    def ver_foto(self, obj):
        return mark_safe(f"<a href='{obj.foto.url}'><img src='{obj.foto.url}' width='25%'></a>")


@admin.register(Empleado)
class Empleado(admin.ModelAdmin):
    list_display = ['id', 'nombre_completo', 'cedula',
                    'correo', 'telefono', 'fecha_contratacion', 'cargo']
    search_fields = ['nombre']


@admin.register(Clientes)
class Cliente(admin.ModelAdmin):
    list_display = ['id', 'nombre_completo', 'cedula', 'correo', 'direccion']
    search_fields = ['nombre_completo']


class Vehiculos(admin.ModelAdmin):
    list_display = ['id', 'vehiculo']


@admin.register(Proveedores)
class Proveedores(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'nit', 'telefono', 'correo']
    search_fields = ['nombre']


@admin.register(Usuarios)
class Usuario(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'correo', 'clave', 'rol', 'foto']
    search_fields = ['nombre']
    list_editable = ["rol"]

    def ver_foto(self, obj):
        return mark_safe(f"<a href='{obj.foto.url}'><img src='{obj.foto.url}' width='25%'></a>")


@admin.register(Calificaciones)
class Calificaciones(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'cantidad_estrellas', 'servicio', 'foto']
    search_fields = ['cantidad_estrellas']


@admin.register(Citas)
class Citas(admin.ModelAdmin):

    list_display = ['id', 'fechaServicio',
                    'hora', 'cliente', 'servicio', 'empleado']

    search_fields = ['tipoServicio']


@admin.register(Facturas)
class Facturas(admin.ModelAdmin):
    list_display = ["id", "cliente", "fecha"]


@admin.register(DetalleFactura)
class DetalleFacturas(admin.ModelAdmin):
    list_display = ["id", "productos", "factura", "cantidad", "total"]


@admin.register(DetallesServicio)
class DetalleServicios(admin.ModelAdmin):
    list_display = ["id", "fecha", "servicio", "producto"]
