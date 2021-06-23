from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import Libro, Usuario

class LibroForm(ModelForm):
    ISBN = forms.CharField(label='ISBN',widget=forms.TextInput(attrs={"placeholder": "13 dígitos"}))
    autor = forms.CharField(label='Autor')
    nombreLibro = forms.CharField(label='Nombre Libro')
    descripcion = forms.CharField(label='Descripción')
    
    class Meta:
        model = Libro
        fields = ['ISBN','nombreLibro', 'autor', 'descripcion','categoria',]
    
class RegistroUsuarioForm(ModelForm):
    correo = forms.CharField(label='E-mail')
    nombre = forms.CharField(label='Nombre')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={"placeholder": "************"}))
    repeatPassword = forms.CharField(label='Repita su Contraseña', widget=forms.PasswordInput(attrs={"placeholder": "************"}))
    
    class Meta:
        model = Usuario
        fields = ['correo', 'nombre', 'password', 'repeatPassword','comentario',]