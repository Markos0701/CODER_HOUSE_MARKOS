# Generated by Django 4.1.3 on 2022-12-08 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppMiembro', '0002_alter_miembro_fecha_nacimiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='miembro',
            name='fecha_nacimiento',
        ),
    ]