from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=254) 
    descripcion_categoria = models.TextField()
    def __str__(self):
        return self.nombre


    
class Productos(models.Model):
    nombre=models.CharField(max_length=254)
    Precio=models.IntegerField(null = False)
    descripcion_producto = models.TextField()
    cantidad=models.IntegerField()
    fecha_Creacion=models.DateField()
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE,blank=False,null=True)
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
    telefono = models.IntegerField()
    cedula = models.IntegerField()
    direccion = models.CharField(max_length=254)
    cargo = models.CharField(max_length=254)
    ROLES = (
        (1,"administrador"),
        (2,"gerente"),
        (3,"empleado"),
        (4,"cliente"), 
    )
    rol=models.IntegerField(choices=ROLES,default=4)
    def __str__(self):
        return self.nombre



class Cofiguracione(models.Model):
    nombre = models.CharField(max_length=254)
    contacto = models.IntegerField()
    ubicacion = models.CharField(max_length=254)


class Vehiculos(models.Model): 
    usuario = models.ForeignKey(Usuarios,on_delete=models.CASCADE, blank=False,null=True)
    vehiculo = models.CharField(max_length=254,blank=False,null=True)
    modelo = models.IntegerField(default=1900)
    placa = models.CharField(max_length=6,blank=False, null=True)  
    kilometraje = models.IntegerField(default=1236456,blank=True,null=True)
    linea = models.CharField(max_length=254,blank=False,null=True)



    
class Calificaciones(models.Model):
    cliente = models.ForeignKey(Usuarios,on_delete=models.CASCADE,blank=False,null=True)
    servicio = models.ForeignKey(Servicios,on_delete=models.CASCADE,blank=False,null=True)
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
    cliente = models.ForeignKey(Usuarios,on_delete=models.CASCADE,blank=False,null=True)
    servicio = models.ForeignKey(Servicios,on_delete=models.CASCADE,blank=False,null=False)
    empleado = models.ForeignKey(Usuarios, on_delete=models.CASCADE,blank=False,null=True)
    vehiculo = models.ForeignKey(Vehiculos,on_delete=models.CASCADE)
    estados = (
        (1, "Pendiente"),
        (2,"Finalizado"),
        (3,"Cancelada"),
    )
    estado_cita = models.IntegerField(choices=estados,default= 3)

    def __str__(self):
        return f'{self.fechaServicio}'
    

class Personalizacion_servicio(models.Model):
    cita = models.ForeignKey(Citas,on_delete=models.CASCADE)
    servicio = models.ManyToManyField(Servicios)
    producto = models.ManyToManyField(Productos)
    def __str__(self):
        return self.cita



class Detalle_Producto(models.Model):
    cita = models.ForeignKey(Citas,on_delete=models.CASCADE,null=True)
    cantidad = models.IntegerField(null=True)
    producto = models.ManyToManyField(Productos,null=True)
    total = models.IntegerField()
    usuario = models.ForeignKey(Usuarios,on_delete=models.CASCADE)

    def __str__(self):
        return self.cita
    
class Promocione(models.Model):
    descripcion = models.CharField(max_length=254)
    foto = models.ImageField(upload_to="fotos_productos/", default="fotos_usuarios/user.png")
    servicio = models.ForeignKey(Servicios, on_delete=models.CASCADE,null=True)
