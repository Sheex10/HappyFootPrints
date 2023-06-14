# Generated by Django 4.2.1 on 2023-06-14 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comuna',
            name='costo_despacho',
            field=models.IntegerField(verbose_name='costo del despacho'),
        ),
        migrations.AlterField(
            model_name='detalle',
            name='subtotal',
            field=models.IntegerField(verbose_name='subtotal de venta'),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='calle',
            field=models.CharField(max_length=100, verbose_name='nombre calle'),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='descripcion',
            field=models.CharField(max_length=600, verbose_name='descripcion direccion'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=700, verbose_name='descripcion producto'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.CharField(max_length=50, verbose_name='correo usuario'),
        ),
        migrations.AlterField(
            model_name='venta',
            name='r_envio',
            field=models.CharField(max_length=500, verbose_name='registro del envio'),
        ),
    ]
