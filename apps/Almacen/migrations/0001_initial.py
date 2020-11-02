# Generated by Django 3.1.1 on 2020-10-12 17:09

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('num_boleta', models.IntegerField(default='', primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='OrdenCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(default='xx.xxx.xxx-x', max_length=12)),
                ('nombre', models.CharField(default='', max_length=20)),
                ('apellido', models.CharField(default='', max_length=30)),
                ('telefono', models.IntegerField(default=999999999999)),
                ('direccion', models.CharField(default='', max_length=50)),
                ('tipo', models.IntegerField(choices=[(0, 'PROVEEDOR'), (1, 'CLIENTE')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ProductoFamilia',
            fields=[
                ('id_familia', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('familia', models.CharField(default='', help_text='La categoria a la que pertenece el producto', max_length=250, unique=True)),
            ],
            managers=[
                ('categorias', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Almacen.persona')),
                ('email', models.EmailField(max_length=254)),
            ],
            bases=('Almacen.persona',),
            managers=[
                ('clientes', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='Almacen.persona')),
                ('id_proveedor', models.AutoField(default=0, editable=False, primary_key=True, serialize=False)),
                ('rubro', models.IntegerField(choices=[(0, '')], default=0)),
            ],
            bases=('Almacen.persona',),
            managers=[
                ('proveedores', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nombre', models.CharField(default='', max_length=50)),
                ('descripcion', models.CharField(default='', max_length=250)),
                ('p_compra', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('p_venta', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('stock', models.IntegerField(default=0)),
                ('fecha_venc', models.DateTimeField(default='00000000')),
                ('id_ref', models.IntegerField(default=0)),
                ('id_familia', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='Almacen.productofamilia')),
                ('id_proveedor', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='Almacen.proveedor')),
            ],
            managers=[
                ('productos', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='OrdenCompraDetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=0)),
                ('id_orden', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='Almacen.ordencompra')),
                ('producto', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Almacen.producto')),
            ],
        ),
        migrations.CreateModel(
            name='BoletaDetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('boleta', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='Almacen.boleta')),
                ('producto', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='Almacen.producto')),
            ],
        ),
        migrations.AddField(
            model_name='ordencompra',
            name='proveedor',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='Almacen.proveedor'),
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=9)),
                ('estado', models.IntegerField(choices=[(0, 'PENDIENTE'), (1, 'PAGADO'), (2, 'CANCELADO')], default=0)),
                ('num_boleta', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='Almacen.boletadetalle')),
                ('cliente', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='Almacen.cliente')),
            ],
        ),
    ]
