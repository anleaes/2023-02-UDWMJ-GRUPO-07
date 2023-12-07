# Generated by Django 4.1 on 2023-12-07 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doadores', '0002_alter_doador_cpf_alter_doador_phone'),
        ('ongs', '0002_alter_ong_address_alter_ong_phone'),
        ('animais', '0004_remove_animal_adoption_status_remove_animal_height_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='donator',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='doadores.doador'),
        ),
        migrations.AddField(
            model_name='animal',
            name='ong',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='ongs.ong'),
        ),
    ]
