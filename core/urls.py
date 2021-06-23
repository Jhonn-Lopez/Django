
from django.urls import path
from .views import home,usuario_creado, listado_libros, form_libro, form_mod_libro, form_eli_libro, form_reg_usuario

urlpatterns = [
    path('', home,name="home"),
    path('usuario-creado', usuario_creado, name="usuario_creado"),
    path('listado-libros', listado_libros, name="listado_libros"),
    path('form-libro', form_libro, name="form_libro"),
    path('form-mod-libro/<id>', form_mod_libro, name="form_mod_libro"),
    path('form-eli-libro/<id>', form_eli_libro, name="form_eli_libro"),
    path('form-reg-usuario', form_reg_usuario, name="form_reg_usuario"), 
]



