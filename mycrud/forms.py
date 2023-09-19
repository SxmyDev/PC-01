from django import forms
from .models import *

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'estado']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen']