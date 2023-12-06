from django.db import models
from animais.models import Animal
from veterinarios.models import Veterinario

# Create your models here.

class Atendimento(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    reason = models.CharField('Razao', max_length=50)
    description = models.CharField('Descricao', max_length=50)
    medicine = models.CharField('Medicamento', max_length=15)
    vaccine = models.CharField('Vacina', max_length=15)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, default=1)
    veterinary = models.ForeignKey(Veterinario, on_delete=models.CASCADE, default=1)
    
    
    class Meta:
        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'
        ordering =['id']

    def __str__(self):
        return self.reason