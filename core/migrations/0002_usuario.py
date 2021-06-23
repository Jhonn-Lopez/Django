# Generated by Django 3.2.4 on 2021-06-22 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('correo', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Correo de Usuario')),
                ('nombre', models.CharField(max_length=25, verbose_name='Nombre de Usuario')),
                ('apellido', models.CharField(max_length=25, verbose_name='Apellido de Usuario')),
                ('password', models.CharField(max_length=12, verbose_name='Contraseña')),
                ('repeatPassword', models.CharField(max_length=12, verbose_name='Repetir Contraseña')),
                ('comentario', models.TextField(max_length=250, verbose_name='Comentario')),
            ],
        ),
    ]
