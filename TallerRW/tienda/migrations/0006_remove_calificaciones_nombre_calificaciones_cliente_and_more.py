# Generated by Django 4.2 on 2024-03-30 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_productos_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calificaciones',
            name='nombre',
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='cliente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.clientes'),
        ),
        migrations.AddField(
            model_name='calificaciones',
            name='servicio',
            field=models.CharField(max_length=254, null=True),
        ),
    ]