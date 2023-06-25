# Generated by Django 4.2.1 on 2023-06-24 23:02

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=51)),
                ('imagen', models.ImageField(blank=True, upload_to='media/img')),
                ('descripcion', models.TextField(max_length=1200)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='nombre', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BeneficioProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=2000)),
                ('producto', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='beneficio_producto', to='producto.producto')),
            ],
        ),
    ]
