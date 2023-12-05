from django import forms
from .models import Adocao

class AdocaoForm(forms.ModelForm):

    class Meta:
        model = Adocao
        exclude = ('created_on' , 'updated_on',)