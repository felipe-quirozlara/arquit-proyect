# Generated by Django 3.2.4 on 2021-11-23 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20211123_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disponibilidad',
            name='creacion',
        ),
    ]
