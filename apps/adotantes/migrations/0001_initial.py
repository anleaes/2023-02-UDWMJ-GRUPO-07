# Generated by Django 4.1 on 2023-12-02 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adotante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('cpf', models.CharField(max_length=11, verbose_name='Cpf')),
                ('address', models.CharField(max_length=50, verbose_name='Endereco')),
                ('phone', models.CharField(max_length=11, verbose_name='Telefone')),
            ],
            options={
                'verbose_name': 'Adotante',
                'verbose_name_plural': 'Adotantes',
                'ordering': ['id'],
            },
        ),
    ]
