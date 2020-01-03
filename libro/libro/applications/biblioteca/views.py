from django.shortcuts import render
from .models import Autor, Libros
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
)

class ListaAutores(ListView):
    template_name = "biblioteca/lista-autores.html"
    model = Autor
    context_object_name = "autores"

#Vista para listar libros de un autor
class ListaLibrosAutores(ListView):
    template_name = "biblioteca/lista-libros.html"
    context_object_name = "libros"

    def get_queryset(self):
        #Identificador de autor
        id = self.kwargs['pk']

        #Filtro de los libros
        lista = Libros.objects.filter(
            autor = id
        )
        #Mostrar resultado
        return lista

    #Vista para registrar un nuevo autor
class AddAutor(CreateView):
    template_name = 'biblioteca/autor-add.html'
    model = Autor
    fields = ['nombre', 'nacionalidad']
    success_url = "/"