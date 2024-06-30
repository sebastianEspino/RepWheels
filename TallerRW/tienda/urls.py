from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'Proveedores', views.ProveedoresViewSet)
router.register(r'Servicios', views.ServiciosViewSet)
router.register(r'Calificaciones', views.CalificacionesViewSet)
router.register(r'Citas', views.CitasViewSet)
router.register(r'Productos',views.ProductosViewSet)
router.register(r'Usuarios',views.UsuariosViewSet)
router.register(r'Facturas',views.FacturasViewSet)
router.register(r'DetalleFactura',views.DetalleFacturaViewSet)
router.register(r'DetalleServicio',views.DetalleServicioViewSet)
router.register(r'Categorias',views.CategoriaViewSet)
router.register(r'Vehiculos',views.VehiculosViewSet)


urlpatterns = [
    path('',views.index, name = "index"),
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
    path('citaEmpleado',views.citasEmpleado,name='citaEmpleado'),
    path('cancelar/<int:id>',views.cancell,name='cancelar'),
    path('terminar/<int:id>',views.finish,name='terminar'),
    
    
    #CRUD calificaciones
    path('calificaciones',views.calificaciones,name='calificaciones'),
    path("calificacionRegistrar", views.calificacionRegistrar, name="calificacionRegistrar"),
    path("calificacion_eliminar/<int:id>", views.calificacion_eliminar, name="calificacion_eliminar"),
    path("calificacion_formulario_editar/<int:id>", views.calificacion_formulario_editar, name="calificacion_formulario_editar"),
    path("calificacionListar", views.listarCalificacion, name="calificacionListar"),
    path("calificacionActualizar", views.calificacionActualizar, name="calificacionActualizar"),
    path("registrarCalificacion", views.registrarCalificacion, name="registrarCalificacion"),
    path("agregar_calificacion_form",views.agregar_calificacion_form, name="agregar_calificacion_form"),


    #crud de categoria
    path('cotizaciones',views.cotizaciones,name='cotizaciones'),
    path('registrarCategoria',views.registrarCategoria,name='registrarCategoria'),
    path('listarCategoria/',views.listarCategoria,name='listarCategoria'),
    path('categoriaRegistrar/',views.categoriaRegistrar,name='categoriaRegistrar'),
    path('categoriaActualizar/',views.categoriaActualizar,name='categoriaActualizar'),
    path('categoriaEliminar/<int:id>',views.categoriaEliminar,name='categoriaEliminar'),
    path('categoriaEditar/<int:id>',views.categoriaEditar,name='categoriaEditar'),
    
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
    path('tyc',views.tyc,name='tyc'),
    path('registerUser',views.registerUser,name="registerUser"),
    path('change_password',views.change_password,name='change_password'),
    path('change',views.change,name="change"),
    path('formEditeProfile',views.editeFormProfile,name="formEditeProfile"),
    path('changeProfile',views.updateInfoProfile,name="changeProfile"),
    path('form_update',views.formPassword,name="form_update"),
    path("recuperacionCorreo",views.emailToPassword,name="recuperacionCorreo"),
    path("completarInformacion",views.completeInformation,name="completarInformacion"),
    path("add_car_profile",views.add_car_profile,name="add_car_profile"),
    path("add_car",views.add_car,name="add_car"),
    path("delete_car/<int:id>",views.deleteCar,name="delete_car"),
    path('restablecimiento',views.restablecimiento,name='restablecimiento'),
    path('updatePictureProfile',views.updatePictureProfile,name='updatePictureProfile'),
    
    #Cart - Shopping

    path("addCart",views.add_cart,name="addCart"),
    path("showCart",views.showCart,name="showCart"),
    path("eliminarProductoCarrito/<int:id>",views.removeOne,name="eliminarProductoCarrito"),
    path("vaciarCarrito",views.removeEvething,name="vaciarCarrito"),
    path("actualizarCarrito/<int:id>",views.updateAmountCar,name="actualizarCarrito"),
    
    path("pagar",views.payment,name="pagar"),





    
 # comment
    
    
    
    
]



