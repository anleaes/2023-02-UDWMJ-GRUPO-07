from django.db import models
from ongs.models import Ong
from doadores.models import Doador

# Create your models here.

class Animal(models.Model):
    create_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    sex = models.CharField('Sexo', max_length=5)
    years_old = models.CharField('Idade', max_length=2)
    specie = models.CharField('Especie', max_length=10)
    race = models.CharField('Raca', max_length=10)
    color = models.CharField('Cor', max_length=10)
    weight = models.CharField('Peso', max_length=2)
    height = models.CharField('Altura', max_length=3)
    adoption_status = models.CharField('Status_adocao', max_length=10)
    #ong = models.ForeignKey(Ong, on_delete=models.CASCADE)
    #donator = models.ForeignKey(Doador, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'
        ordering =['id']
        
    def __str__(self):
        return self.name