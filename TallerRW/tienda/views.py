from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*
from rest_framework import viewsets
from . serializers import *
from django.contrib import messages
from .crypt import *
from django.db import IntegrityError, transaction
from django.core.mail import BadHeaderError, EmailMessage
import datetime
from django.utils.timezone import localtime
from rest_framework.views import APIView
import re
import pytz
est = pytz.timezone('America/Bogota')
from django.db.models import Q
import folium
from .autorizacion import * 

# API with rest framework 

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializers

class ConfiguracionViewSet(viewsets.ModelViewSet):
    queryset = Configuracion.objects.all()
    serializer_class = ConfiguracionSerializers

class ProveedoresViewSet(viewsets.ModelViewSet):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerializers

class ServiciosViewSet(viewsets.ModelViewSet):
    queryset = Servicios.objects.all()
    serializer_class = ServiciosSerializers

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializers

class VehiculosViewSet(viewsets.ModelViewSet):
    queryset = Vehiculos.objects.all()
    serializer_class = VehiculosSerializers


class CitasViewSet(viewsets.ModelViewSet):
    queryset = Citas.objects.all()
    serializer_class = CitasSerializers

class CalificacionesViewSet(viewsets.ModelViewSet):
    queryset = Calificaciones.objects.all()
    serializer_class = CalificacionesSerializers


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializers


class FacturasViewSet(viewsets.ModelViewSet):
    queryset = Facturas.objects.all()
    serializer_class = FacturasSerializers

class DetalleFacturaViewSet(viewsets.ModelViewSet):
    queryset = DetalleFactura.objects.all()
    serializer_class = DetalleFacturaSerializers

class DetalleServicioViewSet(viewsets.ModelViewSet):
    queryset = DetallesServicio.objects.all()
    serializer_class = DetallesServicioSerializers

class RegistrarUsuarioViewSet(viewsets.ModelViewSet):
    queryset = RegistrarUsuario.objects.all()
    serializer_class = RegistrarUsuarioSerializer

class RegistrarUsuario(APIView):
    def post(self, request):
        print(request.data)
        if request.method == "POST":
            nombre = request.data["nombre"]
            correo = request.data["correo"]
            clave1 = request.data["password"]
            clave2 = request.data["confirmPassword"]
            nick = correo
            if nombre == "" or correo == "" or clave1 == "" or clave2 == "":
                return Response(data={'message': 'Todos los campos son obligatorios', 'respuesta': 400}, status=400)
            elif not re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', correo):
                return Response(data={'message': 'El correo no es válido', 'respuesta': 400}, status=400)
            elif clave1 != clave2:
                return Response(data={'message': 'Las contraseñas no coinciden', 'respuesta': 400}, status=400)
            else:
                try:
                    q = Usuarios(
                        nombre=nombre,
                        email=correo,
                        password=hash_password(clave1),

                    )
                    q.save()
                except Exception as e:
                    return Response(data={'message': 'El Usuario ya existe', 'respuesta': 409}, status=409)

        # Renderiza la misma página de registro con los mensajes de error
        return Response(data={'message': f'Usuario creado correctamente tu nick es: {nick}', 'respuesta': 201}, status=201)


def index(request):
    initialMap = folium.Map(location=[6.1817678,-75.6071863],zoom_start=11)
    logueo = request.session.get("logueo", False)
    q = Calificaciones.objects.all()
    s = Servicios.objects.all()
    p = Promociones.objects.all()
    contexto = {"data":q,"servicios":s,"map":initialMap,"Promociones":p}
    return render(request, "tienda/index.html",contexto)


# crud de  productos.


def productos(request):
    p = Productos.objects.all()
    q = Promociones.objects.all()
    contexto = {'data':p,"Promociones":q}
    return render(request,"tienda/productos/producto.html",contexto)


@login_requerido_admin
def listarProductos(request):
    q = Productos.objects.all()
    p = Promociones.objects.all()
    contexto = {"data":q,"Promociones":p}
    return render(request, "tienda/productos/listarProductos.html",contexto)


def editarProductos(request, id):
	q = Productos.objects.get(pk=id)
	c = Categoria.objects.all()
	contexto = {"data": q, "categoria": c}
	return render(request, "tienda/productos/editarProductos.html", contexto)


def actualizarProductos(request):
	if request.method == "POST":
            id = request.POST.get("id")
            nombre = request.POST.get("nombre")
            Precio = request.POST.get("precio")
            descripcion_producto = request.POST.get("descripcion_producto")
            cantidad = request.POST.get("cantidad")
            foto = request.FILES.get("foto_new")
            if not foto:
                foto = 'tienda/media/default.png'
        
            categoria = Categoria.objects.get(pk=request.POST.get("categoria"))
        
    
            if nombre == "" or Precio == "" or descripcion_producto == "" or cantidad == "" or foto == "" or categoria == "":
                messages.error(request,'No se permite campos vacios')
            elif nombre.isnumeric():
                messages.error(request,'No se permite numeros en el nombre del producto')
            elif int(Precio) <= 0 or int(cantidad) <= 0:
                messages.error(request,'No se permite numeros negativos ni valores a cero')
            else: 
                try:
                    q = Productos.objects.get(pk=id)
                    q.nombre = nombre
                    q.Precio = Precio
                    q.descripcion_producto = descripcion_producto
                    q.cantidad = cantidad
                    q.foto = foto
                    q.categoria = categoria
                    q.save()
                    messages.success(request, "Producto actualizado correctamente!!")
                except Exception as e:
                    messages.error(request, f"Error: {e}")
	else:
		messages.warning(request, "Error: No se enviaron datos...")

	return redirect("listarProductos")


def eliminarProductos(request, id):
	try:
		q = Productos.objects.get(pk=id)
		q.delete()
		messages.success(request, "Eliminado, Exitosaamiente!")
	except Exception as e:
		messages.error(request, f"Error: {e}")
        
	return redirect("listarProductos")

@login_requerido_admin
def crearProductoform(request):
	q = Categoria.objects.all()
	contexto = {"data": q}
	return render(request, "tienda/productos/registrarRepuestos.html", contexto)



def crearProducto(request):
    if request.method == "POST":
            nombre = request.POST.get("nombre")
            precio = request.POST.get("precio")
            descripcion_producto = request.POST.get("descripcion_producto")
            cantidad = request.POST.get("cantidad")
            foto = request.FILES.get("foto_new")

            if not foto:
                foto = 'tienda/media/default.png'
            
            
            categoria = Categoria.objects.get(pk=request.POST.get("categoria"))

            if nombre == "" or precio == "" or descripcion_producto == "" or cantidad == "" or categoria == "":
                messages.error(request,'No se permite campos vacios')
            elif nombre.isnumeric():
                messages.error(request,'No se permite numeros en el nombre del producto')
            elif int(precio) <= 0 or int(cantidad) <= 0:
                messages.error(request,'No se permite numeros negativos ni valores a cero')
            
            else: 
                try:
                    q = Productos(
                        nombre = nombre,
                        Precio = precio,
                        descripcion_producto = descripcion_producto,
                        cantidad = cantidad,
                        foto = foto,
                        categoria = categoria
                    )   
                    q.save()
                    messages.success(request, "Guardado correctamente!!")
                except Exception as e:
                    messages.error(request, f"Error: {e}")
                return redirect("listarProductos")
    else:
	    messages.warning(request, "Error: No se enviaron datos...")
    
    return redirect("listarProductos")
	
    

          
#crud de clientes
@login_requerido_admin
def registrarCliente(request):
    return render(request, "tienda/clientes/registrarCliente.html")

@login_requerido_admin
def listarCliente(request):
    q = Usuarios.objects.filter(rol=4)
    contexto = {"data" : q}
    return render(request, "tienda/clientes/listarCliente.html",contexto)


def clientesCrear(request):
    if request.method == 'POST':
        cedula=request.POST.get('cedula')        
        nombre=request.POST.get('nombre_completo')
        correo=request.POST.get('correo')
        password =request.POST.get('password')

        if nombre == "" or cedula == "" or correo == "" or cedula == "":
            messages.error(request,f'Campos Vacios!')
        elif int(cedula) <= 0:
            messages.error(request,f'La cedula no puede ser un numeor negativo')
        elif not re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', correo):
            messages.error(request,f'El correo no es valido')
        elif len(password) <= 6:
            messages.error(request,f'La clave es demasiado corta')
        else:

            try:
                q = Usuarios(
                    cedula=cedula,
                    nombre=nombre,
                    email=correo,
                    password=hash_password(password)
                )
                q.save()
                messages.success(request,"Guardado Correctamente!")
            except Exception as e:
                messages.error(request,f"Error:{e}")
            

    else:
        messages.error(request,"Error: no se enviaron datos")
        

    return redirect('listarCliente')


def clientesEliminar(request,id):
    try:
        q = Usuarios.objects.get(pk = id)
        q.delete()
        messages.success(request,"Cliente eliminado Correctamente!")
    except Exception as e:
        messages.error(request,f"El usuario ya tiene procesos pendientes")
    return redirect('listarCliente')

def clientesEditar(request,id):
    q = Usuarios.objects.get(pk = id)
    contexto = {"data" : q}
    return render(request,"tienda/clientes/editarCliente.html",contexto)

def clientesActualizar(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        cedula=request.POST.get('cedula')        
        nombre_completo=request.POST.get('nombre_completo')
        correo=request.POST.get('correo')
        telefono=request.POST.get('telefono')

        if nombre_completo == "" or cedula == "" or correo == "" or telefono == "":
            messages.error(request,f'Campos Vacios!')
            return redirect("listarCliente")
        elif int(cedula) <= 0 or int(telefono) < 0:
            messages.error(request,f'La cedula no puede ser un numeor negativo')
            return redirect("listarCliente")
        elif not re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', correo):
            messages.error(request,f'El correo no es valido')
            return redirect("listarCliente")
        else:
            try:
                q=Usuarios.objects.get(pk=id)
                q.cedula = cedula
                q.nombre = nombre_completo
                q.email = correo
                q.telefono = telefono
                q.save()
                messages.success(request, "Cliente actualizado correctamente!!")
            except Exception as e:
                messages.error(request,f"ERROR:{e}")
            return redirect("listarCliente")
    else:
        messages.error(request,"Error: no se enviaron datos")
        return redirect("listarCliente")
        
#Crud empleados
@login_requerido_admin
def empleados(request):
	q = Usuarios.objects.filter(rol=3)
	contexto = {"data": q}
	return render(request, "tienda/empleados/listarempleados.html", contexto)

@login_requerido_admin
def nuevoempleado(request):
    u = Usuarios.objects.all()
    contexto = {"data":u}
	
    return render(request, "tienda/empleados/crearempleado.html",contexto)

def newempleado(request):
    if request.method == 'POST':
        cedula = request.POST.get('cedula')
        nombre = request.POST.get('nombre')
        password = request.POST.get('password')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        cargo = request.POST.get('cargo')

        if nombre == "" or cedula == "" or correo == "" or password == "" or telefono == "" or cargo == "":
            messages.error(request,f'Campos Vacios!')
        elif int(telefono) < 0 or int(cedula) < 0:
            messages.error(request,f'Los datos numericos no pueden ser negativos')
        elif not re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', correo):
                messages.error(request,f'El correo no es valido')
        elif len(password) <= 6:
            messages.error(request,f'La clave es demasiado corta')
        else:
            try:
                q = Usuarios(
                    nombre = nombre,
                    cedula = cedula,
                    password = hash_password(password),
                    email = correo,
                    telefono = telefono,
                    cargo = cargo,
                    rol = 3

                )
                q.save()
                messages.success(request, 'guardado correctamente')
            except Exception as e:
                messages.error(request, f"Error: {e}")
    return redirect('empleado')


def empleados_formulario_editar(request, id):
	q = Usuarios.objects.get(pk=id)
	c = Usuarios.objects.filter(rol=3)
	contexto = {"data": q, "empleado": c}
	return render(request, "tienda/empleados/editarempleados.html", contexto)


def empleado_actualizar(request):
	if request.method == "POST":
            id = request.POST.get("id")
            nombre = request.POST.get("nombre")
            correo = request.POST.get("correo")
            telefono = request.POST.get("telefono")
            cargo = request.POST.get("cargo")

            if nombre == ""  or correo == "" or telefono == "" or cargo == "":
                messages.error(request,f'Campos Vacios!')
            elif int(telefono) <= 0:
                messages.error(request,f'Los datos numericos no pueden ser negativos')
            elif not re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', correo):
                    messages.error(request,f'El correo no es valido')
            else:
           
                try:
                    q = Usuarios.objects.get(pk=id)
                    q.nombre = nombre
                    q.email = correo
                    q.telefono = telefono
                    q.cargo = cargo
                    q.save()
                    messages.success(request, "Empleado actualizado correctamente!!")
                except Exception as e:
                    messages.error(request, f"Error: {e}")
	else:
		messages.warning(request, "Error: No se enviaron datos...")

	return redirect("empleado")

def empleado_eliminar(request, id):
	try:
		q = Usuarios.objects.get(pk=id)
		q.delete()
		messages.success(request, "Empleado eliminada correctamente!!")
	except Exception as e:
		messages.error(request, f"Error: {e}")

	return redirect("empleado")

#crud proveedores
def proveedores_registrar(request):
	return render(request, "tienda/proveedores/registrarProveedor.html")

def listar_proveedores(request):
	q = Proveedores.objects.all()
	contexto = {"data": q}
	return render(request, "tienda/proveedores/listarProveedor.html", contexto)


def proveedores_add(request):
	if request.method == "POST":
            nombre = request.POST.get("nombre")
            nit  = request.POST.get("nit")
            correo = request.POST.get("correo")
            tele = request.POST.get("tele")
            q = Proveedores(
                nombre =  nombre,
                correo = correo,
                nit = nit,
                telefono = tele,
        
            )
            q.save()
            messages.success(request, "Guardado correctamente!!")
            return redirect("listarProveedores")
        
def registrar_proveedores_editar(request,id):
    q = Proveedores.objects.get(pk=id)
    contexto = {"data": q}
    return render(request,"tienda/proveedores/registrarProveedorEditar.html",contexto)


def proveedores_actualizar(request):
        if request.method == "POST":
            id = request.POST.get("id")
            nombre = request.POST.get("nombre")
            nit  = request.POST.get("nit")
            correo = request.POST.get("correo")
            tele = request.POST.get("tele")
            try:
                q = Proveedores.objects.get(pk=id)
                q.nombre = nombre
                q.nit = nit
                q.correo = correo
                q.telefono = tele
                q.save() 
                messages.success(request,"Proveedor actualizada correctamente!!")
            except Exception as e:
                messages.error(request,f'Error: {e}')
        else:
            messages.warning(request,f'Error:No se enviaron los datos!!')
        return redirect('listarProveedores')

def proveedores_delete(request,id):
    try:
        q = Proveedores.objects.get(pk=id)
        q.delete()
        messages.success(request,"Proveedores eliminada correctamente!!!")
    except Exception as e:
        messages.error(request,f'Error:{e}')

    return redirect('listarProveedores')

#CRUD de Citas

def citas(request):
    l = request.session.get("logueo",False)
    if l == False:
         c = Servicios.objects.all()
         e = Usuarios.objects.filter(rol=3)  
         contexto = {"data1": c , "data2":e}
         return render(request, "tienda/citas/cita.html",contexto)
    else:
        now = date.today()
        q = Citas.objects.all() 
        for dates in q:
            if dates.fechaServicio.day < now.day or dates.fechaServicio.month < now.month or dates.fechaServicio.year < now.year:
                dates.delete()
        c = Servicios.objects.all()
        e = Usuarios.objects.filter(rol=3)  
        contexto = {"data": q,"data1": c , "data2":e}
        return render(request, "tienda/citas/cita.html",contexto)
    
@login_requerido_emplo
def citasEmpleado(request):
    l = request.session.get('logueo',False)
    u = Usuarios.objects.get(pk=l["id"])
    q = Citas.objects.filter(empleado=u).exclude(estado=3)
    
    context = {'citas':q}
    return render(request, "tienda/citas/citas_empleado.html",context)

def cancell(request):
    
    if request.method == 'POST':
        id = request.POST.get('id')
        obs = request.POST.get('observacion')

        c = Citas.objects.get(pk=id)
        u = Usuarios.objects.get(nombre = c.cliente)
        c.estado = 2
        c.observacion = obs
        c.save()
        destinatario = u.email
        mensaje = f"""
                        <h1 style='color:blue;'>RepWheels</h1>
                        <p>Senor(@) {u.nombre} <br>Motivo de la cancelacion: <br> {obs}</p>
                        <p>Este correo solamente es para brindar informacion</p>
        
                        """
        try:
            msg = EmailMessage("RepWheels", mensaje, settings.EMAIL_HOST_USER, [destinatario])
            msg.content_subtype = "html"  # Habilitar contenido html
            msg.send()

        except BadHeaderError:
            messages.error(request, "Encabezado no válido")
        except Exception as e:
            messages.error(request, f"Error: {e}")

        messages.success(request,'La cita se ha cancelado correctamente!!')

    return redirect('citaEmpleado')

    
def finish(request):
    
    if request.method == "POST":
        id = request.POST.get('id')
        obs = request.POST.get('observacion')
        c = Citas.objects.get(pk=id)
        
        u = Usuarios.objects.get(nombre=c.cliente)
        c.estado = 3
        c.observacion = obs
        c.save()

        destinatario = u.email
        mensaje = f"""
                        <h1 style='color:blue;'>RepWheels</h1>
                        <p>Su cita que adquirio ya ha finalizado</p>
                        """
        try:
            msg = EmailMessage("RepWheels", mensaje, settings.EMAIL_HOST_USER, [destinatario])
            msg.content_subtype = "html"  # Habilitar contenido html
            msg.send()
            messages.success(request,"Correo enviado!!")
        except BadHeaderError:
            messages.error(request, "Encabezado no válido")
        except Exception as e:
            messages.error(request, f"Error: {e}")

        

        messages.success(request,'La cita se ha terminado correctamente!!')

    return redirect('citaEmpleado')
      
@login_requerido_admin
def registrarCita(request):
    e = Usuarios.objects.filter(rol=3)
    c = Servicios.objects.all()
    u = Usuarios.objects.all()
    contexto = {"data": e ,"data1":c,"usuarios":u}
    return render(request, "tienda/citas/registrarCita.html",contexto)

@login_requerido_admin
def listarCita(request):
    q = Citas.objects.all()
    contexto = {"data": q}
    return render(request, "tienda/citas/listarCita.html", contexto)


from datetime import date , time , datetime

def citaRegistrar(request):
    logueo = request.session.get("logueo",False)
    if logueo:
        u = Usuarios.objects.get(pk=logueo["id"])
        if request.method == "POST":
            import datetime

            if u.rol == 1:
                usuario = Usuarios.objects.get(pk=request.POST.get("usuario"))
            else:
                usuario = u

            fecha_servicio = request.POST.get('fechaServicio')
            hora = request.POST.get('hora')
            servicio = Servicios.objects.get(pk=request.POST.get("servicio"))
            empleado = Usuarios.objects.get(pk=request.POST.get("empleado"))
            today = date.today()
            if fecha_servicio == "" or hora == "" or servicio == "" or empleado == "":
                messages.error(request,'No se permiten campos vacios')
                return redirect("citas")
            hora = datetime.datetime.strptime(hora, '%H:%M')
            data_customer = datetime.datetime.strptime(fecha_servicio, '%Y-%m-%d')
            hora_fin = hora + datetime.timedelta(hours=0, minutes=59)

            citas = Citas.objects.filter(Q(fechaServicio=fecha_servicio) | Q(empleado=empleado))

        
            if fecha_servicio == "" or hora == "" or servicio == "" or empleado == "" or data_customer == None:
                messages.error(request,'No se permiten campos vacios')
                return redirect("citas")
            else:
                if data_customer.month >= today.month and data_customer.year >= today.year:   
                    
                    for agenda in citas:
                        hora_inicio_existente = agenda.hora
                        hora_fin_existente = agenda.hora_fin

                        
                        if agenda.empleado == empleado and agenda.fechaServicio == datetime.datetime.strptime(fecha_servicio, '%Y-%m-%d').date():
                            if (hora.time() < hora_fin_existente and hora_fin.time() > hora_inicio_existente):
                                messages.error(request, f"HORAS CRUZADAS No puedes agendar citas a esta hora: {hora} con este servicio: {servicio} y con este empleado: {empleado}")
                                break
                        if (agenda.fechaServicio == fecha_servicio):
                            print('Aqui fecha !!')
                            messages.error(request,'Esta ocupado por otro usuario')
                            break
                    else:
                            cita = Citas(
                                    fechaServicio=fecha_servicio,
                                    hora = hora,
                                    cliente = usuario,
                                    servicio = servicio ,
                                    empleado = empleado,
                                    hora_fin = hora_fin
                                )

                            cita.save()
                                
                            messages.success(request, "Cita guardada correctamente!!")
                    
                else:
                    messages.warning(request, "Error en la fecha!!")
                
            if u.rol == 1:
                return redirect("listarCita")
    else:
        messages.warning(request,"Debes iniciar sesion")

    
    
    return redirect("citas")        

        

def cita_formulario_editar(request, id):
    q = Citas.objects.get(pk=id)
    e = Usuarios.objects.filter(rol=3)
    c = Servicios.objects.all()
    contexto = {"data": q,"data1":e,"data2":c}
    return render(request, "tienda/citas/editarCita.html", contexto)

def citaActualizar(request):
    logueo = request.session.get("logueo",False)
    usuario = Usuarios.objects.get(pk=logueo["id"])
    if request.method == "POST":
        id = request.POST.get("id")
        fecha_servicio = request.POST.get("fechaServicio")
        hora = request.POST.get('hora')
        servicio = Servicios.objects.get(pk=request.POST.get("servicio_e"))
        empleado = Usuarios.objects.get(pk=request.POST.get("empleado_e"))
        try:

            today = date.today()
        
            data_customer = datetime.strptime(fecha_servicio, '%Y-%m-%d')
            if data_customer.month >= today.month and data_customer.year >= today.year:
                 

                q = Citas.objects.get(pk=id)
                q.fechaServicio = fecha_servicio
                q.cliente = usuario
                q.hora = hora
                q.empleado = empleado
                q.servicio = servicio
                
                q.save()

                messages.success(request, "Cita actualizada correctamente!!")
            else:
                messages.warning(request, "Error en la fecha!!")

        except Citas.DoesNotExist:
            messages.error(request, "Cita no encontrada.")
        except Exception as e:
            messages.error(request, f'Error: {e}')
    else:
        messages.warning(request, 'Error: No se enviaron los datos!!')

    if usuario.rol == 4:
        return redirect('citas')
    else:
        return redirect('listarCita') 

def citaEliminar(request, id):
    try:
        cita = Citas.objects.get(pk=id)
        cita.delete()
        messages.success(request, "Cita eliminada correctamente!!!")
    except Citas.DoesNotExist:
        messages.error(request, "Cita no encontrada.")
    except Exception as e:
        messages.error(request, f'Error: {e}')
    return redirect('listarCita')

@login_requerido
def deleteDateFromCustomer(request):
    try:
        if request.method == "POST":
            id = request.POST.get('idDate')
            cita = Citas.objects.get(pk=id)
            cita.delete()
            messages.success(request, "Cita eliminada correctamente!!!")
    except Citas.DoesNotExist:
        messages.error(request, "Cita no encontrada.")
    except Exception as e:
        messages.error(request, f'Error: {e}')
    return redirect('citas')

@login_requerido
def historialCita(request):
     logueo = request.session.get("logueo",False)
     usuario = Usuarios.objects.get(pk=logueo["id"])

     if usuario.rol == 4 :
        c = Citas.objects.filter(cliente = usuario)
     elif usuario.rol == 1:
        c = Citas.objects.all()
     else:
        c = Citas.objects.filter(empleado=usuario)

     contexto = {"data":c}
     return render(request,'tienda/citas/historialCitas.html',contexto)

#CRUD cotizaciones
@login_requerido
def cotizaciones(request):
    e = Usuarios.objects.all()
    s = Servicios.objects.all()
    contexto = {"empleados":e, "servicios":s}
    return render(request, "tienda/categorias/cotizacion.html",contexto)


@login_requerido_admin
def registrarCategoria(request):
    return render(request,'tienda/categorias/registrarCategoria.html')


@login_requerido_admin
def listarCategoria(request):
    q = Categoria.objects.all()
    context = {"data": q}
    return render(request, "tienda/categorias/listarCategoria.html", context)



def categoriaRegistrar(request):
	if request.method == "POST":
            n = request.POST.get("nombre")
            d = request.POST.get("descripcion")    
            if n.isnumeric() or d.isnumeric():
                messages.error(request,f'No se permite numeros en el nombre!') 
            elif n == "" or d == "":
                messages.error(request,f'Campos Vacios!')
                return redirect('registrarCategoria')
            else:     
                q = Categoria(
                    nombre = n,
                    descripcion_categoria = d,      
                )
                q.save()
                messages.success(request, "Guardado correctamente!!")
            
            return redirect("listarCategoria")


def categoriaEliminar(request,id):
    try:
        q = Categoria.objects.get(pk=id)
        q.delete()
        messages.success(request,"Categoria eliminada correctamente!!!")
    except Exception as e:
        messages.error(request,f'Error:{e}')
    return redirect('listarCategoria')


def categoriaEditar(request,id):
    q = Categoria.objects.get(pk=id)
    context = {"data":q}
    return render(request,'tienda/categorias/registrarCategoriaEditar.html',context)



def categoriaActualizar(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        n = request.POST.get("categoria")
        d = request.POST.get("descripcion")   
        if n.isnumeric() or d.isnumeric():
                messages.error(request,f'No se permite numeros en el nombre!') 
        elif n == "" or d == "":
            messages.error(request,f'Campos Vacios!')
            return redirect('registrarCategoria')
        try:
            q  = Categoria.objects.get(pk=id)
            q.nombre = n
            q.descripcion_categoria = d    
            q.save()
        except Exception as e:
                messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,f'Error:No se enviaron los datos!!')
    return redirect('listarCategoria')

#CRUD calificaiones 

def calificaciones(request):
    q = Calificaciones.objects.all()
    s = Servicios.objects.all()
    
    contexto = {"data":q,"servicios":s}
    return render(request, "tienda/calificaciones/calificacion.html",contexto)

def agregar_calificacion_form(request):
    q = request.session.get("logueo",False)
    if q:
        u = Usuarios.objects.get(pk=q["id"])
        if request.method == "POST":
            servicio = Servicios.objects.get(pk=request.POST.get("servicio"))
            estrellas = int(request.POST.get("estrellas"))
            if servicio == "" or estrellas == "":
                messages.error(request,f'Campos Vacios!')
            else:
                try:
                    
                    q = Calificaciones(
                        cliente=u, 
                        servicios = servicio,
                        foto = u.foto,
                        cantidad_estrellas = estrellas
                    )
                    
                    q.save()
                    messages.success(request,"calificacion realizada correctamente")
                    
                except Exception as e:
                    messages.error(request, f"Error: {e}")

    else:
        messages.warning(request,"Debes iniciar sesion para poder realizar la calificacion")        
    
    return redirect('calificaciones')

@login_requerido_admin
def registrarCalificacion(request):
    s = Servicios.objects.all()
    u = Usuarios.objects.all()
    contexto = {"data":s,"usuarios":u}
    return render(request, "tienda/calificaciones/registrarCalificacion.html",contexto)


def listarCalificacion(request):
    r = Calificaciones.objects.all()
    contexto = {"data": r}
    return render(request, "tienda/calificaciones/listarCalificacion.html", contexto)


def calificacionRegistrar(request):
    if request.method == "POST":
        logueo = request.session.get("logueo",False)
        usuario =  Usuarios.objects.get(pk=logueo["id"])
        if usuario.rol == 1:
            usuario = Usuarios.objects.get(pk=request.POST.get("usuario"))
        else:
            usuario = usuario
        servicio = Servicios.objects.get(pk=request.POST.get("servicio"))
        cantidad_estrellas = request.POST.get("cantidad_estrellas")
        if servicio == "" or cantidad_estrellas == "" or usuario == "":
            messages.error(request,f'Campos Vacios!')
        try:
        
            calificacion = Calificaciones(
                cliente=usuario,
                servicios = servicio,
                cantidad_estrellas=cantidad_estrellas,
            )
            calificacion.save()

            messages.success(request, "Calificación guardada correctamente!!")
            return redirect("calificacionListar")
        except Exception as e:
             messages.error(request, f"Error: {e}")
             return redirect('registrarCalificacion')
    return redirect('registrarCalificacion')
        


def calificacion_formulario_editar(request, id):
    r = Calificaciones.objects.get(pk=id)
    s = Servicios.objects.all()
    u = Usuarios.objects.all()
    contexto = {"data": r,"servicios":s,"usuarios":u}
    return render(request, "tienda/calificaciones/editarCalificacion.html", contexto)



def calificacionActualizar(request):
    if request.method == "POST":
        id = request.POST.get("id")
        logueo = request.session.get("logueo",False)
        usuario =  Usuarios.objects.get(pk=logueo["id"])
        if usuario.rol == 1:
            usuario = Usuarios.objects.get(pk=request.POST.get("usuario"))
        else:
            usuario = usuario
        servicio = Servicios.objects.get(pk=request.POST.get("servicio"))
        cantidad_estrellas = request.POST.get("cantidad_estrellas")
        
        if servicio == "" or cantidad_estrellas == "" or usuario=="":
            messages.error(request, f"No puede haber campos vacios")
        elif int(cantidad_estrellas) < 0:
            messages.error(request,f'El numero de estrellas no puede ser negativo')
        else:

            try:
                calificacion = Calificaciones.objects.get(pk=id)
                calificacion.cliente = usuario
                calificacion.servicios = servicio
                calificacion.cantidad_estrellas = cantidad_estrellas

                calificacion.save()

                messages.success(request, "Calificación actualizada correctamente!!")
            except Calificaciones.DoesNotExist:
                messages.error(request, "Calificación no encontrada.")
            except Exception as e:
                messages.error(request, f'Error: {e}')
    else:
        messages.warning(request, 'Error: No se enviaron los datos!!')

    return redirect('calificacionListar')


def calificacion_eliminar(request, id):
    l = request.session.get('logueo',False)
    usuario = Usuarios.objects.get(pk=l['id'])
    try:
        calificacion = Calificaciones.objects.get(pk=id)
        calificacion.delete()

        messages.success(request, "Calificación eliminada correctamente!!!")
    except Calificaciones.DoesNotExist:
        messages.error(request, "Calificación no encontrada.")
    except Exception as e:
        messages.error(request, f'Error: {e}')

    if usuario.rol == 1:
        return redirect('calificacionListar')
    else:
        return redirect('calificaciones')
    


def historialCalificacion(request):
    l = request.session.get('logueo',False)
    usuario = Usuarios.objects.get(pk=l['id'])

    if usuario.rol != 1: 
        calificaciones = Calificaciones.objects.filter(cliente=usuario)
    else:
        calificaciones = Calificaciones.objects.all()
    
    contexto = {"data":calificaciones}
        
    
    return render(request,'tienda/calificaciones/calificaciones_personal.html',contexto)
    

def historialEmergencias(request):
    l = request.session.get('logueo',False)
    usuario = Usuarios.objects.get(pk=l['id'])

    if usuario.rol != 1: 
        emergencia = Emergencia.objects.filter(empleado=usuario)
    else:
        emergencia = Emergencia.objects.all()
    
    contexto = {"data":emergencia}
        
    
    return render(request,'tienda/maps/historialEmergencia.html',contexto)
    

#Crud Servicio

def servicio(request):
    q = Servicios.objects.all()
    p = Promociones.objects.all()
    context = {"data":q , 'promociones' : p}
    return render(request, "tienda/servicios/servicio.html",context)
     
def detalleServicioEliminar(request,id):
    try:
        servicios = DetallesServicio.objects.get(pk=id)
        servicios.delete()

        messages.success(request, "Detalle servicio eliminado eliminado correctamente!!!")
    except Calificaciones.DoesNotExist:
        messages.error(request, "Servicio no encontrada.")
    except Exception as e:
        messages.error(request, f'Error: Error')

    return redirect('listarServicio')

@login_requerido_admin
def registrarServicio(request):
    return render(request,'tienda/servicios/registrarServicio.html')

@login_requerido_admin
def listarServicio(request):
    q = Servicios.objects.all()
    s = DetallesServicio.objects.all()
    
    productos = Productos.objects.all()
    contexto = {"data":q,"productos": productos,"data1":s}
    return render(request,'tienda/servicios/listarServicio.html',contexto)


def registroServicio(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion_servicio = request.POST.get("descripcion_servicio")
        precio = request.POST.get('precio')
        foto = request.FILES.get("foto_new") 
        if not foto:
            foto = 'tienda/media/servicio.jpg'
    
        if nombre.isnumeric() or descripcion_servicio.isnumeric():
            messages.error(request,f'No se permite numeros en el nombre!')
        elif nombre == "" or precio == "" or descripcion_servicio == "" or precio == "":
            messages.error(request,f'Campos Vacios!')
        elif int(precio) <= 0:
            messages.error(request,f'El precio no puede ser negativo')
        else:
            try:
                
                servicios = Servicios(
                    nombre=nombre,
                    descripcion_servicio=descripcion_servicio,
                    precio = precio,
                    foto = foto
                )
                servicios.save()

                messages.success(request, "Servicio guardada correctamente!!")
                return redirect("listarServicio")
            except Exception as e:
                messages.error(request, f"Error: {e}")
    return redirect('registrarServicio') 


def servicioEliminar(request,id):
    try:
        servicios = Servicios.objects.get(pk=id)
        servicios.delete()

        messages.success(request, "Servicio eliminado correctamente!!!")
    except Calificaciones.DoesNotExist:
        messages.error(request, "Servicio no encontrada.")
    except Exception as e:
        messages.error(request, f'Error: {e}')

    return redirect('listarServicio')


def registrarDetalles(request):
    if request.method == "POST":
        id = request.POST.get("id")
        servicio = Servicios.objects.get(pk=id)
        descripcion_proceso = request.POST.get("descripcion_proceso")
        productos_seleccionados = request.POST.getlist('productos')

        if descripcion_proceso == "" or productos_seleccionados == "":
            messages.error(request,'No se permite campos vacios')
        else:
            try:
                
                ds = DetallesServicio(
                    servicio = servicio,
                    descripcion_proceso=descripcion_proceso,
                    
                )
                ds.save()
                ds.producto.set(productos_seleccionados)
            
                messages.success(request, "Servicio guardada correctamente!!")
                return redirect("listarServicio")
            except Exception as e:
                messages.error(request, f"Error: {e}")
                print(e)
    
    return redirect('listarServicio')


def servicio_form_editar(request,id):
    s = Servicios.objects.get(pk=id)

    context = {"data": s}
    return render(request,'tienda/servicios/editarServicio.html',context)


def servicioActualizar(request):
    if request.method == "POST":
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        descripcion_servicio = request.POST.get('descripcion_servicio')
        precio = request.POST.get('precio')
        foto = request.FILES.get("foto_new")

        if not foto:
            foto = 'tienda/media/servicio.jpg'
        
        if nombre.isnumeric() or descripcion_servicio.isnumeric():
            messages.error(request,f'No se permite numeros en el nombre!')
        elif nombre == "" or precio == "" or descripcion_servicio == "" or precio == "":
            messages.error(request,f'Campos Vacios!')
        elif int(precio) <= 0:
            messages.error(request,f'El precio no puede ser negativo')
        else:
                
            try:
                servicio = Servicios.objects.get(pk=id)
                servicio.nombre = nombre
                servicio.descripcion_servicio = descripcion_servicio
                servicio.precio = precio
                foto = foto
                servicio.save()

                messages.success(request, "Servicio actualizada correctamente!!")
            except Calificaciones.DoesNotExist:
                messages.error(request, "Servicio no encontrada.")
            except Exception as e:
                messages.error(request, f'Error: {e}')
    else:
        messages.warning(request, 'Error: No se enviaron los datos!!')

    return redirect('listarServicio')



#Login

def login(request):
    return render(request,'tienda/login/login.html')

def tyc(request):
    return render(request,'tienda/terminos/tyc.html') 

def logueo(request):
    if request.method == "POST":
        user = request.POST.get('correo')
        pss = request.POST.get('clave')
        t = request.POST.get('terminos')
        if user == '' or pss == '':
            messages.error(request,'Error, No se permite campos vacios')
        else:
            try:
                u = Usuarios.objects.get(email=user)
                if verify_password(pss,u.password):
                    request.session["logueo"]={
                        "id":u.id,
                        "nombre":u.nombre,
                        "correo":u.email,
                        "rol":u.rol
                    }
                    request.session["carrito"] = []
                    request.session["items"] = 0
                    messages.success(request, f"Bienvenido {u.nombre}!!")
                    return redirect("index")
                else:
                    messages.error(request, "Error: Contrasena incorrecta")
                    return redirect("login")
            except Exception as e:
                messages.error(request, "Error: Datos incorrecto")
                return redirect("login")
    else:
        messages.warning(request,"Error: No se enviaron los datos")
        return redirect('login')

def logout(request):
    try:
        del request.session['logueo']
        messages.success(request,'Cerrado correctamente!!!')
        return redirect('login')
    except Exception as e:
        messages.warning(request,'Error!')
        return redirect('index')

@login_requerido
def profile(request):
    p = request.session.get("logueo",False)
    u = Usuarios.objects.get(pk=p["id"])
    if u.rol != 1:
        c = u
        contexto = {"data":u,"data1":c}
    else:
        contexto = {"data":u}
    return render(request,'tienda/login/profile.html',contexto)


def completeInformation(request):
    p = request.session.get("logueo",False)    
    if request.method == "POST":

        try:
            n = request.POST.get("info")
            cedula = request.POST.get("cedula")
            telefono = request.POST.get("telefono")
            direccion = request.POST.get("direccion")
            if cedula == '' or telefono == '' or direccion == '':
                 messages.error(request,'No se permite campos vacios')
            elif int(cedula) < 0 or int(telefono) < 0:
                 messages.error(request,'No pueden ser numeros negativos')
            else:
                if Usuarios.objects.get(pk=p['id']).rol == 4:
                    cliente = Usuarios.objects.get(pk=p["id"])
                    cliente.cedula = cedula
                    cliente.telefono = telefono
                    cliente.direccion = direccion
                    cliente.n = n
                    cliente.save()
                else:
                    cargo = request.POST.get('cargo')
                    empleado = Usuarios.objects.get(pk=p["id"])
                    empleado.cargo = cargo
                    empleado.cedula = cedula
                    empleado.telefono = telefono
                    empleado.direccion = direccion
                    empleado.n = n
                    empleado.save()
                 
            messages.success(request,"La informacion se cuardo correctamente")
            return redirect("perfil")
        except Exception as e:
             messages.error(request, f"Error: {e}")
             return redirect('perfil')
            

def register(request):
    return render(request,"tienda/registro/registro.html")

def registerUser(request):
        if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            clave = request.POST.get('pswd')
            t = request.POST.get('terminos')
            if name.isnumeric():
                messages.error(request,f'No se permite numeros en el nombre!') 
            elif name == "" or clave == "":
                messages.error(request,f'Campos Vacios!')
            elif not re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                messages.error(request,f'El correo no es valido')
            elif len(clave) <= 6:
                messages.error(request,f'La clave es demasiado corta')
            elif t == 'on':

                try:
                    user = Usuarios(
                        nombre = name,
                        email = email,
                        password = hash_password(clave)
                    )

                    user.save()       
                    messages.success(request,'Usuario creado exitosamente')
                    return redirect('login')
                except Exception  as e :
                    messages.error(request,f'Campos vacios o Usuario ya existe !!')
                    return redirect('register')
                else:
                    messages.warning(request,f'Usuario ya existe !!') 
            else:
                messages.warning(request,'Debes aceptar los terminos y condiciones') 
    
        return redirect('register')
   

@login_requerido
def add_car(request):
     l = request.session.get("logueo",False)
     u = Usuarios.objects.get(pk=l["id"])
     cliente = Usuarios.objects.get(email = u.email)
     q = Vehiculos.objects.filter(cliente=cliente)
     contexto = {
        "data": q
     }
     return render(request,'tienda/login/vehiculos.html',contexto)


def add_car_profile(request):
    l = request.session.get('logueo',False)
    cliente = Usuarios.objects.get(pk=l["id"])
    if request.method == 'POST':
        vehiculo = request.POST.get("vehiculo")
        modelo = request.POST.get("modelo")
        placa = request.POST.get("placa")
        kilometraje = request.POST.get("km")
        linea = request.POST.get("linea")

        if vehiculo == '' or modelo == '' or placa == '' or kilometraje == '' or linea == '':
            messages.success(request,'No se permite campos vacios')
        elif len(modelo) > 4:
            messages.success(request,'No puede tener mas de 4 digitos')
        elif int(kilometraje) < 0 or int(modelo) < 0:
            messages.success(request,'No pueden ser numeros negativos')
        else:
            try:
                vehiculos = Vehiculos(
                    cliente = cliente, 
                    vehiculo = vehiculo,
                    modelo = modelo,
                    placa = placa,
                    kilometraje = kilometraje,
                    linea = linea

                )

                vehiculos.save()

                messages.success(request,'Vehiculo agregado correctamente')
                return redirect('add_car')
            except Exception as e:
                messages.error(request, f"Error: {e}")

        return redirect('add_car')
                
    else:
        messages.warning(request,'Error')
    
    return redirect('perfil')


def edite_car_profile(request):
    l = request.session.get('logueo',False)
    cliente = Usuarios.objects.get(pk=l["id"])
    if request.method == 'POST':
        id = request.POST.get('id')
        vehiculo = request.POST.get("vehiculo")
        modelo = request.POST.get("modelo")
        placa = request.POST.get("placa")
        kilometraje = request.POST.get("km")
        linea = request.POST.get("linea")

        if vehiculo == '' or modelo == '' or placa == '' or kilometraje == '' or linea == '':
            messages.success(request,'No se permite campos vacios')
        elif len(modelo) > 4:
            messages.success(request,'No puede tener mas de 4 digitos')
        elif int(kilometraje) < 0 or int(modelo) < 0:
            messages.success(request,'No pueden ser numeros negativos')
        else:
            try:
                q = Vehiculos.objects.get(pk=id)
                q.vehiculo = vehiculo
                q.modelo = modelo
                q.placa = placa
                q.kilometraje = kilometraje
                q.linea = linea

                

                q.save()

                messages.success(request,'Vehiculo editado correctamente')
                return redirect('add_car')
            except Exception as e:
                messages.error(request, f"Error: {e}")

        return redirect('add_car')
                
    else:
        messages.warning(request,'Error')
    
    return redirect('perfil')


def deleteCar(request, id):
	try:
		q = Vehiculos.objects.get(pk=id)
		q.delete()
		messages.success(request, "Eliminado, Exitosamiente!")
	except Exception as e:
		messages.error(request, f"Error: {e}")
        
	return redirect("add_car")
    
@login_requerido
def change_password(request):
    return render(request,'tienda/login/restablecer.html')


def change(request):
    
    if request.method == "POST":
        logueo = request.session.get("logueo",False)
        q = Usuarios.objects.get(pk=logueo["id"])
        a = request.POST.get("anteriorP")
        n1 = request.POST.get("nuevaP")
        n2 = request.POST.get("repetirP")

        if a == '' or n1 == '' or n2 == '':
            messages.success(request,"No se puede enviar campos vacios")
        else:
            if verify_password(a,q.password):
                if n1 == n2:
                    q.password = hash_password(n1)
                    q.save()
                    
                    messages.success(request,"Cambio de contraseña exitoso!!!")
            else:
                messages.warning(request,"La clave no son iguales")

    return redirect("index")


@login_requerido
def editeFormProfile(request):
    q = request.session.get("logueo",False)
    p = Usuarios.objects.get(pk=q["id"])

    contexto = {"data":p}

    return render(request,"tienda/login/editeProfile.html",contexto)


def updateInfoProfile(request):
    
    if request.method == 'POST':
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        email = request.POST.get("email")

        if direccion == "" or telefono == "" or email == "":
            messages.success(request,"No se permite campos vacios")
        elif len(telefono) > 10:
            messages.success(request,"El telefono no puede tener mas de 10 digitos")
        elif not re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            messages.error(request,f'El correo no es valido')
        else:
            try:
                q = request.session.get("logueo",False)
                c = Usuarios.objects.get(pk=q["id"])
        
                c.email = email
                c.direccion = direccion
                c.telefono = telefono
                c.save()
                messages.success(request,"Informacion actualizada correctamente!!")
            except Exception as e:
                messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,f'Error:No se enviaron los datos!!')
    return redirect('index')
    


def updatePictureProfile(request):
    if request.method == 'POST':
        foto = request.FILES.get('foto_new')
        q = request.session.get("logueo",False)
        c = Usuarios.objects.get(pk=q["id"])
        if not foto:
            c.foto = 'tienda/media/user.png'
            c.save()
            messages.success(request,"Foto actualizada correctamente!!")
        else:   
            try:
                c.foto = foto
                c.save()
                messages.success(request,"Foto actualizada correctamente!!")
            except Exception as e:
                messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,f'Error:No se enviaron los datos!!')
    return redirect('index')

        

def formPassword(request):
    return render(request,"tienda/login/restablecerPassword.html")

def emailToPassword(request):
    if request.method == "POST":
        correo = request.POST.get("correo")
        if correo == '':
            messages.error(request, "Debes enviar el correo")
        elif not re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', correo):
            messages.error(request,f'El correo no es valido')
        else:
            try:
                q = Usuarios.objects.get(email=correo)     
                from random import randint
                import base64
                token = base64.b64encode(str(randint(100000, 999999)).encode("ascii")).decode("ascii")
                print(token)
                q.token_recuperar = token
                q.save()

                destinatario = correo
                mensaje = f"""
                        <h1 style='color:blue;'>RepWheels</h1>
                        <p>Usted ha solicitado recuperar su contraseña, haga clic en el link y digite el token.</p>
                        <p>Token: <strong>{token}</strong></p>
                        """
                try:
                    msg = EmailMessage("RepWheels", mensaje, settings.EMAIL_HOST_USER, [destinatario])
                    msg.content_subtype = "html"  # Habilitar contenido html
                    msg.send()
                    messages.success(request,"Correo enviado!!")
                except BadHeaderError:
                    messages.error(request, "Encabezado no válido")
                except Exception as e:
                    messages.error(request, f"Error: {e}")

            except Usuarios.DoesNotExist:
                messages.error(request, "No existe el usuario....")
            
            context = {
                'correo':correo
            }
            return render(request, "tienda/login/restablecimiento.html",context)
    else:
        return render(request, "tienda/login/restablecerPassword.html")



def restablecimiento(request):
	if request.method == "POST":
		if request.POST.get("check"):
			correo = request.POST.get("correo")
			q = Usuarios.objects.get(email=correo)
			c1 = request.POST.get("nueva1")
			c2 = request.POST.get("nueva2")
            

			if c1 == c2:
				q.password = hash_password(c1)
				q.token_recuperar = ""
				q.save()
				messages.success(request, "Contraseña guardada correctamente!!")
				return redirect("index")
			else:
				messages.info(request, "Las contraseñas nuevas no coinciden...")
				return redirect("restablecimiento")+"/?correo="+correo
		else:
			correo = request.POST.get("correo")
			token = request.POST.get("token")
			q = Usuarios.objects.get(email=correo)
			if (q.token_recuperar == token) and q.token_recuperar != "":
				contexto = {"check": "ok", "correo":correo}
				return render(request, "tienda/login/restablecimiento.html", contexto)
			else:
				messages.error(request, "Token incorrecto")
				return redirect("restablecimiento")
	else:
		correo = request.GET.get("correo")
		contexto = {"correo":correo}
		return render(request, "tienda/login/restablecimiento.html", contexto)


# Cart - Shopping 


def add_cart(request):
    if request.method == "POST":
        try:
            id_producto = request.POST.get("id")
            cantidad = request.POST.get("cantidad")
            carrito = request.session.get("carrito",False)
            if not carrito:
                request.session["carrito"] = []
                request.session["items"] = 0
                carrito = []

            
            
            q = Productos.objects.get(pk=id_producto)

      
            for p in range(0,len(carrito)):  
                print(carrito[p]['id'])
                if carrito[p]["id"] == int(q.id):
                    
                    if int(q.cantidad) >= (carrito[p]["cantidad"]+int(cantidad)) and int(cantidad)> 0:
                        carrito[p]["cantidad"]+= int(cantidad)
                        
                        carrito[p]["subtotal"] = carrito[p]["cantidad"]*q.Precio
                        
                    else:
                        messages.warning(request,"Cantidad no dispoinble!!")
                    break

            else:
                if q.cantidad >= int(cantidad) and int(cantidad) > 0:
                    carrito.append(
                        {
                            "id":q.id,
                            "foto":q.foto.url,
                            "producto":q.nombre,
                            "precio":q.Precio,
                            "cantidad": int(cantidad),
                            "subtotal": int(cantidad) * q.Precio
                        }
                    )
                else:
                    messages.warning(request, "No se puede agregar, no hay suficiente inventario.")

            request.session["carrito"] = carrito
            
            contexto = {
				"items": len(carrito),
				"total": sum(p["subtotal"] for p in carrito)
			}
            request.session["items"] = len(carrito)

            

            return render(request, "tienda/carrito/carrito.html", contexto)

        except ValueError as e:
                messages.error(request,f"Error: {e}")
        except Exception as e:
            messages.error(request, f"Ocurrió un Error: {e}")
    else:
        messages.warning(request,"No se enviaron datos...")
        
def showCart(request):
    carrito = request.session.get("carrito",False)
    if not carrito :
        request.session["carrito"] = []
        request.session["items"] = 0
        contexto = {

            "items":0,
            "total":0
        }
    else:
        contexto = {
            "items": len(carrito),
            "total": sum(p["subtotal"] for p in carrito)
        }

        request.session["items"] = len(carrito)
    
    return render(request,"tienda/carrito/carrito.html", contexto)

def removeOne(request,id):
    
    carrito = request.session.get("carrito", False)

    if carrito != False:
         
        for  i,item in enumerate(carrito):
            print(i)
            if item["id"] == id:
                carrito.pop(i)
                break
            else:
                messages.warning(request,"No se encontro el producto en el carrito de compras!!")
    
    request.session["items"] = len(carrito)
    request.session["carrito"] = carrito
    return redirect("showCart")

def removeEvething(request):
    try:
        del request.session['carrito']
        messages.success(request,'Carrito vaciado correctamente!!!')
        return redirect('productos')
    except Exception as e:
        messages.warning(request,'Error!')
        return redirect('inicio')
    
def updateAmountCar(request,id):
     carrito = request.session.get("carrito",False)
     cantidad = request.GET.get("cantidad")
     if carrito != False:
          for i, n in enumerate(carrito):
               if n["id"] == id:
                    n["cantidad"] = int(cantidad)
                    n["subtotal"] = int(cantidad) * n["precio"]

                    break
          else:
               messages.warning(request, "No se encontró el producto en el carrito.")

     request.session["carrito"] = carrito
     return redirect("showCart")

               

@transaction.atomic
def payment(request):
    q = request.session.get("logueo",False)
    if q:
        carrito = request.session.get("carrito",False)
        total = sum(p["subtotal"] for p in carrito)
        try:
            u = Usuarios.objects.get(pk=q["id"])
            venta = Facturas(
                cliente = u,
                total = total
            )
            venta.save()

            for i, enum in enumerate(carrito):
                try:
                    p = Productos.objects.get(pk=enum["id"])
                except p.DoesNotExist:
                    carrito.pop(i)
                    request.session["carrito"] = carrito    
                    request.session["items"] = len(carrito)
                
                    raise Exception('El producto no existe...!!')
                if int(enum["cantidad"]) > p.cantidad:
                    raise Exception(f"La cantidad del producto '{enum['producto']}' supera el inventario")

                        

                df = DetalleFactura(
                    
                    factura = venta,
                    producto = p,
                    cantidad = int(enum["cantidad"]),
                    precio = int(int(enum["precio"])*int(enum["cantidad"])),

                )
                    
                cantidad_new = p.cantidad - enum["cantidad"]
                p.cantidad = cantidad_new

                p.save()
                df.save()

            
                request.session["carrito"] = []
                request.session["items"] = 0

            messages.success(request,"La venta se creo correctamente !!")
        except  Exception as e:
            transaction.set_rollback(True)
            messages.error(request, f"Error: {e}")
    else:
         messages.warning(request,"Para realizar la compra debes iniciar sesion!!")
         


    return redirect("productos")

@login_requerido
def compras(request):
    q = request.session.get("logueo",False)
    u = Usuarios.objects.get(pk=q["id"])
    if u.rol != 4:
        v = Facturas.objects.all()
    else:
        v = Facturas.objects.filter(cliente=u)
    context = {"data":v}
    return render(request,"tienda/ventas/ventas.html", context)
    

def details_buy(request,id):
    vent = Facturas.objects.get(pk=id)
    det = DetalleFactura.objects.filter(factura=id)
    context = {"data":det,"data1":vent}
    return render(request,"tienda/ventas/detalleVentas.html", context)


# PDF convert

from django.template.loader import get_template
from xhtml2pdf import pisa

def pdfCalificaciones(request):
    r = Calificaciones.objects.all()
    template_path = 'tienda/reportes/reporteCalificacion.html'
    context = {'data': r }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reportCalificacion.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
    

def pdfCitas(request):
    logueo = request.session.get("logueo",False)
    usuario = Usuarios.objects.get(pk=logueo["id"])
    c = Citas.objects.filter()
    template_path = 'tienda/reportes/reporteCita.html'
    context = {'data': c }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reportCita.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def pdfCompras(request):
    q = request.session.get("logueo",False)
    #Compra
    u = Usuarios.objects.get(pk=q["id"])
    v = Facturas.objects.filter()
    #Detalle de la compra
    template_path = 'tienda/reportes/reporteVenta.html'
    context = {'data': v}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporteCompras.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def pdfFactura(request,id):
    q = request.session.get("logueo",False)
    vent = Facturas.objects.get(pk=id)
    det = DetalleFactura.objects.filter(factura=id)
    context = {"data":det,"data1":vent}
    #Detalle de la compra
    template_path = 'tienda/reportes/facturaCompra.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporteCompras.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


import folium


def map(request):
    initialMap = folium.Map(location=[6.1817678,-75.6071863],zoom_start=11)
    context = {"map":initialMap}
    return render(request, "tienda/maps/maps.html",context)

@login_requerido
def listarEmergencias(request):
    e = Emergencia.objects.all()
    empleados = Usuarios.objects.filter(rol=3)
    context = {'user_locations':e,"empleados":empleados}
    return render(request,"tienda/maps/admin_view.html",context)

@login_requerido_emplo
def listarEmergenciasEmpleado(request):
    l = request.session.get('logueo',False)
    u = Usuarios.objects.get(pk=l["id"])
    q = Emergencia.objects.filter(empleado=u).exclude(estado=3)
    
    context = {"emergencias":q}
    return render(request, "tienda/maps/emergencia_empleado.html",context)
    

def emergencia(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        descripcion = request.POST.get('descripcion_problema')
        ubicacion = request.POST.get('address')

        if nombre == "" or telefono == "" or descripcion == "" or ubicacion == "":
            messages.warning(request,'No se puede campos vacios')
        else:
            try:
                e = Emergencia(
                     nombre = nombre,
                     telefono = telefono,
                     descripcion = descripcion,
                     ubicacion = ubicacion

                     
                )

                e.save()
                messages.success(request,'Ya se ha realizado el envio de su emergencia!!')
            except Exception as e:
                 messages.error(request, f"Error: {e}")

    return redirect('index')

def asignarEmpleado(request):
    if request.method == "POST":
        id = request.POST.get('id')
        empleado = Usuarios.objects.get(pk=request.POST.get('empleado'))

        if empleado == "":
            messages.error(request,'No se permite enviar sin un encargado !!')
        else:
            try:

                q = Emergencia.objects.get(pk=id)
                q.empleado = empleado
                q.save()
                messages.success(request,'Encargado enviado !!')
            except Exception as e:
                 messages.error(request, f"Error: {e}")


    return redirect('listarEmergencias')


def estadoEmergenciaEnProceso(request,id):
    try:
        q = Emergencia.objects.get(pk=id)
        q.estado = 2
        q.save()
        messages.success(request, "Estado cambiado, Exitosaamiente!")
    except Exception as e:
        messages.error(request, f"Error: {e}")
            
    return redirect("listarEmergenciasEmpleado")

def estadoEmergenciaTerminado(request,id):
    try:
        q = Emergencia.objects.get(pk=id)
        q.estado = 3
        q.save()
        messages.success(request, "La emergencia finalizo xitosaamiente!")
    except Exception as e:
        messages.error(request, f"Error: {e}")
            
    return redirect("listarEmergenciasEmpleado")



from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CustomAuthToken(ObtainAuthToken):
	def post(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data,
										   context={'request': request})
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['username']
		# traer datos del usuario para bienvenida y ROL
		usuario = Usuarios.objects.get(email=user)
		token, created = Token.objects.get_or_create(user=usuario)

		return Response({
			'token': token.key,
			'user': {
				'user_id': usuario.pk,
				'email': usuario.email,
				'nombre': usuario.nombre,
				'rol': usuario.rol,
				'foto': usuario.foto.url
			}
		})

     
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated



class UsuarioViewSet(viewsets.ModelViewSet):
	authentication_classes = [TokenAuthentication, SessionAuthentication]
	authentication_classes = [TokenAuthentication]
	permission_classes = [IsAuthenticated]
	queryset = Usuarios.objects.all()
	serializer_class = UsuariosSerializers

