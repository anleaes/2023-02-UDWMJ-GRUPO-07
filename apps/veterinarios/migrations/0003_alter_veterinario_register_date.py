# Generated by Django 4.1 on 2023-12-06 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veterinarios', '0002_alter_veterinario_crm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veterinario',
            name='register_date',
            field=models.CharField(max_length=10, verbose_name='Data'),
        ),
    ]