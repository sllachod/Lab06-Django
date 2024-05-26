from django.urls import path
from . import views

urlpatterns = [
    path('', views.crear_alumno, name='crear_alumno'),  # URL para crear un nuevo alumno
    path('', views.lista_alumnos, name='lista_alumnos'),  # URL para listar todos los alumnos
]