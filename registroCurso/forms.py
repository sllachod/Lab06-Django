from django import forms
from .models import Alumno

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