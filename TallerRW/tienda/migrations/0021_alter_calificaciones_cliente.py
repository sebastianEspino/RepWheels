# Generated by Django 4.2 on 2024-03-20 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0020_remove_calificaciones_nombre_calificaciones_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificaciones',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.clientes'),
        ),
    ]
