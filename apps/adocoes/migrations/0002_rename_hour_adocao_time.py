# Generated by Django 4.1 on 2023-12-06 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adocoes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adocao',
            old_name='hour',
            new_name='time',
        ),
    ]