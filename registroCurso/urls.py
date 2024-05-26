from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_alumno, name='crear_alumno'),  # URL para crear un nuevo alumno
    path('lista/', views.lista_alumnos, name='lista_alumnos'),  # URL para listar todos los alumnos
    path('crearCur/', views.crear_curso, name='crear_curso'),  # URL para crear un nuevo curso
    path('listaCur/', views.lista_cursos, name='lista_cursos'),  # URL para listar todos los cursos
    path('crearNota/', views.crear_nota, name='crear_nota'),  # URL para crear un nueva nota
    path('listaNota/', views.lista_notas_alumno, name='lista_notas_alumno'),  # URL para listar todos las notas
]