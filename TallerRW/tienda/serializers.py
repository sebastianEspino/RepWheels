from rest_framework import serializers
from .models import *


class CategoriaSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id','nombre','descripcion_categoria']

class VehiculosSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vehiculos
        fields = ['id','cliente','vehiculo','modelo','placa','kilometraje','linea']


class ConfiguracionSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Configuracion
        fields = ['id','nombre','contacto','ubicacion','correo']

class RegistrarUsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RegistrarUsuario
        fields = ['id', 'nombre', 'correo', 'clave1', 'clave2']


class ProveedoresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Proveedores
        fields = ['id','nombre','nit','telefono','correo']


class ServiciosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields = ['id','nombre','descripcion_servicio']

class ProductosSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Productos
        fields = ['id','nombre','Precio','descripcion_producto','cantidad','categoria','foto']


class CitasSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Citas
        fields = ['id','fechaServicio','hora','servicio','cliente','empleado','estado']

class CalificacionesSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Calificaciones
        fields = ['id','cliente','cantidad_estrellas']



class UsuariosSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Usuarios
        fields = ['id','nombre','email','password','rol']


class FacturasSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Facturas
        fields = ['id','cliente']

class DetallesServicioSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DetallesServicio
        fields = ['id','servicio','producto','descripcion_proceso']

class DetalleFacturaSerializers(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = DetalleFactura
        fields = ['id','productos','categoria','cantidad','factura']