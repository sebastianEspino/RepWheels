# Generated by Django 4.2 on 2024-01-18 17:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_cotizaciones_citas_calificaciones'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calificaciones',
            name='idCliente',
        ),
    ]
