from django.shortcuts import render
from .models import Autor, Editorial, Libro

def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'app_unidad2/lista_libros.html', {'libros': libros})

def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'app_unidad2/lista_autores.html', {'autores': autores})


