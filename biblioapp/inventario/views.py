from django.shortcuts import render
from django.http import HttpResponse
from .forms import LibroForm
from rest_framework import viewsets
from .serializers import CategoriaSerializer
from .models import Categoria
from .models import Libro
from .models import Usuario
from .serializers import LibroSerializer
from .serializers import UsuarioSerializer


def index(request):
    return HttpResponse("hello world")

def contact(request,name):
    return HttpResponse(f"Bienvenido {name} a la clase")

def categorias(request):
    return render(request, "categorias.html")

def libroFormView( request):
    form = LibroForm(request.POST)
    if form.is_valid():
        form.save()

    return render(request, "form_libros.html", {"form":form})

class CategoriasViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class LibrosViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
