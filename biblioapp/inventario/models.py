from django.db import models
from .validators import validar_par

class Categoria(models.Model):
    nombre=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    nombre=models.CharField(max_length=100,unique=True)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    descripcion=models.TextField()
    precio=models.DecimalField(max_digits=10,decimal_places=2)
    disponible=models.BooleanField(blank=True,default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre=models.CharField(max_length=100,unique=True)
    apellidoPaterno=models.CharField(max_length=100,unique=True)
    apellidoMaterno=models.CharField(max_length=100,unique=True)
    direccion=models.CharField(max_length=100)
    celular=models.IntegerField(unique=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    costo=models.DecimalField(max_digits=10,decimal_places=2)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
    
class libro_compra(models.Model):
    libro=models.ForeignKey(Libro,on_delete=models.CASCADE)
    compra=models.ForeignKey(Compra,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre