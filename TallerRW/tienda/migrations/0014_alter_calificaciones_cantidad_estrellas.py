# Generated by Django 4.2.9 on 2024-04-12 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0013_servicios_productos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificaciones',
            name='cantidad_estrellas',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5),
        ),
    ]