# Generated by Django 4.2 on 2024-03-30 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0010_remove_citas_cliente_remove_citas_cotizacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='citas',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.usuarios'),
        ),
        migrations.AddField(
            model_name='citas',
            name='cotizacion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.cotizaciones'),
        ),
        migrations.AddField(
            model_name='citas',
            name='empleado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.empleado'),
        ),
    ]