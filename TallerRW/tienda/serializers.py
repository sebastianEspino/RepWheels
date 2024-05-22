from rest_framework import serializers
from .models import *


class CategoriaSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'





class ServiciosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields = '__all__'

class ProductosSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'



class CitasSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Citas
        fields = '__all__'



class CalificacionesSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Calificaciones
        fields = '__all__'



class UsuariosSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Usuarios
        fields = '__all__'







