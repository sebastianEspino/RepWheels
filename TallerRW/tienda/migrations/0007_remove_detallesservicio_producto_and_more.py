# Generated by Django 5.0.6 on 2024-08-02 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0006_remove_detallesservicio_producto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallesservicio',
            name='producto',
        ),
        migrations.AddField(
            model_name='detallesservicio',
            name='producto',
            field=models.ManyToManyField(to='tienda.productos'),
        ),
    ]
