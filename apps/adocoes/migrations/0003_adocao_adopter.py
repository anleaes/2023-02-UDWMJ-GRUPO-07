# Generated by Django 4.1 on 2023-12-07 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adotantes', '0001_initial'),
        ('adocoes', '0002_rename_hour_adocao_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='adocao',
            name='adopter',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='adotantes.adotante'),
        ),
    ]
