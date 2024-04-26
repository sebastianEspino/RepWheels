# Generated by Django 4.2.1 on 2024-04-26 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('descripcion_categoria', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=254)),
                ('cedula', models.IntegerField(default=0)),
                ('correo', models.CharField(max_length=254, unique=True)),
                ('telefono', models.IntegerField(default=0)),
                ('direccion', models.CharField(max_length=254)),
                ('n', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=254)),
                ('cedula', models.IntegerField(unique=True)),
                ('correo', models.CharField(max_length=254, unique=True)),
                ('telefono', models.IntegerField(unique=True)),
                ('fecha_contratacion', models.DateField()),
                ('cargo', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('Precio', models.IntegerField()),
                ('descripcion_producto', models.TextField()),
                ('cantidad', models.IntegerField()),
                ('fecha_Creacion', models.DateField()),
                ('foto', models.ImageField(default='fotos_productos/default.png', upload_to='fotos_productos/')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('nit', models.IntegerField(unique=True)),
                ('telefono', models.IntegerField(unique=True)),
                ('correo', models.CharField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('correo', models.CharField(max_length=254, unique=True)),
                ('clave', models.CharField(max_length=8)),
                ('foto', models.ImageField(default='fotos_usuarios/user.png', upload_to='fotos_usuarios/')),
                ('rol', models.IntegerField(choices=[(1, 'administrador'), (2, 'gerente'), (3, 'empleado'), (4, 'cliente')], default=4)),
            ],
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('descripcion_servicio', models.TextField()),
                ('productos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.productos')),
            ],
        ),
        migrations.CreateModel(
            name='Facturas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='DetallesServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('producto', models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.productos')),
                ('servicio', models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.servicios')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(null=True)),
                ('total', models.IntegerField()),
                ('factura', models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.facturas')),
                ('productos', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.productos')),
            ],
        ),
        migrations.CreateModel(
            name='Cotizaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.IntegerField(default=1900)),
                ('placa', models.CharField(max_length=6, null=True)),
                ('kilometraje', models.IntegerField(default=1236456)),
                ('linea', models.CharField(max_length=6, null=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.clientes')),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.empleado')),
                ('servicio', models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.servicios')),
            ],
        ),
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaServicio', models.DateField(null=True)),
                ('hora', models.TimeField(null=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.usuarios')),
                ('cotizacion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.cotizaciones')),
                ('empleado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Calificaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(max_length=254, null=True)),
                ('cantidad_estrellas', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (4, '5')], default=5)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.usuarios')),
            ],
        ),
    ]
