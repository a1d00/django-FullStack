from django.urls import path
from . import views

urlpatterns = [
    path('contact/<str:name>', views.contact,name='contact'),
    path('categorias', views.categorias,name='categorias'),
    path('/libros/', views.libroFormView,name='libros'),
    path('saludo/',views.index),
]
