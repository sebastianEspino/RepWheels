from django.db import models

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
    fecha_Creacion=models.DateField()
    categoria=models.ForeignKey(Categoria,on_delete=models.DO_NOTHING,blank=False,null=True)
    foto = models.ImageField(upload_to="fotos_productos/", default="fotos_productos/default.png")
    
    def __str__(self):
        return self.nombre
    
class Servicios(models.Model):
    nombre=models.CharField(max_length=254)
    descripcion_servicio = models.TextField()
    foto = models.ImageField(upload_to="fotos_servicios/", default="fotos_servicios/servicio.jpg")
    precio = models.IntegerField(null=False,blank=False,default=100000)
    def __str__(self):
        return self.nombre
    

class Usuarios(models.Model):
    nombre=models.CharField(max_length=254)
    correo=models.CharField(max_length=254,unique=True)
    clave=models.CharField(max_length=8,null=False)
    foto = models.ImageField(upload_to="fotos_usuarios/", default="fotos_usuarios/user.png")
   
    ROLES = (
        (1,"administrador"),
        (2,"gerente"),
        (3,"empleado"),
        (4,"cliente"), 
    )
    rol=models.IntegerField(choices=ROLES,default=4)
    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre_completo = models.CharField(max_length=200,blank=False,null=True)
    cedula=models.IntegerField(unique=True)
    correo=models.CharField(max_length=254,unique=True)
    telefono=models.IntegerField(unique=True)
    fecha_contratacion=models.DateField()
    cargo=models.CharField(max_length=254)
    def __str__(self):
        return self.nombre_completo

class DetallesServicio(models.Model):
    fecha = models.DateField()
    servicio = models.ForeignKey(Servicios,on_delete=models.DO_NOTHING,default='1')
    producto = models.ForeignKey(Productos,on_delete=models.DO_NOTHING,default='1')
    def __str__(self):
        return self.fecha

class Clientes(models.Model):
    nombre_completo = models.ForeignKey(Usuarios,on_delete=models.CASCADE,blank=False,null=True)
    cedula=models.IntegerField(blank=True,null=False)
    correo = models.CharField(max_length=254,unique=True)
    telefono=models.IntegerField(blank=False,null =True)
    direccion=models.CharField(max_length=254)
    n = models.IntegerField(null=False, blank=True,default=0)
    def __str__(self):
        return self.nombre_completo


class Vehiculos(models.Model): 
    cliente = models.ForeignKey(Clientes,on_delete=models.DO_NOTHING, blank=False,null=True)
    vehiculo = models.CharField(max_length=254,blank=False,null=True)
    modelo = models.IntegerField(default=1900)
    placa = models.CharField(max_length=6,blank=False, null=True)  
    kilometraje = models.IntegerField(default=1236456,blank=True,null=True)
    linea = models.CharField(max_length=254,blank=False,null=True)


    
class Cotizaciones(models.Model):
    vehiculo = models.CharField(max_length=254,blank=False,null=True)
    modelo = models.IntegerField(default=1900)
    placa = models.CharField(max_length=6,blank=False, null=True)  
    kilometraje = models.IntegerField(default=1236456)
    linea = models.CharField(max_length=254,blank=False,null=True)
    servicio=models.ForeignKey(Servicios,on_delete=models.DO_NOTHING,blank= False, null= True)
    cliente = models.ForeignKey(Usuarios,on_delete=models.DO_NOTHING, blank=False,null=True)
    empleado = models.ForeignKey(Empleado,on_delete=models.DO_NOTHING)
    def _str_(self):
        return self.servicio
    
class Calificaciones(models.Model):
    cliente = models.ForeignKey(Usuarios,on_delete=models.DO_NOTHING,blank=False,null=True)
    servicio = models.ForeignKey(Servicios,on_delete=models.DO_NOTHING,blank=False,null=True)
    foto = models.ImageField(upload_to="fotos_productos/", default="fotos_usuarios/user.png")
    Estrellas= (
        (1, "1"),
        (2,"2"),
        (3,"3"),
        (4,"4"),
        (4,"5"),
         
    )
    cantidad_estrellas = models.IntegerField(choices=Estrellas,default=5)
    def __str__(self):
        return self.servicio
    

class Citas(models.Model):
    fechaServicio = models.DateField(null=True)
    hora = models.TimeField(null=True)
    cliente = models.ForeignKey(Usuarios,on_delete=models.DO_NOTHING,blank=False,null=True)
    servicio = models.ForeignKey(Servicios,on_delete=models.DO_NOTHING,blank=False,null=False)
    empleado = models.ForeignKey(Empleado, on_delete=models.DO_NOTHING,blank=False,null=True)
    estados = (
        (1, "Pendiente"),
        (2,"Finalizado"),
        (3,"Cancelada"),
    )
    estado_cita = models.IntegerField(choices=estados,default= 3)

    def __str__(self):
        return f'{self.fechaServicio}'

class Facturas(models.Model):
    cliente = models.ForeignKey(Usuarios,on_delete=models.DO_NOTHING,blank=False,null=True)
    fecha = models.DateField(auto_now=True)
    def __str__(self):
        return self.cliente

class DetalleFactura(models.Model):
    productos = models.CharField(max_length=254)
    cantidad = models.IntegerField(null=True)
    factura = models.ForeignKey(Facturas,on_delete=models.DO_NOTHING,default='1')
    total = models.IntegerField()

    def __str__(self):
        return self.factura