# Generated by Django 4.1 on 2023-12-02 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veterinarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veterinario',
            name='crm',
            field=models.CharField(max_length=15, verbose_name='Crm'),
        ),
    ]
