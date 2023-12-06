from django.db import models
from adotantes.models import Adotante

# Create your models here.

class Adocao(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    date = models.DateField('Data')
    hour = models.CharField('Hora', max_length=5)
    status = models.CharField('Status', max_length=10) 
    #adotante = models.ForeignKey(Adotante, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Adocao'
        verbose_name_plural = 'Adocoes'
        ordering =['id']

    def __str__(self):
        return self.status