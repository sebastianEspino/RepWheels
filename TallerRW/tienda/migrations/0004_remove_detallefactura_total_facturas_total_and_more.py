# Generated by Django 5.0.6 on 2024-08-10 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_alter_detallefactura_precio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallefactura',
            name='total',
        ),
        migrations.AddField(
            model_name='facturas',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='detallefactura',
            name='precio',
            field=models.IntegerField(),
        ),
    ]
