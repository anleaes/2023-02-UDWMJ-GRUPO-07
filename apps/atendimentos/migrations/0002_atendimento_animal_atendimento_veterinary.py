# Generated by Django 4.1 on 2023-12-06 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animais', '0003_alter_animal_adoption_status'),
        ('veterinarios', '0002_alter_veterinario_crm'),
        ('atendimentos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='atendimento',
            name='animal',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='animais.animal'),
        ),
        migrations.AddField(
            model_name='atendimento',
            name='veterinary',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='veterinarios.veterinario'),
        ),
    ]