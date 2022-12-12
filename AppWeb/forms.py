from django import forms
from .models import *

class NoticiaForm(forms.ModelForm):

    class Meta:
        model = NoticiaModel
        fields = ["Autor", "Titulo", "Noticia", "Imagen"]