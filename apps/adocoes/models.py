from django.db import models
from adotantes.models import Adotante
from datetime import datetime
from animais.models import Animal
# Create your models here.

class Adocao(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    date_hour = models.DateTimeField('Data e Hora da Adoção', auto_now_add=True)
    adopter = models.ForeignKey(Adotante, on_delete=models.CASCADE, default=1)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, default=0)
    
    class Meta:
        verbose_name = 'Adocao'
        verbose_name_plural = 'Adocoes'
        ordering =['id']

    def __str__(self):
        return self.date_hour