from django.db import models

# Create your models here.
class Veterinario(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    crm = models.CharField('Crm', max_length=15) 
    register_date = models.CharField('Data', max_length=10)
    
    class Meta:
        verbose_name = 'Veterinario'
        verbose_name_plural = 'Veterinarios'
        ordering =['id']

    def __str__(self):
        return self.name