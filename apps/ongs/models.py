from django.db import models

# Create your models here.
class Ong(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    address = models.CharField('Endereço', max_length=50) 
    phone = models.CharField('Telefone', max_length=11)
    
    class Meta:
        verbose_name = 'Ong'
        verbose_name_plural = 'Ongs'
        ordering =['id']

    def __str__(self):
        return self.name