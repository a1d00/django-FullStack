from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'/categorias', views.CategoriasViewSet)
router.register(r'/Usuarios', views.CategoriasViewSet)
router.register(r'/Libros', views.CategoriasViewSet)

urlpatterns = [
    path('contact/<str:name>', views.contact,name='contact'),
    #path('categorias', views.categorias,name='categorias'),
    #path('/libros/', views.libroFormView,name='libros'),
    #path('saludo/',views.index),
    path('',include(router.urls))
]
