from django.db import models
from django.contrib.auth.models import AbstractUser
from .authentication import CustomUserManager

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=254) 
    descripcion_categoria = models.TextField()
    def __str__(self):
        return self.nombre

class Proveedores(models.Model):
    nombre=models.CharField(max_length=254)
    nit=models.IntegerField(unique=True)
    telefono=models.IntegerField(unique=True)
    correo=models.CharField(max_length=254,unique=True)
    def __str__(self):
        return self.nombre
    
class Productos(models.Model):
    nombre=models.CharField(max_length=254)
    Precio=models.IntegerField(null = False)
    descripcion_producto = models.TextField()
    cantidad=models.IntegerField()
    #fecha_Creacion=models.DateField()
    categoria=models.ForeignKey(Categoria,on_delete=models.DO_NOTHING,blank=False,null=True)
    foto = models.ImageField(upload_to="tienda/media/", default="tienda/media/default.png")
    
    def __str__(self):
        return self.nombre
    
class Servicios(models.Model):
    nombre = models.CharField(max_length=254)
    descripcion_servicio = models.TextField()
    foto = models.ImageField(upload_to="media/", default="tienda/media/servicio.jpg")
    precio = models.IntegerField(null=False,blank=False,default=100000)
    def __str__(self):
        return self.nombre
    
class Promociones(models.Model):
    servicio = models.ForeignKey(Servicios,on_delete=models.DO_NOTHING,blank=False,null=True)
    descripcion = models.CharField(max_length=254)
    foto = models.ImageField(upload_to="tienda/media/", default="tienda/media/servicio.jpg")

class Usuarios(AbstractUser):
    username = None
    nombre = models.CharField(max_length=254)
	# Custom model authentication: paso 4, el campo email para django es obligatorio, cambiar correo -> email
    email = models.EmailField(max_length=254, unique=True,blank=False,null=True)
	# Custom model authentication: paso 5, el campo password para django es obligatorio, cambiar clave -> password
    password = models.CharField(max_length=254,blank=False,null=True)
    foto = models.ImageField(upload_to="tienda/media/", default="tienda/media/user.png")
    token_recuperar = models.CharField(max_length=254,blank=False,null=False,default=0)
    telefono=models.IntegerField(null=False,blank=True,default='0')
    #fecha_contratacion=models.DateField(blank=True,null=False)
    cargo = models.CharField(max_length=254,null=False)
    direccion=models.CharField(max_length=254)
    cedula=models.IntegerField(blank=True,null=False,default='0')

    ROLES = (
        (1,"administrador"),
        (2,"proveedor"),
        (3,"empleado"),
        (4,"cliente"), 
    )
    rol=models.IntegerField(choices=ROLES,default=4)
    n = models.IntegerField(blank=True,null=False,default=0)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nombre"]
    objects = CustomUserManager()

    def __str__(self):
        return self.nombre
    

class Facturas(models.Model):
    cliente = models.ForeignKey(Usuarios,on_delete=models.DO_NOTHING,blank=False,null=True)
    fecha = models.DateField(auto_now=True)
    total = models.IntegerField(default=0)
    def __str__(self):
        return f'{self.cliente}'
    

class DetallesServicio(models.Model):
    servicio = models.ForeignKey(Servicios,on_delete=models.DO_NOTHING,default='1')
    producto = models.ManyToManyField(Productos,related_name='productos')
    descripcion_proceso = models.CharField(max_length=254,blank=False,null=True)
    



class Vehiculos(models.Model): 
    cliente = models.ForeignKey(Usuarios,on_delete=models.DO_NOTHING, blank=False,null=True)
    vehiculo = models.CharField(max_length=254,blank=False,null=True)
    modelo = models.IntegerField(default=1900)
    placa = models.CharField(max_length=6,blank=False, null=True)  
    kilometraje = models.IntegerField(default=1236456,blank=True,null=True)
    linea = models.CharField(max_length=254,blank=False,null=True)


class Citas(models.Model):
    fechaServicio = models.DateField(null=True)
    hora = models.TimeField(null=True)
    hora_fin = models.TimeField()
    cliente = models.ForeignKey(Usuarios,on_delete=models.DO_NOTHING,blank=False,null=True,related_name='cliente')
    servicio = models.ForeignKey(Servicios,on_delete=models.DO_NOTHING,blank=False,null=False)
    empleado = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING,blank=False,null=True,related_name='empleado')
    estados = (
        (1,"Pendiente"),
        (2,"Cancelado"),
        (3,"Finalizada"),

    )
    estado = models.IntegerField(choices=estados,default=1)
    observacion = models.CharField(max_length=254,null=False,blank=True)
    def __str__(self):
        return f'{self.fechaServicio}'
    
    def get_estado_display(self):
        return dict(self.estados).get(self.estado)


class DetalleFactura(models.Model):
    factura = models.ForeignKey(Facturas,on_delete=models.DO_NOTHING,default='1')
    producto = models.ForeignKey(Productos,on_delete=models.DO_NOTHING,default='1')
    cantidad = models.IntegerField()
    precio = models.IntegerField()
    
    def __str__(self):
        return f'{self.factura}'

    
    
class Calificaciones(models.Model):
    cliente = models.ForeignKey(Usuarios,on_delete=models.DO_NOTHING,blank=False,null=True)
    servicios = models.ForeignKey(Servicios,on_delete=models.DO_NOTHING,blank=False,null=True)
    foto = models.ImageField(upload_to="tienda/media/", default="tienda/media/user.png")
    Estrellas= (
        (1, "1"),
        (2,"2"),
        (3,"3"),
        (4,"4"),
        (4,"5"),
         
    )
    cantidad_estrellas = models.IntegerField(choices=Estrellas,default=5)
    def __str__(self):
        return f'{self.servicios}'
    
class Configuracion(models.Model):
    nombre = models.CharField(max_length=254)
    contacto = models.CharField(max_length=254)
    ubicacion = models.CharField(max_length=254)
    correo = models.CharField(max_length=254,blank=False,null=True)
    

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class RegistrarUsuario(models.Model):
	nombre = models.CharField(max_length=254)
	correo = models.EmailField(max_length=254, unique=True)
	clave1 = models.CharField(max_length=254)
	clave2 = models.CharField(max_length=254)

class Emergencia(models.Model):
    nombre = models.CharField(max_length=50)    
    telefono = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=254)
    ubicacion = models.CharField(max_length=254)
    empleado = models.ForeignKey(Usuarios, on_delete=models.DO_NOTHING,blank=True,null=True)
    estados = (
        (1,"Solicitada"),
        (2,"En proceso"),
        (3,"Finalizada"),

    )
    estado = models.IntegerField(choices=estados,default=1)


    def get_estado_display(self):
        return dict(self.estados).get(self.estado)
