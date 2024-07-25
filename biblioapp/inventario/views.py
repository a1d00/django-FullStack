from django.shortcuts import render
from django.http import HttpResponse
from .forms import LibroForm

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