from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*
from rest_framework import viewsets
from . serializers import *
from django.contrib import messages



# API with rest framework 

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializers

class ProveedoresViewSet(viewsets.ModelViewSet):
    queryset = Proveedores.objects.all()
    serializer_class = ProveedoresSerializers

class ServiciosViewSet(viewsets.ModelViewSet):
    queryset = Servicios.objects.all()
    serializer_class = ServiciosSerializers

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializers

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializers

class ClientesViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClientesSerializers

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


def index(request):
    logueo = request.session.get("logueo", False)
    q = Calificaciones.objects.all()
    contexto = {"data":q}
    return render(request, "tienda/index.html")


# crud de  productos.

def productos(request):
    p = Productos.objects.all()
    contexto = {'data':p}
    return render(request,"tienda/productos/producto.html",contexto)


def listarProductos(request):
    q = Productos.objects.all()
    contexto = {"data":q}
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
		fecha_Creacion = request.POST.get("fecha_Creacion")
		categoria = Categoria.objects.get(pk=request.POST.get("categoria"))
		try:
			q = Productos.objects.get(pk=id)
			q.nombre = nombre
			q.Precio = Precio
			q.descripcion_producto = descripcion_producto
			q.cantidad = cantidad
			q.fecha_Creacion = fecha_Creacion
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
		messages.success(request, "Eliminado, Exitosamiente!")
	except Exception as e:
		messages.error(request, f"Error: {e}")
        
	return redirect("listarProductos")

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
		fecha_Creacion = request.POST.get("fecha_Creacion")
		categoria = Categoria.objects.get(pk=request.POST.get("categoria"))
		try:
			q = Productos(
                nombre = nombre,
                Precio = precio,
                descripcion_producto = descripcion_producto,
                cantidad = cantidad,
                fecha_Creacion = fecha_Creacion,
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

def registrarCliente(request):
    return render(request, "tienda/clientes/registrarCliente.html")

def listarCliente(request):
    q = Clientes.objects.all()
    contexto = {"data" : q}
    return render(request, "tienda/clientes/listarCliente.html",contexto)

def clientesCrear(request):
    if request.method == 'POST':
        cedula=request.POST.get('cedula')        
        nombre=request.POST.get('nombre_completo')
        correo=request.POST.get('correo')
        telefono=request.POST.get('telefono')

        try:
            q = Clientes(
                cedula=cedula,
                nombre_completo=nombre,
                correo=correo,
                telefono=telefono
            )
            q.save()
            messages.success(request,"Guardado Correctamente!")
        except Exception as e:
            messages.error(request,f"Error:{e}")
        return redirect('listarCliente')

    else:
        messages.error(request,"Error: no se enviaron datos")
        return redirect("listarCliente")

def clientesEliminar(request,id):
    try:
        q = Clientes.objects.get(pk = id)
        q.delete()
        messages.success(request,"Cliente eliminado Correctamente!")
    except Exception as e:
        messages.error(request,f"Error:{e}")
    return redirect('listarCliente')

def clientesEditar(request,id):
    q = Clientes.objects.get(pk = id)
    contexto = {"data" : q}
    return render(request,"tienda/clientes/editarCliente.html",contexto)

def clientesActualizar(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        cedula=request.POST.get('cedula')        
        nombre_completo=request.POST.get('nombre_completo')
        correo=request.POST.get('correo')
        telefono=request.POST.get('telefono')
        try:
            q=Clientes.objects.get(pk=id)
            q.cedula = cedula
            q.nombre_completo = nombre_completo
            q.correo = correo
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
def empleados(request):
	q = Empleado.objects.all()
	contexto = {"data": q}
	return render(request, "tienda/empleados/listarempleados.html", contexto)

def nuevoempleado(request):
	return render(request, "tienda/empleados/crearempleado.html")

def newempleado(request):
    if request.method == 'POST':
        cedula = request.POST.get('cedula')
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        fechac = request.POST.get('fecha')
        cargo = request.POST.get('cargo')
        try:
            q = Empleado(
                nombre_completo = nombre,
                cedula = cedula,
                correo = correo,
                telefono = telefono,
                fecha_contratacion = fechac,
                cargo = cargo
            )
            q.save()
            messages.success(request, 'guardado correctamente')
        except Exception as e:
            messages.error(request, f"Error: {e}")
    return redirect('empleado')

def empleados_formulario_editar(request, id):
	q = Empleado.objects.get(pk=id)
	c = Empleado.objects.all()
	contexto = {"data": q, "empleado": c}
	return render(request, "tienda/empleados/editarempleados.html", contexto)


def empleado_actualizar(request):
	if request.method == "POST":
		id = request.POST.get("id")
		nombre = request.POST.get("nombre")
		cedula = request.POST.get("cedula")
		correo = request.POST.get("correo")
		telefono = request.POST.get("telefono")
		cargo = request.POST.get("cargo")
		try:
			q = Empleado.objects.get(pk=id)
			q.nombre_completo = nombre
			q.cedula = cedula
			q.correo = correo
			q.telefono = telefono
			q.cargo = cargo
			q.save()
			messages.success(request, "Producto actualizado correctamente!!")
		except Exception as e:
			messages.error(request, f"Error: {e}")
	else:
		messages.warning(request, "Error: No se enviaron datos...")

	return redirect("empleado")

def empleado_eliminar(request, id):
	try:
		q = Empleado.objects.get(pk=id)
		q.delete()
		messages.success(request, "Empleado eliminada correctamente!!")
	except Exception as e:
		messages.error(request, f"Error: {e}")

	return redirect("empleado")

#crud proveedores
def proveedores_registrar(request):
	return render(request, "tienda/proveedores/registrarProveedor.html")

def listar_proveedores(request):
	# SELECT * FROM categoria
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
    q = Citas.objects.all()
    e = Empleado.objects.all()
    c = Cotizaciones.objects.all()
    contexto = {"data": e ,"data1":c,"data2":q}
    return render(request, "tienda/citas/cita.html",contexto)

def registrarCita(request):
    e = Empleado.objects.all()
    c = Cotizaciones.objects.all()
    contexto = {"data": e ,"data1":c}
    return render(request, "tienda/citas/registrarCita.html",contexto)

def listarCita(request):
    q = Citas.objects.all()
    contexto = {"data": q}
    return render(request, "tienda/citas/listarCita.html", contexto)

def citaRegistrar(request):
   
    if request.method == "POST":
        opcion = request.POST.get("type_f")
        logueo = request.session.get("logueo",False)
        usuario = Usuarios.objects.get(pk=logueo["id"])
        fecha_servicio = request.POST.get('fechaServicio')
        tipo_servicio = request.POST.get('tipoServicio')
        hora = request.POST.get('hora')
        cliente = usuario
        cotizacion = Cotizaciones.objects.get(pk=request.POST.get("Cotizacion"))
        empleado = Empleado.objects.get(pk=request.POST.get("empleado"))

        cita = Citas(
            fechaServicio=fecha_servicio,
            hora = hora,
            cliente = cliente,
            cotizacion = cotizacion,
            empleado = empleado
            
        )
        cita.save()

        messages.success(request, "Cita guardada correctamente!!")
       
        return redirect("listarCita")

def cita_formulario_editar(request, id):
    q = Citas.objects.get(pk=id)
    e = Empleado.objects.all()
    c = Cotizaciones.objects.all()
    contexto = {"data": q,"data1":e,"data2":c}
    return render(request, "tienda/citas/editarCita.html", contexto)

def citaActualizar(request):
    if request.method == "POST":
        logueo = request.session.get("logueo",False)
        usuario = Usuarios.objects.get(pk=logueo["id"])
        id = request.POST.get("id")
        fecha_servicio = request.POST.get("fechaServicio")
        cliente = usuario
        hora = request.POST.get('hora')
        cotizacion = Cotizaciones.objects.get(pk=request.POST.get("Cotizacion"))
        empleado = Empleado.objects.get(pk=request.POST.get("empleado"))
        try:
            q = Citas.objects.get(pk=id)
            q.fechaServicio = fecha_servicio
            q.cliente = usuario
            q.hora = hora
            q.empleado = empleado
            q.cotizacion = cotizacion
            
            q.save()

            messages.success(request, "Cita actualizada correctamente!!")
        except Citas.DoesNotExist:
            messages.error(request, "Cita no encontrada.")
        except Exception as e:
            messages.error(request, f'Error: {e}')
    else:
        messages.warning(request, 'Error: No se enviaron los datos!!')

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




#CRUD cotizaciones

def cotizaciones(request):
    e = Empleado.objects.all()
    s = Servicios.objects.all()
    contexto = {"empleados":e, "servicios":s}
    return render(request, "tienda/cotizaciones/cotizacion.html",contexto)


def registrarCotizacion(request):
    e = Empleado.objects.all()
    s = Servicios.objects.all()
    contexto = {"empleados":e, "servicios":s}
    return render(request,'tienda/cotizaciones/registrarCotizacion.html',contexto)


def listarCotizacion(request):
    q = Cotizaciones.objects.all()
    context = {"data": q}
    return render(request, "tienda/cotizaciones/listarCotizacion.html", context)

def cotizacionRegistrar(request):
     
	if request.method == "POST":
            l = request.session.get("logueo",False)
            u = Usuarios.objects.get(pk=l["id"])
            marca = request.POST.get("vehiculo")
            placa = request.POST.get("placa")
            modelo = request.POST.get("modelo")
            kilometraje = request.POST.get("km")
            linea = request.POST.get("linea")
            empleado = request.POST.get("empleado")
            servicio = request.POST.get("servicio")
            
            
            q = Cotizaciones(
                vehiculo = marca,
                modelo = modelo,
                placa = placa,
                kilometraje = kilometraje,
                linea = linea,
                empleado = empleado,
                servicio = servicio,
                cliente = u             
            )
            q.save()
            messages.success(request, "Guardado correctamente!!")
            
            return redirect("listarCotizacion")
        
def cotizacionEliminar(request,id):
    try:
        q = Cotizaciones.objects.get(pk=id)
        q.delete()
        messages.success(request,"Empleado eliminada correctamente!!!")
    except Exception as e:
        messages.error(request,f'Error:{e}')
    return redirect('listarCotizacion')

def cotizacionEditar(request,id):
    q = Cotizaciones.objects.get(pk=id)
    context = {"data":q}
    return render(request,'tienda/cotizaciones/registrarCotizacionEditar.html',context)

def cotizacionActualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        tipo = request.POST.get('opcion')
        d = request.POST.get('d')
        correo = request.POST.get('correo')
        empleado = request.POST.get('emple')
        try:
            q  = Cotizaciones.objects.get(pk=id)
            q.tipos = tipo
            q.descripcion = d
            q.correo = correo
            q.empleado = empleado
            q.save()
        except Exception as e:
                messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,f'Error:No se enviaron los datos!!')
    return redirect('listarCotizacion')

#CRUD calificaiones 

def calificaciones(request):
    q = Calificaciones.objects.all()
    contexto = {"data":q}
    return render(request, "tienda/calificaciones/calificacion.html",contexto)


def registrarCalificacion(request):
    return render(request, "tienda/calificaciones/registrarCalificacion.html")

def listarCalificacion(request):
    r = Calificaciones.objects.all()
    contexto = {"data": r}
    return render(request, "tienda/calificaciones/listarCalificacion.html", contexto)

def calificacionRegistrar(request):
    if request.method == "POST":
        logueo = request.session.get("logueo",False)
        usuario =  Usuarios.objects.get(pk=logueo["id"])
        nombre = usuario
        servicio = request.POST.get("servicio")
        cantidad_estrellas = request.POST.get("cantidad_estrellas")

        calificacion = Calificaciones(
            cliente=nombre,
            servicio = servicio,
            cantidad_estrellas=cantidad_estrellas,
        )
        calificacion.save()

        messages.success(request, "Calificación guardada correctamente!!")
        return redirect("calificacionListar")

def calificacion_formulario_editar(request, id):
    r = Calificaciones.objects.get(pk=id)
    contexto = {"data": r}
    return render(request, "tienda/calificaciones/editarCalificacion.html", contexto)

def calificacionActualizar(request):
    if request.method == "POST":
        id = request.POST.get("id")
        logueo = request.session.get("logueo",False)
        usuario =  Usuarios.objects.get(pk=logueo["id"])
        nombre = usuario
        servicio = request.POST.get("servicio")
        cantidad_estrellas = request.POST.get("cantidad_estrellas")
        

        try:
            calificacion = Calificaciones.objects.get(pk=id)
            calificacion.cliente = usuario
            calificacion.servicio = servicio
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
    try:
        calificacion = Calificaciones.objects.get(pk=id)
        calificacion.delete()

        messages.success(request, "Calificación eliminada correctamente!!!")
    except Calificaciones.DoesNotExist:
        messages.error(request, "Calificación no encontrada.")
    except Exception as e:
        messages.error(request, f'Error: {e}')

    return redirect('calificacionListar')

#Crud Servicio

def servicio(request):
    return render(request, "tienda/servicios/servicio.html")


def registrarServicio(request):
    p = Productos.objects.all()
    contexto = {"data":p}
    return render(request,'tienda/servicios/registrarServicio.html',contexto)


def listarServicio(request):
    q = Servicios.objects.all()
    contexto = {"data":q}
    return render(request,'tienda/servicios/listarServicio.html',contexto)

def registroServicio(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion_servicio = request.POST.get("descripcion_servicio")
        producto = Productos.objects.get(pk=request.POST.get("producto"))
        servicios = Servicios(
            nombre=nombre,
            descripcion_servicio=descripcion_servicio,
            productos = producto
        )
        servicios.save()

        messages.success(request, "Servicio guardada correctamente!!")
        return redirect("listarServicio")

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


def servicio_form_editar(request,id):
    s = Servicios.objects.get(pk=id)
    p = Productos.objects.all()

    context = {"data": s,"data1": p}
    return render(request,'tienda/servicios/editarServicio.html',context)

def servicioActualizar(request):
    if request.method == "POST":
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        descripcion_servicio = request.POST.get('descripcion_servicio')
        productos = Productos.objects.get(pk=request.POST.get("producto"))

        try:
            servicio = Servicios.objects.get(pk=id)
            servicio.nombre = nombre
            servicio.descripcion_servicio = descripcion_servicio
            servicio.productos = productos
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

def logueo(request):
    if request.method == "POST":
        email = request.POST.get('correo')
        pss = request.POST.get('clave')
        try:
            u = Usuarios.objects.get(correo=email,clave=pss)
            request.session["logueo"]={
                "id":u.id,
                "nombre":u.nombre,
                "correo":u.correo,
                "rol":u.rol
            }
            request.session["carrito"] = []
            request.session["items"] = 0
            messages.success(request, f"Bienvenido {u.nombre}!!")
            return redirect("index")
        except Exception as e:
            messages.error(request, "Error: Usuario o contraseña incorrectos...")
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

def profile(request):
    p = request.session.get("logueo",False)
    q = Usuarios.objects.get(pk=p["id"])
    if q.rol == 4:
        c = Clientes.objects.get(correo=q.correo)
        contexto = {"data":q,"data1":c}
    else:
        contexto = {"data":q}
    return render(request,'tienda/login/profile.html',contexto)

def completeInformation(request):
    p = request.session.get("logueo",False)
    q = Usuarios.objects.get(pk=p["id"])
    
    if request.method == "POST":
        n = request.POST.get("info")
        cedula = request.POST.get("cedula")
        telefono = request.POST.get("telefono")
        direccion = request.POST.get("direccion")

        cliente = Clientes.objects.get(correo=q.correo)
        cliente.cedula = cedula
        cliente.telefono = telefono
        cliente.direccion = direccion
        cliente.n = n
        cliente.save()
        

        cliente.save()
        messages.success(request,"La informacion se cuardo correctamente")

    return redirect("perfil")
          

def register(request):
    return render(request,"tienda/registro/registro.html")

def registerUser(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        clave = request.POST.get('pswd')
        user = Usuarios(
            nombre = name,
            correo = email,
            clave = clave
        )

        cliente = Clientes(
            nombre_completo = name,
            correo = email,
            cedula = 0,
            telefono = 0,
            direccion = "desconocida"

             
        )
        cliente.save()

        user.save()

        messages.success(request,'Usuario creado exitosamente')
        return redirect('login')
    

def change_password(request):
    return render(request,'tienda/login/restablecer.html')

def change(request):
    
    if request.method == "POST":
        logueo = request.session.get("logueo",False)
        q = Usuarios.objects.get(pk=logueo["id"])
        a = request.POST.get("anteriorP")
        n1 = request.POST.get("nuevaP")
        n2 = request.POST.get("repetirP")

        if a == q.clave:
             if n1 == n2:
                q.clave = n1
                q.save()
                
                messages.success(request,"Cambio de contraseña exitoso!!!")
        else:
             messages.warning(request,"La clave no son iguales")

    return redirect("index")


def editeFormProfile(request):
    q = request.session.get("logueo",False)
    p = Usuarios.objects.get(pk=q["id"])

    contexto = {"data":p}

    return render(request,"tienda/login/editeProfile.html",contexto)


def updateInfoProfile(request):
    
    if request.method == 'POST':
        id = request.POST.get("id")
        correo = request.POST.get("email")
        foto = request.POST.get("foto")

        try:
            q = request.session.get("logueo",False)
            p = Usuarios.objects.get(pk=q["id"])

            p.correo = correo,
            p.foto = foto.url

            p.save()
            messages.success(request,"Proveedor actualizada correctamente!!")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,f'Error:No se enviaron los datos!!')
    return redirect('index')
        

# Cart - Shopping 


def add_cart(request):
    if request.method == "POST":
        try:
            carrito = request.session.get("carrito",False)
            if not carrito:
                request.session["carrito"] = []
                request.session["items"] = 0
                carrito = []

            id_producto = request.POST.get("id")
            cantidad = request.POST.get("cantidad")

            q = Productos.objects.get(pk=id_producto)

            for p in carrito:
                if p["id"] == id_producto:
                    if q.cantidad >= (p["cantidad"] + int(cantidad) and int(cantidad)> 0):
                        p["cantidad"]+= int(cantidad)
                        p["subtotal"] = p["cantidad"]*q.Precio
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
    

def payment(request):
    q = request.session.get("logueo",False)
    carrito = request.session.get("carrito",False)
    try:
        u = Usuarios.objects.get(pk=q["id"])
        venta = Facturas(
            cliente = u
        )
        venta.save()

        for i, enum in enumerate(carrito):
            try:
                p = Productos.objects.get(pk=enum["id"])
            except Productos.DoesNotExist:
                carrito.pop(i)
                request.session["carrito"] = carrito    
                request.session["items"] = len(carrito)
			
                raise Exception('El producto no existe...!!')
            if int(enum["cantidad"]) > p.cantidad:
                raise Exception(f"La cantidad del producto '{enum['producto']}' supera el inventario")
            

            df = DetalleFactura(
                 
                factura = venta,
                productos = enum["producto"],
                cantidad = enum["cantidad"],
                total = enum["subtotal"]

            )
            cantidad_new = p.cantidad - enum["cantidad"]
            p.cantidad = cantidad_new
            p.save()
            df.save()

            del request.session["carrito"]
            request.session["items"] = 0

        messages.success(request,"La venta se creo correctamente !!")
    except:
        messages.warning(request,"Error al momento de crear la venta !!")

    return redirect("productos")


def update_totales_carrito(request,id):
	try:
		carro = request.session['carrito']
		cantidad = request.GET.get('cantidad')
		for i in carro:
			if i["id"] == id:
				i["cantidad"] = int(cantidad)
				i["subtotal"] = int(cantidad) * i["precio"]
				
		
		request.session['items'] = len(carro)
		return redirect("showCart")
	except Exception as e:
		messages.warning(request,"No se pudo eliminar el producto")
	return redirect("showCart")


def agregar_calificacion_form(request):
    logueo = request.session.get("logueo",False)
    u = Usuarios.objects.get(pk=logueo["id"])
   
    
    if request.method == "POST":
        try:
           
            servicio = request.POST.get("servicio")
            estrellas = int(request.POST.get("estrellas"))
            q = Calificaciones(
                 cliente=u,
                 servicio = servicio,
                 cantidad_estrellas = estrellas
            )
            print("eee",estrellas)
            q.save()
            messages.success(request,"Realizado.....")
            return redirect('calificaciones')
        except Exception as e:
             messages.error(request, f"Error: {e}")
             return redirect('calificaciones')
     

    
        
            
                  
         
