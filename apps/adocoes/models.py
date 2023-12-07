from django.db import models
from adotantes.models import Adotante

# Create your models here.

class Adocao(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    date = models.CharField('Data', max_length=10)
    time = models.CharField('Hora', max_length=5)
    adopter = models.ForeignKey(Adotante, on_delete=models.CASCADE, default=4)
    
    class Meta:
        verbose_name = 'Adocao'
        verbose_name_plural = 'Adocoes'
        ordering =['id']

    def __str__(self):
        return self.date