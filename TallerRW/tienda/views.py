from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*
from django.contrib import messages

def index(request):
    logueo = request.session.get("logueo", False)
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
		#categoria = Categoria.objects.get(pk=request.POST.get("categoria"))
		try:
			q = Productos.objects.get(pk=id)
			q.nombre = nombre
			q.Precio = Precio
			q.descripcion_producto = descripcion_producto
			q.cantidad = cantidad
			q.fecha_Creacion = fecha_Creacion
			#q.categoria = categoria
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
		#categoria = Categoria.objects.get(pk=request.POST.get("categoria"))
		try:
			q = Productos(
                nombre = nombre,
                Precio = precio,
                descripcion_producto = descripcion_producto,
                cantidad = cantidad,
                fecha_Creacion = fecha_Creacion,
                #categoria = categoria
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
    contexto = {"data":q}
    return render(request, "tienda/citas/cita.html",contexto)

def registrarCita(request):
    return render(request, "tienda/citas/registrarCita.html")

def listarCita(request):
    q = Citas.objects.all()
    contexto = {"data": q}
    return render(request, "tienda/citas/listarCita.html", contexto)

def citaRegistrar(request):
    if request.method == "POST":
        fecha_servicio = request.POST.get('fechaServicio')
        tipo_servicio = request.POST.get('tipoServicio')
        hora = request.POST.get('hora')
        empleado = request.POST.get('empleado')

        #id_cliente = request.POST.get("id_cliente")
        #id_empleado = request.POST.get("id_empleado")

        cita = Citas(
            fechaServicio=fecha_servicio,
            tipoServicio=tipo_servicio,
            empleado = empleado,
            hora = hora
            #idCliente_id=id_cliente,
            #idEmpleado_id=id_empleado,
        )
        cita.save()

        messages.success(request, "Cita guardada correctamente!!")
        return redirect("listarCita")

def cita_formulario_editar(request, id):
    q = Citas.objects.get(pk=id)
    contexto = {"data": q}
    return render(request, "tienda/citas/editarCita.html", contexto)

def citaActualizar(request):
    if request.method == "POST":
        id = request.POST.get("id")
        fecha_servicio = request.POST.get("fechaServicio")
        tipo_servicio = request.POST.get("tipoServicio"),
        hora = request.POST.get('hora'),
        empleado = request.POST.get('empleado')
       # id_cliente = request.POST.get("id_cliente")
       # id_empleado = request.POST.get("id_empleado")

        try:
            q = Citas.objects.get(pk=id)
            q.fechaServicio = fecha_servicio
            q.tipoServicio = tipo_servicio
            q.hora = hora
            q.empleado = empleado
            #cita.idCliente_id = id_cliente
            #cita.idEmpleado_id = id_empleado
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
    return render(request, "tienda/cotizaciones/cotizacion.html")


def registrarCotizacion(request):
    return render(request,'tienda/cotizaciones/registrarCotizacion.html')


def listarCotizacion(request):
    q = Cotizaciones.objects.all()
    context = {"data": q}
    return render(request, "tienda/cotizaciones/listarCotizacion.html", context)

def cotizacionRegistrar(request):
	if request.method == "POST":
            tipo = request.POST.get("opcion")
            descripcion = request.POST.get("d")
            correo = request.POST.get("correo")
            emple = request.POST.get("emple")
            q = Cotizaciones(
                tipos=tipo,
                descripcion =  descripcion,
                correo = correo,
                empleado = emple
                
        
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
        nombre = request.POST.get("nombre")
        cantidad_estrellas = request.POST.get("cantidad_estrellas")

        calificacion = Calificaciones(
            nombre=nombre,
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
        nombre = request.POST.get("nombre")
        cantidad_estrellas = request.POST.get("cantidad_estrellas")
        #id_cliente = request.POST.get("id_cliente")

        try:
            calificacion = Calificaciones.objects.get(pk=id)
            calificacion.nombre = nombre
            calificacion.cantidad_estrellas = cantidad_estrellas
            #calificacion.idCliente_id = id_cliente
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
    
    return render(request,'tienda/servicios/registrarServicio.html')

def listarServicio(request):
    q = Servicios.objects.all()
    contexto = {"data":q}
    return render(request,'tienda/servicios/listarServicio.html',contexto)

def registroServicio(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion_servicio = request.POST.get("descripcion_servicio")
        servicios = Servicios(
            nombre=nombre,
            descripcion_servicio=descripcion_servicio
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
    context = {"data": s}
    return render(request,'tienda/servicios/editarServicio.html',context)

def servicioActualizar(request):
    if request.method == "POST":
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        descripcion_servicio = request.POST.get('descripcion_servicio')

        try:
            servicio = Servicios.objects.get(pk=id)
            servicio.nombre = nombre
            servicio.descripcion_servicio = descripcion_servicio
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
    return render(request,'tienda/login/profile.html')

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

        user.save()

        messages.success(request,'Usuario creado exitosamente')
        return redirect('login')
    

def change_password(request):
    return render(request,'tienda/login/restablecer.html')