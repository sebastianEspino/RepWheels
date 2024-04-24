from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'Proveedores', views.ProveedoresViewSet)
router.register(r'Empleado', views.EmpleadoViewSet)
router.register(r'Servicios', views.ServiciosViewSet)
router.register(r'Calificaciones', views.CalificacionesViewSet)
router.register(r'Clientes', views.ClientesViewSet)
router.register(r'Citas', views.CitasViewSet)
router.register(r'Productos',views.ProductosViewSet)
router.register(r'Usuarios',views.UsuariosViewSet)
router.register(r'Facturas',views.FacturasViewSet)
router.register(r'DetalleFactura',views.DetalleFacturaViewSet)
router.register(r'DetalleServicio',views.DetalleServicioViewSet)


urlpatterns = [
    path('',views.index, name = "index", ),
    path('api/1.0/', include(router.urls)),
    #crud de productos
    path('productos',views.productos,name='productos'),
    path('listarProductos',views.listarProductos, name= "listarProductos"),
    path("editarProductos/<int:id>", views.editarProductos, name="editarProductos"),
    path("actualizarProductos/", views.actualizarProductos, name="actualizarProductos"),
    path("eliminarProductos/<int:id>", views.eliminarProductos, name="eliminarProductos"),
    path("crearProductoform/", views.crearProductoform, name="crearProductoform"),
	path("crearProducto/", views.crearProducto, name="crearProducto"),
    
    #Crud empleados
    path("empleados/", views.empleados, name="empleado"),
    path("nuevoempleados/", views.nuevoempleado, name="nuevoempleados"),
    path("newempleados/", views.newempleado, name="newempleados"),
    path("empleados_formulario_editar/<int:id>", views.empleados_formulario_editar, name="empleados_formulario_editar"),
    path("empleado_actualizar/", views.empleado_actualizar, name="empleado_actualizar"),
    path("empleado_eliminar/<int:id>", views.empleado_eliminar, name="empleado_eliminar"),
    
    #Crud de clientes
    path('registrarCliente/',views.registrarCliente, name="registrarCliente"),
    path('listarCliente/',views.listarCliente, name="listarCliente"),
    path('clientesCrear/',views.clientesCrear, name="clientesCrear"),
    path('clientesEditar/<int:id>',views.clientesEditar, name="clientesEditar"),
    path('clientesEliminar/<int:id>',views.clientesEliminar, name="clientesEliminar"),
    path('clientesActualizar/',views.clientesActualizar, name="clientesActualizar"),
    
    #crud de proveedores
    path("registrarProveedores", views.proveedores_registrar, name="registrarProveedores"),
    path("listarProveedores/", views.listar_proveedores, name="listarProveedores"),
    path("addProveedores/", views.proveedores_add, name="proveedores_form"),
    path("proveedos_editar/<int:id>", views.registrar_proveedores_editar, name="proveedores_form_act"),
    path("proveedores_actualizar/", views.proveedores_actualizar, name="proveedores_actualizar"),
    path("deleteProveedores/<int:id>", views.proveedores_delete, name="deleteProveedores"),
    
    #CRUD citas
    path('citas',views.citas,name='citas'),
    path("registrarCita", views.registrarCita, name="registrarCitar"),
    path("listarCita", views.listarCita, name="listarCita"),
    path("citaRegistrar", views.citaRegistrar, name="citaRegistrar"),
    path("citaEliminar/<int:id>", views.citaEliminar, name="citaEliminar"),
    path("cita_formulario_editar/<int:id>", views.cita_formulario_editar, name="cita_formulario_editar"),
    path("citaActualizar", views.citaActualizar, name="citaActualizar"),
    
    #CRUD calificaciones
    path('calificaciones',views.calificaciones,name='calificaciones'),
    path("calificacionRegistrar", views.calificacionRegistrar, name="calificacionRegistrar"),
    path("calificacion_eliminar/<int:id>", views.calificacion_eliminar, name="calificacion_eliminar"),
    path("calificacion_formulario_editar/<int:id>", views.calificacion_formulario_editar, name="calificacion_formulario_editar"),
    path("calificacionListar", views.listarCalificacion, name="calificacionListar"),
    path("calificacionActualizar", views.calificacionActualizar, name="calificacionActualizar"),
    path("registrarCalificacion", views.registrarCalificacion, name="registrarCalificacion"),

    #crud de cotizaciones
    path('cotizaciones',views.cotizaciones,name='cotizaciones'),
    path('registrarCotizacion',views.registrarCotizacion,name='registrarCotizacion'),
    path('listarCotizacion/',views.listarCotizacion,name='listarCotizacion'),
    path('cotizacionRegistrar/',views.cotizacionRegistrar,name='cotizacionRegistrar'),
    path('cotizacionActualizar/',views.cotizacionActualizar,name='cotizacionActualizar'),
    path('cotizacionEliminar/<int:id>',views.cotizacionEliminar,name='cotizacionEliminar'),
    path('cotizacionEditar/<int:id>',views.cotizacionEditar,name='cotizacionEditar'),
    
    #crud Servicios
    path('servicios',views.servicio,name='servicios'),
    path("registrarServicio",views.registrarServicio,name='registrarServicio'),
    path("listarServicio",views.listarServicio,name='listarServicio'),
    path("registroServicio",views.registroServicio,name="registroServicio"),
    path("servicioEliminar/<int:id>",views.servicioEliminar,name="servicioEliminar"),
    path("servicioEditar/<int:id>",views.servicio_form_editar,name="servicioEditar"),
    path("servicioActualizar",views.servicioActualizar,name="servicioActualizar"),

    #Login and Register
    path("login",views.login,name="login"),
    path("logueo",views.logueo,name="logueo"),
    path('logout',views.logout,name='logout'),
    path('perfil',views.profile,name="perfil"),
    path('register',views.register,name="register"),
    path('registerUser',views.registerUser,name="registerUser"),
    path('change_password',views.change_password,name='change_password'),
    path('change',views.change,name="change"),
    path('formEditeProfile',views.editeFormProfile,name="formEditeProfile"),
    path('changeProfile',views.updateInfoProfile,name="changeProfile"),
    
    #Cart - Shopping

    path("addCart",views.add_cart,name="addCart"),
    path("showCart",views.showCart,name="showCart"),



    
 
    
    
    
    
]
