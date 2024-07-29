from django.contrib import admin
from .models import Categoria,Libro,Compra,Usuario,libro_compra

admin.site.register(Categoria)
admin.site.register(Libro)
admin.site.register(Compra)
admin.site.register(Usuario)
admin.site.register(libro_compra)
