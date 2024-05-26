from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_alumno, name='crear_alumno'),  
    path('lista/', views.lista_alumnos, name='lista_alumnos'),  
    path('crearCur/', views.crear_curso, name='crear_curso'),  
    path('listaCur/', views.lista_cursos, name='lista_cursos'),  
    path('crearNota/', views.crear_nota, name='crear_nota'),  
    path('listaNota/', views.lista_notas_alumno, name='lista_notas_alumno'),  
]