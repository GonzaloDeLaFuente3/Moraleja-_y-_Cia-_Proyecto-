# Generated by Django 4.2.1 on 2023-06-24 23:02

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
                ('ingredientes', models.TextField(max_length=2000)),
                ('cantidad_personas', models.IntegerField()),
                ('elaboracion', models.TextField(max_length=2000)),
                ('imagen', models.ImageField(blank=True, upload_to='media/img')),
                ('productos', models.ManyToManyField(to='producto.producto')),
            ],
        ),
    ]
