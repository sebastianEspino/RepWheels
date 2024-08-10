from django.contrib import admin
from .models import *
from django.utils.html import mark_safe

# Register your models here.
@admin.register(Categoria)
class Categoria(admin.ModelAdmin):
    list_display = ['id','nombre','descripcion_categoria']
    search_fields = ['nombre']

@admin.register(Productos)
class Producto(admin.ModelAdmin):
    list_display = ['id','nombre','Precio','descripcion_producto','cantidad','foto','ver_foto']
    search_fields = ['nombre']

    def ver_foto(self, obj):
        return mark_safe(f"<a href='{obj.foto.url}'><img src='{obj.foto.url}' width='25%'></a>")

    
@admin.register(Servicios)
class Servicio(admin.ModelAdmin):
    list_display = ['id','nombre','descripcion_servicio','foto','precio','ver_foto']
    search_fields = ['nombre']

    def ver_foto(self, obj):
        return mark_safe(f"<a href='{obj.foto.url}'><img src='{obj.foto.url}' width='25%'></a>")


class Vehiculos(admin.ModelAdmin):
    list_display = ['id','vehiculo']
    
@admin.register(Proveedores)
class Proveedores(admin.ModelAdmin):
    list_display = ['id','nombre','nit','telefono','correo']
    search_fields = ['nombre']
    
@admin.register(Usuarios)
class Usuario(admin.ModelAdmin):
    list_display=['id','nombre','email','password','rol','foto','ver_foto','token_recuperar']
    search_fields = ['nombre']
    list_editable = ["rol"]

    def ver_foto(self, obj):
        return mark_safe(f"<a href='{obj.foto.url}'><img src='{obj.foto.url}' width='25%'></a>")


@admin.register(Calificaciones)
class Calificaciones(admin.ModelAdmin):
    list_display=['id','cliente','servicios','cantidad_estrellas','foto']
    search_fields = ['cantidad_estrellas']



@admin.register(Citas)
class Citas(admin.ModelAdmin):
     list_display=['id','fechaServicio','hora','cliente','servicio','empleado','estado','hora_fin']
     search_fields = ['tipoServicio']

@admin.register(Facturas)
class Facturas(admin.ModelAdmin):
    list_display = ["id","cliente","fecha","total"]


@admin.register(DetalleFactura)
class DetalleFacturas(admin.ModelAdmin):
    list_display = ["id","factura","cantidad","precio"]


@admin.register(DetallesServicio)
class DetalleServicios(admin.ModelAdmin):
    list_display = ["id","descripcion_proceso","servicio"]

@admin.register(Promociones)
class Promociones(admin.ModelAdmin):
    list_display = ["id","servicio","descripcion","foto"]

@admin.register(Configuracion)
class Configuracion (admin.ModelAdmin):
    list_display = ["id","nombre","contacto","ubicacion"]