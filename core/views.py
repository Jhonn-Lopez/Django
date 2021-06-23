from django.shortcuts import render, redirect
from.models import Libro, Usuario
from .forms import LibroForm, RegistroUsuarioForm
from django.contrib import messages
from django.core.exceptions import ValidationError
 
# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def listado_libros(request):
    libros = Libro.objects.all()
    datos = {
        'libros': libros
     }
    return render(request, 'core/listado_libros.html', datos)

def usuario_creado(request):
    return render(request, 'core/usuario_creado.html')    

def form_libro(request):
    datos = {
        'form': LibroForm()
    }
    if request.method == 'POST':
        formulario = LibroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            formulario = LibroForm()
            messages.add_message(request, messages.INFO, 'Registro Creado Correctamente.')
            return  redirect(to="listado_libros")
        else:
            datos['mensaje'] = "ISBN Incorrecto"
    return render(request, 'core/form_libro.html', datos)

def form_mod_libro(request, id):
    libro = Libro.objects.get(ISBN=id)
    datos = {
        'form': LibroForm(instance=libro)
    }
    if request.method == 'POST':
        formulario = LibroForm(data=request.POST, instance=libro)
        if formulario.is_valid:
            formulario.save()
            messages.add_message(request, messages.INFO, 'Registro Modificado Correctamente.')
            return  redirect(to="listado_libros")
    return render(request, 'core/form_mod_libro.html', datos)    

def form_eli_libro(request, id):
    libro = Libro.objects.get(ISBN=id)
    libro.delete()
    messages.add_message(request, messages.INFO, 'Registro Eliminado Correctamente.')
    return redirect(to="listado_libros")    

def form_reg_usuario(request):
    datos = {
        'form': RegistroUsuarioForm()
    }
    if request.method == 'POST':
        formulario = RegistroUsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            formulario = RegistroUsuarioForm()
            datos['mensaje'] = "Datos Ingresados correctamente"
            return redirect(to="usuario_creado")
        else:
            datos['mensaje'] = "Ya se ha registrado anteriormente con este Correo Electronico, pruebe con otro."
    return render(request, 'core/form_reg_usuario.html', datos)
