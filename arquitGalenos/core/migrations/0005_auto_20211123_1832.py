# Generated by Django 3.2.4 on 2021-11-23 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_hora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hora',
            name='hora',
        ),
        migrations.AddField(
            model_name='disponibilidad',
            name='creacion',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='hora',
            name='fecha',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='hora',
            name='hora_fin',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='hora',
            name='hora_inicio',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='rut',
            field=models.IntegerField(),
        ),
    ]
