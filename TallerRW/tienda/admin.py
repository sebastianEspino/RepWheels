from django.contrib import admin
from .models import *
from django.utils.html import mark_safe

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Categoria._meta.fields]
    search_fields = ['nombre']



@admin.register(Productos)
class Producto(admin.ModelAdmin):
    list_display = [field.name for field in Productos._meta.fields]
    search_fields = ['nombre']

    def ver_foto(self, obj):
        return mark_safe(f"<a href='{obj.foto.url}'><img src='{obj.foto.url}' width='25%'></a>")


@admin.register(Servicios)
class Servicio(admin.ModelAdmin):
    list_display = [field.name for field in Servicios._meta.fields]
    search_fields = ['nombre']

    def ver_foto(self, obj):
        return mark_safe(f"<a href='{obj.foto.url}'><img src='{obj.foto.url}' width='25%'></a>")






class Vehiculos(admin.ModelAdmin):
    list_display = [field.name for field in Vehiculos._meta.fields]




@admin.register(Usuarios)
class Usuario(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'correo', 'clave', 'rol', 'foto']
    search_fields = ['nombre']
    list_editable = ["rol"]

    def ver_foto(self, obj):
        return mark_safe(f"<a href='{obj.foto.url}'><img src='{obj.foto.url}' width='25%'></a>")


@admin.register(Calificaciones)
class Calificaciones(admin.ModelAdmin):
    list_display = [field.name for field in Calificaciones._meta.fields]
    search_fields = ['cantidad_estrellas']


@admin.register(Citas)
class Citas(admin.ModelAdmin):

    list_display = [field.name for field in Citas._meta.fields]


