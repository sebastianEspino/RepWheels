# Generated by Django 4.2 on 2024-03-26 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='foto',
            field=models.ImageField(default='fotos_usuarios/user.png', upload_to='fotos_usuarios/'),
        ),
    ]
