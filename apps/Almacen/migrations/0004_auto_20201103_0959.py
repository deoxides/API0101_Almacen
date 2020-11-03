# Generated by Django 3.1.2 on 2020-11-03 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Almacen', '0003_auto_20201026_1910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rubro', models.CharField(choices=[('O', 'OTROS'), ('A', 'ALIMENTOS PERECEDEROS Y NO PERECEDEROS'), ('B', 'BEBIDAS'), ('AA', 'ARTICULOS DE ASEO'), ('PB', 'PRODUCTOS DE BAZAR')], default='O', max_length=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='proveedor',
            name='rubro',
        ),
        migrations.AddField(
            model_name='proveedor',
            name='rubro',
            field=models.ManyToManyField(default='O', to='Almacen.Rubros'),
        ),
    ]
