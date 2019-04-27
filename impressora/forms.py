from django.forms import ModelForm
from .models import Printer
from django import forms

class Impressora(ModelForm):
    class Meta:
        model = Printer
        widgets = {'etiqueta': forms.TextInput(attrs={'placeholder': 'EX: ABRBE1PT0091175'})}# Adiciona o placeholder
        fields = ['serial', 'ip', 'modelo', 'contador', 'etiqueta', 'galpao', 'coluna', 'status']



class Busca_Rede(forms.Form):

    ip = forms.GenericIPAddressField()

class Busca_Coluna(forms.Form):

    coluna = forms.CharField()


