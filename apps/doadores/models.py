from django.db import models

# Create your models here.

class Doador(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    cpf = models.CharField('Cpf', max_length=11)
    address = models.CharField('Endereco', max_length=50)
    phone = models.CharField('Telefone', max_length=11)
    
    class Meta:
        verbose_name = 'Doador'
        verbose_name_plural = 'Doadores'
        ordering =['id']

    def __str__(self):
        return self.name