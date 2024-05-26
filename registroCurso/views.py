from django.shortcuts import render, redirect
from .forms import *
from .models import *

def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'registroCurso/crear_alumno.html', {'form': form})

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'registroCurso/lista_alumnos.html', {'alumnos': alumnos})

def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cursos')
    else:
        form = CursoForm()
    return render(request, 'registroCurso/crear_curso.html', {'form': form})

def lista_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'registroCurso/lista_cursos.html', {'cursos': cursos})