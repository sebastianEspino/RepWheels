# Generated by Django 4.2 on 2024-01-19 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_alter_citas_tiposervicio_alter_productos_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='categoria',
        ),
    ]
