from django import forms
from .models import Equipo

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre_equipo', 'tipo', 'descripcion', 'fecha_adquisicion', 'estado']
