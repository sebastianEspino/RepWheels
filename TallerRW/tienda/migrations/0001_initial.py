# Generated by Django 4.2.1 on 2024-05-03 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
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
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=8)),
                ('foto', models.ImageField(default='fotos_usuarios/user.png', upload_to='fotos_usuarios/')),
                ('rol', models.IntegerField(choices=[(1, 'administrador'), (2, 'gerente'), (3, 'empleado'), (4, 'cliente')], default=4)),
                ('token_recuperar', models.CharField(blank=True, default='', max_length=254, null=True)),
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
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
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
                ('vehiculo', models.CharField(max_length=254, null=True)),
                ('modelo', models.IntegerField(default=1900)),
                ('placa', models.CharField(max_length=6, null=True)),
                ('kilometraje', models.IntegerField(default=1236456)),
                ('linea', models.CharField(max_length=254, null=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.empleado')),
                ('servicio', models.ForeignKey(default='Mantenimiento', on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.servicios')),
            ],
        ),
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaServicio', models.DateField(null=True)),
                ('hora', models.TimeField(null=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
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
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
