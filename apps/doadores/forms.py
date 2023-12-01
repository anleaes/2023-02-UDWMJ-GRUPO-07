from django import forms
from .models import Doador

class DoadorForm(forms.ModelForm):

    class Meta:
        model = Doador
        exclude = ('created_on' , 'updated_on',)
