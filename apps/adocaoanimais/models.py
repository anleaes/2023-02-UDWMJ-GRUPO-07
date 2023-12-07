from django.db import models
from animais.models import Animal
from adocoes.models import Adocao

# Create your models here.
class Adocaoanimal(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, default=1)
    adoption = models.ForeignKey(Adocao, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = 'Adocaoanimal'
        verbose_name_plural = 'Adocaoanimais'
        ordering =['id']

    def __str__(self):
        return self.animal