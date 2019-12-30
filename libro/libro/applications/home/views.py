from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
)

class Indexview(TemplateView):
    template_name = "home/index.html"

class ListaLibros(ListView):
    template_name = "home/lista.html"
    queryset = ['Cujo', 'Carrie', 'Dr. Sueño', 'Libro escolarc  ']
    context_object_name = "libros"
