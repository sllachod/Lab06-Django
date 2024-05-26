from django.shortcuts import render, redirect
from .forms import *
from .models import *

#CREAR ALUMNO
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

#CREAR CURSO
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

#CREAR NOTA
def crear_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_notas_alumno')
    else:
        form = NotaForm()
    return render(request, 'registroCurso/crear_nota.html', {'form': form})

def lista_notas_alumno(request):
    notas = Nota.objects.select_related('alumno', 'curso').all()
    return render(request, 'registroCurso/lista_notas_alumno.html', {'notas': notas})