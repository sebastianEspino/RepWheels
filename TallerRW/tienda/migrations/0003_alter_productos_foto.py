# Generated by Django 4.2.1 on 2024-07-19 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_registrarusuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='foto',
            field=models.ImageField(default='media/default.png', upload_to='media/'),
        ),
    ]
