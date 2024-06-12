# Generated by Django 5.0.6 on 2024-06-12 00:35

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
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
            name='Configuracion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('contacto', models.CharField(max_length=254)),
                ('ubicacion', models.CharField(max_length=254)),
                ('correo', models.CharField(max_length=254, null=True)),
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
            name='Servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('descripcion_servicio', models.TextField()),
                ('foto', models.ImageField(default='fotos_servicios/servicio.jpg', upload_to='fotos_servicios/')),
                ('precio', models.IntegerField(default=100000)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nombre', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('password', models.CharField(max_length=254, null=True)),
                ('foto', models.ImageField(default='fotos_usuarios/user.png', upload_to='fotos_usuarios/')),
                ('token_recuperar', models.CharField(default=0, max_length=254)),
                ('telefono', models.IntegerField(blank=True, default='0')),
                ('cargo', models.CharField(max_length=254)),
                ('direccion', models.CharField(max_length=254)),
                ('cedula', models.IntegerField(blank=True, default='0')),
                ('rol', models.IntegerField(choices=[(1, 'administrador'), (2, 'proveedor'), (3, 'empleado'), (4, 'cliente')], default=4)),
                ('n', models.IntegerField(blank=True, default=0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaServicio', models.DateField(null=True)),
                ('hora', models.TimeField(null=True)),
                ('estado', models.IntegerField(choices=[(1, 'Pendiente'), (2, 'Cancelado'), (3, 'Finalizada')], default=1)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='cliente', to=settings.AUTH_USER_MODEL)),
                ('empleado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='empleado', to=settings.AUTH_USER_MODEL)),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.servicios')),
            ],
        ),
        migrations.CreateModel(
            name='Facturas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
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
                ('foto', models.ImageField(default='fotos_productos/default.png', upload_to='fotos_productos/')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('total', models.IntegerField()),
                ('cita', models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.citas')),
                ('producto', models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.productos')),
            ],
        ),
        migrations.CreateModel(
            name='Promociones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=254)),
                ('foto', models.ImageField(default='fotos_servicios/servicio.jpg', upload_to='fotos_servicios/')),
                ('servicio', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.servicios')),
            ],
        ),
        migrations.CreateModel(
            name='DetallesServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_proceso', models.CharField(max_length=254, null=True)),
                ('producto', models.ManyToManyField(to='tienda.productos')),
                ('servicio', models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.servicios')),
            ],
        ),
        migrations.CreateModel(
            name='Calificaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(default='fotos_usuarios/user.png', upload_to='fotos_productos/')),
                ('cantidad_estrellas', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (4, '5')], default=5)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('servicios', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.servicios')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehiculo', models.CharField(max_length=254, null=True)),
                ('modelo', models.IntegerField(default=1900)),
                ('placa', models.CharField(max_length=6, null=True)),
                ('kilometraje', models.IntegerField(blank=True, default=1236456, null=True)),
                ('linea', models.CharField(max_length=254, null=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
