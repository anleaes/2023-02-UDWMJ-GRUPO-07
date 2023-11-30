from django.db import models

# Create your models here.
class Ong(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    address = models.TextField('Endereco', max_length=100) 
    phone = models.TextField('Telefone', max_length=20)
    
    class Meta:
        verbose_name = 'Ong'
        verbose_name_plural = 'Ongs'
        ordering =['id']

    def __str__(self):
        return self.name
