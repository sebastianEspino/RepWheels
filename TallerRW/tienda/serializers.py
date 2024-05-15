from rest_framework import serializers
from .models import *


class CategoriaSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id','nombre','descripcion_categoria']


class ProveedoresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Proveedores
        fields = ['id','nombre','nit','telefono','correo']


class ServiciosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields = ['id','nombre','descripcion_servicio','precio']

class ProductosSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Productos
        fields = ['id','nombre','Precio','descripcion_producto','cantidad','categoria','foto']

class EmpleadoSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empleado
        fields = ['id','nombre_completo','cedula','correo','telefono','fecha_contratacion','cargo']


class ClientesSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Clientes
        fields = ['id','nombre_completo','cedula','correo','telefono','direccion']

class CitasSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Citas
        fields = '__all__'
class CalificacionesSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Calificaciones
        fields = ['id','cliente','cantidad_estrellas']



class UsuariosSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Usuarios
        fields = ['id','nombre','correo','clave','rol']


class FacturasSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Facturas
        fields = ['id','cliente']

class DetallesServicioSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DetallesServicio
        fields = ['id','servicio','producto']

class DetalleFacturaSerializers(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = DetalleFactura
        fields = ['id','productos','categoria','cantidad','factura']


