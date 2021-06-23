from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria =models.IntegerField(primary_key=True, verbose_name='Id de Categoria')
    nombreCategoria =models.CharField(max_length=50, verbose_name='Nombre de la Categoria')

    def __str__(self):
        return self.nombreCategoria
   
class Libro(models.Model):
    ISBN =models.CharField(max_length=13, primary_key=True, verbose_name='ISBN')        
    nombreLibro =models.CharField(max_length=50, verbose_name='Nombre del Libro')
    autor =models.CharField(max_length=75, verbose_name='Autor')
    descripcion =models.CharField(max_length=250, null=True, blank=True, verbose_name='Descripcion')
    categoria =models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.ISBN

class Usuario(models.Model):
    correo = models.CharField(primary_key=True, max_length=75, verbose_name='Correo de Usuario')
    nombre = models.CharField(max_length=25, verbose_name='Nombre de Usuario')
    password = models.CharField(max_length=12, verbose_name='Contraseña')
    repeatPassword = models.CharField(max_length=12, verbose_name='Repetir Contraseña')
    comentario = models.TextField(max_length=250, verbose_name='Comentario')

    def __str__(self):
        return self.correo         