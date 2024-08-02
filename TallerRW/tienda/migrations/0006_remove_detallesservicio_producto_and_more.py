# Generated by Django 5.0.6 on 2024-08-02 01:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_alter_usuarios_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallesservicio',
            name='producto',
        ),
        migrations.AddField(
            model_name='detallesservicio',
            name='producto',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='tienda.productos'),
        ),
    ]
