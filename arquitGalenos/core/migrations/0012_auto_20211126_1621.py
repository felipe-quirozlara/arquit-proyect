# Generated by Django 3.2.4 on 2021-11-26 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_cita_habilitada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disponibilidad',
            name='colaccion_fin',
        ),
        migrations.RemoveField(
            model_name='disponibilidad',
            name='colaccion_inicio',
        ),
    ]
