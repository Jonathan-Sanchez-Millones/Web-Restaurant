# Generated by Django 2.0.2 on 2019-06-30 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_myuser_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='apellidos',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Apellidos'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='nombres',
            field=models.CharField(blank=True, default='', max_length=200, null=True, verbose_name='Nombres'),
        ),
    ]
