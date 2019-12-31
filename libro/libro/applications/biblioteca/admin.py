from django.contrib import admin

# Register your models here.
from .models import Autor, Libros

#Clase para el administrador del autor
class AutorAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'nacionalidad',
        'id'
    )
    #Atributo para buscar dentro de un campo
    search_fields = ('nombre', 'nacionalidad',)


#Clase para el administrador del libro
class LibrosAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'resumen',
        'autor',
        'id'
    )
    #Atributo para buscar dentro de un campo
    search_fields = ('title',)
    #Atributo para filtro de autor
    list_filter = ('autor',)



admin.site.register(Autor, AutorAdmin)
admin.site.register(Libros, LibrosAdmin)
