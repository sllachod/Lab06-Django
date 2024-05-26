from django import forms
from .models import *

class AlumnoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=200, label='Nombre del Alumno')
    
    class Meta:
        model = Alumno
        fields = ['nombre']

    def save(self, commit=True):
        alumno = super().save(commit=False)
        if commit:
            alumno.save()
        return alumno
    

class CursoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=200, label='Nombre del Curso')
    
    class Meta:
        model = Curso
        fields = ['nombre']

    def save(self, commit=True):
        curso = super().save(commit=False)
        if commit:
            curso.save()
        return curso