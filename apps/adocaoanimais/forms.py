from django import forms
from .models import Adocaoanimal

class AdocaoanimalForm(forms.ModelForm):

    class Meta:
        model = Adocaoanimal
        exclude = ('created_on' , 'updated_on',)