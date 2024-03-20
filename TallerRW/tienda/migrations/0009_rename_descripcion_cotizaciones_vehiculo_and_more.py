# Generated by Django 4.2 on 2024-02-24 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0008_productos_foto_alter_citas_tiposervicio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cotizaciones',
            old_name='descripcion',
            new_name='vehiculo',
        ),
        migrations.RemoveField(
            model_name='calificaciones',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='citas',
            name='tipoServicio',
        ),
        migrations.RemoveField(
            model_name='cotizaciones',
            name='tipos',
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='cliente',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.clientes'),
        ),
        migrations.AddField(
            model_name='citas',
            name='cliente',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.clientes'),
        ),
        migrations.AddField(
            model_name='citas',
            name='cotizacion',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.cotizaciones'),
        ),
        migrations.AddField(
            model_name='cotizaciones',
            name='cliente',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.clientes'),
        ),
        migrations.AddField(
            model_name='cotizaciones',
            name='modelo',
            field=models.IntegerField(default=1900),
        ),
        migrations.AddField(
            model_name='cotizaciones',
            name='servicio',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.servicios'),
        ),
        migrations.AddField(
            model_name='productos',
            name='categoria',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.categoria'),
        ),
        migrations.AddField(
            model_name='productos',
            name='proveedor',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.proveedores'),
        ),
        migrations.AddField(
            model_name='servicios',
            name='productos',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.productos'),
        ),
        migrations.AlterField(
            model_name='citas',
            name='empleado',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.empleado'),
        ),
        migrations.AlterField(
            model_name='cotizaciones',
            name='empleado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.empleado'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='foto',
            field=models.ImageField(default='fotos_productos/stock.jpg', upload_to='fotos_productos/'),
        ),
        migrations.CreateModel(
            name='Facturas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('cliente', models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.clientes')),
            ],
        ),
        migrations.CreateModel(
            name='DetallesServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('producto', models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.productos')),
                ('servicio', models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.servicios')),
            ],
        ),
        migrations.CreateModel(
            name='DetalleFactura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productos', models.CharField(max_length=254)),
                ('categoria', models.CharField(max_length=254)),
                ('cantidad', models.IntegerField(null=True)),
                ('total', models.IntegerField()),
                ('factura', models.ForeignKey(default='0', on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.facturas')),
            ],
        ),
    ]
