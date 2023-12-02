from django import forms
from .models import Adotante

class AdotanteForm(forms.ModelForm):

    class Meta:
        model = Adotante
        exclude = ('created_on' , 'updated_on',)