# Generated by Django 2.0.2 on 2019-07-02 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_myuser_password_decrypt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bebida',
            name='descripcion',
            field=models.TextField(verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='carrito',
            name='descripcion',
            field=models.TextField(verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='descripcion',
            field=models.TextField(verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='plato',
            name='descripcion',
            field=models.TextField(verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='promocion',
            name='descripcion',
            field=models.TextField(verbose_name='Descripcion'),
        ),
    ]
