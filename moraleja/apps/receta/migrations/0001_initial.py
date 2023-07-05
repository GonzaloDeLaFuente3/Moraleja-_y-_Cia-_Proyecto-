# Generated by Django 4.2.1 on 2023-07-05 00:37

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='nombre', unique=True)),
                ('ingredientes', models.TextField(max_length=2000)),
                ('cantidad_personas', models.IntegerField()),
                ('elaboracion', ckeditor.fields.RichTextField()),
                ('extra', ckeditor.fields.RichTextField()),
                ('imagen', models.ImageField(blank=True, upload_to='recetas')),
                ('productos', models.ManyToManyField(to='producto.producto')),
            ],
        ),
    ]
