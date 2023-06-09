# Generated by Django 4.1.5 on 2023-06-12 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='id de rol')),
                ('nombre', models.CharField(max_length=30, verbose_name='nombre de categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id_comuna', models.IntegerField(primary_key=True, serialize=False, verbose_name='id de comuna')),
                ('nombre', models.CharField(max_length=20, verbose_name='nombre comuna')),
                ('costo_despacho', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.IntegerField(primary_key=True, serialize=False, verbose_name='id de region')),
                ('nombre', models.CharField(max_length=30, verbose_name='nombre de region')),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id_rol', models.IntegerField(primary_key=True, serialize=False, verbose_name='id de rol')),
                ('nombreRol', models.CharField(max_length=30, verbose_name='nombre del rol')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.IntegerField(primary_key=True, serialize=False, verbose_name='id del usuario')),
                ('nombre', models.CharField(max_length=20, verbose_name='nombre del usuario')),
                ('apellido', models.CharField(max_length=20, verbose_name='apellido usuario')),
                ('correo', models.CharField(max_length=30, verbose_name='correo usuario')),
                ('clave', models.CharField(max_length=12, verbose_name='clave usuario')),
                ('telefono', models.IntegerField(verbose_name='telefono usuario')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='happy.rol')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.IntegerField(primary_key=True, serialize=False, verbose_name='id de venta')),
                ('f_venta', models.DateField()),
                ('r_envio', models.CharField(max_length=100, verbose_name='registro del envio')),
                ('costo_envio', models.IntegerField(verbose_name='costo envío')),
                ('total', models.IntegerField()),
                ('carrito', models.IntegerField(verbose_name='1-Carrito - 0- Venta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='happy.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.IntegerField(primary_key=True, serialize=False, verbose_name='id del producto')),
                ('nombre', models.CharField(max_length=30, verbose_name='nombre del producto')),
                ('descripcion', models.CharField(max_length=100, verbose_name='descripcion producto')),
                ('precio', models.IntegerField(verbose_name='precio producto')),
                ('stock', models.IntegerField()),
                ('foto', models.ImageField(upload_to='foto producto')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='happy.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id_direccion', models.IntegerField(primary_key=True, serialize=False, verbose_name='id de direccion')),
                ('calle', models.CharField(max_length=50, verbose_name='nombre calle')),
                ('numero', models.IntegerField(verbose_name='numero casa')),
                ('descripcion', models.CharField(max_length=100, verbose_name='descripcion direccion')),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='happy.comuna')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='happy.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id_detalle', models.IntegerField(primary_key=True, serialize=False, verbose_name='id de detalle')),
                ('cantidad', models.IntegerField(verbose_name='cantidad')),
                ('subtotal', models.IntegerField()),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='happy.producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='happy.venta')),
            ],
        ),
        migrations.AddField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='happy.region'),
        ),
    ]
