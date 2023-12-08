from django.db import models
from ongs.models import Ong
from doadores.models import Doador

# Create your models here.

class Animal(models.Model):
    create_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    SEX_CHOICES = [
        ('Macho', 'Macho'),
        ('Fêmea', 'Fêmea'),
    ]
    sex = models.CharField('Sexo', max_length=5, choices=SEX_CHOICES, default='Macho')
    years_old_value = models.PositiveIntegerField('Idade', default= 0)
    years_old_unit = models.CharField('Unidade de Idade', max_length=10, choices=[
        ('anos', 'Anos'),
        ('meses', 'Meses'),
    ], default='meses')
    SPECIE_CHOICES = [
        ('Gato', 'Gato'),
        ('Cachorro', 'Cachorro'),
    ] 
    specie = models.CharField('Especie', max_length=10, choices=SPECIE_CHOICES, default='Cachorro')
    race = models.CharField('Raca', max_length=10)
    color = models.CharField('Cor', max_length=10)
    weight_value = models.PositiveIntegerField('Peso',  default= 0)
    weight_unit = models.CharField('Unidade de Peso', max_length=10, choices=[
        ('gramas', 'Gramas'),
        ('quilos', 'Quilos'),
    ], default='gramas')
    height_value = models.PositiveIntegerField('Altura', default= 0)
    height_unit = models.CharField('Unidade de Altura', max_length=11, choices=[
        ('centimetros', 'Centímetros'),
        ('metros', 'Metros'),
    ], default= 'metros')
    ong = models.ForeignKey(Ong, on_delete=models.CASCADE, default=1)
    donator = models.ForeignKey(Doador, on_delete=models.CASCADE, default=1)

    @property
    def formatted_years_old(self):
        return f"{self.years_old_value} {self.years_old_unit}"

    @property
    def formatted_weight(self):
        return f"{self.weight_value} {self.weight_unit}"

    @property
    def formatted_height(self):
        return f"{self.height_value} {self.height_unit}"

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'
        ordering =['id']
        
    def __str__(self):
        return "%s - %s - %s - %s - %s" % (self.name, self.specie, self.sex, self.race, self.ong)
